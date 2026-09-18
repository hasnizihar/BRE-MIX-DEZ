# Review Checklist

## Engineering Review

- [x] Does the equation match the engineering specification?
- [x] Does the table data match the source?
- [x] Are units correct?
- [x] Is interpolation correct?
- [x] Are rounding rules correct?
- [x] Are boundary conditions handled?
- [x] Are worked examples reproduced?
- [x] Were engineering data files accidentally modified?

## Code Review

- [x] Is the function independently testable?
- [x] Does the function have a source reference?
- [x] Are variable names engineering-meaningful?
- [x] Is the function in the correct layer (not UI)?
- [x] Are inputs validated?
- [x] Is the calculation trace available?

## Test Review

- [x] Do unit tests cover the equation?
- [x] Do boundary tests cover edge cases?
- [x] Do golden tests still pass?
- [x] Were no expected values modified?

---

*Created: 2026-09-18*
