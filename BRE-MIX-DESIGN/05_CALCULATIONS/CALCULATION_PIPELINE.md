# Calculation Pipeline

> **Source:** SRC-BRE-001 — BRE BR 331, Second Edition, 1997

---

## Deterministic Calculation Workflow

The BRE mix design follows a **strict sequential pipeline**. Each step depends on the outputs of previous steps.

```
┌─────────────────────────────────────────────────────┐
│                    USER INPUTS                       │
│  f_ck, cement_class, agg_type, slump, d_max,        │
│  RD_agg, %600, [s], [k], [w/c_max], [C_min]        │
└──────────────────────┬──────────────────────────────┘
                       ↓
┌──────────────────────────────────────────────────────┐
│  STEP 1: Calculate Target Mean Strength              │
│  f_m = f_ck + k × s                                 │
│  Inputs: f_ck, k, s                                 │
│  Output: f_m (N/mm²)                                │
│  Equation: EQ-BRE-001, EQ-BRE-002                   │
└──────────────────────┬──────────────────────────────┘
                       ↓
┌──────────────────────────────────────────────────────┐
│  STEP 2: Determine Reference Strength at w/c 0.5    │
│  Lookup: TBL-BRE-002                                │
│  Inputs: cement_class, agg_type, age                 │
│  Output: f_ref (N/mm²)                              │
└──────────────────────┬──────────────────────────────┘
                       ↓
┌──────────────────────────────────────────────────────┐
│  STEP 3: Determine Water/Cement Ratio                │
│  Lookup: GRAPH-BRE-001 (Figure 4)                   │
│  Inputs: f_m, f_ref                                  │
│  Output: w/c (dimensionless)                        │
│  Check: IF w/c_max specified, w/c = min(w/c, w/c_max)│
└──────────────────────┬──────────────────────────────┘
                       ↓
┌──────────────────────────────────────────────────────┐
│  STEP 4: Determine Free Water Content                │
│  Lookup: TBL-BRE-003 (Table 3)                      │
│  Inputs: slump, d_max, fine_agg_type, coarse_agg_type│
│  Output: W (kg/m³)                                   │
└──────────────────────┬──────────────────────────────┘
                       ↓
┌──────────────────────────────────────────────────────┐
│  STEP 5: Calculate Cement Content                    │
│  C = W / (w/c)                                       │
│  Equation: EQ-BRE-003                                │
│  Check: C ≥ C_min (if specified)                     │
│  Check: C ≤ C_max (if specified)                     │
│  Output: C (kg/m³)                                   │
└──────────────────────┬──────────────────────────────┘
                       ↓
┌──────────────────────────────────────────────────────┐
│  STEP 6: Estimate Wet Density                        │
│  Lookup: GRAPH-BRE-002 (Figure 5)                   │
│  Inputs: W, RD_agg                                   │
│  Output: D_wet (kg/m³)                              │
└──────────────────────┬──────────────────────────────┘
                       ↓
┌──────────────────────────────────────────────────────┐
│  STEP 7: Calculate Total Aggregate                   │
│  A_total = D_wet - C - W                            │
│  Equation: EQ-BRE-004                                │
│  Output: A_total (kg/m³, SSD)                       │
└──────────────────────┬──────────────────────────────┘
                       ↓
┌──────────────────────────────────────────────────────┐
│  STEP 8: Determine Fine Aggregate Proportion         │
│  Lookup: GRAPH-BRE-003 (Figure 6)                   │
│  Inputs: d_max, slump, w/c, %600                    │
│  Output: P_fine (%)                                  │
└──────────────────────┬──────────────────────────────┘
                       ↓
┌──────────────────────────────────────────────────────┐
│  STEP 9: Calculate Fine Aggregate                    │
│  FA = A_total × (P_fine / 100)                      │
│  Equation: EQ-BRE-005                                │
│  Output: FA (kg/m³, SSD)                            │
└──────────────────────┬──────────────────────────────┘
                       ↓
┌──────────────────────────────────────────────────────┐
│  STEP 10: Calculate Coarse Aggregate                 │
│  CA = A_total - FA                                  │
│  Equation: EQ-BRE-006                                │
│  Output: CA (kg/m³, SSD)                            │
└──────────────────────┬──────────────────────────────┘
                       ↓
┌──────────────────────────────────────────────────────┐
│  STEP 11: Apply Moisture Corrections (if required)   │
│  Equations: EQ-BRE-007, EQ-BRE-008, EQ-BRE-009     │
│  Inputs: MC_FA, MC_CA, Abs_FA, Abs_CA               │
│  Outputs: W_batch, FA_batch, CA_batch               │
└──────────────────────┬──────────────────────────────┘
                       ↓
┌──────────────────────────────────────────────────────┐
│  STEP 12: Engineering Checks                         │
│  - Total mass ≈ D_wet                               │
│  - w/c ≤ w/c_max                                    │
│  - C ≥ C_min                                        │
│  - All values in reasonable ranges                   │
└──────────────────────┬──────────────────────────────┘
                       ↓
┌──────────────────────────────────────────────────────┐
│  OUTPUT: Final Mix Design                            │
│  W, C, FA, CA (SSD basis, per m³)                    │
│  W_batch, C, FA_batch, CA_batch (moisture corrected) │
│  Calculation trace                                   │
│  Engineering checks and warnings                     │
└──────────────────────────────────────────────────────┘
```

---

## Data Flow Summary

| Step | Inputs | Data Source | Outputs |
|------|--------|-----------|---------|
| 1 | f_ck, k, s | Equation | f_m |
| 2 | cement_class, agg_type, age | TBL-BRE-002 | f_ref |
| 3 | f_m, f_ref | GRAPH-BRE-001 | w/c |
| 4 | slump, d_max, agg_types | TBL-BRE-003 | W |
| 5 | W, w/c | Equation | C |
| 6 | W, RD_agg | GRAPH-BRE-002 | D_wet |
| 7 | D_wet, C, W | Equation | A_total |
| 8 | d_max, slump, w/c, %600 | GRAPH-BRE-003 | P_fine |
| 9 | A_total, P_fine | Equation | FA |
| 10 | A_total, FA | Equation | CA |
| 11 | FA, CA, moisture data | Equations | batch quantities |
| 12 | all values | Rules | checks/warnings |

---

*Source: SRC-BRE-001*
*Created: 2026-09-18*
