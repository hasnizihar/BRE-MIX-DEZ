# Data Readiness Register

> This register tracks all missing data and unresolved engineering queries required to complete the BRE Mix Design calculation engine.

| ID       | Data Requirement | Source | Status | Required For |
| -------- | ---------------- | ------ | ------ | ------------ |
| DATA-001 | Figure 4 values (Strength vs W/C) | BR 331 | [PENDING_USER_DATA] | Stage 2 (w/c ratio) |
| DATA-002 | Figure 5 values (Wet density) | BR 331 | [PENDING_USER_DATA] | Stage 4 (Total Aggregate) |
| DATA-003 | Figure 6 values (Fine Aggregate %) | BR 331 | [PENDING_USER_DATA] | Stage 5 (Fine Aggregate) |
| DATA-004 | Standard Deviation (n < 20) | BR 331 | [PENDING_USER_DATA] | Stage 1 (EQ-BRE-002) |
| DATA-005 | Coarse Aggregate fraction ratio | BR 331 (REVIEW-001) | [PENDING_USER_DATA] | Stage 5 (Coarse Aggregate) |
| DATA-006 | Mixed water exact formula | BR 331 (REVIEW-002) | [PENDING_USER_DATA] | Stage 3 (Water Content) |
| DATA-007 | Exact calculation rounding rules | BR 331 (REVIEW-003) | [PENDING_USER_DATA] | All Stages |

## Policy
**Do not invent or estimate values to fill this register.**
If a calculation requires a pending dataset, it must predictably fail by raising an EngineeringDataUnavailableError specifying the corresponding DATA-ID.
