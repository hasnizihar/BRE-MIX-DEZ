# Interpolation Rules

> Document every situation in the BRE method where interpolation is required.

---

## INT-001: Table 2 — Interpolation Between Ages

| Field | Value |
|-------|-------|
| **Source** | TBL-BRE-002 |
| **Variables** | Age (days) → Compressive strength (N/mm²) |
| **Data Points** | 3, 7, 28, 91 days |
| **Method** | Linear interpolation between adjacent age values |
| **Boundary Handling** | Do not extrapolate beyond 3 days or 91 days |
| **Status** | INFERRED — linear interpolation is standard engineering practice; BRE does not explicitly specify the method |

**Formula:**
```
f_ref(age) = f_ref(age_lower) + (age - age_lower) / (age_upper - age_lower) × (f_ref(age_upper) - f_ref(age_lower))
```

> **NOTE:** For most practical applications, 28-day strength is used and interpolation is not needed. Interpolation between ages is only needed for non-standard design ages.

---

## INT-002: Figure 4 — w/c Ratio Determination

| Field | Value |
|-------|-------|
| **Source** | GRAPH-BRE-001 |
| **Variables** | Target mean strength (N/mm²) → w/c ratio |
| **Method** | Interpolation along the curve for the relevant cement/aggregate combination |
| **Boundary Handling** | Do not extrapolate beyond the documented curve range |
| **Status** | ENGINEERING REVIEW REQUIRED — the exact interpolation of the curves depends on the digitized data quality |

**Note:** Figure 4 curves are smooth, continuous relationships. Linear interpolation between digitized points is acceptable if data points are sufficiently close together.

---

## INT-003: Figure 5 — Wet Density Estimation

| Field | Value |
|-------|-------|
| **Source** | GRAPH-BRE-002 |
| **Variables** | Free water content (kg/m³) + RD_agg → Wet density (kg/m³) |
| **Method** | Bilinear interpolation between water content and relative density values |
| **Boundary Handling** | Do not extrapolate beyond documented ranges |
| **Status** | DIGITIZED — values are approximations |

**Formula (bilinear):**
```
D_wet(W, RD) = interpolate between nearest (W, RD) data points
```

---

## INT-004: Figure 6 — Fine Aggregate Proportion

| Field | Value |
|-------|-------|
| **Source** | GRAPH-BRE-003 |
| **Variables** | w/c ratio + % passing 600µm → Fine aggregate proportion (%) |
| **Method** | Bilinear interpolation between w/c ratio and % passing 600µm curves |
| **Boundary Handling** | Clamp to nearest boundary value; warn user |
| **Status** | DIGITIZED — values are approximations |

---

## INT-005: Table 3 — NO Interpolation Within Slump Ranges

| Field | Value |
|-------|-------|
| **Source** | TBL-BRE-003 |
| **Variables** | Slump (mm) → Free water content (kg/m³) |
| **Method** | **NOT applicable** — each slump range maps to a single discrete value |
| **Note** | The slump falls into one of four ranges; the water content is a step function, not continuous |
| **Status** | CROSS-VERIFIED |

---

## General Interpolation Rules

1. **Linear interpolation** is the default method unless otherwise specified.
2. **Do not extrapolate** beyond the documented data ranges. If a value falls outside, flag it as an error or warning.
3. **Digitized graph data** should have sufficient point density to make linear interpolation between adjacent points acceptably accurate.
4. **Intermediate precision:** Maintain full floating-point precision during interpolation; round only for final display.

---

*Source: SRC-BRE-001*
*Created: 2026-09-18*
