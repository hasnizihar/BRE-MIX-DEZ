# BRE Mix Design — Stage 5: Fine Aggregate

> **Source:** SRC-BRE-001 — BRE BR 331, Second Edition, 1997
> **BRE Stage:** 5 (Fine & Coarse Aggregate Proportions)

---

## Purpose

Determine the **proportion of fine aggregate** as a percentage of the total aggregate content, and calculate the fine aggregate mass.

---

## Method

The fine aggregate proportion is determined from **Figure 6** in BRE BR 331. Figure 6 provides recommended proportions of fine aggregate based on:

1. Maximum aggregate size (10, 20, or 40 mm)
2. Required workability (slump range)
3. Free water/cement ratio
4. Percentage of fine aggregate passing the 600 µm sieve (grading indicator)

---

## Figure 6: Recommended Proportions of Fine Aggregate

### GRAPH-BRE-003

**Description:**
Figure 6 consists of **three sub-charts** (one for each maximum aggregate size: 10, 20, 40 mm). Each sub-chart contains:
- **X-axis:** Free water/cement ratio (0.2 to 0.8)
- **Y-axis:** Proportion of fine aggregate (% of total aggregate)
- **Curves:** Different curves for different percentages passing 600 µm sieve (e.g., 15%, 30%, 45%, 60%, 80%, 100%)
- **Panels:** Different panels or regions for different slump ranges

### Digitized Data — Figure 6

> **VERIFICATION STATUS: DIGITIZED**
> The following values are approximations from multiple technical sources. They should be verified against the original Figure 6 in BR 331.

#### 20 mm Maximum Aggregate Size, Slump 30–60 mm

| w/c Ratio | 15% passing 600µm | 30% passing 600µm | 45% passing 600µm | 60% passing 600µm | 80% passing 600µm | 100% passing 600µm |
|-----------|-------|-------|-------|-------|-------|--------|
| 0.30 | 17 | 22 | 27 | 32 | 38 | 44 |
| 0.40 | 20 | 26 | 32 | 37 | 43 | 49 |
| 0.50 | 23 | 30 | 36 | 42 | 48 | 54 |
| 0.60 | 27 | 34 | 40 | 47 | 53 | 58 |
| 0.70 | 30 | 37 | 44 | 51 | 57 | 62 |
| 0.80 | 33 | 40 | 48 | 55 | 60 | 65 |

#### 20 mm Maximum Aggregate Size, Slump 60–180 mm

| w/c Ratio | 15% passing 600µm | 30% passing 600µm | 45% passing 600µm | 60% passing 600µm | 80% passing 600µm | 100% passing 600µm |
|-----------|-------|-------|-------|-------|-------|--------|
| 0.30 | 19 | 24 | 30 | 35 | 41 | 47 |
| 0.40 | 23 | 29 | 35 | 41 | 47 | 53 |
| 0.50 | 27 | 34 | 40 | 46 | 52 | 58 |
| 0.60 | 30 | 38 | 44 | 51 | 57 | 62 |
| 0.70 | 33 | 41 | 48 | 55 | 61 | 66 |
| 0.80 | 36 | 44 | 52 | 59 | 64 | 69 |

> **ENGINEERING REVIEW REQUIRED:** Complete digitization of Figure 6 for all aggregate sizes (10, 20, 40 mm) and all slump ranges (0–10, 10–30, 30–60, 60–180 mm) is required. The values above are approximate and cover only 20 mm aggregate at two slump ranges.

---

## Equations

### EQ-BRE-005: Fine Aggregate Content

```
FA = A_total × (P_fine / 100)
```

| Variable | Meaning | Unit |
|----------|---------|------|
| FA | Fine aggregate content | kg/m³ |
| A_total | Total aggregate content (from Stage 4) | kg/m³ |
| P_fine | Proportion of fine aggregate from Figure 6 | % |

- **Source:** SRC-BRE-001
- **Verification Status:** VERIFIED

---

## Procedure

```
Step 1: Obtain maximum aggregate size (10, 20, or 40 mm)
         ↓
Step 2: Obtain required workability (slump range)
         ↓
Step 3: Obtain w/c ratio (from Stage 1)
         ↓
Step 4: Obtain % passing 600 µm sieve (from sieve analysis — user input)
         ↓
Step 5: Look up fine aggregate proportion from Figure 6
        (select correct sub-chart and interpolate)
         ↓
Step 6: Calculate fine aggregate:
        FA = A_total × (P_fine / 100)
         ↓
Step 7: Record FA in kg/m³ (SSD basis)
```

## Engineering Notes

1. The 600 µm sieve is the **key grading parameter** used in the BRE method for fine aggregate characterization.
2. A finer sand (higher % passing 600 µm) generally requires a **lower proportion** of fine aggregate.
3. A coarser sand (lower % passing 600 µm) requires a **higher proportion** of fine aggregate.
4. The proportions from Figure 6 are recommendations — trial mixes may show that adjustment is needed.
5. If the % passing 600 µm falls between the curves, **linear interpolation** between curves is appropriate.

## Software Notes

- **Suggested function name:** `determine_fine_aggregate_proportion(max_agg_size, slump, wc_ratio, pct_passing_600)` and `calculate_fine_aggregate(A_total, P_fine)`
- **Data required:** Complete Figure 6 digitized data for all aggregate sizes and slump ranges
- **Interpolation:** Bilinear interpolation (between w/c ratios and % passing 600 µm curves)

---

*Source: SRC-BRE-001*
*Verification Status: VERIFIED (equation), DIGITIZED (Figure 6 data — partial)*
*Created: 2026-09-18*
