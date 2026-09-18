# Equations Register

> Complete list of all BRE mix design equations with full specifications.

---

## EQ-BRE-001: Target Mean Strength

| Field | Value |
|-------|-------|
| **Name** | Target Mean Strength |
| **Purpose** | Calculate the mean compressive strength the mix must achieve |
| **Source** | SRC-BRE-001 |
| **Location** | BRE BR 331, Stage 1 |
| **Equation** | `f_m = f_ck + M` |
| **Inputs** | f_ck (N/mm²), M (N/mm²) |
| **Outputs** | f_m (N/mm²) |
| **Validity** | f_ck > 0, M ≥ 0 |
| **Rounding** | Round to 1 decimal place for display |
| **Status** | CROSS-VERIFIED |
| **Software Function** | `calculate_target_mean_strength()` |

## EQ-BRE-002: Margin

| Field | Value |
|-------|-------|
| **Name** | Margin |
| **Purpose** | Calculate the statistical margin above characteristic strength |
| **Source** | SRC-BRE-001 |
| **Equation** | `M = k × s` |
| **Inputs** | k (dimensionless), s (N/mm² - see STD-BRE-001) |
| **Outputs** | M (N/mm²) |
| **Validity** | k > 0, s ≥ 0 |
| **Status** | CROSS-VERIFIED |
| **Software Function** | `calculate_margin()` |

## EQ-BRE-003: Cement Content

| Field | Value |
|-------|-------|
| **Name** | Cement Content |
| **Purpose** | Calculate required cement per cubic metre |
| **Source** | SRC-BRE-001 |
| **Location** | BRE BR 331, Stage 3 |
| **Equation** | `C = W / (w/c)` |
| **Inputs** | W (kg/m³), w/c (dimensionless) |
| **Outputs** | C (kg/m³) |
| **Validity** | W > 0, w/c > 0 |
| **Assumptions** | No minimum/maximum constraints applied at this stage |
| **Rounding** | Round to nearest 5 kg/m³ for practical batching |
| **Status** | VERIFIED |
| **Software Function** | `calculate_cement_content()` |

## EQ-BRE-004: Total Aggregate Content

| Field | Value |
|-------|-------|
| **Name** | Total Aggregate Content |
| **Purpose** | Calculate total aggregate per cubic metre (SSD basis) |
| **Source** | SRC-BRE-001 |
| **Location** | BRE BR 331, Stage 4 |
| **Equation** | `A_total = D_wet - C - W` |
| **Inputs** | D_wet (kg/m³), C (kg/m³), W (kg/m³) |
| **Outputs** | A_total (kg/m³) |
| **Validity** | D_wet > C + W |
| **Status** | VERIFIED |
| **Software Function** | `calculate_total_aggregate()` |

## EQ-BRE-005: Fine Aggregate Content

| Field | Value |
|-------|-------|
| **Name** | Fine Aggregate Content |
| **Purpose** | Calculate fine aggregate per cubic metre |
| **Source** | SRC-BRE-001 |
| **Location** | BRE BR 331, Stage 5 |
| **Equation** | `FA = A_total × (P_fine / 100)` |
| **Inputs** | A_total (kg/m³), P_fine (%) |
| **Outputs** | FA (kg/m³) |
| **Validity** | A_total > 0, 0 < P_fine < 100 |
| **Status** | VERIFIED |
| **Software Function** | `calculate_fine_aggregate()` |

## EQ-BRE-006: Coarse Aggregate Content

| Field | Value |
|-------|-------|
| **Name** | Coarse Aggregate Content |
| **Purpose** | Calculate coarse aggregate per cubic metre |
| **Source** | SRC-BRE-001 |
| **Location** | BRE BR 331, Stage 5 |
| **Equation** | `CA = A_total - FA` |
| **Inputs** | A_total (kg/m³), FA (kg/m³) |
| **Outputs** | CA (kg/m³) |
| **Validity** | A_total > FA |
| **Status** | VERIFIED |
| **Software Function** | `calculate_coarse_aggregate()` |

## EQ-BRE-007: Adjusted Batch Water

| Field | Value |
|-------|-------|
| **Name** | Adjusted Batch Water |
| **Purpose** | Calculate actual water to add, correcting for aggregate moisture |
| **Source** | SRC-BRE-001 |
| **Equation** | `W_batch = W - FA×(MC_FA-Abs_FA)/100 - CA×(MC_CA-Abs_CA)/100` |
| **Inputs** | W, FA, CA (kg/m³), MC_FA, MC_CA, Abs_FA, Abs_CA (%) |
| **Outputs** | W_batch (kg/m³) |
| **Validity** | W_batch should be > 0; warn if negative |
| **Status** | CROSS-VERIFIED |
| **Software Function** | `calculate_batch_water()` |

## EQ-BRE-008: Adjusted Fine Aggregate

| Field | Value |
|-------|-------|
| **Name** | Adjusted Fine Aggregate (wet mass) |
| **Equation** | `FA_batch = FA × (1 + MC_FA / 100)` |
| **Status** | CROSS-VERIFIED |
| **Software Function** | `calculate_batch_fine_aggregate()` |

## EQ-BRE-009: Adjusted Coarse Aggregate

| Field | Value |
|-------|-------|
| **Name** | Adjusted Coarse Aggregate (wet mass) |
| **Equation** | `CA_batch = CA × (1 + MC_CA / 100)` |
| **Status** | CROSS-VERIFIED |
| **Software Function** | `calculate_batch_coarse_aggregate()` |

---

*Source: SRC-BRE-001*
*Created: 2026-09-18*
