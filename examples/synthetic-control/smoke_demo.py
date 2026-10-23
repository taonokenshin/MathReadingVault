#!/usr/bin/env python3
"""Exercise public controller copies against disposable synthetic roots only."""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
CONTROLLER = REPOSITORY_ROOT / "tools" / "manual_batch_control.py"
# A preserved historical mapping, used solely with temporary fixture roots.
AUTOMATION_ID = "mathreadingvault-serre"


def main() -> int:
    fixture = json.loads(Path(__file__).with_name("fixture.json").read_text())
    with tempfile.TemporaryDirectory(prefix="math-reading-synthetic-") as temporary:
        workspace = Path(temporary)
        vault = workspace / "vault"
        automations = workspace / "automations"
        vault.mkdir()
        configuration = automations / AUTOMATION_ID / "automation.toml"
        configuration.parent.mkdir(parents=True)
        fields = dict(fixture["automation"])
        fields["id"] = AUTOMATION_ID

        def write_configuration() -> None:
            configuration.write_text("".join(
                f"{key} = {json.dumps(value)}\n" for key, value in fields.items()
            ))

        def invoke(command: str, *, competitor: bool = False) -> dict:
            environment = os.environ.copy()
            environment["CODEX_THREAD_ID"] = fixture[
                "competing_identity" if competitor else "owner_identity"
            ]
            environment["PYTHONDONTWRITEBYTECODE"] = "1"
            result = subprocess.run(
                [sys.executable, str(CONTROLLER), command,
                 "--automation-id", AUTOMATION_ID,
                 "--vault-root", str(vault),
                 "--automations-root", str(automations),
                 "--reason", "synthetic-demo-noncounted"],
                capture_output=True, text=True, check=True, env=environment,
                timeout=15,
            )
            return json.loads(result.stdout)

        write_configuration()
        initialized = invoke("initialize")
        assert initialized["decision"] == "INITIALIZED", initialized
        fields["status"] = "ACTIVE"
        fields["updated_at"] = fixture["activation_updated_at"]
        write_configuration()
        started = invoke("claim")
        assert started["decision"] == "START", started
        heartbeat = invoke("heartbeat")
        assert heartbeat["decision"] == "HEARTBEAT", heartbeat
        competing = invoke("claim", competitor=True)
        assert competing["decision"] == "EXIT", competing
        assert competing["reason"] == "lock-busy", competing
        aborted = invoke("abort")
        assert aborted["decision"] == "ABORTED_NONCOUNTED", aborted
        inspected = invoke("inspect")
        assert inspected["completed_occurrences"] == 0, inspected
        assert inspected["current_occurrence"] is None, inspected
        assert inspected["lock_exists"] is False, inspected
        print(json.dumps({
            "demo": "synthetic-controller",
            "passed": True,
            "decisions": [initialized["decision"], started["decision"],
                          heartbeat["decision"], competing["decision"],
                          aborted["decision"]],
            "competing_claim_reason": competing["reason"],
            "completed_occurrences": inspected["completed_occurrences"],
            "lock_exists_after_abort": inspected["lock_exists"],
            "real_automations_accessed": False,
        }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
