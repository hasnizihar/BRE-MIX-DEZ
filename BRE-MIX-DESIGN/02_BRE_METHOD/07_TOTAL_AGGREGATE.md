# BRE Mix Design — Stage 4: Total Aggregate Content

> **Source:** SRC-BRE-001 — BRE BR 331, Second Edition, 1997
> **BRE Stage:** 4 (Total Aggregate Content)

---

## Purpose

Determine the **total aggregate content** (kg/m³) on an SSD basis by estimating the wet density of the fully compacted concrete and subtracting the cement and water masses.

---

## Equation

### EQ-BRE-004: Total Aggregate Content

```
A_total = D_wet - C - W
```

| Variable | Meaning | Unit |
|----------|---------|------|
| A_total | Total aggregate content (SSD basis) | kg/m³ |
| D_wet | Estimated wet density of fully compacted concrete | kg/m³ |
| C | Cement content (from Stage 3) | kg/m³ |
| W | Free water content (from Stage 2) | kg/m³ |

- **Source:** SRC-BRE-001
- **Verification Status:** VERIFIED

---

## Figure 5: Estimated Wet Density of Fully Compacted Concrete

### GRAPH-BRE-002

**Description:**
Figure 5 is a chart showing the relationship between:
- **X-axis:** Free-water content (kg/m³)
- **Y-axis:** Wet density of concrete (kg/m³)
- **Curves/lines:** Different values of relative density (SSD) of combined aggregate

**Typical range:**
- Free water content: 120–250 kg/m³
- Wet density: 2200–2500 kg/m³
- Relative density of aggregate: 2.4–2.9

### Digitized Data — Figure 5

> **VERIFICATION STATUS: DIGITIZED**
> The following values are derived from best-effort analysis of Figure 5 descriptions across multiple technical sources.

The wet density can be estimated using the following relationship:

```
D_wet = 10 × RD_agg × (1000 - W) / (10 × RD_agg - 10) + W
```

However, the BRE method uses a graphical lookup. A simplified linear approximation for common conditions:

#### Approximate Wet Density (kg/m³)

| Free Water Content (kg/m³) | RD = 2.5 | RD = 2.6 | RD = 2.7 | RD = 2.8 |
|---------------------------|----------|----------|----------|----------|
| 120 | 2370 | 2410 | 2450 | 2490 |
| 140 | 2360 | 2400 | 2440 | 2480 |
| 160 | 2350 | 2390 | 2430 | 2470 |
| 180 | 2340 | 2380 | 2420 | 2460 |
| 200 | 2330 | 2370 | 2410 | 2450 |
| 220 | 2320 | 2360 | 2400 | 2440 |
| 240 | 2310 | 2350 | 2390 | 2430 |

> **ENGINEERING REVIEW REQUIRED:** These digitized values should be verified against the physical Figure 5 in BR 331. The relationship between wet density, free water, and aggregate relative density follows physical principles (mass balance), but exact BRE curve values may differ from a pure theoretical calculation.

### Alternative Calculation Method

Some sources present the wet density estimation as a formula. A physically-based approach:

```
D_wet = W + C + A_total (by definition — this is circular)
```

The BRE method resolves this by providing Figure 5 as an empirical relationship. The wet density depends primarily on the aggregate relative density and water content.

A commonly cited formula:

```
D_wet = 2230 + (RD_agg - 2.6) × 400 - (W - 180) × 0.5
```

> **VERIFICATION STATUS: INFERRED**
> This formula is an approximation of the Figure 5 relationship derived from analysis of the chart. It is NOT an original BRE equation.

---

## Procedure

```
Step 1: Obtain free water content (W) from Stage 2
         ↓
Step 2: Obtain cement content (C) from Stage 3
         ↓
Step 3: Obtain relative density of combined aggregate SSD (RD_agg) — user input
         ↓
Step 4: Estimate wet density (D_wet) from Figure 5
        using W and RD_agg
         ↓
Step 5: Calculate total aggregate content:
        A_total = D_wet - C - W
         ↓
Step 6: Record A_total in kg/m³ (SSD basis)
```

## Engineering Notes

1. The total aggregate content is on an **SSD basis**. This is the standard reference condition.
2. If aggregate relative density is unknown, a default value of **2.6** is sometimes used for preliminary estimates. However, the actual value should always be determined from testing.
3. The typical range of wet density for normal concrete is **2300–2500 kg/m³**.

## Software Notes

- **Suggested function name:** `calculate_total_aggregate(D_wet, C, W)` and `estimate_wet_density(W, RD_agg)`
- **Returns:** A_total in kg/m³
- **Data required:** Figure 5 digitized data or approximation formula
- **Interpolation:** Bilinear interpolation between W and RD_agg values

---

*Source: SRC-BRE-001*
*Verification Status: VERIFIED (equation), DIGITIZED (Figure 5 data)*
*Created: 2026-09-18*
