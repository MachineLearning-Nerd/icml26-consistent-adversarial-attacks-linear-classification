# Reproduction: consistent adversarial attacks in linear classification

This repository reproduces claims from *On the Existence of Consistent
Adversarial Attacks in High-Dimensional Linear Classification* (arXiv
2506.12454). The cumulative verifier preserves the judge-accepted
finite-dimensional check of Proposition 1 and tests later displayed theorems
against their definitions and appendix derivation.

## Baseline result

Proposition 1 states that an ℓ₂ label-preserving attack exists exactly when
`epsilon * ||w_hat_perp|| >= |<w_hat, x>|`. The baseline checks deterministic
feasible and infeasible cases and requires a deliberately incorrect
`||w_hat||` mutation to be rejected.

## Experiment log

| Branch / experiment | Purpose | Exact run command | Assessment | Compute |
| --- | --- | --- | --- | --- |
| `orx/judged-baseline-regression` | Preserve the accepted Proposition 1 check | `uv sync --frozen && .venv/bin/python repro/src/verify.py` | VERIFIED in 400/400 cases; mutation rejected | Hugging Face `cpu-upgrade`, 64 CPUs allocated, 16 s |
| `orx/claim-2-printed-formula-audit` | Test Theorem 3.1 exactly as printed | `uv sync --frozen && .venv/bin/python repro/src/verify.py` | FALSIFIED: printed robust error 0.5000 versus definition-faithful 0.69146 | Hugging Face `cpu-upgrade`, 64 CPUs allocated, 31 s |
| `orx/latent-theorem-integrity-audit` | Audit Theorems 4.1/4.2 against Appendix D | `uv sync --frozen && .venv/bin/python repro/src/verify.py` | Pending source-integrity verifier | Hugging Face `cpu-upgrade`, estimated 1 core |

The environment is locked by `uv.lock`. Research computation is run only with
OpenResearch on Hugging Face CPU hardware.
