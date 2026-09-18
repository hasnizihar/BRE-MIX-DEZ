# Rounding Rules

---

## Source Rounding

> **VERIFICATION STATUS: UNSPECIFIED for most values**
> BRE BR 331 does not appear to prescribe specific rounding rules for each calculation step. The following are based on standard engineering practice and common sense.

---

## Recommended Rounding Rules

| Value | Precision (Calculation) | Precision (Display) | Precision (Batching) | Notes |
|-------|------------------------|--------------------|--------------------|-------|
| Target mean strength (f_m) | Full float | 1 decimal (N/mm²) | N/A | |
| Margin (M) | Full float | 1 decimal (N/mm²) | N/A | |
| w/c ratio | Full float | 2 decimal places | 2 decimal places | |
| Free water content (W) | Full float | Nearest integer (kg/m³) | Nearest integer | |
| Cement content (C) | Full float | Nearest 5 kg/m³ | Nearest 5 kg/m³ | Common practice |
| Total aggregate (A_total) | Full float | Nearest integer (kg/m³) | Nearest 5 kg/m³ | |
| Fine aggregate (FA) | Full float | Nearest integer (kg/m³) | Nearest 5 kg/m³ | |
| Coarse aggregate (CA) | Full float | Nearest integer (kg/m³) | Nearest 5 kg/m³ | |
| Fine aggregate proportion (P_fine) | Full float | Nearest integer (%) | N/A | |
| Wet density (D_wet) | Full float | Nearest 10 kg/m³ | N/A | |
| Batch water (W_batch) | Full float | Nearest integer (kg) | Nearest integer | |

---

## General Rules

1. **Avoid premature rounding.** Carry full floating-point precision through all intermediate calculations.
2. **Round only for display** and final batch quantities.
3. **Rounding method:** Round half up (standard rounding) unless otherwise specified.
4. **Batch quantities:** Round to practical batching precision (nearest 5 kg for solids, nearest 1 kg for water).
5. **Report values:** Show to the precision indicated above.

---

## Items Marked UNSPECIFIED

The following rounding decisions are NOT specified by the BRE source:

- Whether to round cement content to nearest 5 or 10 kg/m³
- Whether to round aggregate to nearest 5 or 10 kg/m³
- Whether intermediate values in Figure 4/5/6 lookups should be rounded
- Whether the final total should be adjusted to exactly match the wet density

These decisions should be documented as `UNSPECIFIED` and the implementation should use the conservative approach of maintaining precision.

---

*Created: 2026-09-18*
