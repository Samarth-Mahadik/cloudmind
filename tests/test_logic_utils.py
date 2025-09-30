# tests/test_logic_utils.py
from engine.logic_utils import (
    save_json,
    load_json,
    parse_timestamp,
    jaccard_similarity,
)


def test_save_and_load_json(tmp_path):
    p = tmp_path / "sample.json"
    data = {"x": 1, "y": [1, 2, 3]}
    save_json(str(p), data)
    loaded = load_json(str(p))
    assert loaded == data


def test_parse_timestamp_iso():
    ts = "2025-09-01T12:00:00"
    dt = parse_timestamp(ts)
    assert dt.year == 2025 and dt.month == 9


def test_jaccard_similarity():
    a = ["a", "b", "c"]
    b = ["b", "c", "d"]
    sim = jaccard_similarity(a, b)
    assert 0 < sim < 1
