# Claim 2 source audit

The source and hashes are recorded in the Claim 1 audit. The exact anchors are
Assumptions 3.1–3.3, Theorem 3.1 equations (24)–(27), Definition 2 equations
(2)–(3), and Lemma 1 equations (70)–(76).

Equations (24)–(25) print `nu * (mu - epsilon_tilde * A) < 0` and then state
that `(nu, mu)` is jointly zero-mean Gaussian with covariance `[[1,m],[m,q]]`.
For negative `nu`, a label-preserving worst-case attack must shift in the
opposite direction. Definition 2 plus Lemma 1 therefore produces the signed
margin condition `sign(nu) * mu < epsilon_tilde * A`. The two expressions are
not equivalent for nonzero attack strength.

The counterexample uses `m=0`, `q=1`, ℓ₂ attacks, and positive rescaled budget.
These values satisfy every stated assumption. At zero budget both expressions
coincide, providing a non-falsification control.
