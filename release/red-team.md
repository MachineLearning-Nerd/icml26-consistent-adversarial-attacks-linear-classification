# Evaluator-blind pre-publication red team

The reviewer used only the candidate artifact and the evaluator rubric. No
repository paths, experiment IDs, OpenResearch logs, or storage hints were
provided.

## Round 1

Files opened, in order:

1. `README.md`
2. `logbook.json`
3. `pages/index.md`
4. `pages/verification-run/page.md`
5. `pages/claims/page.md`

Conclusion: the historical weak verifier was easier to find than the current
evidence. The current claim contracts, raw data, checker, controls, and runtime
could not be verified from the canonical navigation. Release was rejected.

Fixes: current verification was placed first in README, `logbook.json`, and
`pages/index.md`; the old pages were labeled exactly “Historical rejected
baseline”; a single current page was added with inline numbers and direct
links to every evidence type.

## Round 2 after fixes

Files opened, in order:

1. `README.md`
2. `logbook.json`
3. `pages/current-verification/page.md`
4. `current/data/results.json`
5. `current/data/checker-output.json`
6. `current/data/control-output.json`
7. `current/data/runtime.csv`
8. `current/code/verify.py`
9. `current/code/release_audit.py`
10. `current/audits/claim_1/claim_contract.json`
11. `current/audits/claim_2/claim_contract.json`
12. `current/audits/claim_3/claim_contract.json`
13. `current/audits/claim_4/claim_contract.json`
14. `current/audits/claim_5/claim_contract.json`
15. `current/release/visibility-matrix.md`

Conclusion: all five exact claim contracts, verdicts, numerical evidence,
raw data, independent checker results, negative controls, limitations,
environment, command, seeds, CPU allocation, and runtime were discoverable.
Claim 4 remains scientifically BLOCKED after four routes, but its evidence is
visible. No conclusion depended on an unpublished or hidden artifact.
