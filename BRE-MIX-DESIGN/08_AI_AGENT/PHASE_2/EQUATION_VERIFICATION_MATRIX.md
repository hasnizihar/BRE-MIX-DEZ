# Equation Verification Matrix

> **Master Control Sheet** for Phase 2 implementation.
> An equation is not considered complete until all columns are verified.

| Equation | Implemented | Unit Test | Boundary | Invalid | Data Verified | Trace | Engineering Review |
| -------- | ----------: | --------: | -------: | ------: | ------------: | ----: | -----------------: |
| EQ-BRE-001 | IMPLEMENTED | UNIT_TESTED | BOUNDARY | INVALID | VERIFIED | TRACE_READY | PENDING |
| EQ-BRE-002 | NOT_STARTED | NOT_STARTED | NOT_STARTED | NOT_STARTED | BLOCKED_DATA | NOT_STARTED | PENDING |
| EQ-BRE-003 | NOT_STARTED | NOT_STARTED | NOT_STARTED | NOT_STARTED | VERIFIED | NOT_STARTED | PENDING |
| EQ-BRE-004 | NOT_STARTED | NOT_STARTED | NOT_STARTED | NOT_STARTED | BLOCKED_DATA | NOT_STARTED | PENDING |
| EQ-BRE-005 | NOT_STARTED | NOT_STARTED | NOT_STARTED | NOT_STARTED | BLOCKED_DATA | NOT_STARTED | PENDING |
| EQ-BRE-006 | NOT_STARTED | NOT_STARTED | NOT_STARTED | NOT_STARTED | VERIFIED | NOT_STARTED | PENDING |
| EQ-BRE-007 | NOT_STARTED | NOT_STARTED | NOT_STARTED | NOT_STARTED | VERIFIED | NOT_STARTED | PENDING |
| EQ-BRE-008 | NOT_STARTED | NOT_STARTED | NOT_STARTED | NOT_STARTED | VERIFIED | NOT_STARTED | PENDING |
| EQ-BRE-009 | NOT_STARTED | NOT_STARTED | NOT_STARTED | NOT_STARTED | VERIFIED | NOT_STARTED | PENDING |

## Legend
- **NOT_STARTED**: Development has not begun.
- **IMPLEMENTED**: Code exists in `src/bre_engine/calculations/`.
- **UNIT_TESTED**: Normal cases pass.
- **BOUNDARY/INVALID**: Edge case tests pass.
- **DATA_VERIFIED**: Underlying constants/formulas are sourced from verified BR 331 data. `BLOCKED_DATA` if missing.
- **TRACE**: Connected to `TraceTracker`.
- **ENGINEERING_REVIEW**: Final human engineering sign-off.
