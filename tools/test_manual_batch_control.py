#!/usr/bin/env python3
"""Unit tests for manual_batch_control.py."""

from __future__ import annotations

import argparse
import json
import os
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

import manual_batch_control as control


class ManualBatchControlTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        base = Path(self.temporary.name)
        self.vault = base / "vault"
        self.automations = base / "automations"
        self.vault.mkdir()
        self.automations.mkdir()
        self.thread_id = "test-thread-a"
        self.environment = mock.patch.dict(
            os.environ, {"CODEX_THREAD_ID": self.thread_id}
        )
        self.environment.start()

    def tearDown(self) -> None:
        self.environment.stop()
        self.temporary.cleanup()

    def write_automation(
        self, automation_id: str, status: str, updated_at: int
    ) -> None:
        directory = self.automations / automation_id
        directory.mkdir(parents=True)
        text = (
            'version = 1\n'
            f'id = {json.dumps(automation_id)}\n'
            'kind = "cron"\n'
            'name = "test"\n'
            'prompt = "test"\n'
            f'status = {json.dumps(status)}\n'
            f'updated_at = {updated_at}\n'
        )
        (directory / "automation.toml").write_text(text)

    def write_runtime(
        self,
        automation_id: str,
        *,
        status: str,
        completed: int,
        baseline: int,
        target: int = None,
    ) -> Path:
        spec = control.SPECS[automation_id]
        path = self.vault / spec["runtime"]
        path.parent.mkdir(parents=True, exist_ok=True)
        value = {
            "schema_version": 2,
            "lane": spec["lane"],
            "automation_id": automation_id,
            "target_occurrences": spec["target"] if target is None else target,
            "status": status,
            "completed_occurrences": completed,
            "current_occurrence": None,
            "current_started_at": None,
            "manual_rearm_required": True,
            "pause_required": False,
            "last_paused_automation_updated_at": baseline,
        }
        path.write_text(json.dumps(value))
        return path

    def args(self, command: str, automation_id: str, reason: str = "test"):
        return argparse.Namespace(
            command=command,
            automation_id=automation_id,
            vault_root=self.vault,
            automations_root=self.automations,
            reason=reason,
            claim_token=None,
        )

    def owner(self, automation_id: str):
        lock = self.vault / control.SPECS[automation_id]["lock"]
        return json.loads((lock / "owner.json").read_text())

    def set_thread(self, thread_id: str) -> None:
        self.thread_id = thread_id
        os.environ["CODEX_THREAD_ID"] = thread_id

    def age_current_claim(
        self,
        automation_id: str,
        minutes: int,
        *,
        heartbeat_minutes: int = 0,
    ) -> None:
        spec = control.SPECS[automation_id]
        runtime_path = self.vault / spec["runtime"]
        runtime = json.loads(runtime_path.read_text())
        old = datetime.now(timezone.utc) - timedelta(minutes=minutes)
        runtime["current_started_at"] = old.isoformat()
        runtime["occurrence_started_at"] = old.isoformat()
        runtime_path.write_text(json.dumps(runtime))
        owner_path = self.vault / spec["lock"] / "owner.json"
        owner = json.loads(owner_path.read_text())
        owner["started_at"] = old.isoformat()
        heartbeat = datetime.now(timezone.utc) - timedelta(
            minutes=heartbeat_minutes
        )
        owner["heartbeat_at"] = heartbeat.isoformat()
        owner_path.write_text(json.dumps(owner))

    def test_new_paused_lane_initialization_then_twelve_counted_occurrences(self):
        for automation_id in ("mathreadingvault-serre", "mathreadingvault-cohen"):
            with self.subTest(automation_id=automation_id):
                self.write_automation(automation_id, "PAUSED", 100)
                control.command_initialize(self.args("initialize", automation_id))
                path = self.vault / control.SPECS[automation_id]["runtime"]
                baseline = path.read_bytes()
                with self.assertRaises(control.ControlError):
                    control.command_initialize(self.args("initialize", automation_id))
                self.assertEqual(path.read_bytes(), baseline)
                config = self.automations / automation_id / "automation.toml"
                config.write_text(config.read_text().replace('"PAUSED"', '"ACTIVE"').replace("updated_at = 100", "updated_at = 200"))
                for occurrence in range(1, 13):
                    control.command_claim(self.args("claim", automation_id))
                    self.assertEqual(self.owner(automation_id)["occurrence"], occurrence)
                    self.age_current_claim(automation_id, 55)
                    control.command_complete(self.args("complete", automation_id))
                    runtime = json.loads(path.read_text())
                    self.assertEqual(runtime["completed_occurrences"], occurrence)
                    self.assertEqual(runtime["pause_required"], occurrence == 12)
                control.command_claim(self.args("claim", automation_id))
                self.assertFalse((self.vault / control.SPECS[automation_id]["lock"]).exists())
                self.assertEqual(json.loads(path.read_text())["completed_occurrences"], 12)

    def test_initialization_rejects_active_automation_without_writing(self):
        automation_id = "mathreadingvault-serre"
        self.write_automation(automation_id, "ACTIVE", 100)
        with self.assertRaises(control.ControlError):
            control.command_initialize(self.args("initialize", automation_id))
        self.assertFalse((self.vault / control.SPECS[automation_id]["runtime"]).exists())

    def test_fresh_activation_claims_and_completes_one_hour_batch(self):
        automation_id = "mathreadingvault-dieudonne"
        self.write_automation(automation_id, "ACTIVE", 200)
        runtime_path = self.write_runtime(
            automation_id, status="dormant", completed=0, baseline=100
        )

        self.assertEqual(control.command_claim(self.args("claim", automation_id)), 0)
        runtime = json.loads(runtime_path.read_text())
        self.assertEqual(runtime["status"], "running")
        self.assertEqual(runtime["current_occurrence"], 1)

        self.age_current_claim(automation_id, 50)
        complete_args = self.args("complete", automation_id)
        self.assertEqual(
            control.command_complete(complete_args), 0
        )
        runtime = json.loads(runtime_path.read_text())
        self.assertEqual(runtime["status"], "pause_required")
        self.assertEqual(runtime["completed_occurrences"], 1)
        self.assertIsNotNone(runtime["pause_attempt_started_at"])
        self.assertIsNotNone(runtime["pause_retry_not_before_at"])

        automation_file = (
            self.automations / automation_id / "automation.toml"
        )
        text = automation_file.read_text()
        automation_file.write_text(
            text.replace('status = "ACTIVE"', 'status = "PAUSED"').replace(
                "updated_at = 200", "updated_at = 300"
            )
        )
        self.assertEqual(
            control.command_confirm_paused(
                self.args("confirm-paused", automation_id)
            ),
            0,
        )
        runtime = json.loads(runtime_path.read_text())
        self.assertEqual(runtime["status"], "completed")
        self.assertFalse(runtime["pause_required"])
        self.assertIsNone(runtime["pause_attempt_started_at"])
        self.assertIsNone(runtime["pause_retry_not_before_at"])
        self.assertEqual(runtime["last_paused_automation_updated_at"], 300)

    def test_pause_lease_suppresses_duplicate_hourly_pause_request(self):
        automation_id = "mathreadingvault-dieudonne"
        self.write_automation(automation_id, "ACTIVE", 200)
        runtime_path = self.write_runtime(
            automation_id, status="dormant", completed=0, baseline=100
        )

        self.assertEqual(
            control.command_claim(self.args("claim", automation_id)), 0
        )
        self.age_current_claim(automation_id, 50)
        self.assertEqual(
            control.command_complete(self.args("complete", automation_id)),
            0,
        )
        first = json.loads(runtime_path.read_text())

        self.set_thread("test-thread-b")
        self.assertEqual(
            control.command_claim(self.args("claim", automation_id)), 0
        )
        second = json.loads(runtime_path.read_text())
        self.assertEqual(
            second["pause_attempt_started_at"],
            first["pause_attempt_started_at"],
        )
        self.assertFalse(
            (self.vault / control.SPECS[automation_id]["lock"]).exists()
        )

    def test_expired_pause_lease_authorizes_one_retry(self):
        automation_id = "mathreadingvault-dieudonne"
        self.write_automation(automation_id, "ACTIVE", 200)
        runtime_path = self.write_runtime(
            automation_id,
            status="pause_required",
            completed=1,
            baseline=100,
        )
        runtime = json.loads(runtime_path.read_text())
        runtime["pause_required"] = True
        runtime["pause_unconfirmed"] = True
        runtime["pause_retry_count"] = 0
        old = datetime.now(timezone.utc) - timedelta(
            minutes=control.PAUSE_RETRY_MINUTES + 1
        )
        runtime["pause_attempt_started_at"] = old.isoformat()
        runtime["pause_retry_not_before_at"] = (
            old + timedelta(minutes=control.PAUSE_RETRY_MINUTES)
        ).isoformat()
        runtime_path.write_text(json.dumps(runtime))

        self.assertEqual(
            control.command_claim(self.args("claim", automation_id)), 0
        )
        retried = json.loads(runtime_path.read_text())
        self.assertEqual(retried["pause_retry_count"], 1)
        self.assertGreater(
            control.parse_time(retried["pause_attempt_started_at"]),
            old,
        )

    def test_no_fresh_activation_does_not_start(self):
        automation_id = "mathreadingvault-neukirch-marcus"
        self.write_automation(automation_id, "ACTIVE", 100)
        runtime_path = self.write_runtime(
            automation_id, status="completed", completed=1, baseline=100
        )
        self.assertEqual(control.command_claim(self.args("claim", automation_id)), 0)
        runtime = json.loads(runtime_path.read_text())
        self.assertEqual(runtime["status"], "completed")
        lock = self.vault / control.SPECS[automation_id]["lock"]
        self.assertFalse(lock.exists())

    def test_main_batch_continues_after_nonterminal_completion(self):
        automation_id = (
            "math-reading-vault-neukirch-marcus-deep-study"
        )
        self.write_automation(automation_id, "ACTIVE", 200)
        runtime_path = self.write_runtime(
            automation_id, status="completed", completed=13, baseline=100,
            target=13,
        )
        self.assertEqual(control.command_claim(self.args("claim", automation_id)), 0)
        self.assertEqual(json.loads(runtime_path.read_text())["target_occurrences"], 12)
        self.age_current_claim(automation_id, 55)
        complete_args = self.args("complete", automation_id)
        self.assertEqual(
            control.command_complete(complete_args), 0
        )
        runtime = json.loads(runtime_path.read_text())
        self.assertEqual(runtime["status"], "armed")
        self.assertEqual(runtime["completed_occurrences"], 1)
        self.assertEqual(control.command_claim(self.args("claim", automation_id)), 0)
        runtime = json.loads(runtime_path.read_text())
        self.assertEqual(runtime["current_occurrence"], 2)

    def test_twelve_occurrence_lanes_stop_and_do_not_claim_thirteenth(self):
        for automation_id, spec in control.SPECS.items():
            if spec["target"] != 12:
                continue
            with self.subTest(automation_id=automation_id):
                self.write_automation(automation_id, "ACTIVE", 200)
                path = self.write_runtime(
                    automation_id, status="armed", completed=11,
                    baseline=100,
                    target=13 if spec["run_kind"] == "manual-main-batch" else 12,
                )
                control.command_claim(self.args("claim", automation_id))
                self.assertEqual(self.owner(automation_id)["occurrence"], 12)
                self.age_current_claim(automation_id, spec["minimum_minutes"] + 5)
                control.command_complete(self.args("complete", automation_id))
                runtime = json.loads(path.read_text())
                self.assertEqual(runtime["completed_occurrences"], 12)
                self.assertEqual(runtime["target_occurrences"], 12)
                self.assertTrue(runtime["pause_required"])
                control.command_claim(self.args("claim", automation_id))
                self.assertEqual(json.loads(path.read_text()), runtime)
                self.assertFalse((self.vault / spec["lock"]).exists())

    def test_legacy_running_owner_adopts_twelve_without_reset_or_interruption(self):
        automation_id = "math-reading-vault-dieudonne-infinitesimal-calculus-deep-study"
        spec = control.SPECS[automation_id]
        self.write_automation(automation_id, "ACTIVE", 200)
        path = self.write_runtime(
            automation_id, status="armed", completed=1, baseline=100, target=9,
        )
        # Create the actual pre-change owner with the old target.
        with mock.patch.dict(spec, {"target": 9}):
            control.command_claim(self.args("claim", automation_id))
        before = json.loads(path.read_text())
        owner_before = self.owner(automation_id)
        control.command_heartbeat(self.args("heartbeat", automation_id))
        after = json.loads(path.read_text())
        self.assertEqual(after, {**before, "target_occurrences": 12})
        owner_after = self.owner(automation_id)
        for key in owner_before:
            if key not in {"target_occurrences", "heartbeat_at"}:
                self.assertEqual(owner_after[key], owner_before[key])
        self.assertEqual(owner_after["target_occurrences"], 12)
        self.age_current_claim(automation_id, 55)
        control.command_complete(self.args("complete", automation_id))
        self.assertEqual(json.loads(path.read_text())["completed_occurrences"], 2)

    def test_legacy_ninth_owner_continues_to_twelve_without_migration_heartbeat(self):
        automation_id = "math-reading-vault-neukirch-marcus-deep-study"
        self.write_automation(automation_id, "ACTIVE", 200)
        path = self.write_runtime(
            automation_id, status="armed", completed=8, baseline=100, target=9,
        )
        with mock.patch.dict(control.SPECS[automation_id], {"target": 9}):
            control.command_claim(self.args("claim", automation_id))
        self.age_current_claim(automation_id, 55)
        control.command_complete(self.args("complete", automation_id))
        runtime = json.loads(path.read_text())
        self.assertEqual(runtime["target_occurrences"], 12)
        self.assertEqual(runtime["completed_occurrences"], 9)
        self.assertEqual(runtime["status"], "armed")
        self.assertFalse(runtime["pause_required"])

    def test_paused_legacy_history_is_preserved_until_user_reactivation(self):
        automation_id = "math-reading-vault-apostol-analysis-and-analytic-nt"
        self.write_automation(automation_id, "PAUSED", 200)
        path = self.write_runtime(
            automation_id, status="completed", completed=13,
            baseline=100, target=13,
        )
        before = path.read_bytes()
        control.command_inspect(self.args("inspect", automation_id))
        control.command_claim(self.args("claim", automation_id))
        self.assertEqual(path.read_bytes(), before)
        config = self.automations / automation_id / "automation.toml"
        config.write_text(config.read_text().replace('"PAUSED"', '"ACTIVE"'))
        control.command_claim(self.args("claim", automation_id))
        runtime = json.loads(path.read_text())
        self.assertEqual(runtime["target_occurrences"], 12)
        self.assertEqual(runtime["completed_occurrences"], 0)
        self.assertEqual(runtime["current_occurrence"], 1)

    def test_legacy_six_owner_adopts_twelve_without_reset(self):
        for automation_id in (
            "math-reading-vault-lang-algebra-gtm211-deep-study",
            "mathreadingvault-brualdi-beck-robins",
        ):
            with self.subTest(automation_id=automation_id):
                spec = control.SPECS[automation_id]
                self.write_automation(automation_id, "ACTIVE", 200)
                path = self.write_runtime(
                    automation_id, status="armed", completed=2,
                    baseline=100, target=6,
                )
                with mock.patch.dict(spec, {"target": 6}):
                    control.command_claim(self.args("claim", automation_id))
                before = json.loads(path.read_text())
                owner_before = self.owner(automation_id)
                control.command_heartbeat(self.args("heartbeat", automation_id))
                after = json.loads(path.read_text())
                self.assertEqual(after, {**before, "target_occurrences": 12})
                owner_after = self.owner(automation_id)
                for key in owner_before:
                    if key not in {"target_occurrences", "heartbeat_at"}:
                        self.assertEqual(owner_after[key], owner_before[key])
                self.age_current_claim(automation_id, spec["minimum_minutes"] + 5)
                control.command_complete(self.args("complete", automation_id))
                self.assertEqual(json.loads(path.read_text())["completed_occurrences"], 3)

    def test_legacy_sixth_completion_continues_to_twelve(self):
        for automation_id in (
            "math-reading-vault-lang-algebra-gtm211-deep-study",
            "mathreadingvault-brualdi-beck-robins",
        ):
            with self.subTest(automation_id=automation_id):
                spec = control.SPECS[automation_id]
                self.write_automation(automation_id, "ACTIVE", 200)
                path = self.write_runtime(
                    automation_id, status="armed", completed=5,
                    baseline=100, target=6,
                )
                with mock.patch.dict(spec, {"target": 6}):
                    control.command_claim(self.args("claim", automation_id))
                self.age_current_claim(automation_id, spec["minimum_minutes"] + 5)
                control.command_complete(self.args("complete", automation_id))
                runtime = json.loads(path.read_text())
                self.assertEqual(runtime["target_occurrences"], 12)
                self.assertEqual(runtime["completed_occurrences"], 6)
                self.assertEqual(runtime["status"], "armed")
                self.assertFalse(runtime["pause_required"])

    def test_completed_six_history_waits_for_explicit_reactivation(self):
        for automation_id in (
            "math-reading-vault-lang-algebra-gtm211-deep-study",
            "mathreadingvault-brualdi-beck-robins",
        ):
            with self.subTest(automation_id=automation_id):
                self.write_automation(automation_id, "PAUSED", 100)
                path = self.write_runtime(
                    automation_id, status="completed", completed=6,
                    baseline=100, target=6,
                )
                before = path.read_bytes()
                control.command_inspect(self.args("inspect", automation_id))
                control.command_claim(self.args("claim", automation_id))
                self.assertEqual(path.read_bytes(), before)
                config = self.automations / automation_id / "automation.toml"
                config.write_text(config.read_text().replace('"PAUSED"', '"ACTIVE"').replace('updated_at = 100', 'updated_at = 200'))
                control.command_claim(self.args("claim", automation_id))
                runtime = json.loads(path.read_text())
                self.assertEqual(runtime["target_occurrences"], 12)
                self.assertEqual(runtime["completed_occurrences"], 0)
                self.assertEqual(runtime["current_occurrence"], 1)

    def test_all_reading_specs_use_fifty_minute_mathematics_budget(self):
        for automation_id, spec in control.SPECS.items():
            with self.subTest(automation_id=automation_id):
                self.assertEqual(spec["minimum_minutes"], 50)
                self.assertIn("about 50 minutes of direct mathematics", spec["time_budget"])
                self.assertGreaterEqual(spec["wrap_minutes"], 60)
                self.assertIn(spec["lease_minutes"], {75, 90})
                expected = 1 if spec["run_kind"] == "one-hour-remainder-sprint" else 12
                self.assertEqual(spec["target"], expected)

    def test_fresh_claims_reject_less_than_fifty_minutes_on_every_lane(self):
        for automation_id, spec in control.SPECS.items():
            with self.subTest(automation_id=automation_id):
                self.write_automation(automation_id, "ACTIVE", 200)
                path = self.write_runtime(
                    automation_id, status="dormant", completed=0, baseline=100,
                )
                control.command_claim(self.args("claim", automation_id))
                owner = self.owner(automation_id)
                self.assertEqual(owner["minimum_minutes"], 50)
                self.assertEqual(owner["mathematics_target_minutes"], 50)
                self.age_current_claim(automation_id, 49)
                with self.assertRaises(control.ControlError):
                    control.command_complete(self.args("complete", automation_id))
                self.assertEqual(json.loads(path.read_text())["completed_occurrences"], 0)
                self.assertTrue((self.vault / spec["lock"]).exists())
                self.age_current_claim(automation_id, 55)
                control.command_complete(self.args("complete", automation_id))
                self.assertEqual(json.loads(path.read_text())["completed_occurrences"], 1)

    def test_legacy_inflight_timing_contract_is_not_extended_or_rejected(self):
        for automation_id, old_minimum, old_wrap in (
            ("math-reading-vault-neukirch-marcus-deep-study", 30, 45),
            ("mathreadingvault-brualdi-beck-robins", 40, 65),
        ):
            with self.subTest(automation_id=automation_id):
                spec = control.SPECS[automation_id]
                self.write_automation(automation_id, "ACTIVE", 200)
                path = self.write_runtime(
                    automation_id, status="armed", completed=2, baseline=100,
                )
                with mock.patch.dict(spec, {"minimum_minutes": old_minimum, "wrap_minutes": old_wrap}):
                    control.command_claim(self.args("claim", automation_id))
                owner_path = self.vault / spec["lock"] / "owner.json"
                owner = self.owner(automation_id)
                owner.pop("minimum_minutes")
                owner.pop("mathematics_target_minutes")
                owner_path.write_text(json.dumps(owner))
                original_expiry = owner["lease_expires_at"]
                control.command_heartbeat(self.args("heartbeat", automation_id))
                after = self.owner(automation_id)
                self.assertEqual(after["wrap_minutes"], old_wrap)
                self.assertEqual(after["lease_expires_at"], original_expiry)
                self.age_current_claim(automation_id, old_minimum + 2)
                control.command_complete(self.args("complete", automation_id))
                self.assertEqual(json.loads(path.read_text())["completed_occurrences"], 3)
                control.command_claim(self.args("claim", automation_id))
                self.assertEqual(self.owner(automation_id)["minimum_minutes"], 50)

    def test_claimed_minimum_stays_frozen_until_completion(self):
        automation_id = "mathreadingvault-cohen"
        self.write_automation(automation_id, "ACTIVE", 200)
        path = self.write_runtime(
            automation_id, status="dormant", completed=0, baseline=100,
        )
        control.command_claim(self.args("claim", automation_id))
        self.age_current_claim(automation_id, 55)
        with mock.patch.dict(control.SPECS[automation_id], {"minimum_minutes": 60}):
            control.command_complete(self.args("complete", automation_id))
        self.assertEqual(json.loads(path.read_text())["completed_occurrences"], 1)

    def test_six_target_is_not_accepted_by_unrelated_lanes(self):
        for automation_id, spec in control.SPECS.items():
            if spec["run_kind"] in {
                "manual-six-hour-combinatorics-batch",
                "manual-lang-six-occurrence-batch",
            }:
                continue
            path = self.write_runtime(
                automation_id, status="armed", completed=0,
                baseline=100, target=6,
            )
            with self.assertRaises(control.ControlError):
                control.validate_runtime(json.loads(path.read_text()), automation_id, spec)

    def test_target_compatibility_is_limited_to_known_main_targets(self):
        for automation_id, spec in control.SPECS.items():
            path = self.write_runtime(
                automation_id, status="armed", completed=0, baseline=100,
                target=10 if spec["run_kind"] == "manual-main-batch" else 13,
            )
            with self.assertRaises(control.ControlError):
                control.validate_runtime(json.loads(path.read_text()), automation_id, spec)
            if spec["run_kind"] not in {"manual-main-batch", "manual-twelve-occurrence-batch"}:
                expected = 1 if spec["run_kind"] == "one-hour-remainder-sprint" else 12
                self.assertEqual(spec["target"], expected)

    def test_stale_lock_is_recovered_without_thread_listing(self):
        automation_id = "mathreadingvault-apostol-stein"
        self.write_automation(automation_id, "ACTIVE", 200)
        runtime_path = self.write_runtime(
            automation_id, status="running", completed=0, baseline=100
        )
        runtime = json.loads(runtime_path.read_text())
        old = datetime.now(timezone.utc) - timedelta(minutes=160)
        runtime["current_occurrence"] = 1
        runtime["current_started_at"] = old.isoformat()
        runtime["manual_rearm_required"] = False
        runtime["sprint_id"] = "old-sprint"
        runtime_path.write_text(json.dumps(runtime))
        lock = self.vault / control.SPECS[automation_id]["lock"]
        lock.parent.mkdir(parents=True, exist_ok=True)
        lock.mkdir()
        (lock / "owner.json").write_text(
            json.dumps(
                {
                    "automation_id": automation_id,
                    "sprint_id": "old-sprint",
                    "occurrence": 1,
                    "started_at": old.isoformat(),
                    "heartbeat_at": old.isoformat(),
                    "control_protocol_version": 2,
                    "owner_thread_id": "old-thread",
                    "claim_token": "old-token",
                }
            )
        )

        self.assertEqual(control.command_claim(self.args("claim", automation_id)), 0)
        runtime = json.loads(runtime_path.read_text())
        self.assertIsNone(runtime["current_occurrence"])
        self.assertEqual(runtime["status"], "armed")
        self.assertIn("last_interrupted", runtime)
        self.assertNotIn(
            "claim_token",
            json.dumps(runtime["last_interrupted"]),
        )
        self.assertFalse(lock.exists())

        self.assertEqual(control.command_claim(self.args("claim", automation_id)), 0)
        runtime = json.loads(runtime_path.read_text())
        self.assertEqual(runtime["current_occurrence"], 1)
        self.assertEqual(runtime["status"], "running")
        self.assertNotEqual(
            self.owner(automation_id)["owner_thread_id"], "old-thread"
        )

    def test_fresh_heartbeat_prevents_recovery_within_lease(self):
        automation_id = "mathreadingvault-dieudonne"
        self.write_automation(automation_id, "ACTIVE", 200)
        runtime_path = self.write_runtime(
            automation_id, status="dormant", completed=0, baseline=100
        )
        self.assertEqual(control.command_claim(self.args("claim", automation_id)), 0)
        old = datetime.now(timezone.utc) - timedelta(minutes=50)
        runtime = json.loads(runtime_path.read_text())
        runtime["current_started_at"] = old.isoformat()
        runtime["occurrence_started_at"] = old.isoformat()
        runtime_path.write_text(json.dumps(runtime))
        owner_path = (
            self.vault / control.SPECS[automation_id]["lock"] / "owner.json"
        )
        owner = json.loads(owner_path.read_text())
        owner["started_at"] = old.isoformat()
        owner_path.write_text(json.dumps(owner))

        heartbeat_args = self.args("heartbeat", automation_id)
        self.assertEqual(control.command_heartbeat(heartbeat_args), 0)
        self.assertEqual(control.command_claim(self.args("claim", automation_id)), 0)
        self.assertTrue(owner_path.exists())
        runtime = json.loads(runtime_path.read_text())
        self.assertEqual(runtime["current_occurrence"], 1)

    def test_claim_binds_owner_to_current_codex_thread(self):
        automation_id = (
            "math-reading-vault-neukirch-marcus-deep-study"
        )
        self.write_automation(automation_id, "ACTIVE", 200)
        self.write_runtime(
            automation_id, status="armed", completed=3, baseline=100
        )
        self.assertEqual(
            control.command_claim(self.args("claim", automation_id)), 0
        )
        owner = self.owner(automation_id)
        self.assertEqual(owner["owner_thread_id"], "test-thread-a")
        self.assertEqual(
            owner["control_protocol_version"],
            control.CONTROL_PROTOCOL_VERSION,
        )
        self.assertNotIn("claim_token", owner)

    def test_protocol_version_change_rejects_old_owner(self):
        automation_id = (
            "math-reading-vault-apostol-analysis-and-analytic-nt"
        )
        self.write_automation(automation_id, "ACTIVE", 200)
        self.write_runtime(
            automation_id, status="armed", completed=2, baseline=100
        )
        self.assertEqual(
            control.command_claim(self.args("claim", automation_id)), 0
        )
        owner_path = (
            self.vault
            / control.SPECS[automation_id]["lock"]
            / "owner.json"
        )
        owner = json.loads(owner_path.read_text())
        owner["control_protocol_version"] = (
            control.CONTROL_PROTOCOL_VERSION - 1
        )
        owner_path.write_text(json.dumps(owner))
        with self.assertRaises(control.ControlError):
            control.command_heartbeat(
                self.args("heartbeat", automation_id)
            )

    def test_orphan_runtime_recovery_exits_before_reclaim(self):
        automation_id = (
            "math-reading-vault-apostol-analysis-and-analytic-nt"
        )
        self.write_automation(automation_id, "ACTIVE", 200)
        runtime_path = self.write_runtime(
            automation_id, status="running", completed=2, baseline=100
        )
        old = datetime.now(timezone.utc) - timedelta(minutes=40)
        runtime = json.loads(runtime_path.read_text())
        runtime["manual_rearm_required"] = False
        runtime["sprint_id"] = "live-sprint"
        runtime["current_occurrence"] = 3
        runtime["current_started_at"] = old.isoformat()
        runtime["occurrence_started_at"] = old.isoformat()
        runtime_path.write_text(json.dumps(runtime))

        self.assertEqual(
            control.command_claim(self.args("claim", automation_id)), 0
        )
        runtime = json.loads(runtime_path.read_text())
        lock = self.vault / control.SPECS[automation_id]["lock"]
        self.assertIsNone(runtime["current_occurrence"])
        self.assertEqual(runtime["status"], "armed")
        self.assertFalse(lock.exists())

        self.assertEqual(
            control.command_claim(self.args("claim", automation_id)), 0
        )
        runtime = json.loads(runtime_path.read_text())
        self.assertEqual(runtime["current_occurrence"], 3)

    def test_silent_owner_is_recovered_at_next_hour(self):
        automation_id = "mathreadingvault-neukirch-marcus"
        self.write_automation(automation_id, "ACTIVE", 200)
        runtime_path = self.write_runtime(
            automation_id, status="dormant", completed=0, baseline=100
        )
        self.assertEqual(
            control.command_claim(self.args("claim", automation_id)), 0
        )
        self.age_current_claim(
            automation_id, 40, heartbeat_minutes=40
        )

        self.assertEqual(
            control.command_claim(self.args("claim", automation_id)), 0
        )
        runtime = json.loads(runtime_path.read_text())
        lock = self.vault / control.SPECS[automation_id]["lock"]
        self.assertIsNone(runtime["current_occurrence"])
        self.assertEqual(runtime["status"], "armed")
        self.assertEqual(
            runtime["last_interrupted"]["reason"],
            "heartbeat-timeout",
        )
        self.assertFalse(lock.exists())

    def test_absolute_lease_expires_even_with_recent_heartbeat(self):
        automation_id = (
            "math-reading-vault-neukirch-marcus-deep-study"
        )
        self.write_automation(automation_id, "ACTIVE", 200)
        runtime_path = self.write_runtime(
            automation_id, status="armed", completed=3, baseline=100
        )
        runtime = json.loads(runtime_path.read_text())
        runtime["manual_rearm_required"] = False
        runtime["sprint_id"] = "live-sprint"
        runtime_path.write_text(json.dumps(runtime))
        self.assertEqual(
            control.command_claim(self.args("claim", automation_id)), 0
        )
        self.age_current_claim(automation_id, 80)

        self.assertEqual(
            control.command_claim(self.args("claim", automation_id)), 0
        )
        runtime = json.loads(runtime_path.read_text())
        self.assertIsNone(runtime["current_occurrence"])
        self.assertEqual(
            runtime["last_interrupted"]["reason"],
            "occurrence-lease-expired",
        )

    def test_delayed_owner_heartbeat_self_expires_noncounted(self):
        automation_id = (
            "math-reading-vault-dieudonne-infinitesimal-calculus-deep-study"
        )
        self.write_automation(automation_id, "ACTIVE", 200)
        runtime_path = self.write_runtime(
            automation_id, status="armed", completed=4, baseline=100
        )
        runtime = json.loads(runtime_path.read_text())
        runtime["manual_rearm_required"] = False
        runtime["sprint_id"] = "live-sprint"
        runtime_path.write_text(json.dumps(runtime))
        self.assertEqual(
            control.command_claim(self.args("claim", automation_id)), 0
        )
        self.age_current_claim(
            automation_id, 40, heartbeat_minutes=40
        )
        heartbeat_args = self.args("heartbeat", automation_id)

        self.assertEqual(control.command_heartbeat(heartbeat_args), 0)
        runtime = json.loads(runtime_path.read_text())
        lock = self.vault / control.SPECS[automation_id]["lock"]
        self.assertIsNone(runtime["current_occurrence"])
        self.assertEqual(runtime["completed_occurrences"], 4)
        self.assertFalse(lock.exists())

    def test_old_thread_cannot_complete_replacement_claim(self):
        automation_id = "math-reading-vault-dieudonne-infinitesimal-calculus-deep-study"
        self.write_automation(automation_id, "ACTIVE", 200)
        runtime_path = self.write_runtime(
            automation_id, status="armed", completed=8, baseline=100
        )
        runtime = json.loads(runtime_path.read_text())
        runtime["manual_rearm_required"] = False
        runtime["sprint_id"] = "live-sprint"
        runtime_path.write_text(json.dumps(runtime))

        self.assertEqual(control.command_claim(self.args("claim", automation_id)), 0)
        self.age_current_claim(
            automation_id, 160, heartbeat_minutes=160
        )
        self.assertEqual(control.command_claim(self.args("claim", automation_id)), 0)
        self.set_thread("test-thread-b")
        self.assertEqual(control.command_claim(self.args("claim", automation_id)), 0)
        self.assertEqual(
            self.owner(automation_id)["owner_thread_id"], "test-thread-b"
        )
        self.age_current_claim(automation_id, 55)

        self.set_thread("test-thread-a")
        stale_complete = self.args("complete", automation_id)
        with self.assertRaises(control.ControlError):
            control.command_complete(stale_complete)

        self.set_thread("test-thread-b")
        current_complete = self.args("complete", automation_id)
        self.assertEqual(control.command_complete(current_complete), 0)

    def test_twelve_hour_combinatorics_batch_requires_twelve_long_occurrences(self):
        automation_id = "mathreadingvault-brualdi-beck-robins"
        self.write_automation(automation_id, "ACTIVE", 200)
        runtime_path = self.write_runtime(
            automation_id, status="dormant", completed=0, baseline=100
        )
        spec = control.SPECS[automation_id]
        lock = self.vault / spec["lock"]

        for occurrence in range(1, 13):
            self.assertEqual(
                control.command_claim(self.args("claim", automation_id)), 0
            )
            runtime = json.loads(runtime_path.read_text())
            self.assertEqual(runtime["current_occurrence"], occurrence)

            self.age_current_claim(automation_id, 50)

            complete_args = self.args("complete", automation_id)
            self.assertEqual(
                control.command_complete(complete_args),
                0,
            )

        runtime = json.loads(runtime_path.read_text())
        self.assertEqual(runtime["completed_occurrences"], 12)
        self.assertEqual(runtime["status"], "pause_required")
        self.assertTrue(runtime["manual_rearm_required"])
        self.assertFalse(lock.exists())

    def test_combinatorics_short_occurrence_cannot_be_counted(self):
        automation_id = "mathreadingvault-brualdi-beck-robins"
        self.write_automation(automation_id, "ACTIVE", 200)
        runtime_path = self.write_runtime(
            automation_id, status="dormant", completed=0, baseline=100
        )
        self.assertEqual(
            control.command_claim(self.args("claim", automation_id)), 0
        )

        complete_args = self.args("complete", automation_id)
        with self.assertRaises(control.ControlError):
            control.command_complete(complete_args)

        runtime = json.loads(runtime_path.read_text())
        self.assertEqual(runtime["completed_occurrences"], 0)
        self.assertEqual(runtime["current_occurrence"], 1)

    def test_lang_batch_requires_twelve_qualified_occurrences(self):
        automation_id = (
            "math-reading-vault-lang-algebra-gtm211-deep-study"
        )
        self.write_automation(automation_id, "ACTIVE", 200)
        runtime_path = self.write_runtime(
            automation_id, status="dormant", completed=0, baseline=100
        )
        spec = control.SPECS[automation_id]
        lock = self.vault / spec["lock"]

        for occurrence in range(1, 13):
            self.assertEqual(
                control.command_claim(self.args("claim", automation_id)), 0
            )
            runtime = json.loads(runtime_path.read_text())
            self.assertEqual(runtime["current_occurrence"], occurrence)

            self.age_current_claim(automation_id, 55)

            complete_args = self.args("complete", automation_id)
            self.assertEqual(
                control.command_complete(complete_args),
                0,
            )

        runtime = json.loads(runtime_path.read_text())
        self.assertEqual(runtime["completed_occurrences"], 12)
        self.assertEqual(runtime["status"], "pause_required")
        self.assertTrue(runtime["manual_rearm_required"])
        self.assertFalse(lock.exists())

    def test_lang_short_occurrence_cannot_be_counted(self):
        automation_id = (
            "math-reading-vault-lang-algebra-gtm211-deep-study"
        )
        self.write_automation(automation_id, "ACTIVE", 200)
        runtime_path = self.write_runtime(
            automation_id, status="dormant", completed=0, baseline=100
        )
        self.assertEqual(
            control.command_claim(self.args("claim", automation_id)), 0
        )

        complete_args = self.args("complete", automation_id)
        with self.assertRaises(control.ControlError):
            control.command_complete(complete_args)

        runtime = json.loads(runtime_path.read_text())
        self.assertEqual(runtime["completed_occurrences"], 0)
        self.assertEqual(runtime["current_occurrence"], 1)

    def credit_fixture(self, completed=6):
        automation_id = "math-reading-vault-apostol-analysis-and-analytic-nt"
        self.write_automation(automation_id, "ACTIVE", 200)
        path = self.write_runtime(automation_id, status="armed", completed=completed, baseline=100)
        runtime = json.loads(path.read_text())
        ended = datetime.now(timezone.utc) - timedelta(minutes=5)
        started = ended - timedelta(minutes=76)
        runtime["sprint_id"] = "credit-test-sprint"
        runtime["last_interrupted"] = {
            "at": ended.isoformat(),
            "reason": "occurrence-lease-expired",
            "noncounted": True,
            "occurrence": completed + 1,
            "previous_owner": {
                "automation_id": automation_id,
                "sprint_id": runtime["sprint_id"],
                "occurrence": completed + 1,
                "started_at": started.isoformat(),
                "minimum_minutes": 50,
            },
        }
        path.write_text(json.dumps(runtime))
        log = self.vault / "Books/test/runs/submitted.md"
        log.parent.mkdir(parents=True)
        log.write_text("durable validated submission")
        args = self.args("credit-interrupted", automation_id, "explicit user: count this occurrence")
        args.user_authorized = True
        args.sprint_id = runtime["sprint_id"]
        args.occurrence = completed + 1
        args.started_at = started.isoformat()
        args.run_log = str(log.relative_to(self.vault))
        return path, args

    def test_user_credit_is_audited_idempotent_and_preserves_interruption(self):
        path, args = self.credit_fixture()
        original = json.loads(path.read_text())["last_interrupted"]
        control.command_credit_interrupted(args)
        runtime = json.loads(path.read_text())
        self.assertEqual(runtime["completed_occurrences"], 7)
        self.assertEqual(runtime["status"], "armed")
        self.assertEqual(runtime["last_interrupted"], original)
        self.assertEqual(len(runtime["user_authorized_credits"]), 1)
        self.assertFalse((self.vault / control.SPECS[args.automation_id]["lock"]).exists())
        baseline = path.read_bytes()
        control.command_credit_interrupted(args)
        self.assertEqual(path.read_bytes(), baseline)

    def test_user_credit_rejects_missing_authorization_and_wrong_identity(self):
        path, args = self.credit_fixture()
        for field, value in (("user_authorized", False), ("sprint_id", "wrong"),
                             ("occurrence", 8), ("started_at", "2000-01-01T00:00:00Z"),
                             ("run_log", "missing.md")):
            with self.subTest(field=field):
                original = getattr(args, field)
                setattr(args, field, value)
                baseline = path.read_bytes()
                with self.assertRaises(control.ControlError):
                    control.command_credit_interrupted(args)
                self.assertEqual(path.read_bytes(), baseline)
                self.assertFalse((self.vault / control.SPECS[args.automation_id]["lock"]).exists())
                setattr(args, field, original)

    def test_user_credit_uses_original_duration_and_rejects_other_interruptions(self):
        path, args = self.credit_fixture()
        original = json.loads(path.read_text())
        for short, reason in ((True, "occurrence-lease-expired"), (False, "heartbeat-timeout")):
            runtime = json.loads(json.dumps(original))
            runtime["last_interrupted"]["reason"] = reason
            if short:
                start = control.parse_time(args.started_at)
                runtime["last_interrupted"]["at"] = (start + timedelta(minutes=20)).isoformat()
            path.write_text(json.dumps(runtime))
            baseline = path.read_bytes()
            with self.assertRaises(control.ControlError):
                control.command_credit_interrupted(args)
            self.assertEqual(path.read_bytes(), baseline)

    def test_user_credit_does_not_disturb_existing_lock_or_current_occurrence(self):
        path, args = self.credit_fixture()
        lock = self.vault / control.SPECS[args.automation_id]["lock"]
        lock.mkdir()
        owner = lock / "owner.json"
        owner.write_text('{"automation_id": "another-owner"}')
        baseline = path.read_bytes()
        with self.assertRaises(control.ControlError):
            control.command_credit_interrupted(args)
        self.assertEqual(path.read_bytes(), baseline)
        self.assertEqual(owner.read_text(), '{"automation_id": "another-owner"}')
        owner.unlink()
        lock.rmdir()
        runtime = json.loads(path.read_text())
        runtime["current_occurrence"] = 7
        path.write_text(json.dumps(runtime))
        baseline = path.read_bytes()
        with self.assertRaises(control.ControlError):
            control.command_credit_interrupted(args)
        self.assertEqual(path.read_bytes(), baseline)

    def test_final_user_credit_requires_pause(self):
        path, args = self.credit_fixture(completed=11)
        control.command_credit_interrupted(args)
        runtime = json.loads(path.read_text())
        self.assertEqual(runtime["completed_occurrences"], 12)
        self.assertTrue(runtime["pause_required"])
        self.assertEqual(runtime["status"], "pause_required")
        self.assertIsNotNone(runtime["pause_attempt_started_at"])

    def test_user_credit_never_releases_a_replacement_lock(self):
        path, args = self.credit_fixture()
        baseline = path.read_bytes()
        lock = self.vault / control.SPECS[args.automation_id]["lock"]
        replacement = {"automation_id": args.automation_id, "operation_id": "replacement"}
        def replaced(*unused):
            (lock / "owner.json").write_text(json.dumps(replacement))
            raise control.ControlError("replacement claim")
        with mock.patch.object(control, "credit_interrupted_locked", side_effect=replaced):
            with self.assertRaises(control.ControlError):
                control.command_credit_interrupted(args)
        self.assertEqual(path.read_bytes(), baseline)
        self.assertEqual(json.loads((lock / "owner.json").read_text()), replacement)

    def test_stale_administrative_lock_does_not_replace_interruption(self):
        path, args = self.credit_fixture()
        lock = self.vault / control.SPECS[args.automation_id]["lock"]
        lock.mkdir()
        old = (datetime.now(timezone.utc) - timedelta(minutes=40)).isoformat()
        owner = {"automation_id": args.automation_id, "operation": "credit-interrupted",
                 "started_at": old, "heartbeat_at": old}
        (lock / "owner.json").write_text(json.dumps(owner))
        baseline = path.read_bytes()
        result = control.recover_stale_lock(self.vault, lock, owner)
        self.assertEqual(result["decision"], "EXIT")
        self.assertEqual(path.read_bytes(), baseline)
        self.assertFalse(lock.exists())

    def test_sanitize_history_removes_durable_claim_tokens(self):
        automation_id = (
            "math-reading-vault-neukirch-marcus-deep-study"
        )
        self.write_automation(automation_id, "ACTIVE", 200)
        runtime_path = self.write_runtime(
            automation_id, status="armed", completed=3, baseline=100
        )
        runtime = json.loads(runtime_path.read_text())
        runtime["last_interrupted"] = {
            "reason": "legacy",
            "previous_owner": {
                "occurrence": 4,
                "claim_token": "must-not-persist",
            },
        }
        runtime_path.write_text(json.dumps(runtime))

        self.assertEqual(
            control.command_sanitize_history(
                self.args("sanitize-history", automation_id)
            ),
            0,
        )
        runtime = json.loads(runtime_path.read_text())
        self.assertNotIn("claim_token", json.dumps(runtime))


if __name__ == "__main__":
    unittest.main()
