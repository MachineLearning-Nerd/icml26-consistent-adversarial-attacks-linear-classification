# Research command record

The fixed experiment command on every node was:

```bash
uv sync --frozen && .venv/bin/python repro/src/verify.py
```

Every launch used this orchestration form, with the experiment ID changed per
row:

```bash
orx exp run <experiment-id> --flavor cpu-upgrade --image ghcr.io/astral-sh/uv:python3.12-bookworm-slim
orx exp wait <experiment-id> --timeout 480
orx logs <run-id> --bytes <requested-bytes>
```

Experiment IDs and run IDs are retained in `orx exp desc` and the OpenResearch
run table, not required for repository reproduction. Startup read-only commands
included `orx projects --json`, `orx runs`, `orx project view`, `orx exp
status`, `git status --short`, `git rev-parse`, `git branch -a`, `df`, and
environment-name-only inspection. Paper and verdict retrieval used explicit
source URLs and an explicit browser User-Agent; hashes are in
`evidence/results.json`.

No training, verifier, benchmark, data-generation, or claim computation ran on
the local machine. Local commands were limited to reading, editing, hashing,
git operations, and `orx` orchestration.
