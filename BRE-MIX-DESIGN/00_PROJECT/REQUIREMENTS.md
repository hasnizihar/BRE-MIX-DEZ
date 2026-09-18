# Requirements

> Software requirements derived from the BRE engineering method.

## REQ-001: Target Mean Strength Calculation

| Field | Value |
|-------|-------|
| ID | REQ-001 |
| Category | Calculation |
| Description | Calculate target mean strength from characteristic strength, k factor, and standard deviation |
| Source | SRC-BRE-001, Stage 1 |
| Equation | EQ-BRE-001 |
| Priority | Essential |
| Status | Defined |

## REQ-002: Water/Cement Ratio Determination

| Field | Value |
|-------|-------|
| ID | REQ-002 |
| Category | Calculation |
| Description | Determine required free water/cement ratio from target mean strength, cement type, and aggregate type |
| Source | SRC-BRE-001, Stage 1, Figure 4 / Table 2 |
| Equation | Uses GRAPH-BRE-001, TBL-BRE-002 |
| Priority | Essential |
| Status | Defined |

## REQ-003: Free Water Content Estimation

| Field | Value |
|-------|-------|
| ID | REQ-003 |
| Category | Calculation |
| Description | Estimate free water content from workability, aggregate size, and aggregate type |
| Source | SRC-BRE-001, Stage 2, Table 3 |
| Table | TBL-BRE-003 |
| Priority | Essential |
| Status | Defined |

## REQ-004: Cement Content Calculation

| Field | Value |
|-------|-------|
| ID | REQ-004 |
| Category | Calculation |
| Description | Calculate cement content = free water content ÷ w/c ratio; check against min/max limits |
| Source | SRC-BRE-001, Stage 3 |
| Equation | EQ-BRE-003 |
| Priority | Essential |
| Status | Defined |

## REQ-005: Total Aggregate Content

| Field | Value |
|-------|-------|
| ID | REQ-005 |
| Category | Calculation |
| Description | Calculate total aggregate content = estimated wet density − cement − water |
| Source | SRC-BRE-001, Stage 4, Figure 5 |
| Equation | EQ-BRE-004 |
| Priority | Essential |
| Status | Defined |

## REQ-006: Fine Aggregate Proportion

| Field | Value |
|-------|-------|
| ID | REQ-006 |
| Category | Calculation |
| Description | Determine fine aggregate proportion from Figure 6 based on w/c ratio, max aggregate size, workability, and % passing 600 µm |
| Source | SRC-BRE-001, Stage 5, Figure 6 |
| Graph | GRAPH-BRE-003 |
| Priority | Essential |
| Status | Defined |

## REQ-007: Coarse Aggregate Content

| Field | Value |
|-------|-------|
| ID | REQ-007 |
| Category | Calculation |
| Description | Calculate coarse aggregate = total aggregate − fine aggregate |
| Source | SRC-BRE-001, Stage 5 |
| Equation | EQ-BRE-006 |
| Priority | Essential |
| Status | Defined |

## REQ-008: Moisture Corrections

| Field | Value |
|-------|-------|
| ID | REQ-008 |
| Category | Calculation |
| Description | Apply moisture and absorption corrections for field batching |
| Source | SRC-BRE-001 |
| Priority | Essential |
| Status | Defined |

## REQ-009: Calculation Transparency

| Field | Value |
|-------|-------|
| ID | REQ-009 |
| Category | Software |
| Description | User must be able to view the complete calculation trace including every intermediate step, equation used, table consulted, and source reference |
| Source | Project requirement |
| Priority | Essential |
| Status | Defined |

## REQ-010: Engineering Warnings

| Field | Value |
|-------|-------|
| ID | REQ-010 |
| Category | Software |
| Description | Display ERROR, WARNING, and INFORMATION messages for engineering validation |
| Source | Project requirement |
| Priority | Essential |
| Status | Defined |

## REQ-011: PDF Report Generation

| Field | Value |
|-------|-------|
| ID | REQ-011 |
| Category | Software |
| Description | Generate a printable PDF report containing project info, inputs, calculation trace, results, and source references |
| Source | Project requirement |
| Priority | Essential |
| Status | Defined |

## REQ-012: Project Saving

| Field | Value |
|-------|-------|
| ID | REQ-012 |
| Category | Software |
| Description | Save and load mix design projects including all inputs, results, and calculation traces |
| Source | Project requirement |
| Priority | Essential |
| Status | Defined |

## REQ-013: Input Validation

| Field | Value |
|-------|-------|
| ID | REQ-013 |
| Category | Software |
| Description | Validate all user inputs against documented BRE valid ranges and engineering constraints |
| Source | SRC-BRE-001, project requirement |
| Priority | Essential |
| Status | Defined |

---

*Created: 2026-09-18*
