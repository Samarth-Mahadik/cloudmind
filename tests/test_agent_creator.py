# tests/test_agent_creator.py
from engine.agent_creator import detect_repeated_sequences


def test_detect_repeated_sequences_simple():
    # commands_with_ts: list of (ts, cmd)
    cmds = [
        ("2025-01-01T00:00:00", "cd proj"),
        ("2025-01-01T00:00:01", "git status"),
        ("2025-01-01T00:00:02", "git add ."),
        ("2025-01-01T00:01:00", "cd proj"),
        ("2025-01-01T00:01:01", "git status"),
        ("2025-01-01T00:01:02", "git add ."),
        ("2025-01-01T00:02:00", "cd proj"),
        ("2025-01-01T00:02:01", "git status"),
        ("2025-01-01T00:02:02", "git add ."),
    ]
    detected = detect_repeated_sequences(cmds, seq_len=3, trigger=3)
    assert len(detected) >= 1
    seq0 = detected[0]["sequence"]
    assert seq0 == ["cd proj", "git status", "git add ."]
