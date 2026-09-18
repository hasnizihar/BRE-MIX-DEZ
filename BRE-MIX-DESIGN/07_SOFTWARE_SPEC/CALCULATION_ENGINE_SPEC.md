# Calculation Engine Specification

## Purpose

The BRE Calculation Engine is a **pure calculation module** that takes validated inputs and produces a complete mix design with full traceability.

## Interface

```python
# Conceptual interface
def design_mix(inputs: MixDesignInputs) -> MixDesignResult:
    """
    Execute the complete BRE 5-stage mix design procedure.
    
    Returns a result containing:
    - Final mix proportions (SSD basis, per m³)
    - Batch quantities (moisture corrected)
    - Complete calculation trace
    - Engineering checks and warnings
    """
```

## Functions (one per calculation step)

| Function | Equation | Inputs | Output |
|----------|----------|--------|--------|
| `calculate_margin(k, s)` | EQ-BRE-002 | k, s | M (N/mm²) |
| `calculate_target_mean_strength(f_ck, M)` | EQ-BRE-001 | f_ck, M | f_m (N/mm²) |
| `lookup_reference_strength(cement_class, agg_type, age)` | TBL-BRE-002 | class, type, age | f_ref (N/mm²) |
| `determine_wc_ratio(f_m, f_ref, wc_max)` | GRAPH-BRE-001 | f_m, f_ref, wc_max | w/c |
| `lookup_free_water(slump, max_agg_size, fine_type, coarse_type)` | TBL-BRE-003 | slump, size, types | W (kg/m³) |
| `calculate_cement_content(W, wc, C_min, C_max)` | EQ-BRE-003 | W, w/c, limits | C (kg/m³), flags |
| `estimate_wet_density(W, RD_agg)` | GRAPH-BRE-002 | W, RD_agg | D_wet (kg/m³) |
| `calculate_total_aggregate(D_wet, C, W)` | EQ-BRE-004 | D_wet, C, W | A_total (kg/m³) |
| `lookup_fine_proportion(max_agg_size, slump, wc, pct_600)` | GRAPH-BRE-003 | size, slump, w/c, %600 | P_fine (%) |
| `calculate_fine_aggregate(A_total, P_fine)` | EQ-BRE-005 | A_total, P_fine | FA (kg/m³) |
| `calculate_coarse_aggregate(A_total, FA)` | EQ-BRE-006 | A_total, FA | CA (kg/m³) |
| `calculate_batch_corrections(W, FA, CA, MC_FA, MC_CA, Abs_FA, Abs_CA)` | EQ-BRE-007/008/009 | all | batch quantities |
| `run_engineering_checks(result)` | Rules | all values | checks[] |
| `generate_trace(result)` | N/A | all values | trace record |

## Design Principles

1. Each function must be independently testable
2. Each function must include source reference in docstring
3. No side effects — pure functions only
4. Full precision maintained internally; rounding only on output
5. Engineering data loaded from JSON files, not hardcoded

---

*Created: 2026-09-18*
