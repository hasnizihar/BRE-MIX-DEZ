# Engineering Data Dictionary

> **Purpose:** Define every engineering variable used in the BRE mix design method.
> **Source:** SRC-BRE-001 — BRE BR 331, Second Edition, 1997

---

## User Inputs

| Field ID | Name | Symbol | Unit | Data Type | Required | Allowed Range | Default | Source | Used By |
|----------|------|--------|------|-----------|----------|--------------|---------|--------|---------|
| INP-001 | Characteristic compressive strength | f_ck | N/mm² | float | Yes | >0, typically 20–60 | None | User/specification | EQ-BRE-001 |
| INP-002 | Cement strength class | - | - | enum | Yes | {42.5, 52.5} | None | User | TBL-BRE-002 |
| INP-003 | Type of coarse aggregate | - | - | enum | Yes | {Crushed, Uncrushed} | None | User | TBL-BRE-002, TBL-BRE-003 |
| INP-004 | Type of fine aggregate | - | - | enum | Yes | {Crushed, Uncrushed} | None | User | TBL-BRE-003 |
| INP-005 | Required slump | - | mm | float | Yes* | 0–180 | None | User/specification | TBL-BRE-003 |
| INP-006 | Required Vebe time | - | seconds | float | Yes* | >0 | None | User | TBL-BRE-003 |
| INP-007 | Maximum aggregate size | d_max | mm | enum | Yes | {10, 20, 40} | None | User | TBL-BRE-003, GRAPH-BRE-003 |
| INP-008 | Relative density of combined aggregate (SSD) | RD_agg | dimensionless | float | Yes | >0, typically 2.4–2.9 | None | User/testing | GRAPH-BRE-002 |
| INP-009 | Percentage passing 600 µm sieve | %600 | % | float | Yes | 0–100 | None | User/sieve analysis | GRAPH-BRE-003 |
| INP-010 | Standard deviation | s | N/mm² | float | No | ≥0 | STD-BRE-001 | User/production data | EQ-BRE-002 |
| INP-011 | Proportion defective | - | % | float | No | >0 | 5% | User/specification | k factor |
| INP-012 | Maximum w/c ratio | w/c_max | dimensionless | float | No | >0, ≤1.0 | None | Specification | Stage 1 check |
| INP-013 | Minimum cement content | C_min | kg/m³ | float | No | >0 | None | Specification | Stage 3 check |
| INP-014 | Maximum cement content | C_max | kg/m³ | float | No | >0 | None | Specification | Stage 3 check |
| INP-015 | Moisture content of fine aggregate | MC_FA | % | float | No | ≥0 | 0 (SSD) | Testing | Field corrections |
| INP-016 | Moisture content of coarse aggregate | MC_CA | % | float | No | ≥0 | 0 (SSD) | Testing | Field corrections |
| INP-017 | Absorption of fine aggregate | Abs_FA | % | float | No | ≥0 | 0 | Testing | Field corrections |
| INP-018 | Absorption of coarse aggregate | Abs_CA | % | float | No | ≥0 | 0 | Testing | Field corrections |
| INP-019 | Age at test | - | days | enum | No | {3, 7, 28, 91} | 28 | User | TBL-BRE-002 |

*INP-005 or INP-006 required — one workability measure must be provided.

---

## Derived Values (Calculated)

| Field ID | Name | Symbol | Unit | Equation | Depends On |
|----------|------|--------|------|----------|-----------|
| DER-001 | Margin | M | N/mm² | EQ-BRE-002 | k, s |
| DER-002 | Target mean strength | f_m | N/mm² | EQ-BRE-001 | f_ck, M |
| DER-003 | Reference strength at w/c 0.5 | f_ref | N/mm² | TBL-BRE-002 | Cement class, aggregate type, age |
| DER-004 | Free water/cement ratio | w/c | dimensionless | GRAPH-BRE-001 | f_m, f_ref |
| DER-005 | Free water content | W | kg/m³ | TBL-BRE-003 | Slump, d_max, aggregate type |
| DER-006 | Cement content | C | kg/m³ | EQ-BRE-003 | W, w/c |
| DER-007 | Estimated wet density | D_wet | kg/m³ | GRAPH-BRE-002 | W, RD_agg |
| DER-008 | Total aggregate content | A_total | kg/m³ | EQ-BRE-004 | D_wet, C, W |
| DER-009 | Fine aggregate proportion | P_fine | % | GRAPH-BRE-003 | d_max, slump, w/c, %600 |
| DER-010 | Fine aggregate content | FA | kg/m³ | EQ-BRE-005 | A_total, P_fine |
| DER-011 | Coarse aggregate content | CA | kg/m³ | EQ-BRE-006 | A_total, FA |
| DER-012 | Batch water | W_batch | kg | EQ-BRE-007 | W, FA, CA, MC_FA, MC_CA, Abs_FA, Abs_CA |
| DER-013 | Batch fine aggregate | FA_batch | kg | EQ-BRE-008 | FA, MC_FA |
| DER-014 | Batch coarse aggregate | CA_batch | kg | EQ-BRE-009 | CA, MC_CA |

---

## Constants

| Field ID | Name | Symbol | Value | Unit | Source | Status |
|----------|------|--------|-------|------|--------|--------|
| CON-001 | k factor (5% defectives) | k | 1.64 | dimensionless | SRC-BRE-001 | CROSS-VERIFIED |
| CON-002 | k factor (1% defectives) | k | 2.33 | dimensionless | SRC-BRE-001 | CROSS-VERIFIED |
| CON-003 | k factor (2.5% defectives) | k | 1.96 | dimensionless | SRC-BRE-001 | CROSS-VERIFIED |
| CON-004 | k factor (10% defectives) | k | 1.28 | dimensionless | SRC-BRE-001 | CROSS-VERIFIED |

---

## Lookup Data

| Field ID | Name | Data Source | Lookup Keys | Output |
|----------|------|-----------|-------------|--------|
| LKP-001 | Reference strength at w/c 0.5 | TBL-BRE-002 | Cement class, aggregate type, age | N/mm² |
| LKP-002 | Free water content | TBL-BRE-003 | Slump range, d_max, aggregate type | kg/m³ |
| LKP-003 | w/c ratio for target strength | GRAPH-BRE-001 | f_m, f_ref | dimensionless |
| LKP-004 | Estimated wet density | GRAPH-BRE-002 | W, RD_agg | kg/m³ |
| LKP-005 | Fine aggregate proportion | GRAPH-BRE-003 | d_max, slump, w/c, %600 | % |

---

*Source: SRC-BRE-001*
*Created: 2026-09-18*
