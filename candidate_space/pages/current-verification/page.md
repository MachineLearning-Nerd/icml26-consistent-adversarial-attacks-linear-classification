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

## Claim 2 — printed-formula audit pending

Theorem 3.1 equations (24)–(25) are tested exactly as printed. At `m=0`, the
printed Gaussian integral is analytically `0.5` for all positive attack budgets,
while Definition 2 plus Lemma 1 gives `Phi(epsilon_tilde)`. The candidate
verifier includes four million bivariate-Gaussian samples, four dense
dimension-512 constructions, an epsilon-zero non-falsification control, and a
label-direction mutation control. Status remains **BLOCKED** until the remote
run completes.
