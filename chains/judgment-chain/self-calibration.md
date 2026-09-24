# Self-calibration — probabilistic check on your own decision

Before a non-trivial hunk and before DONE:

```
DECISION: <one sentence>
P(wrong): <0–1, honest>
CHEAP PROBE THAT WOULD SHOW I AM WRONG:
```

If P(wrong) ≥ 0.3, you must run that probe (or steal one aspect that names it)
before applying the hunk. Writing 0.05 on everything is a lie — Judgment treats
uncalibrated confidence as CONJECTURE.

After the probe: if you were wrong, log REFUTED and change the decision.
A calibration log with no REFUTED rows across many tasks is itself suspect.
