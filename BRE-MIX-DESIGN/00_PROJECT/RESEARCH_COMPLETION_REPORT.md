# Research Completion Report

> **Project:** BRE Concrete Mix Design Engineering Knowledge Base
> **Date:** 2026-09-18
> **Phase:** Phase 1 — Research & Engineering Documentation

---

## 1. What Was Researched

The complete BRE/DoE concrete mix-design method as documented in BRE BR 331, *Design of Normal Concrete Mixes*, Second Edition, 1997. Additionally, the relationship between this historical mix-design method and current UK concrete specification standards (BS 8500, BS EN 206) was researched and documented.

## 2. Sources Found

| ID | Source | Tier | Status |
|----|--------|------|--------|
| SRC-BRE-001 | BRE BR 331, 2nd Ed, 1997 | 1 | VERIFIED (PDF obtained) |
| SRC-BSI-001 | BS 8500-1:2023 | 1 | VERIFIED |
| SRC-BSI-002 | BS 8500-2:2023 | 1 | VERIFIED |
| SRC-BSEN-001 | BS EN 206 | 1 | VERIFIED |
| SRC-BSEN-002 | BS EN 197-1 | 1 | VERIFIED |
| SRC-BSEN-003 | BS EN 12620 | 1 | VERIFIED |
| SRC-CS-001 | Concrete Society | 2 | VERIFIED |
| SRC-CC-001 | Concrete Centre | 2 | VERIFIED |
| SRC-TRID-001 | TRID/TRB | 3 | VERIFIED |
| SRC-UNI-001 | EMU Lecture Notes | 3 | SECONDARY |

**Total: 10 sources catalogued**

## 3. Sources Verified

- BRE BR 331: PDF downloaded from official BRE Group website ✓
- ISBN 1-86081-172-8 confirmed via TRID ✓
- BS 8500:2023 current editions confirmed via BSI/Concrete Centre ✓
- All Tier 1 sources confirmed for existence and relevance ✓

## 4. BRE Method Sections Documented

| File | Content | Status |
|------|---------|--------|
| 00_OVERVIEW.md | Method overview, 5-stage workflow | Complete |
| 01_SCOPE.md | Assumptions (A1-A7), Limitations (L1-L7) | Complete |
| 02_INPUT_REQUIREMENTS.md | 19 engineering inputs + validation rules | Complete |
| 03_TARGET_MEAN_STRENGTH.md | EQ-BRE-001/002, k factors, worked example | Complete |
| 04_WATER_CEMENT_RATIO.md | Table 2, Figure 4 (partial digitization) | Complete |
| 05_WATER_CONTENT.md | Table 3, workability classification | Complete |
| 06_CEMENT_CONTENT.md | EQ-BRE-003, min/max checks | Complete |
| 07_TOTAL_AGGREGATE.md | EQ-BRE-004, Figure 5 (partial digitization) | Complete |
| 08_FINE_AGGREGATE.md | EQ-BRE-005, Figure 6 (partial digitization) | Complete |
| 09_COARSE_AGGREGATE.md | EQ-BRE-006 | Complete |
| 10_ADJUSTMENTS.md | Trial mix, durability, combined aggregate | Complete |
| 11_FIELD_CORRECTIONS.md | EQ-BRE-007/008/009 | Complete |
| 12_FINAL_MIX.md | Output format, checks, report template | Complete |
| 13_SPECIAL_CASES.md | Air-entrained, PFA, GGBS | Complete |
| 99_TRACEABILITY.md | All items mapped to sources | Complete |

## 5. Equations Extracted

| ID | Name | Status |
|----|------|--------|
| EQ-BRE-001 | Target mean strength | CROSS-VERIFIED |
| EQ-BRE-002 | Margin | CROSS-VERIFIED |
| EQ-BRE-003 | Cement content | VERIFIED |
| EQ-BRE-004 | Total aggregate | VERIFIED |
| EQ-BRE-005 | Fine aggregate | VERIFIED |
| EQ-BRE-006 | Coarse aggregate | VERIFIED |
| EQ-BRE-007 | Batch water | CROSS-VERIFIED |
| EQ-BRE-008 | Batch fine aggregate | CROSS-VERIFIED |
| EQ-BRE-009 | Batch coarse aggregate | CROSS-VERIFIED |

**Total: 9 equations extracted and documented**

## 6. Tables Extracted

| ID | Name | Status |
|----|------|--------|
| TBL-BRE-001 | Workability classification | CROSS-VERIFIED |
| TBL-BRE-002 | Compressive strength at w/c 0.5 | CROSS-VERIFIED |
| TBL-BRE-003 | Free water content | CROSS-VERIFIED |

**Total: 3 tables extracted; 2 with JSON machine-readable data**

## 7. Graphs Identified

| ID | Figure | Digitization Status |
|----|--------|-------------------|
| GRAPH-BRE-001 | Figure 4: Strength vs w/c ratio | PARTIAL |
| GRAPH-BRE-002 | Figure 5: Wet density | PARTIAL |
| GRAPH-BRE-003 | Figure 6: Fine aggregate proportion | PARTIAL |

**Total: 3 graphs identified; all require complete digitization from physical source**

## 8. Data Digitized

- Table 2 values: 4 rows × 4 age columns = 16 data points ✓
- Table 3 values: 6 rows × 4 slump columns = 24 data points ✓
- k factor values: 4 values ✓
- Figure 4: ~11 data points for one cement/aggregate combination
- Figure 5: ~28 data points (estimated)
- Figure 6: ~72 data points (2 of 12 sub-tables)

## 9. Worked Examples Found

- Constructed 2 golden test cases from the BRE method steps
- CASE-001: C30, 42.5 cement, uncrushed 20mm
- CASE-002: C40, 42.5 cement, crushed 20mm, with durability constraints

## 10. Validation Cases Created

| Type | Count | Status |
|------|-------|--------|
| Golden test cases | 2 | Created |
| Equation tests | 6 | Planned |
| Component tests | 7 | Planned |
| Boundary tests | 10 | Planned |
| Invalid input tests | 8 | Planned |
| Independent verification | 3 | Planned |

## 11. Current Standards Reviewed

- BS 8500-1:2023 and BS 8500-2:2023 — confirmed as current UK standards
- BS EN 206 — European framework standard identified
- BS EN 197-1 — cement classification confirmed
- BS EN 12620 — aggregate standard identified
- Relationship between BRE and current standards documented
- One conflict identified and resolved (CONFLICT-001: cement classification)

## 12. Conflicts Identified

| ID | Topic | Status |
|----|-------|--------|
| CONFLICT-001 | Cement classification (old vs current) | RESOLVED — BR 331 2nd ed already uses 42.5/52.5 |

## 13. Unverified Information

| Item | Reason | Priority |
|------|--------|----------|
| Standard deviation guidance table | Not directly extracted from PDF | MEDIUM |
| Coarse aggregate fraction proportions | Not found in available sources | LOW |
| Mixed aggregate water formula exact wording | SECONDARY source only | LOW |

## 14. Engineering Review Items

| Item | Description | Priority |
|------|-------------|----------|
| Figure 4 complete digitization | Require physical copy for accurate curve data | HIGH |
| Figure 5 complete digitization | Require physical copy for chart data | HIGH |
| Figure 6 complete digitization | Only 20mm/2 slump ranges done; need all 12 sub-tables | HIGH |
| Standard deviation defaults | Verify exact table from BR 331 | MEDIUM |
| Rounding rules | Many marked UNSPECIFIED | LOW |

## 15. Missing Information

| Item | Impact | Mitigation |
|------|--------|-----------|
| Complete Figure 4 curve data | Cannot accurately determine w/c ratio | Use approximation formula + flag |
| Complete Figure 5 chart data | Approximate wet density only | Use linear approximation + flag |
| Complete Figure 6 for 10mm and 40mm | Cannot proportion for these sizes | Partial digitization available for 20mm |
| Worked examples from BR 331 | Golden tests are constructed, not original | Cross-verified intermediate values |

## 16. Recommended Next Phase

### Immediate (before coding):
1. **Obtain physical copy of BR 331** — for complete digitization of Figures 4, 5, 6
2. **Complete Figure 6 digitization** for all 3 aggregate sizes × 4 slump ranges = 12 sub-tables
3. **Verify standard deviation guidance table** from BR 331

### Phase 2 (calculation engine):
1. Implement calculation engine in Python (no UI)
2. Implement all equations (EQ-BRE-001 to EQ-BRE-009)
3. Implement all table lookups
4. Implement Figure 4/5/6 interpolation
5. Run golden tests
6. Run boundary tests

## 17. Overall Research Completeness

| Area | Status | Confidence | Notes |
|------|--------|-----------|-------|
| BRE method | Complete | High | All 5 stages documented with equations |
| Equations | Complete | High | 9 equations, all verified |
| Tables | Complete | High | 3 tables, cross-verified, JSON created |
| Graphs | Partial | Medium | 3 identified; partial digitization |
| Standards | Complete | High | Relationships documented |
| Validation | Structured | Medium | 2 golden cases; 34 tests planned |
| Traceability | Complete | High | Full matrix created |
| Software spec | Complete | High | Architecture, engine, UI, DB, reports |
| AI governance | Complete | High | Rules, workflow, guardrails, templates |

---

## Files Created Summary

| Directory | Files Created |
|-----------|--------------|
| Root | 2 (AGENTS.md, README.md) |
| 00_PROJECT/ | 5 (scope, roadmap, requirements, terminology, decisions, changelog) |
| 01_SOURCES/ | 2 (source register, BR331 review) |
| 02_BRE_METHOD/ | 15 (overview through traceability) |
| 03_STANDARDS/ | 1 (standard relationships) |
| 04_ENGINEERING_DATA/ | 4 (data dictionary, constants, 2 JSON tables) |
| 05_CALCULATIONS/ | 6 (pipeline, equations, interpolation, rounding, units, errors) |
| 06_VALIDATION/ | 3 (validation plan, 2 golden case JSON files) |
| 07_SOFTWARE_SPEC/ | 6 (architecture, engine, UI, DB, reports, traceability) |
| 08_AI_AGENT/ | 7 (rules, workflow, template, guardrails, checklist, protocol, audit) |
| **Total** | **~51 files** |

---

*Report generated: 2026-09-18*
*Phase 1 Status: COMPLETE (with engineering review items noted)*
