# Method

Three routes test the exact printed statement:

1. A symmetry certificate evaluates equations (24)–(25) at `m=0` in closed
   form and derives the definition-faithful values independently.
2. Four million independent bivariate-Gaussian draws compare the printed and
   definition-faithful indicators with standard errors.
3. Four dense dimension-512 Gaussian constructions directly audit the target
   overlap, predictor norm, attack budget, target invariance, robust error, and
   boundary error.

The zero-budget case must not report a mismatch. A mutation that omits the
label-dependent attack direction must be rejected at positive budget.
