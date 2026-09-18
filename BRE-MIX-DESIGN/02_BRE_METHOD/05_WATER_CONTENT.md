# BRE Mix Design — Stage 2: Water Content

> **Source:** SRC-BRE-001 — BRE BR 331, Second Edition, 1997
> **BRE Stage:** 2 (Water Content)

---

## Purpose

Determine the **free water content** (kg/m³) required to achieve the specified workability for the given aggregate size and type.

## Engineering Principle

The water content required depends on:
1. **Desired workability** (slump or Vebe time)
2. **Maximum aggregate size** (larger aggregates require less water)
3. **Type of aggregate** (crushed aggregates require more water than uncrushed)

---

## Table 3: Approximate Free-Water Contents (kg/m³)

### TBL-BRE-003

| Slump Range (mm) | Vebe Time (s) | 10 mm Uncrushed | 10 mm Crushed | 20 mm Uncrushed | 20 mm Crushed | 40 mm Uncrushed | 40 mm Crushed |
|-------------------|---------------|-----------------|---------------|-----------------|---------------|-----------------|---------------|
| 0–10 | >12 | 150 | 180 | 135 | 170 | 115 | 155 |
| 10–30 | 6–12 | 180 | 205 | 160 | 190 | 140 | 175 |
| 30–60 | 3–6 | 205 | 230 | 180 | 210 | 160 | 190 |
| 60–180 | 0–3 | 225 | 250 | 195 | 225 | 175 | 205 |

- **Source:** SRC-BRE-001
- **Verification Status:** CROSS-VERIFIED — values confirmed by multiple Tier 2/3 sources
- **Units:** kg/m³
- **Interpolation:** NOT specified within a slump range — the entire range maps to one value

### Engineering Notes

1. The table applies to the **type of fine aggregate** — if the fine aggregate type differs from the coarse aggregate type, the water content should be estimated based on the fine aggregate type (as the fine aggregate has a greater influence on water demand).

2. For **mixed aggregate types** (e.g., uncrushed fine with crushed coarse), the BRE method suggests:
   ```
   W = (2/3 × W_fine_type) + (1/3 × W_coarse_type)
   ```
   where W_fine_type is the water content for the fine aggregate type and W_coarse_type is for the coarse aggregate type.

   > **VERIFICATION STATUS: SECONDARY** — This weighted average formula is consistently reported in Tier 2/3 sources but exact wording from BR 331 requires verification.

3. The slump ranges are inclusive of the boundary values.

4. Vebe times correspond inversely to slump ranges — higher Vebe time = lower workability.

---

## Workability Classification (from BRE method)

### TBL-BRE-001: Workability Levels

| Degree of Workability | Slump (mm) | Vebe Time (s) | Typical Use |
|-----------------------|------------|---------------|-------------|
| Very low | 0–10 | >12 | Roads, vibrated heavy sections |
| Low | 10–30 | 6–12 | Road construction, mass concrete |
| Medium | 30–60 | 3–6 | Normal reinforced concrete |
| High | 60–180 | 0–3 | Heavily reinforced, thin sections |

- **Source:** SRC-BRE-001
- **Verification Status:** CROSS-VERIFIED

---

## Procedure

```
Step 1: Determine required workability
        (slump in mm or Vebe time in seconds)
         ↓
Step 2: Identify maximum aggregate size (10, 20, or 40 mm)
         ↓
Step 3: Identify aggregate type (crushed or uncrushed)
         ↓
Step 4: Look up free water content from Table 3
         ↓
Step 5: If fine and coarse aggregate types differ:
        Apply weighted average:
        W = (2/3 × W_fine_type) + (1/3 × W_coarse_type)
         ↓
Step 6: Record free water content (W) in kg/m³
```

## Software Notes

- **Suggested function name:** `determine_free_water_content(slump, max_agg_size, fine_agg_type, coarse_agg_type)`
- **Returns:** Free water content (W) in kg/m³
- **Data required:** Table 3 values
- **Interpolation:** Not applicable within slump ranges (discrete lookup). If slump falls on a range boundary, use the range it falls into.
- **Mixed aggregates:** Apply 2/3:1/3 weighted average formula

---

*Source: SRC-BRE-001*
*Verification Status: CROSS-VERIFIED (Table 3), SECONDARY (mixed aggregate formula)*
*Created: 2026-09-18*
