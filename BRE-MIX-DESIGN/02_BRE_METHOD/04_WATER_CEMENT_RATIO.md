# BRE Mix Design — Stage 1: Water/Cement Ratio

> **Source:** SRC-BRE-001 — BRE BR 331, Second Edition, 1997
> **BRE Stage:** 1 (Strength — continued)

---

## Purpose

Determine the **free water/cement ratio** required to achieve the target mean strength for the given cement type and aggregate type.

## Method

The BRE method uses a **two-step graphical/tabular procedure**:

1. **Table 2** provides approximate compressive strengths at a fixed w/c ratio of 0.5 for different cement classes and aggregate types.
2. **Figure 4** provides curves relating compressive strength to w/c ratio. Using the target mean strength and the Table 2 reference value, the required w/c ratio is determined.

---

## Table 2: Approximate Compressive Strengths (N/mm²) at w/c = 0.5

| Cement Strength Class | Type of Coarse Aggregate | 3 days | 7 days | 28 days | 91 days |
|-----------------------|-------------------------|--------|--------|---------|---------|
| 42.5 | Uncrushed | 22 | 30 | 42 | 49 |
| 42.5 | Crushed | 27 | 36 | 49 | 56 |
| 52.5 | Uncrushed | 29 | 37 | 48 | 54 |
| 52.5 | Crushed | 34 | 43 | 55 | 61 |

- **Table ID:** TBL-BRE-002
- **Source:** SRC-BRE-001
- **Verification Status:** CROSS-VERIFIED — values confirmed by multiple Tier 2/3 sources
- **Units:** N/mm² (= MPa)
- **Interpolation:** Linear interpolation between ages is PERMITTED
- **Note:** These are reference strengths at w/c = 0.5 used as an entry point to Figure 4

---

## Figure 4: Relationship Between Compressive Strength and w/c Ratio

### Description

Figure 4 is a graphical chart with:
- **X-axis:** Free water/cement ratio (typically 0.3 to 0.9)
- **Y-axis:** Compressive strength (N/mm²)
- **Curves:** Multiple curves for different starting strengths at w/c = 0.5

### How to Use

1. From Table 2, find the reference compressive strength at w/c = 0.5 for your cement class and aggregate type
2. On Figure 4, locate this reference strength on the curve at w/c = 0.5
3. Follow the appropriate curve to find the w/c ratio corresponding to your target mean strength

### Digitized Data — Figure 4 Reference Curves

> **VERIFICATION STATUS: DIGITIZED**
> The following data points are derived from best-effort digitization of Figure 4 using multiple published sources. They are NOT original tabulated values from BRE BR 331. Values have been cross-referenced across multiple university and technical publications.

The curves in Figure 4 can be approximated using the relationship between the reference strength at w/c = 0.5 and the desired target strength. The curves follow a general pattern where:

- Decreasing w/c ratio increases strength
- The relationship is approximately logarithmic/power curve

#### Approximate Strength vs w/c Ratio Data Points

For **28-day strength, Cement 42.5, Uncrushed aggregate** (Reference strength at 0.5 = 42 N/mm²):

| w/c Ratio | Approximate Strength (N/mm²) |
|-----------|------------------------------|
| 0.30 | 65 |
| 0.35 | 58 |
| 0.40 | 52 |
| 0.45 | 47 |
| 0.50 | 42 |
| 0.55 | 37 |
| 0.60 | 33 |
| 0.65 | 29 |
| 0.70 | 25 |
| 0.75 | 22 |
| 0.80 | 19 |

> **ENGINEERING REVIEW REQUIRED:** These digitized values should be verified against a physical copy of BR 331 Figure 4. The exact shape of the curves and the spacing between them is critical for accurate w/c ratio determination.

---

## Procedure for w/c Ratio Selection

```
Step 1: From Table 2, obtain reference strength at w/c = 0.5
        for the specified cement class and aggregate type
         ↓
Step 2: Using Figure 4, determine the w/c ratio required
        to achieve the target mean strength (from Stage 1)
         ↓
Step 3: IF a maximum w/c ratio is specified for durability:
        Select the LOWER of:
          - the strength-based w/c ratio (Step 2)
          - the specified maximum w/c ratio
         ↓
Step 4: Record the selected w/c ratio
```

## Durability Check

The final w/c ratio must be checked against any durability requirements:

```
w/c_final = MIN(w/c_strength, w/c_max_durability)
```

If w/c_max_durability controls, the actual strength will exceed the target mean strength.

If no durability limit is specified, use the strength-based value.

---

## Software Notes

- **Suggested function name:** `determine_wc_ratio(f_m, cement_class, aggregate_type, age, wc_max=None)`
- **Returns:** w/c ratio (dimensionless)
- **Data required:** Table 2 values and Figure 4 curve data
- **Interpolation:** Required for both Table 2 (between ages) and Figure 4 (between data points)
- **Input validation:** f_m > 0, valid cement class, valid aggregate type

---

*Source: SRC-BRE-001*
*Verification Status: CROSS-VERIFIED (Table 2), DIGITIZED (Figure 4 curve data)*
*Created: 2026-09-18*
