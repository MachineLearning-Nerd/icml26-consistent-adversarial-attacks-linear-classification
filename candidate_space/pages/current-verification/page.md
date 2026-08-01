# Current verification

## Claim 1 — pending baseline run

The current verifier supersedes the historical weak multi-claim verifier for
new evidence. Historical pages remain preserved at the judged revision
`5157b05fbbbad2885cd379658d7b58e688863e94`.

- Exact claim: Proposition 1, Section 3.1, equation (9), scoped here to ℓ₂ and
  strict non-boundary cases.
- Code: `repro/src/verify.py` and `repro/src/core.py`.
- Fixed command: `uv sync --frozen && .venv/bin/python repro/src/verify.py`.
- Pinned environment: `pyproject.toml` and `uv.lock`.
- Raw result: pending Hugging Face `cpu-upgrade` run.
- Independent checker: extremal orthogonal feasibility certificate.
- Negative control: full-norm mutation must be rejected.
- Limitations: equality and non-ℓ₂ geometries are excluded from the numerical
  scope; Claims 2–5 remain unresolved in the baseline.
