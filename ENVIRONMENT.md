# Environment and artifact record

## Fixed reproduction command

From a clean checkout:

    uv sync --frozen && .venv/bin/python repro/src/verify.py

The project is pinned by pyproject.toml and uv.lock. The committed uv.lock
SHA-256 is b2508cf35b49d001059c7e47e99a3f3b8ad7837209855298d1684391455583d1.
The fixed command and evidence revision are recorded in evidence/results.json.

## Recorded scientific campaign

The committed evidence was produced at science revision
3688690d5ee0a644b06807b0dd6d0525be19edcc with seeds 1031, 2081, 4093, and
8179. The historical runs used Hugging Face cpu-upgrade hardware, exposed 64
CPUs, and requested no GPU. No monetary cost is inferred from provider logs.

| Evidence | Recorded scope |
| --- | --- |
| C1 | 400 exact l2 proposition cases in dimension 64, split 200 feasible and 200 infeasible. |
| C2 | Four million Gaussian samples plus four dimension-512 constructions. |
| C3 | Literal equation transcription, Appendix (119) comparison, and repaired control. |
| C4 | Four routes: completeness, scaling, decomposition over 2,000,000 cases, and eligibility. |
| C5 | Two million Gaussian samples across four correlations plus zero-threshold control. |

The dossier publication did not rerun this campaign. It verifies the committed
raw results, checker/control records, source hashes, and code/release
topology. The evidence package remains available in evidence and
candidate_space/current/data.

## Evidence policy

- Audit literal equations before proposing a correction.
- Keep intended corrections separate from literal verdicts.
- Preserve equality and zero-budget non-falsification controls.
- Do not guess missing Figure 5 settings.
- Treat finite numerical certificates as evidence for their disclosed scope.
- Keep the historical judged baseline separate from current evidence.
