# Traceability Matrix

> **Purpose:** Map every engineering requirement to its source, specification, software module, and test.

---

## Requirement → Source → Specification → Module → Test

| Requirement ID | Description | Source | Equation/Table | Specification | Software Module | Test |
|---------------|-------------|--------|----------------|--------------|----------------|------|
| REQ-001 | Target mean strength | SRC-BRE-001 | EQ-BRE-001, EQ-BRE-002 | `03_TARGET_MEAN_STRENGTH.md` | `strength.py` | TEST-EQ-001, TEST-EQ-002 |
| REQ-002 | w/c ratio | SRC-BRE-001 | TBL-BRE-002, GRAPH-BRE-001 | `04_WATER_CEMENT_RATIO.md` | `wc_ratio.py` | TEST-CMP-002 |
| REQ-003 | Free water content | SRC-BRE-001 | TBL-BRE-003 | `05_WATER_CONTENT.md` | `water.py` | TEST-CMP-003 |
| REQ-004 | Cement content | SRC-BRE-001 | EQ-BRE-003 | `06_CEMENT_CONTENT.md` | `cement.py` | TEST-EQ-003, TEST-CMP-004 |
| REQ-005 | Total aggregate | SRC-BRE-001 | EQ-BRE-004, GRAPH-BRE-002 | `07_TOTAL_AGGREGATE.md` | `aggregate.py` | TEST-EQ-004, TEST-CMP-005 |
| REQ-006 | Fine aggregate proportion | SRC-BRE-001 | EQ-BRE-005, GRAPH-BRE-003 | `08_FINE_AGGREGATE.md` | `aggregate.py` | TEST-EQ-005, TEST-CMP-006 |
| REQ-007 | Coarse aggregate | SRC-BRE-001 | EQ-BRE-006 | `09_COARSE_AGGREGATE.md` | `aggregate.py` | TEST-EQ-006 |
| REQ-008 | Moisture corrections | SRC-BRE-001 | EQ-BRE-007/008/009 | `11_FIELD_CORRECTIONS.md` | `corrections.py` | TEST-CMP-007 |
| REQ-009 | Calculation transparency | Project | N/A | `12_FINAL_MIX.md` | `trace.py` | Manual |
| REQ-010 | Engineering warnings | Project | N/A | `ERROR_RULES.md` | `validation.py` | TEST-INV-* |
| REQ-011 | PDF report | Project | N/A | `REPORT_SPEC.md` | `report.py` | Manual |
| REQ-012 | Project saving | Project | N/A | `DATABASE_SPEC.md` | `database.py` | Manual |
| REQ-013 | Input validation | SRC-BRE-001 | N/A | `ERROR_RULES.md` | `validation.py` | TEST-INV-* |

---

## Data Source → Engineering Document → JSON Data → Software Lookup

| Data Source | Engineering Document | Machine-Readable Data | Software Lookup |
|-------------|---------------------|-----------------------|----------------|
| STD-BRE-001 | `03_TARGET_MEAN_STRENGTH.md` | `STD-BRE-001.md` | `lookup_standard_deviation()` |
| TBL-BRE-002 | `04_WATER_CEMENT_RATIO.md` | `TBL-BRE-002.json` | `lookup_reference_strength()` |
| TBL-BRE-003 | `05_WATER_CONTENT.md` | `TBL-BRE-003.json` | `lookup_free_water()` |
| GRAPH-BRE-001 | `04_WATER_CEMENT_RATIO.md` | Future: `GRAPH-BRE-001.json` | `lookup_wc_ratio()` |
| GRAPH-BRE-002 | `07_TOTAL_AGGREGATE.md` | Future: `GRAPH-BRE-002.json` | `estimate_wet_density()` |
| GRAPH-BRE-003 | `08_FINE_AGGREGATE.md` | Future: `GRAPH-BRE-003.json` | `lookup_fine_proportion()` |

---

## Golden Test Traceability

| Golden Test | Requirements Covered | Equations Tested | Tables Used | Status |
|------------|---------------------|-----------------|-------------|--------|
| CASE-001 | REQ-001 to REQ-007 | EQ-001 to EQ-006 | TBL-002, TBL-003, GRAPH-001/002/003 | Planned |
| CASE-002 | REQ-001 to REQ-007, REQ-013 | EQ-001 to EQ-006 | TBL-002, TBL-003, GRAPH-001/002/003 | Planned |

---

*Created: 2026-09-18*
