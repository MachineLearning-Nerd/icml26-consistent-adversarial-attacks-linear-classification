# Evaluator entry: Claim 3

Run the cumulative verifier with:

```bash
uv sync --frozen && .venv/bin/python repro/src/verify.py
```

The machine-readable `claim_3` record lists every displayed left side, every
Appendix (119) expression signature, all conflicts, the parameterization
orientation check, and the repaired negative control. It exits nonzero unless
the literal inconsistency is detected and the repaired control is accepted.

Status before remote execution: **BLOCKED**.
