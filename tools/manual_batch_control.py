#!/usr/bin/env python3
"""Deterministic control plane for manually activated reading batches.

This script owns only automation/runtime/lock bookkeeping. It never reads or
writes mathematical notes. Every command emits one JSON object so a scheduled
task can branch without calling thread-list tools or assembling cleanup shell.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, Optional, Tuple


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_VAULT_ROOT = REPOSITORY_ROOT
DEFAULT_AUTOMATIONS_ROOT = REPOSITORY_ROOT / ".local-automations"
HEARTBEAT_TIMEOUT_MINUTES = 35
ORPHAN_RUNTIME_TIMEOUT_MINUTES = 35
PAUSE_RETRY_MINUTES = 120
CONTROL_PROTOCOL_VERSION = 4
MATHEMATICS_TARGET_MINUTES = 50
MINIMUM_OCCURRENCE_MINUTES = 50
OCCURRENCE_TIME_BUDGET = "55-60 minutes; about 50 minutes of direct mathematics"

SPECS: Dict[str, Dict[str, Any]] = {
    "math-reading-vault-neukirch-marcus-deep-study": {
        "lane": "neukirch_marcus",
        "runtime": "Infrastructure/sprint_runtime/neukirch_marcus.json",
        "lock": "Infrastructure/sprint_runtime/neukirch_marcus.lock",
        "target": 12,
        "run_kind": "manual-main-batch",
        "time_budget": OCCURRENCE_TIME_BUDGET,
        "minimum_minutes": MINIMUM_OCCURRENCE_MINUTES,
        "wrap_minutes": 60,
        "lease_minutes": 75,
    },
    "math-reading-vault-apostol-analysis-and-analytic-nt": {
        "lane": "apostol_stein",
        "runtime": "Infrastructure/sprint_runtime/apostol_stein.json",
        "lock": "Infrastructure/sprint_runtime/apostol_stein.lock",
        "target": 12,
        "run_kind": "manual-main-batch",
        "time_budget": OCCURRENCE_TIME_BUDGET,
        "minimum_minutes": MINIMUM_OCCURRENCE_MINUTES,
        "wrap_minutes": 60,
        "lease_minutes": 75,
    },
    "math-reading-vault-dieudonne-infinitesimal-calculus-deep-study": {
        "lane": "dieudonne",
        "runtime": "Infrastructure/sprint_runtime/dieudonne.json",
        "lock": "Infrastructure/sprint_runtime/dieudonne.lock",
        "target": 12,
        "run_kind": "manual-main-batch",
        "time_budget": OCCURRENCE_TIME_BUDGET,
        "minimum_minutes": MINIMUM_OCCURRENCE_MINUTES,
        "wrap_minutes": 60,
        "lease_minutes": 75,
    },
    "mathreadingvault-neukirch-marcus": {
        "lane": "neukirch_marcus",
        "runtime": (
            "Infrastructure/remainder_sprint_runtime/neukirch_marcus.json"
        ),
        "lock": "Infrastructure/sprint_runtime/neukirch_marcus.lock",
        "target": 1,
        "run_kind": "one-hour-remainder-sprint",
        "time_budget": OCCURRENCE_TIME_BUDGET,
        "minimum_minutes": MINIMUM_OCCURRENCE_MINUTES,
        "wrap_minutes": 65,
        "lease_minutes": 90,
    },
    "mathreadingvault-apostol-stein": {
        "lane": "apostol_stein",
        "runtime": (
            "Infrastructure/remainder_sprint_runtime/apostol_stein.json"
        ),
        "lock": "Infrastructure/sprint_runtime/apostol_stein.lock",
        "target": 1,
        "run_kind": "one-hour-remainder-sprint",
        "time_budget": OCCURRENCE_TIME_BUDGET,
        "minimum_minutes": MINIMUM_OCCURRENCE_MINUTES,
        "wrap_minutes": 65,
        "lease_minutes": 90,
    },
    "mathreadingvault-dieudonne": {
        "lane": "dieudonne",
        "runtime": "Infrastructure/remainder_sprint_runtime/dieudonne.json",
        "lock": "Infrastructure/sprint_runtime/dieudonne.lock",
        "target": 1,
        "run_kind": "one-hour-remainder-sprint",
        "time_budget": OCCURRENCE_TIME_BUDGET,
        "minimum_minutes": MINIMUM_OCCURRENCE_MINUTES,
        "wrap_minutes": 65,
        "lease_minutes": 90,
    },
    "mathreadingvault-brualdi-beck-robins": {
        "lane": "brualdi_stanley_beck_robins",
        "runtime": (
            "Infrastructure/sprint_runtime/"
            "brualdi_stanley_beck_robins.json"
        ),
        "lock": (
            "Infrastructure/sprint_runtime/"
            "brualdi_stanley_beck_robins.lock"
        ),
        "target": 12,
        "run_kind": "manual-six-hour-combinatorics-batch",
        "time_budget": OCCURRENCE_TIME_BUDGET,
        "minimum_minutes": MINIMUM_OCCURRENCE_MINUTES,
        "wrap_minutes": 65,
        "lease_minutes": 90,
    },
    "math-reading-vault-lang-algebra-gtm211-deep-study": {
        "lane": "lang_algebra",
        "runtime": "Infrastructure/sprint_runtime/lang_algebra.json",
        "lock": "Infrastructure/sprint_runtime/lang_algebra.lock",
        "target": 12,
        "run_kind": "manual-lang-six-occurrence-batch",
        "time_budget": OCCURRENCE_TIME_BUDGET,
        "minimum_minutes": MINIMUM_OCCURRENCE_MINUTES,
        "wrap_minutes": 60,
        "lease_minutes": 75,
    },
    "mathreadingvault-serre": {
        "lane": "serre_finite_groups",
        "runtime": "Infrastructure/sprint_runtime/serre_finite_groups.json",
        "lock": "Infrastructure/sprint_runtime/serre_finite_groups.lock",
        "target": 12,
        "run_kind": "manual-twelve-occurrence-batch",
        "time_budget": OCCURRENCE_TIME_BUDGET,
        "minimum_minutes": MINIMUM_OCCURRENCE_MINUTES,
        "wrap_minutes": 60,
        "lease_minutes": 75,
    },
    "mathreadingvault-cohen": {
        "lane": "cohen_number_theory",
        "runtime": "Infrastructure/sprint_runtime/cohen_number_theory.json",
        "lock": "Infrastructure/sprint_runtime/cohen_number_theory.lock",
        "target": 12,
        "run_kind": "manual-twelve-occurrence-batch",
        "time_budget": OCCURRENCE_TIME_BUDGET,
        "minimum_minutes": MINIMUM_OCCURRENCE_MINUTES,
        "wrap_minutes": 60,
        "lease_minutes": 75,
    },
}


class ControlError(RuntimeError):
    """A control-plane invariant was violated."""


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def iso_now() -> str:
    return now_utc().astimezone().isoformat(timespec="seconds")


def current_thread_id() -> str:
    """Return the immutable Codex task identity inherited by tool calls."""
    value = os.environ.get("CODEX_THREAD_ID", "").strip()
    if not value:
        raise ControlError(
            "CODEX_THREAD_ID is required for ownership-sensitive commands"
        )
    return value


def emit(payload: Dict[str, Any]) -> int:
    print(json.dumps(payload, ensure_ascii=False, sort_keys=True))
    return 0


def read_json(path: Path) -> Dict[str, Any]:
    try:
        value = json.loads(path.read_text())
    except Exception as exc:
        raise ControlError(f"cannot read JSON {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ControlError(f"JSON root is not an object: {path}")
    return value


def atomic_write_json(path: Path, value: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(
        f".{path.name}.tmp-{os.getpid()}-{uuid.uuid4().hex}"
    )
    try:
        with temporary.open("x", encoding="utf-8") as handle:
            json.dump(value, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(str(temporary), str(path))
    finally:
        if temporary.exists():
            temporary.unlink()


def toml_json_field(text: str, name: str) -> Any:
    match = re.search(rf"^{re.escape(name)} = (.+)$", text, re.MULTILINE)
    if not match:
        raise ControlError(f"automation.toml missing field: {name}")
    try:
        return json.loads(match.group(1))
    except json.JSONDecodeError as exc:
        raise ControlError(f"invalid automation.toml field {name}") from exc


def read_automation(
    automations_root: Path, automation_id: str
) -> Dict[str, Any]:
    path = automations_root / automation_id / "automation.toml"
    try:
        text = path.read_text()
    except Exception as exc:
        raise ControlError(f"cannot read automation config {path}: {exc}") from exc
    return {
        "path": str(path),
        "id": toml_json_field(text, "id"),
        "status": toml_json_field(text, "status"),
        "updated_at": toml_json_field(text, "updated_at"),
    }


def parse_time(value: Any) -> Optional[datetime]:
    if not isinstance(value, str) or not value:
        return None
    normalized = value.replace("Z", "+00:00")
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def runtime_started_at(runtime: Dict[str, Any]) -> Optional[datetime]:
    for key in (
        "current_started_at",
        "occurrence_started_at",
        "activated_at",
    ):
        parsed = parse_time(runtime.get(key))
        if parsed is not None:
            return parsed
    return None


def lock_age_minutes(lock_path: Path, owner: Dict[str, Any]) -> float:
    started = parse_time(owner.get("heartbeat_at"))
    if started is None:
        started = parse_time(owner.get("started_at"))
    if started is None:
        started = datetime.fromtimestamp(
            lock_path.stat().st_mtime, tz=timezone.utc
        )
    return max(0.0, (now_utc() - started).total_seconds() / 60.0)


def occurrence_age_minutes(
    lock_path: Path, owner: Dict[str, Any]
) -> float:
    started = parse_time(owner.get("started_at"))
    if started is None:
        started = datetime.fromtimestamp(
            lock_path.stat().st_mtime, tz=timezone.utc
        )
    return max(0.0, (now_utc() - started).total_seconds() / 60.0)


def redact_private_owner_fields(value: Any) -> Any:
    if isinstance(value, dict):
        return {
            key: redact_private_owner_fields(item)
            for key, item in value.items()
            if key not in {"claim_token", "owner_thread_id"}
        }
    if isinstance(value, list):
        return [redact_private_owner_fields(item) for item in value]
    return value


def public_owner(owner: Dict[str, Any]) -> Dict[str, Any]:
    return redact_private_owner_fields(owner)


def write_runtime(path: Path, runtime: Dict[str, Any]) -> None:
    sanitized = redact_private_owner_fields(runtime)
    runtime.clear()
    runtime.update(sanitized)
    atomic_write_json(path, runtime)


def owner_expiry(
    lock_path: Path,
    owner: Dict[str, Any],
    spec: Optional[Dict[str, Any]],
) -> Dict[str, Any]:
    heartbeat_age = lock_age_minutes(lock_path, owner)
    occurrence_age = occurrence_age_minutes(lock_path, owner)
    lease_minutes = None if spec is None else int(spec["lease_minutes"])
    bases = []
    if heartbeat_age >= HEARTBEAT_TIMEOUT_MINUTES:
        bases.append("heartbeat-timeout")
    if lease_minutes is not None and occurrence_age >= lease_minutes:
        bases.append("occurrence-lease-expired")
    return {
        "expired": bool(bases),
        "recovery_basis": bases,
        "heartbeat_age_minutes": round(heartbeat_age, 1),
        "occurrence_age_minutes": round(occurrence_age, 1),
        "heartbeat_timeout_minutes": HEARTBEAT_TIMEOUT_MINUTES,
        "lease_minutes": lease_minutes,
    }


def read_owner(lock_path: Path) -> Dict[str, Any]:
    owner_json = lock_path / "owner.json"
    if owner_json.exists():
        try:
            return read_json(owner_json)
        except ControlError:
            return {"owner_file": "invalid"}
    return {"owner_file": "missing"}


def release_lock(
    lock_path: Path,
    automation_id: str,
    *,
    allow_stale: bool = False,
) -> None:
    if not lock_path.exists():
        return
    if not lock_path.is_dir():
        raise ControlError(f"lock path is not a directory: {lock_path}")
    owner = read_owner(lock_path)
    owner_id = owner.get("automation_id")
    if not allow_stale and owner_id != automation_id:
        raise ControlError(
            f"lock owner mismatch: expected {automation_id}, got {owner_id}"
        )
    allowed = {"owner.json", "owner.md"}
    unexpected = [item.name for item in lock_path.iterdir() if item.name not in allowed]
    if unexpected:
        raise ControlError(f"lock contains unexpected files: {unexpected}")
    for item in list(lock_path.iterdir()):
        item.unlink()
    lock_path.rmdir()


def paths_for(
    vault_root: Path, automation_id: str
) -> Tuple[Dict[str, Any], Path, Path]:
    if automation_id not in SPECS:
        raise ControlError(f"unknown automation id: {automation_id}")
    spec = SPECS[automation_id]
    return (
        spec,
        vault_root / spec["runtime"],
        vault_root / spec["lock"],
    )


def validate_runtime(
    runtime: Dict[str, Any], automation_id: str, spec: Dict[str, Any]
) -> None:
    if runtime.get("automation_id") != automation_id:
        raise ControlError(
            "runtime automation_id does not match the requested automation"
        )
    if runtime.get("lane") != spec["lane"]:
        raise ControlError("runtime lane does not match the control mapping")
    runtime_target = int(runtime.get("target_occurrences", -1))
    # Target changes must preserve active ownership and completed history.
    # Owned writes adopt the current configured target without resetting work.
    legacy_main_target = (
        spec["run_kind"] == "manual-main-batch"
        and spec["target"] == 12
        and runtime_target in {9, 13}
    )
    legacy_six_target = (
        spec["run_kind"] in {
            "manual-six-hour-combinatorics-batch",
            "manual-lang-six-occurrence-batch",
        }
        and spec["target"] == 12
        and runtime_target == 6
    )
    if (
        runtime_target != spec["target"]
        and not legacy_main_target
        and not legacy_six_target
    ):
        raise ControlError("runtime target_occurrences does not match the mapping")


def recover_stale_lock(
    vault_root: Path,
    lock_path: Path,
    owner: Dict[str, Any],
) -> Dict[str, Any]:
    owner_id = owner.get("automation_id")
    owner_spec = SPECS.get(owner_id) if isinstance(owner_id, str) else None
    expiry = owner_expiry(lock_path, owner, owner_spec)
    if not expiry["expired"]:
        return {
            "decision": "EXIT",
            "reason": "lock-busy",
            **expiry,
            "owner": public_owner(owner),
        }
    if not isinstance(owner_id, str) or owner_id not in SPECS:
        raise ControlError("cannot recover expired lock with unknown owner")
    owner_spec, owner_runtime_path, expected_lock_path = paths_for(
        vault_root, owner_id
    )
    if expected_lock_path != lock_path:
        raise ControlError("stale lock path does not match owner mapping")
    if owner.get("operation") == "credit-interrupted":
        # An administrative lock never starts a mathematical occurrence.
        # Recovering it must not replace the original interruption evidence.
        release_lock(lock_path, owner_id, allow_stale=True)
        return {
            "decision": "EXIT",
            "reason": "stale-lock-recovered-no-math",
            **expiry,
            "previous_owner": public_owner(owner),
        }
    owner_runtime = read_json(owner_runtime_path)
    validate_runtime(owner_runtime, owner_id, owner_spec)
    interrupted_owner = public_owner(owner)
    owner_runtime["last_interrupted"] = {
        "at": iso_now(),
        "reason": "+".join(expiry["recovery_basis"]),
        "noncounted": True,
        "occurrence": owner.get("occurrence"),
        "previous_owner": interrupted_owner,
        "heartbeat_age_minutes": expiry["heartbeat_age_minutes"],
        "occurrence_age_minutes": expiry["occurrence_age_minutes"],
    }
    if (
        owner_runtime.get("current_occurrence") == owner.get("occurrence")
        and owner_runtime.get("sprint_id") == owner.get("sprint_id")
    ):
        owner_runtime["current_occurrence"] = None
        owner_runtime["current_started_at"] = None
        owner_runtime["occurrence_started_at"] = None
    if int(owner_runtime.get("completed_occurrences", 0)) >= int(
        owner_runtime.get("target_occurrences", 0)
    ):
        owner_runtime["status"] = "pause_required"
        owner_runtime["pause_required"] = True
    else:
        owner_runtime["status"] = "armed"
    write_runtime(owner_runtime_path, owner_runtime)
    release_lock(lock_path, owner_id, allow_stale=True)
    return {
        "decision": "EXIT",
        "reason": "stale-lock-recovered-no-math",
        **expiry,
        "previous_owner": interrupted_owner,
    }


def validate_claim_identity(
    runtime: Dict[str, Any],
    owner: Dict[str, Any],
    automation_id: str,
) -> None:
    if owner.get("automation_id") != automation_id:
        raise ControlError("claim owner belongs to another automation")
    if owner.get("control_protocol_version") != CONTROL_PROTOCOL_VERSION:
        raise ControlError(
            "lock owner uses an incompatible control protocol version"
        )
    if owner.get("owner_thread_id") != current_thread_id():
        raise ControlError(
            "current Codex task does not own the lane lock"
        )
    if runtime.get("current_occurrence") != owner.get("occurrence"):
        raise ControlError("owner occurrence and runtime occurrence differ")
    if runtime.get("sprint_id") != owner.get("sprint_id"):
        raise ControlError("owner sprint_id and runtime sprint_id differ")


def expire_owned_occurrence(
    runtime_path: Path,
    lock_path: Path,
    runtime: Dict[str, Any],
    owner: Dict[str, Any],
    automation_id: str,
    spec: Dict[str, Any],
    expiry: Dict[str, Any],
) -> Dict[str, Any]:
    runtime["last_interrupted"] = {
        "at": iso_now(),
        "reason": "+".join(expiry["recovery_basis"]),
        "noncounted": True,
        "occurrence": owner.get("occurrence"),
        "previous_owner": public_owner(owner),
        "heartbeat_age_minutes": expiry["heartbeat_age_minutes"],
        "occurrence_age_minutes": expiry["occurrence_age_minutes"],
    }
    runtime["current_occurrence"] = None
    runtime["current_started_at"] = None
    runtime["occurrence_started_at"] = None
    if int(runtime.get("completed_occurrences", 0)) >= int(
        spec["target"]
    ):
        runtime["status"] = "pause_required"
        runtime["pause_required"] = True
    else:
        runtime["status"] = "armed"
    write_runtime(runtime_path, runtime)
    release_lock(lock_path, automation_id)
    return {
        "decision": "OWNERSHIP_EXPIRED_NONCOUNTED",
        "occurrence": owner.get("occurrence"),
        **expiry,
    }


def initialize_new_batch(
    runtime: Dict[str, Any],
    spec: Dict[str, Any],
    config_updated_at: int,
) -> None:
    stamp = now_utc().astimezone().strftime("%Y%m%dT%H%M%S%z")
    runtime["sprint_id"] = (
        f"{spec['lane']}-{stamp}-{uuid.uuid4().hex[:6]}"
    )
    runtime["activated_at"] = iso_now()
    runtime["activation_source"] = "direct-user-activation"
    runtime["activation_config_updated_at"] = config_updated_at
    runtime["target_occurrences"] = spec["target"]
    runtime["completed_occurrences"] = 0
    runtime["completed_at"] = None
    runtime["last_completed_at"] = None
    runtime["current_occurrence"] = None
    runtime["current_started_at"] = None
    runtime["occurrence_started_at"] = None
    runtime["next_expected_start"] = None
    runtime["manual_rearm_required"] = False
    runtime["pause_required"] = False
    runtime["pause_unconfirmed"] = False
    runtime["pause_retry_count"] = 0
    runtime["pause_attempt_started_at"] = None
    runtime["pause_retry_not_before_at"] = None
    runtime["last_pause_error"] = None
    runtime["status"] = "armed"


def begin_pause_attempt(
    runtime: Dict[str, Any],
    *,
    retry: bool,
) -> Dict[str, Any]:
    started = now_utc().astimezone()
    retry_at = started + timedelta(minutes=PAUSE_RETRY_MINUTES)
    runtime["pause_attempt_started_at"] = started.isoformat(timespec="seconds")
    runtime["pause_retry_not_before_at"] = retry_at.isoformat(timespec="seconds")
    runtime["pause_unconfirmed"] = True
    if retry:
        runtime["pause_retry_count"] = (
            int(runtime.get("pause_retry_count", 0)) + 1
        )
    return {
        "pause_attempt_started_at": runtime["pause_attempt_started_at"],
        "pause_retry_not_before_at": runtime["pause_retry_not_before_at"],
        "pause_retry_minutes": PAUSE_RETRY_MINUTES,
    }


def pause_attempt_wait(runtime: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    started = parse_time(runtime.get("pause_attempt_started_at"))
    if started is None:
        return None
    elapsed = max(0.0, (now_utc() - started).total_seconds() / 60.0)
    if elapsed >= PAUSE_RETRY_MINUTES:
        return None
    return {
        "decision": "EXIT",
        "reason": "pause-update-in-flight",
        "pause_attempt_age_minutes": round(elapsed, 1),
        "pause_retry_minutes": PAUSE_RETRY_MINUTES,
        "pause_retry_not_before_at": runtime.get(
            "pause_retry_not_before_at"
        ),
    }


def command_initialize(args: argparse.Namespace) -> int:
    """Prepare a new paused lane without claiming or resetting any batch."""
    spec, runtime_path, lock_path = paths_for(args.vault_root, args.automation_id)
    config = read_automation(args.automations_root, args.automation_id)
    if config["id"] != args.automation_id or config["status"] != "PAUSED":
        raise ControlError("initialization requires the matching PAUSED automation")
    if runtime_path.exists() or lock_path.exists():
        raise ControlError("initialization cannot overwrite an existing runtime or lock")
    runtime = {
        "schema_version": 2,
        "automation_id": args.automation_id,
        "lane": spec["lane"],
        "target_occurrences": spec["target"],
        "status": "dormant",
        "sprint_id": None,
        "completed_occurrences": 0,
        "current_occurrence": None,
        "current_started_at": None,
        "occurrence_started_at": None,
        "manual_rearm_required": True,
        "pause_required": False,
        "pause_unconfirmed": False,
        "last_paused_automation_updated_at": int(config["updated_at"]),
        "initialized_at": iso_now(),
    }
    write_runtime(runtime_path, runtime)
    return emit({"decision": "INITIALIZED", "target_occurrences": spec["target"]})


def command_claim(args: argparse.Namespace) -> int:
    spec, runtime_path, lock_path = paths_for(
        args.vault_root, args.automation_id
    )
    config = read_automation(args.automations_root, args.automation_id)
    runtime = read_json(runtime_path)
    validate_runtime(runtime, args.automation_id, spec)

    if config["id"] != args.automation_id:
        raise ControlError("automation.toml id mismatch")
    if config["status"] != "ACTIVE":
        return emit({"decision": "EXIT", "reason": "automation-not-active"})
    if runtime.get("pause_required") or runtime.get("status") == "pause_required":
        wait = pause_attempt_wait(runtime)
        if wait is not None:
            return emit(wait)
        pause = begin_pause_attempt(runtime, retry=True)
        write_runtime(runtime_path, runtime)
        return emit(
            {
                "decision": "PAUSE_ONLY",
                "reason": "pause-retry-authorized",
                "fast_path": True,
                **pause,
            }
        )

    if lock_path.exists():
        owner = read_owner(lock_path)
        recovered = recover_stale_lock(
            args.vault_root,
            lock_path,
            owner,
        )
        return emit(recovered)

    lock_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        lock_path.mkdir()
    except FileExistsError:
        return emit({"decision": "EXIT", "reason": "lock-race-lost"})

    try:
        config = read_automation(args.automations_root, args.automation_id)
        runtime = read_json(runtime_path)
        validate_runtime(runtime, args.automation_id, spec)
        if config["status"] != "ACTIVE":
            release_lock(lock_path, args.automation_id, allow_stale=True)
            return emit(
                {"decision": "EXIT", "reason": "automation-became-paused"}
            )

        completed = int(runtime.get("completed_occurrences", 0))
        target = spec["target"]
        if completed >= target:
            if runtime.get("manual_rearm_required", True):
                baseline = int(
                    runtime.get("last_paused_automation_updated_at", 0)
                )
                if int(config["updated_at"]) <= baseline:
                    release_lock(
                        lock_path, args.automation_id, allow_stale=True
                    )
                    return emit(
                        {
                            "decision": "EXIT",
                            "reason": "no-fresh-user-activation",
                        }
                    )
                initialize_new_batch(runtime, spec, int(config["updated_at"]))
                completed = 0
            else:
                runtime["status"] = "pause_required"
                runtime["pause_required"] = True
                pause = begin_pause_attempt(runtime, retry=True)
                write_runtime(runtime_path, runtime)
                release_lock(lock_path, args.automation_id, allow_stale=True)
                return emit(
                    {
                        "decision": "PAUSE_ONLY",
                        "reason": "target-already-met",
                        "fast_path": True,
                        **pause,
                    }
                )
        elif runtime.get("status") in {"completed", "dormant"}:
            if runtime.get("manual_rearm_required", True):
                baseline = int(
                    runtime.get("last_paused_automation_updated_at", 0)
                )
                if int(config["updated_at"]) <= baseline:
                    release_lock(
                        lock_path, args.automation_id, allow_stale=True
                    )
                    return emit(
                        {
                            "decision": "EXIT",
                            "reason": "no-fresh-user-activation",
                        }
                    )
                initialize_new_batch(runtime, spec, int(config["updated_at"]))
                completed = 0

        current = runtime.get("current_occurrence")
        if current is not None:
            started = runtime_started_at(runtime)
            if started is None or (
                now_utc() - started
            ).total_seconds() < ORPHAN_RUNTIME_TIMEOUT_MINUTES * 60:
                release_lock(lock_path, args.automation_id, allow_stale=True)
                return emit(
                    {
                        "decision": "EXIT",
                        "reason": "runtime-current-without-stale-lock",
                        "runtime_orphan_timeout_minutes": (
                            ORPHAN_RUNTIME_TIMEOUT_MINUTES
                        ),
                    }
                )
            runtime["last_interrupted"] = {
                "at": iso_now(),
                "reason": "stale-runtime-recovery",
                "noncounted": True,
                "occurrence": current,
            }
            runtime["current_occurrence"] = None
            runtime["current_started_at"] = None
            runtime["occurrence_started_at"] = None
            runtime["status"] = "armed"
            write_runtime(runtime_path, runtime)
            release_lock(lock_path, args.automation_id, allow_stale=True)
            return emit(
                {
                    "decision": "EXIT",
                    "reason": "orphan-runtime-recovered-no-math",
                    "occurrence": current,
                    "runtime_orphan_timeout_minutes": (
                        ORPHAN_RUNTIME_TIMEOUT_MINUTES
                    ),
                }
            )

        occurrence = int(runtime.get("completed_occurrences", 0)) + 1
        if occurrence > target:
            runtime["status"] = "pause_required"
            runtime["pause_required"] = True
            pause = begin_pause_attempt(runtime, retry=True)
            write_runtime(runtime_path, runtime)
            release_lock(lock_path, args.automation_id, allow_stale=True)
            return emit(
                {
                    "decision": "PAUSE_ONLY",
                    "reason": "occurrence-overflow",
                    "fast_path": True,
                    **pause,
                }
            )

        previous_interruption = runtime.get("last_interrupted")
        interrupted_occurrence = None
        if isinstance(previous_interruption, dict):
            interrupted_occurrence = previous_interruption.get("occurrence")
            previous_owner = previous_interruption.get("previous_owner")
            if (
                interrupted_occurrence is None
                and isinstance(previous_owner, dict)
            ):
                interrupted_occurrence = previous_owner.get("occurrence")
        if interrupted_occurrence != occurrence:
            previous_interruption = None

        started = now_utc().astimezone()
        started_at = started.isoformat(timespec="seconds")
        wrap_minutes = int(spec["wrap_minutes"])
        lease_minutes = int(spec["lease_minutes"])
        wrap_at = (
            started + timedelta(minutes=wrap_minutes)
        ).isoformat(timespec="seconds")
        lease_expires_at = (
            started + timedelta(minutes=lease_minutes)
        ).isoformat(timespec="seconds")
        runtime["target_occurrences"] = target
        runtime["status"] = "running"
        runtime["current_occurrence"] = occurrence
        runtime["current_started_at"] = started_at
        runtime["occurrence_started_at"] = started_at
        runtime["next_expected_start"] = None
        write_runtime(runtime_path, runtime)
        owner = {
            "automation_id": args.automation_id,
            "lane": spec["lane"],
            "sprint_id": runtime.get("sprint_id"),
            "occurrence": occurrence,
            "target_occurrences": target,
            "started_at": started_at,
            "heartbeat_at": started_at,
            "heartbeat_timeout_minutes": HEARTBEAT_TIMEOUT_MINUTES,
            "minimum_minutes": spec["minimum_minutes"],
            "mathematics_target_minutes": MATHEMATICS_TARGET_MINUTES,
            "wrap_minutes": wrap_minutes,
            "wrap_at": wrap_at,
            "lease_minutes": lease_minutes,
            "lease_expires_at": lease_expires_at,
            "control_protocol_version": CONTROL_PROTOCOL_VERSION,
            "owner_thread_id": current_thread_id(),
        }
        atomic_write_json(lock_path / "owner.json", owner)
        payload = {
            "decision": "START",
            "lane": spec["lane"],
            "sprint_id": runtime.get("sprint_id"),
            "occurrence": occurrence,
            "target_occurrences": target,
            "run_kind": spec["run_kind"],
            "time_budget": spec["time_budget"],
            "minimum_minutes": spec["minimum_minutes"],
            "mathematics_target_minutes": MATHEMATICS_TARGET_MINUTES,
            "heartbeat_timeout_minutes": HEARTBEAT_TIMEOUT_MINUTES,
            "wrap_minutes": wrap_minutes,
            "wrap_at": wrap_at,
            "lease_minutes": lease_minutes,
            "lease_expires_at": lease_expires_at,
            "ownership": "codex-thread-bound",
            "control_protocol_version": CONTROL_PROTOCOL_VERSION,
            "runtime": str(runtime_path),
            "lock": str(lock_path),
        }
        if isinstance(previous_interruption, dict):
            payload["previous_interruption"] = redact_private_owner_fields(
                previous_interruption
            )
            payload["reconcile_interrupted_run_log"] = True
        return emit(payload)
    except Exception:
        if lock_path.exists():
            try:
                release_lock(lock_path, args.automation_id, allow_stale=True)
            except Exception:
                pass
        raise


def command_complete(args: argparse.Namespace) -> int:
    spec, runtime_path, lock_path = paths_for(
        args.vault_root, args.automation_id
    )
    runtime = read_json(runtime_path)
    validate_runtime(runtime, args.automation_id, spec)
    if not lock_path.exists():
        raise ControlError("cannot complete without the lane lock")
    owner = read_owner(lock_path)
    validate_claim_identity(
        runtime, owner, args.automation_id
    )
    expiry = owner_expiry(lock_path, owner, spec)
    if expiry["expired"]:
        return emit(
            expire_owned_occurrence(
                runtime_path,
                lock_path,
                runtime,
                owner,
                args.automation_id,
                spec,
                expiry,
            )
        )
    occurrence = int(owner.get("occurrence", -1))
    expected = int(runtime.get("completed_occurrences", 0)) + 1
    if occurrence != expected:
        raise ControlError("occurrence is not the next countable occurrence")
    minimum_minutes = owner.get("minimum_minutes")
    if minimum_minutes is None:
        # Pre-change owners did not pin a minimum. Keep their original
        # timing contract; new claims always record the current minimum.
        minimum_minutes = {45: 30, 65: 40}.get(
            owner.get("wrap_minutes"), spec.get("minimum_minutes")
        )
    if minimum_minutes is not None:
        started = parse_time(owner.get("started_at"))
        if started is None:
            raise ControlError("counted occurrence has no valid start time")
        elapsed_minutes = (
            now_utc() - started
        ).total_seconds() / 60.0
        if elapsed_minutes < float(minimum_minutes):
            raise ControlError(
                "occurrence is too short to count: "
                f"{elapsed_minutes:.1f} < {minimum_minutes} minutes"
            )

    timestamp = iso_now()
    runtime["target_occurrences"] = spec["target"]
    runtime["completed_occurrences"] = occurrence
    runtime["last_completed_at"] = timestamp
    runtime["current_occurrence"] = None
    runtime["current_started_at"] = None
    runtime["occurrence_started_at"] = None
    runtime["next_expected_start"] = None
    if occurrence >= spec["target"]:
        runtime["completed_at"] = timestamp
        runtime["manual_rearm_required"] = True
        runtime["pause_required"] = True
        runtime["status"] = "pause_required"
        pause = begin_pause_attempt(runtime, retry=False)
        decision = "PAUSE_SELF"
    else:
        runtime["status"] = "armed"
        pause = {}
        decision = "CONTINUE"
    write_runtime(runtime_path, runtime)
    release_lock(lock_path, args.automation_id)
    return emit(
        {
            "decision": decision,
            "completed_occurrences": occurrence,
            "target_occurrences": spec["target"],
            **pause,
        }
    )


def command_credit_interrupted(args: argparse.Namespace) -> int:
    """Credit one lease-expired submission only on explicit user instruction.

    The caller verifies the durable submission; the controller records its
    run-log path without reading mathematical notes. Ordinary completion and
    claim timing rules are unchanged.
    """
    if not getattr(args, "user_authorized", False):
        raise ControlError("retroactive credit requires explicit user authorization")
    if not args.reason.strip() or args.reason == "unspecified":
        raise ControlError("retroactive credit requires the user's instruction")
    if not args.sprint_id or args.occurrence is None or not args.started_at:
        raise ControlError("credit requires exact sprint, occurrence and original start")
    requested_start = parse_time(args.started_at)
    if requested_start is None or not args.run_log:
        raise ControlError("credit requires a valid original start and durable run log")
    log_path = (args.vault_root / args.run_log).resolve()
    try:
        relative_log = str(log_path.relative_to(args.vault_root.resolve()))
    except ValueError as exc:
        raise ControlError("credit run log must be inside the vault") from exc
    if not log_path.is_file() or log_path.suffix != ".md" or log_path.parent.name != "runs":
        raise ControlError("credit requires an existing Markdown run log")
    spec, runtime_path, lock_path = paths_for(args.vault_root, args.automation_id)
    thread_id = current_thread_id()
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        lock_path.mkdir()
    except FileExistsError as exc:
        raise ControlError("cannot credit while the lane lock exists") from exc
    lock_identity = (lock_path.stat().st_dev, lock_path.stat().st_ino)
    operation_id = uuid.uuid4().hex
    try:
        timestamp = iso_now()
        atomic_write_json(lock_path / "owner.json", {
            "automation_id": args.automation_id,
            "operation": "credit-interrupted",
            "operation_id": operation_id,
            "started_at": timestamp,
            "heartbeat_at": timestamp,
            "owner_thread_id": thread_id,
        })
        payload = credit_interrupted_locked(
            args, spec, runtime_path, relative_log, requested_start, timestamp,
            lock_path, operation_id,
        )
    finally:
        if lock_path.exists():
            owner = read_owner(lock_path)
            if owner.get("operation_id") == operation_id:
                release_lock(lock_path, args.automation_id)
            elif (lock_path.stat().st_dev, lock_path.stat().st_ino) == lock_identity and not any(lock_path.iterdir()):
                lock_path.rmdir()
    return emit(payload)


def credit_interrupted_locked(
    args: argparse.Namespace, spec: Dict[str, Any], runtime_path: Path,
    relative_log: str, requested_start: datetime, timestamp: str,
    lock_path: Path, operation_id: str,
) -> Dict[str, Any]:
    runtime = read_json(runtime_path)
    validate_runtime(runtime, args.automation_id, spec)
    if runtime.get("sprint_id") != args.sprint_id:
        raise ControlError("credit sprint does not match the current batch")
    identity = {
        "sprint_id": args.sprint_id,
        "occurrence": args.occurrence,
        "original_started_at": args.started_at,
        "run_log": relative_log,
    }
    credits = runtime.get("user_authorized_credits", [])
    if not isinstance(credits, list):
        raise ControlError("invalid credit audit history")
    for credit in credits:
        if not isinstance(credit, dict):
            raise ControlError("invalid credit audit record")
        if all(credit.get(key) == value for key, value in identity.items()):
            if int(runtime.get("completed_occurrences", 0)) < args.occurrence:
                raise ControlError("credit audit and completed count disagree")
            return {
                "decision": "ALREADY_CREDITED",
                "completed_occurrences": runtime["completed_occurrences"],
                "target_occurrences": spec["target"],
                "credit": credit,
            }
    if runtime.get("status") != "armed" or runtime.get("current_occurrence") is not None:
        raise ControlError("credit requires an armed batch without a current occurrence")
    occurrence = int(runtime.get("completed_occurrences", 0)) + 1
    if args.occurrence != occurrence or occurrence > spec["target"]:
        raise ControlError("credit must be exactly the next uncounted occurrence")
    interrupted = runtime.get("last_interrupted")
    if not isinstance(interrupted, dict) or interrupted.get("noncounted") is not True:
        raise ControlError("credit requires the latest noncounted interruption")
    if interrupted.get("reason") != "occurrence-lease-expired":
        raise ControlError("credit is limited to an absolute-lease expiration")
    owner = interrupted.get("previous_owner")
    if not isinstance(owner, dict) or (
        owner.get("automation_id") != args.automation_id
        or owner.get("sprint_id") != args.sprint_id
        or owner.get("occurrence") != occurrence
        or interrupted.get("occurrence") != occurrence
        or parse_time(owner.get("started_at")) != requested_start
    ):
        raise ControlError("credit does not match the original interrupted claim")
    ended = parse_time(interrupted.get("at"))
    minimum = owner.get("minimum_minutes")
    if minimum is None:
        minimum = {45: 30, 65: 40}.get(owner.get("wrap_minutes"), spec["minimum_minutes"])
    if ended is None or (ended - requested_start).total_seconds() < float(minimum) * 60:
        raise ControlError("original interrupted occurrence was too short to count")
    credit = {
        **identity,
        "at": timestamp,
        "authorization": "explicit-user-instruction",
        "reason": args.reason,
        "original_interruption_at": interrupted["at"],
        "original_interruption_reason": interrupted["reason"],
    }
    runtime["user_authorized_credits"] = credits + [credit]
    runtime["target_occurrences"] = spec["target"]
    runtime["completed_occurrences"] = occurrence
    runtime["last_completed_at"] = timestamp
    runtime["current_occurrence"] = None
    runtime["current_started_at"] = None
    runtime["occurrence_started_at"] = None
    runtime["next_expected_start"] = None
    if occurrence >= spec["target"]:
        runtime["completed_at"] = timestamp
        runtime["manual_rearm_required"] = True
        runtime["pause_required"] = True
        runtime["status"] = "pause_required"
        pause = begin_pause_attempt(runtime, retry=False)
        decision = "PAUSE_SELF"
    else:
        pause = {}
        decision = "CONTINUE"
    administrative_owner = read_owner(lock_path)
    if administrative_owner.get("operation_id") != operation_id or owner_expiry(lock_path, administrative_owner, None)["expired"]:
        raise ControlError("administrative credit lock expired or was replaced")
    write_runtime(runtime_path, runtime)
    return {
        "decision": decision,
        "completed_occurrences": occurrence,
        "target_occurrences": spec["target"],
        "credit": credit,
        **pause,
    }


def command_abort(args: argparse.Namespace) -> int:
    spec, runtime_path, lock_path = paths_for(
        args.vault_root, args.automation_id
    )
    runtime = read_json(runtime_path)
    validate_runtime(runtime, args.automation_id, spec)
    if not lock_path.exists():
        raise ControlError("cannot abort without the lane lock")
    owner = read_owner(lock_path)
    validate_claim_identity(
        runtime, owner, args.automation_id
    )
    runtime["last_interrupted"] = {
        "at": iso_now(),
        "reason": args.reason,
        "noncounted": True,
        "owner": public_owner(owner),
    }
    runtime["current_occurrence"] = None
    runtime["current_started_at"] = None
    runtime["occurrence_started_at"] = None
    runtime["status"] = "armed"
    write_runtime(runtime_path, runtime)
    release_lock(lock_path, args.automation_id)
    return emit({"decision": "ABORTED_NONCOUNTED", "reason": args.reason})


def command_heartbeat(args: argparse.Namespace) -> int:
    spec, runtime_path, lock_path = paths_for(
        args.vault_root, args.automation_id
    )
    if not lock_path.exists():
        raise ControlError("cannot heartbeat without the lane lock")
    runtime = read_json(runtime_path)
    validate_runtime(runtime, args.automation_id, spec)
    owner = read_owner(lock_path)
    validate_claim_identity(
        runtime, owner, args.automation_id
    )
    expiry = owner_expiry(lock_path, owner, spec)
    if expiry["expired"]:
        return emit(
            expire_owned_occurrence(
                runtime_path,
                lock_path,
                runtime,
                owner,
                args.automation_id,
                spec,
                expiry,
            )
        )
    timestamp = iso_now()
    if runtime["target_occurrences"] != spec["target"]:
        runtime["target_occurrences"] = spec["target"]
        write_runtime(runtime_path, runtime)
    owner["target_occurrences"] = spec["target"]
    owner["heartbeat_at"] = timestamp
    atomic_write_json(lock_path / "owner.json", owner)
    return emit(
        {
            "decision": "HEARTBEAT",
            "occurrence": owner.get("occurrence"),
            "target_occurrences": spec["target"],
            "heartbeat_at": timestamp,
            "heartbeat_timeout_minutes": HEARTBEAT_TIMEOUT_MINUTES,
            "wrap_minutes": spec["wrap_minutes"],
            "lease_minutes": spec["lease_minutes"],
            "control_protocol_version": CONTROL_PROTOCOL_VERSION,
            "lease_expires_at": owner.get("lease_expires_at"),
        }
    )


def command_confirm_paused(args: argparse.Namespace) -> int:
    spec, runtime_path, lock_path = paths_for(
        args.vault_root, args.automation_id
    )
    if lock_path.exists():
        raise ControlError("cannot confirm pause while the lane lock exists")
    config = read_automation(args.automations_root, args.automation_id)
    if config["status"] != "PAUSED":
        raise ControlError("automation is not PAUSED")
    runtime = read_json(runtime_path)
    validate_runtime(runtime, args.automation_id, spec)
    runtime["last_paused_automation_updated_at"] = int(config["updated_at"])
    runtime["pause_required"] = False
    runtime["pause_unconfirmed"] = False
    runtime["pause_retry_count"] = 0
    runtime["pause_attempt_started_at"] = None
    runtime["pause_retry_not_before_at"] = None
    runtime["last_pause_error"] = None
    runtime["manual_rearm_required"] = True
    if int(runtime.get("completed_occurrences", 0)) >= spec["target"]:
        runtime["status"] = "completed"
    write_runtime(runtime_path, runtime)
    return emit(
        {
            "decision": "PAUSE_CONFIRMED",
            "automation_updated_at": int(config["updated_at"]),
        }
    )


def command_mark_pause_required(args: argparse.Namespace) -> int:
    spec, runtime_path, _ = paths_for(args.vault_root, args.automation_id)
    runtime = read_json(runtime_path)
    validate_runtime(runtime, args.automation_id, spec)
    runtime["status"] = "pause_required"
    runtime["pause_required"] = True
    runtime["pause_unconfirmed"] = True
    runtime["pause_retry_count"] = int(runtime.get("pause_retry_count", 0)) + 1
    runtime["pause_attempt_started_at"] = None
    runtime["pause_retry_not_before_at"] = None
    runtime["last_pause_error"] = {"at": iso_now(), "reason": args.reason}
    write_runtime(runtime_path, runtime)
    return emit({"decision": "PAUSE_REQUIRED_RECORDED"})


def command_inspect(args: argparse.Namespace) -> int:
    spec, runtime_path, lock_path = paths_for(
        args.vault_root, args.automation_id
    )
    config = read_automation(args.automations_root, args.automation_id)
    runtime = read_json(runtime_path)
    validate_runtime(runtime, args.automation_id, spec)
    return emit(
        {
            "decision": "INSPECT",
            "automation_status": config["status"],
            "automation_updated_at": config["updated_at"],
            "runtime_status": runtime.get("status"),
            "sprint_id": runtime.get("sprint_id"),
            "user_authorized_credits": runtime.get("user_authorized_credits", []),
            "completed_occurrences": runtime.get("completed_occurrences"),
            "target_occurrences": runtime.get("target_occurrences"),
            "configured_target_occurrences": spec["target"],
            "current_occurrence": runtime.get("current_occurrence"),
            "pause_required": runtime.get("pause_required"),
            "pause_attempt_started_at": runtime.get(
                "pause_attempt_started_at"
            ),
            "pause_retry_not_before_at": runtime.get(
                "pause_retry_not_before_at"
            ),
            "pause_retry_minutes": PAUSE_RETRY_MINUTES,
            "lock_exists": lock_path.exists(),
            "heartbeat_timeout_minutes": HEARTBEAT_TIMEOUT_MINUTES,
            "wrap_minutes": spec["wrap_minutes"],
            "lease_minutes": spec["lease_minutes"],
            "control_protocol_version": CONTROL_PROTOCOL_VERSION,
            "ownership": "codex-thread-bound",
        }
    )


def command_sanitize_history(args: argparse.Namespace) -> int:
    spec, runtime_path, _ = paths_for(args.vault_root, args.automation_id)
    runtime = read_json(runtime_path)
    validate_runtime(runtime, args.automation_id, spec)
    sanitized = redact_private_owner_fields(runtime)
    changed = sanitized != runtime
    if changed:
        write_runtime(runtime_path, runtime)
    return emit(
        {
            "decision": "HISTORY_SANITIZED",
            "private_owner_fields_removed": changed,
        }
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "command",
        choices=(
            "initialize",
            "claim",
            "heartbeat",
            "complete",
            "credit-interrupted",
            "abort",
            "confirm-paused",
            "mark-pause-required",
            "inspect",
            "sanitize-history",
        ),
    )
    parser.add_argument("--automation-id", required=True, choices=tuple(SPECS))
    parser.add_argument(
        "--vault-root", type=Path, default=DEFAULT_VAULT_ROOT
    )
    parser.add_argument(
        "--automations-root", type=Path, default=DEFAULT_AUTOMATIONS_ROOT
    )
    parser.add_argument("--reason", default="unspecified")
    parser.add_argument("--user-authorized", action="store_true")
    parser.add_argument("--sprint-id")
    parser.add_argument("--occurrence", type=int)
    parser.add_argument("--started-at")
    parser.add_argument("--run-log")
    parser.add_argument(
        "--claim-token",
        help="deprecated compatibility argument; ownership is thread-bound",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    handlers = {
        "initialize": command_initialize,
        "claim": command_claim,
        "heartbeat": command_heartbeat,
        "complete": command_complete,
        "credit-interrupted": command_credit_interrupted,
        "abort": command_abort,
        "confirm-paused": command_confirm_paused,
        "mark-pause-required": command_mark_pause_required,
        "inspect": command_inspect,
        "sanitize-history": command_sanitize_history,
    }
    try:
        return handlers[args.command](args)
    except ControlError as exc:
        print(
            json.dumps(
                {"decision": "CONTROL_ERROR", "error": str(exc)},
                ensure_ascii=False,
                sort_keys=True,
            )
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
