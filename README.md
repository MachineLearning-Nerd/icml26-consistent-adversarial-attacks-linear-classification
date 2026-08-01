# Reproduction: consistent adversarial attacks in linear classification

This repository reproduces claims from *On the Existence of Consistent
Adversarial Attacks in High-Dimensional Linear Classification* (arXiv
2506.12454). The baseline preserves the judge-accepted finite-dimensional
check of Proposition 1. Claims 2–5 remain unresolved at this node.

## Baseline result

Proposition 1 states that an ℓ₂ label-preserving attack exists exactly when
`epsilon * ||w_hat_perp|| >= |<w_hat, x>|`. The baseline checks deterministic
feasible and infeasible cases and requires a deliberately incorrect
`||w_hat||` mutation to be rejected.

## Experiment log

| Branch / experiment | Purpose | Exact run command | Assessment | Compute |
| --- | --- | --- | --- | --- |
| `orx/judged-baseline-regression` | Preserve the accepted Proposition 1 check | `uv sync --frozen && .venv/bin/python repro/src/verify.py` | Pending first baseline run | Hugging Face `cpu-upgrade`, estimated 1 core |

The environment is locked by `uv.lock`. Research computation is run only with
OpenResearch on Hugging Face CPU hardware.
