# Method

For four deterministic seeds, generate 100 Gaussian instances in dimension 64.
Choose the attack budget at 0.25, 0.75, 1.25, or 2 times the exact threshold,
so equality is never tested. Compare equation (9) with a feasibility certificate
that constructs the extremal orthogonal perturbation and audits its norm,
target-invariance residual, and attacked margin.

The negative control replaces the orthogonal norm with the full predictor norm.
At least one disagreement with the feasibility certificate is required; an
undetected mutation makes the verifier exit nonzero.
