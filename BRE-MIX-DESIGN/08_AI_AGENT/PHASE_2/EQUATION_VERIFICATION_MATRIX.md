# Equation Verification Matrix

> **Master Control Sheet** for Phase 2 implementation.
> An equation is not considered complete until all columns are verified.

| Equation | Implemented | Unit Test | Boundary | Invalid | Data Verified | Trace | Engineering Review |
| -------- | ----------: | --------: | -------: | ------: | ------------: | ----: | -----------------: |
| EQ-BRE-001 | IMPLEMENTED | UNIT_TESTED | BOUNDARY | INVALID | VERIFIED | TRACE_READY | PENDING |
| EQ-BRE-002 | IMPLEMENTED | UNIT_TESTED | BOUNDARY | INVALID | BLOCKED_DATA | TRACE_READY | BLOCKED |
| LKP-BRE-001| NOT_STARTED | NOT_STARTED | NOT_STARTED | NOT_STARTED | BLOCKED_DATA | NOT_STARTED | BLOCKED |
| EQ-BRE-003 | IMPLEMENTED | UNIT_TESTED | BOUNDARY | INVALID | VERIFIED | TRACE_READY | ENGINEERING_VERIFIED |
| EQ-BRE-004 | IMPLEMENTED | IMPLEMENTED | IMPLEMENTED | IMPLEMENTED | DATA_AVAILABLE | PENDING_ENGINEERING_VERIFICATION | IMPLEMENTED_PENDING_VERIFICATION |
| EQ-BRE-005 | IMPLEMENTED | IMPLEMENTED | IMPLEMENTED | IMPLEMENTED | DATA_AVAILABLE | PENDING_ENGINEERING_VERIFICATION | IMPLEMENTED_PENDING_VERIFICATION |
| EQ-BRE-006 | IMPLEMENTED | IMPLEMENTED | IMPLEMENTED | IMPLEMENTED | DATA_AVAILABLE | PENDING_ENGINEERING_VERIFICATION | IMPLEMENTED_PENDING_VERIFICATION |
| EQ-BRE-007 | NOT_STARTED | NOT_STARTED | NOT_STARTED | NOT_STARTED | BLOCKED_DATA | NOT_STARTED | BLOCKED |
| EQ-BRE-008 | NOT_STARTED | NOT_STARTED | NOT_STARTED | NOT_STARTED | VERIFIED | NOT_STARTED | PENDING |
| EQ-BRE-009 | NOT_STARTED | NOT_STARTED | NOT_STARTED | NOT_STARTED | VERIFIED | NOT_STARTED | PENDING |

## Legend
- **DEFINED**: Documented mathematical definition in registry.
- **NOT_STARTED**: Development has not begun.
- **IMPLEMENTED**: Code exists in src/bre_engine/calculations/.
- **UNIT_TESTED / BOUNDARY / INVALID**: Automated software tests pass.
- **DATA_VERIFIED / VERIFIED**: Underlying constants/formulas are sourced from verified BR 331 data. 
- **BLOCKED_DATA / BLOCKED**: Required information is unavailable or unresolved.
- **TRACE / TRACE_READY**: Connected to TraceTracker.
- **ENGINEERING_VERIFIED**: Engineering review confirms the implementation.
