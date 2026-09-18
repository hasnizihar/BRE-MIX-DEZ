# BRE Mix Design — Stage 5: Coarse Aggregate

> **Source:** SRC-BRE-001 — BRE BR 331, Second Edition, 1997
> **BRE Stage:** 5 (continued)

---

## Purpose

Calculate the **coarse aggregate content** as the remainder of total aggregate after subtracting fine aggregate.

---

## Equation

### EQ-BRE-006: Coarse Aggregate Content

```
CA = A_total - FA
```

| Variable | Meaning | Unit |
|----------|---------|------|
| CA | Coarse aggregate content | kg/m³ |
| A_total | Total aggregate content (from Stage 4) | kg/m³ |
| FA | Fine aggregate content (from Stage 5) | kg/m³ |

- **Source:** SRC-BRE-001
- **Verification Status:** VERIFIED

---

## Coarse Aggregate Fractions

For multi-fraction coarse aggregates (e.g., 10–20 mm and 20–40 mm), the BRE method provides guidance on the proportioning of coarse aggregate into different size fractions.

### Two-Fraction Split (for 20 mm maximum aggregate)

Typical proportioning for 20 mm maximum aggregate:
- 10–20 mm fraction: proportion of coarse aggregate

### Three-Fraction Split (for 40 mm maximum aggregate)

Typical proportioning for 40 mm maximum aggregate:
- 5–10 mm fraction
- 10–20 mm fraction
- 20–40 mm fraction

> **VERIFICATION STATUS: UNVERIFIED**
> The exact BRE BR 331 recommended coarse aggregate fraction proportions (e.g., for 2-fraction or 3-fraction splits) could not be extracted from the available sources with sufficient confidence.
>
> **ENGINEERING REVIEW REQUIRED:** Verify the exact proportioning recommendations for coarse aggregate fractions from BR 331.

---

## Procedure

```
Step 1: Obtain A_total from Stage 4
         ↓
Step 2: Obtain FA from Stage 5 (fine aggregate)
         ↓
Step 3: Calculate CA = A_total - FA
         ↓
Step 4: IF coarse aggregate is to be proportioned into fractions:
        Apply recommended BRE proportioning
        (when verified data is available)
         ↓
Step 5: Record CA in kg/m³ (SSD basis)
```

## Engineering Notes

1. The coarse aggregate content is a **derived value** — it is whatever remains after the fine aggregate proportion has been determined.
2. For single-size coarse aggregate, the full CA quantity is one fraction.
3. For graded coarse aggregate, the proportioning into fractions ensures proper packing density.
4. All quantities are on an **SSD basis** and must be corrected for actual moisture content before batching.

## Software Notes

- **Suggested function name:** `calculate_coarse_aggregate(A_total, FA)`
- **Returns:** CA in kg/m³
- **Optionally:** `proportion_coarse_fractions(CA, max_agg_size, fractions)` for multi-fraction proportioning

---

*Source: SRC-BRE-001*
*Verification Status: VERIFIED (equation), UNVERIFIED (fraction proportioning)*
*Created: 2026-09-18*
