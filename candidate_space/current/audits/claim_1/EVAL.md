# Evaluator entry: Claim 1

Run exactly:

```bash
uv sync --frozen && .venv/bin/python repro/src/verify.py
```

The command exits nonzero if Proposition 1 disagrees with the independent
feasibility certificate, the mutation control is not rejected, or a GPU device
is detected. Raw machine-readable evidence is printed between
`BEGIN_MACHINE_READABLE_EVIDENCE` and `END_MACHINE_READABLE_EVIDENCE`.

Status before the baseline run: **BLOCKED** pending remote execution.
