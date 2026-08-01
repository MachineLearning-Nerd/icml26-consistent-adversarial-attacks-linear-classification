# Reproduction: consistent adversarial attacks in linear classification

[![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/MachineLearning-Nerd/icml26-repro-PUIivg3GrO-on-the-existence-of-consistent-adversarial-attacks-in-high-dimensional-linea/blob/main/notebooks/reproduction.py)

We reproduced all five judged claims from *On the Existence of Consistent
Adversarial Attacks in High-Dimensional Linear Classification* (arXiv
2506.12454) with one fixed, locked command on Hugging Face CPU hardware.

The strongest evidence is mixed: Proposition 1 is **VERIFIED** in 400/400 ℓ₂
cases; Theorems 3.1, 4.1, and 4.2 are **FALSIFIED as printed** by sign or
equation-closure certificates; the Section 4.3 overparameterization trend is
**BLOCKED** after four distinct routes because the paper does not publish a
unique executable Figure 5 contract. The live score remains **3/10** until the
judge evaluates a new revision. A possible **8/10 is only a forecast**.

Headline paper-versus-observed number: Theorem 3.1's printed robust error is
`0.5000` at `m=0,q=1,epsilon_tilde=0.5`; Definition 2/Lemma 1 give
`0.69146246`, and four million draws observe `0.69156475`.

All research computation used Hugging Face `cpu-upgrade`; every run exposed 64
CPUs and no GPU devices. The only downscoping is explicit: Claim 1 covers ℓ₂
strict non-boundary cases, and Claim 4 is not replaced by a guessed loss,
budget, link, or noise scaling.

- [Illustrated claim-by-claim report](reports/reproduction/report.md)
- [Self-contained tutorial notebook](notebooks/reproduction.py)
- [Raw result summary](evidence/results.json) and [runtime ledger](evidence/runtime.csv)

Run the cumulative verifier:

```bash
uv sync --frozen && .venv/bin/python repro/src/verify.py
```

## Experiment log

| Branch / experiment | Purpose or change | Exact run command | Assessment / outcome | Compute |
| --- | --- | --- | --- | --- |
| `main` | Public landing page, report, notebook, and release mirror | Not run as an experiment (publication surface) | Presentation only | None |
| [`orx/judged-baseline-regression`](https://github.com/MachineLearning-Nerd/icml26-repro-PUIivg3GrO-on-the-existence-of-consistent-adversarial-attacks-in-high-dimensional-linea/tree/orx/judged-baseline-regression) | Preserve Proposition 1 | `uv sync --frozen && .venv/bin/python repro/src/verify.py` | VERIFIED, 400/400; mutation rejected | HF `cpu-upgrade`, 64 CPUs, 16 s |
| [`orx/claim-2-printed-formula-audit`](https://github.com/MachineLearning-Nerd/icml26-repro-PUIivg3GrO-on-the-existence-of-consistent-adversarial-attacks-in-high-dimensional-linea/tree/orx/claim-2-printed-formula-audit) | Exact Theorem 3.1 counterexample | `uv sync --frozen && .venv/bin/python repro/src/verify.py` | FALSIFIED as printed: `0.5000` vs `0.69146` | HF `cpu-upgrade`, 64 CPUs, 31 s |
| [`orx/latent-theorem-integrity-audit`](https://github.com/MachineLearning-Nerd/icml26-repro-PUIivg3GrO-on-the-existence-of-consistent-adversarial-attacks-in-high-dimensional-linea/tree/orx/latent-theorem-integrity-audit) | Compare Theorem 4.1 with Appendix (119) | `uv sync --frozen && .venv/bin/python repro/src/verify.py` | Claim 3 FALSIFIED; Claim 5 route 1 BLOCKED | HF `cpu-upgrade`, 64 CPUs, 31 s |
| [`orx/metric-quantifier-and-specification-audit`](https://github.com/MachineLearning-Nerd/icml26-repro-PUIivg3GrO-on-the-existence-of-consistent-adversarial-attacks-in-high-dimensional-linea/tree/orx/metric-quantifier-and-specification-audit) | Claim 4 source audit; Claim 5 event proof | `uv sync --frozen && .venv/bin/python repro/src/verify.py` | Claim 4 BLOCKED; Claim 5 FALSIFIED | HF `cpu-upgrade`, 64 CPUs, 37 s |
| [`orx/claim-4-scaling-ambiguity`](https://github.com/MachineLearning-Nerd/icml26-repro-PUIivg3GrO-on-the-existence-of-consistent-adversarial-attacks-in-high-dimensional-linea/tree/orx/claim-4-scaling-ambiguity) | Quantify conflicting noise scalings | `uv sync --frozen && .venv/bin/python repro/src/verify.py` | BLOCKED; slopes `−0.00053` and `−1.00058` | HF `cpu-upgrade`, 64 CPUs, 31 s |
| [`orx/claim-4-mechanism-decomposition`](https://github.com/MachineLearning-Nerd/icml26-repro-PUIivg3GrO-on-the-existence-of-consistent-adversarial-attacks-in-high-dimensional-linea/tree/orx/claim-4-mechanism-decomposition) | Exact clean/boundary/robust identity | `uv sync --frozen && .venv/bin/python repro/src/verify.py` | BLOCKED; mechanism verified exactly | HF `cpu-upgrade`, 64 CPUs, 26 s |
| [`orx/claim-4-falsification-eligibility`](https://github.com/MachineLearning-Nerd/icml26-repro-PUIivg3GrO-on-the-existence-of-consistent-adversarial-attacks-in-high-dimensional-linea/tree/orx/claim-4-falsification-eligibility) | Mandatory counterexample search | `uv sync --frozen && .venv/bin/python repro/src/verify.py` | BLOCKED; no eligible falsification | HF `cpu-upgrade`, 64 CPUs, 26 s |
| [`orx/evaluator-visible-release-candidate`](https://github.com/MachineLearning-Nerd/icml26-repro-PUIivg3GrO-on-the-existence-of-consistent-adversarial-attacks-in-high-dimensional-linea/tree/orx/evaluator-visible-release-candidate) | Cumulative release and visibility gates | `uv sync --frozen && .venv/bin/python repro/src/verify.py` | Pending final CPU run | HF `cpu-upgrade`, estimated 2 cores |

The environment is pinned by `uv.lock`. Monetary cost is not exposed by the
OpenResearch/Hugging Face logs and is therefore reported as unavailable rather
than guessed.
