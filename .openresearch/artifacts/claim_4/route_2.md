# Route 2 — high-dimensional noise-scaling audit

For `p>=d`, the structured feature matrix in Assumption 4.2 gives each signal
coordinate variance `p/d^2`. Equation (28)'s `u~N(0,I_p/p)` therefore yields
signal-to-noise ratio `(p/d)^2`, a nonzero constant in the proportional limit.
Assumption 4.2's `u~N(0,I_p)` instead yields SNR `p/d^2`, which vanishes as
`1/d` at fixed `p/d`.

The independent checker uses one million draws at each of
`d=125,250,500,1000`, with fixed `p/d=2`. It requires the first log-log SNR
slope to be zero and the second to be minus one, within `0.03`, and requires
all empirical variances to agree with their independent analytic values to
1.5%.

This route tests the high-dimensional sequences directly. It cannot select
which contradictory source definition generated Figure 5, so its scientific
verdict remains **BLOCKED**.
