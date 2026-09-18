# BRE Mix Design — Input Requirements

> **Source:** SRC-BRE-001 — BRE BR 331, Second Edition, 1997

---

## Complete Input List

### User Inputs (Required)

| # | Input | Symbol | Unit | BRE Stage | Valid Range | Notes |
|---|-------|--------|------|-----------|-------------|-------|
| 1 | Characteristic compressive strength | f_ck | N/mm² | 1 | Typically 20–60 | 28-day cube strength |
| 2 | Age at test | - | days | 1 | 3, 7, 28, 91 | Default: 28 days |
| 3 | Cement strength class | - | - | 1 | 42.5, 52.5 | Per BS EN 197-1 |
| 4 | Type of coarse aggregate | - | - | 1 | Crushed, Uncrushed | Affects strength and water demand |
| 5 | Type of fine aggregate | - | - | 2 | Crushed, Uncrushed | Affects water demand |
| 6 | Workability — Slump | - | mm | 2 | 0–180 | Or use Vebe time |
| 7 | Workability — Vebe time | - | seconds | 2 | >0 | Alternative to slump |
| 8 | Maximum aggregate size | d_max | mm | 2 | 10, 20, 40 | Nominal maximum size |
| 9 | Relative density of combined aggregate (SSD) | RD_agg | dimensionless | 4 | Typically 2.4–2.9 | Saturated Surface-Dry basis |
| 10 | Percentage of fine aggregate passing 600 µm sieve | %600 | % | 5 | 15–100 | From sieve analysis |

### User Inputs (Optional / Specification-Dependent)

| # | Input | Symbol | Unit | Purpose | Default |
|---|-------|--------|------|---------|---------|
| 11 | Standard deviation | s | N/mm² | Margin calculation | See guidance values |
| 12 | Proportion defective (k factor) | k | dimensionless | Margin calculation | 1.64 (5% defectives) |
| 13 | Specified maximum w/c ratio | w/c_max | dimensionless | Durability limit | None |
| 14 | Specified minimum cement content | C_min | kg/m³ | Durability limit | None |
| 15 | Specified maximum cement content | C_max | kg/m³ | Practical limit | None |

### Field Correction Inputs

| # | Input | Symbol | Unit | Purpose |
|---|-------|--------|------|---------|
| 16 | Moisture content of fine aggregate | MC_FA | % | Moisture correction |
| 17 | Moisture content of coarse aggregate | MC_CA | % | Moisture correction |
| 18 | Absorption of fine aggregate | Abs_FA | % | Moisture correction |
| 19 | Absorption of coarse aggregate | Abs_CA | % | Moisture correction |
| 20 | Batch volume | V_batch | m³ or litres | Batch sizing |

### Project Information (Non-Engineering)

| # | Input | Purpose |
|---|-------|---------|
| 21 | Project name | Identification |
| 22 | Mix reference | Identification |
| 23 | Date | Record |
| 24 | Engineer | Record |
| 25 | Notes | Documentation |

---

## Input Validation Rules

### Critical Engineering Validation

| Input | Validation Rule | Severity |
|-------|----------------|----------|
| f_ck | Must be > 0 N/mm² | ERROR |
| f_ck | Typically 20–60 N/mm²; warn if outside | WARNING |
| Cement class | Must be 42.5 or 52.5 | ERROR |
| Aggregate type | Must be Crushed or Uncrushed | ERROR |
| Slump | Must be ≥ 0 mm | ERROR |
| Slump > 180 mm | Outside documented range | WARNING |
| Max aggregate size | Must be 10, 20, or 40 mm | ERROR |
| RD_agg | Must be > 0 | ERROR |
| RD_agg < 2.0 or > 3.0 | Unusual value | WARNING |
| %600 | Must be 0–100% | ERROR |
| s | Must be ≥ 0 | ERROR |
| k | Must be > 0 | ERROR |
| w/c_max | If specified, must be > 0 and ≤ 1.0 | ERROR |
| C_min | If specified, must be > 0 | ERROR |

---

*Source: SRC-BRE-001*
*Verification Status: CROSS-VERIFIED*
*Created: 2026-09-18*
