# Case: unquoted VERIFIED must fail G4

Author writes:

```
| 1 | tests pass | VERIFIED | pass | pytest | tests pass | today |
```

Law: evidence cell has no quote / no command tail.
Expected: `scripts/gate.sh g4` exits non-zero.
