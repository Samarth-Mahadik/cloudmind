# tests/test_orchestrator.py
import os
from engine.orchestrator import run_workflow
from engine.logic_utils import save_json, ensure_dir


def test_run_workflow_dry(tmp_path):
    agents_dir = tmp_path / "agents"
    agents_dir.mkdir()
    a1 = {
        "name": "a1",
        "sequence": ["echo hi"],
        "triggers": {"on_success": ["a2"]},
    }
    a2 = {"name": "a2", "sequence": ["echo bye"], "triggers": {}}
    save_json(str(agents_dir / "a1.json"), a1)
    save_json(str(agents_dir / "a2.json"), a2)

    res = run_workflow("a1", execute=False, agents_dir=str(agents_dir))
    assert "steps" in res
    assert res["steps"][0]["agent"] == "a1"
    assert any(s["agent"] == "a2" for s in res["steps"])
