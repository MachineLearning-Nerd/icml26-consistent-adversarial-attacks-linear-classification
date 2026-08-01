# Evaluator entry: Claim 5 — route 1

The cumulative fixed command prints the dependency audit as `claim_5`:

```bash
uv sync --frozen && .venv/bin/python repro/src/verify.py
```

This route is expected to report **BLOCKED** while passing the integrity
check: the displayed dependency is demonstrably undefined, but no guessed
repair is promoted to theorem evidence.
