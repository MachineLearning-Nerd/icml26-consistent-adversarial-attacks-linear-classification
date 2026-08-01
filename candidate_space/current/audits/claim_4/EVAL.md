# Evaluator entry: Claim 4 — route 1

The cumulative verifier prints `claim_4.source_fields`, `missing_fields`, the
noise-scaling conflict, unbound trend quantifiers, and the complete-spec
control using:

```bash
uv sync --frozen && .venv/bin/python repro/src/verify.py
```

Expected route verdict: **BLOCKED**. Further materially different routes are
required before release.
