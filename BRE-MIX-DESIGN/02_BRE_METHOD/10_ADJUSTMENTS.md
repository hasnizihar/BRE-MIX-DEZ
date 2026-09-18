# BRE Mix Design — Adjustments

> **Source:** SRC-BRE-001 — BRE BR 331, Second Edition, 1997

---

## Purpose

Document adjustments that may be necessary to the initial mix design proportions.

## Types of Adjustments

### 1. Durability-Driven Adjustments

If durability requirements (from BS 8500 or project specification) impose:
- A maximum w/c ratio lower than the strength-based value
- A minimum cement content higher than the strength-based value

Then the mix proportions must be recalculated using the governing values. See `06_CEMENT_CONTENT.md` for the procedure.

### 2. Trial Mix Adjustments

After conducting a trial mix, adjustments may be needed if:
- **Workability** does not match the target slump → adjust free water content
- **Strength** does not match the target → adjust w/c ratio
- **Cohesion/finishing** is poor → adjust fine aggregate proportion

### BRE Guidance on Trial Mix Adjustments

The BRE method provides the following guidance for adjustments after trial mixes:

#### Workability adjustment

```
IF actual slump ≠ target slump:
    Adjust water content by approximately ±5 kg/m³ per 25 mm change in slump
    (for 20 mm aggregate)
```

> **VERIFICATION STATUS: SECONDARY**
> This guidance value is commonly cited in Tier 2/3 sources. Exact BR 331 wording requires verification.

#### Strength adjustment

```
IF actual 28-day strength ≠ target mean strength:
    Adjust w/c ratio
    Use Figure 4 with the actual trial-mix results to refine
```

#### Cohesion adjustment

```
IF mix appears harsh or segregating:
    Increase fine aggregate proportion by 2–5%
    Recheck total aggregate content
```

### 3. Combined Aggregate Type Adjustment

When fine and coarse aggregates are different types (e.g., uncrushed fine with crushed coarse):
- Water content is adjusted using the 2/3:1/3 weighted average (see `05_WATER_CONTENT.md`)

---

## Engineering Notes

1. Adjustments are iterative — each change may require rechecking other parameters.
2. The BRE method is a **first approximation** — trial mixes and adjustments are an integral part of the process.
3. When multiple adjustments are needed, work from the top of the calculation pipeline downwards.

---

*Source: SRC-BRE-001*
*Verification Status: SECONDARY (adjustment guidance values)*
*Created: 2026-09-18*
