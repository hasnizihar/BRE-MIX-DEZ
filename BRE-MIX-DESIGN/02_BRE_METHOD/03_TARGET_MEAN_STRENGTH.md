# BRE Mix Design — Stage 1: Target Mean Strength

> **Source:** SRC-BRE-001 — BRE BR 331, Second Edition, 1997
> **BRE Stage:** 1 (Strength)

---

## Purpose

Calculate the **target mean strength** (f_m) that the concrete mix must achieve to ensure that the specified **characteristic strength** (f_ck) is met with an acceptable probability.

## Engineering Principle

Concrete strength test results are assumed to follow a **normal distribution** (Assumption A1). To ensure that no more than a specified percentage of results fall below the characteristic strength, the mix must be designed for a higher mean strength.

The difference between target mean strength and characteristic strength is called the **margin**.

---

## Equations

### EQ-BRE-001: Target Mean Strength

```
f_m = f_ck + M
```

| Variable | Meaning | Unit |
|----------|---------|------|
| f_m | Target mean compressive strength | N/mm² |
| f_ck | Specified characteristic compressive strength | N/mm² |
| M | Margin | N/mm² |

### EQ-BRE-002: Margin

```
M = k × s
```

| Variable | Meaning | Unit |
|----------|---------|------|
| M | Margin | N/mm² |
| k | Statistical factor for proportion defective | dimensionless |
| s | Standard deviation of concrete strength results | N/mm² |

---

## k Factor Values

The k factor is derived from the **inverse normal distribution** for the specified proportion defective.

| Proportion Defective | k Factor |
|---------------------|----------|
| 10% | 1.28 |
| 5% | 1.64 |
| 2.5% | 1.96 |
| 1% | 2.33 |

- **Source:** SRC-BRE-001
- **Verification Status:** CROSS-VERIFIED — confirmed by multiple sources
- **Most common value:** k = 1.64 (5% defectives)
- **Engineering note:** k = 1.64 was aligned with the then-current BS 5328 requirement. Current BS 8500/BS EN 206 uses similar statistical concepts.

---

## Standard Deviation Guidance

The BRE method provides guidance for selecting the standard deviation when no site-specific data is available.

### When historical data IS available

Use the calculated standard deviation from at least 20–40 consecutive test results from similar production conditions.

### When historical data is NOT available

The BRE method suggests using the following as a guide:

| Level of Control | Approximate Standard Deviation (s) | Resulting Margin (M = 1.64 × s) |
|-----------------|-------------------------------------|----------------------------------|
| Very good control | Approximately 4 N/mm² | ≈ 6.6 N/mm² |
| Normal / moderate control | Approximately 5–6 N/mm² | ≈ 8–10 N/mm² |
| Poor control | Approximately 8 N/mm² | ≈ 13 N/mm² |

> **VERIFICATION STATUS: SECONDARY**
>
> The exact table of default standard deviations from BR 331 could not be directly extracted from the PDF.
> The values above are derived from multiple Tier 2/3 sources and are consistent with standard UK practice.
> A commonly cited BRE guidance value is a margin of approximately **10–12 N/mm²** when no data is available.
>
> **ENGINEERING REVIEW REQUIRED:** Verify exact standard deviation guidance table from BR 331 physical copy.

---

## Calculation Procedure

```
Step 1: Obtain characteristic strength (f_ck) — user input
         ↓
Step 2: Determine proportion defective — user input or default 5%
         ↓
Step 3: Select k factor from table
         ↓
Step 4: Determine standard deviation (s) — from historical data or guidance
         ↓
Step 5: Calculate margin: M = k × s
         ↓
Step 6: Calculate target mean strength: f_m = f_ck + M
```

## Worked Example

```
Given:
  f_ck = 30 N/mm²
  Proportion defective = 5%  →  k = 1.64
  Standard deviation (s) = 8 N/mm²

Calculate:
  Margin (M) = 1.64 × 8 = 13.12 N/mm²
  Target mean strength (f_m) = 30 + 13.12 = 43.12 N/mm²

Therefore:
  f_m ≈ 43 N/mm²
```

## Software Notes

- **Suggested function name:** `calculate_target_mean_strength(f_ck, k, s)`
- **Returns:** `f_m` in N/mm²
- **Input validation:** f_ck > 0, k > 0, s ≥ 0
- **Rounding:** See `05_CALCULATIONS/ROUNDING_RULES.md`

---

*Source: SRC-BRE-001*
*Verification Status: CROSS-VERIFIED (equation and k factors); SECONDARY (standard deviation guidance)*
*Created: 2026-09-18*
