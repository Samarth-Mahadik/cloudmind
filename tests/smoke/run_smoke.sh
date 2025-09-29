#!/usr/bin/env bash
set -e

# Ensure correct project root
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$PROJECT_ROOT"

# Add project root to Python path
export PYTHONPATH="$PROJECT_ROOT:$PYTHONPATH"

# 1. create test raw_actions.json
mkdir -p data
cat > data/raw_actions.json <<'JSON'
[
  {"timestamp":"2025-01-01T00:00:00","type":"cli","command":"cd /tmp"},
  {"timestamp":"2025-01-01T00:00:01","type":"cli","command":"git status"},
  {"timestamp":"2025-01-01T00:00:02","type":"cli","command":"git add ."},
  {"timestamp":"2025-01-01T00:10:00","type":"cli","command":"cd /tmp"},
  {"timestamp":"2025-01-01T00:10:01","type":"cli","command":"git status"},
  {"timestamp":"2025-01-01T00:10:02","type":"cli","command":"git add ."},
  {"timestamp":"2025-01-01T00:20:00","type":"cli","command":"cd /tmp"},
  {"timestamp":"2025-01-01T00:20:01","type":"cli","command":"git status"},
  {"timestamp":"2025-01-01T00:20:02","type":"cli","command":"git add ."}
]
JSON

# 2. run agent creator (dry-run)
python engine/agent_creator.py

# 3. run orchestrator dry-run if any agents created
python engine/orchestrator.py --start agent_cd_git_add --agents-dir ./agents || true

echo "SMOKE: done"
