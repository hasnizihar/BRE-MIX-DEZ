# BRE Mix Design Method — Overview

> **Source:** SRC-BRE-001 — BRE BR 331, Design of Normal Concrete Mixes, Second Edition, 1997

---

## Method Summary

The BRE/DoE method is an **empirical mix-proportioning procedure** for normal-weight concrete. It uses a systematic 5-stage approach to determine the quantities of cement, water, fine aggregate, and coarse aggregate required to produce concrete meeting specified strength and workability requirements.

## Historical Context

| Event | Year |
|-------|------|
| Original DoE method published | 1975 |
| Revised | 1988 |
| BRE BR 331, Second Edition published | 1997 |
| BS 5328 replaced by BS 8500 / BS EN 206 | 2003 |

The method was developed by the Department of the Environment (DoE) and later maintained by BRE. The 1997 second edition is the final published edition.

## Design Workflow

```
USER REQUIREMENTS
       ↓
STAGE 1: STRENGTH
  ├── Characteristic strength (input)
  ├── Percentage defectives (input/selected)
  ├── Standard deviation (input/estimated)
  ├── Margin = k × s
  ├── Target mean strength = f_ck + Margin
  └── Free water/cement ratio (from Figure 4 / Table 2)
       ↓
STAGE 2: WATER CONTENT
  ├── Required workability — slump or Vebe (input)
  ├── Maximum aggregate size (input)
  ├── Aggregate type (input)
  └── Free water content (from Table 3)
       ↓
STAGE 3: CEMENT CONTENT
  ├── Cement = Free water ÷ w/c ratio
  ├── Check ≥ minimum cement content
  └── Check ≤ maximum cement content
       ↓
STAGE 4: TOTAL AGGREGATE
  ├── Relative density of aggregate SSD (input)
  ├── Estimated wet density (from Figure 5)
  └── Total aggregate = Wet density − Cement − Water
       ↓
STAGE 5: AGGREGATE PROPORTIONS
  ├── Percentage passing 600 µm (input from sieve analysis)
  ├── Fine aggregate proportion (from Figure 6)
  ├── Fine aggregate = Total aggregate × proportion
  └── Coarse aggregate = Total aggregate − Fine aggregate
       ↓
ADJUSTMENTS
  ├── Moisture corrections
  ├── Absorption corrections
  └── Batch quantities
       ↓
FINAL MIX DESIGN
       ↓
TRIAL MIX VERIFICATION
```

## The Five Stages

| Stage | Focus | Key Inputs | Key Outputs | Primary Data Source |
|-------|-------|-----------|-------------|-------------------|
| 1 | Strength | f_ck, k, s, cement type, aggregate type | f_m, w/c ratio | Figure 4, Table 2 |
| 2 | Water content | Slump/Vebe, max agg. size, agg. type | Free water (kg/m³) | Table 3 |
| 3 | Cement content | Free water, w/c ratio, min/max limits | Cement (kg/m³) | Calculated |
| 4 | Total aggregate | Relative density SSD, free water | Total aggregate (kg/m³) | Figure 5 |
| 5 | Aggregate proportions | %passing 600µm, w/c, slump, agg. size | Fine & coarse agg. (kg/m³) | Figure 6 |

## Key Features of the Method

1. **Empirical basis** — derived from extensive experimental data
2. **Tabulated/graphical data** — not purely formula-based; relies heavily on lookup tables and charts
3. **First approximation** — the method produces an initial design that must be verified through trial mixes
4. **SSD basis** — aggregate quantities are calculated on a Saturated Surface-Dry basis
5. **Free water** — uses free water (not total water) for all calculations
6. **Applicable to normal concrete** — not intended for lightweight, heavyweight, or special concretes

## Key Tables and Figures

| Reference | Title | Purpose |
|-----------|-------|---------|
| Table 2 | Approximate compressive strengths at w/c = 0.5 | Reference strength for w/c ratio determination |
| Table 3 | Approximate free-water contents | Water content lookup |
| Figure 4 | Relationship between compressive strength and w/c ratio | w/c ratio determination |
| Figure 5 | Estimated wet density of fully compacted concrete | Density estimation |
| Figure 6 | Recommended proportions of fine aggregate | Fine/coarse split |

## Modifications Documented in BR 331

The publication also documents modifications for:
- Air-entrained concrete
- Use of PFA (pulverised-fuel ash) as partial cement replacement
- Use of GGBS (ground granulated blastfurnace slag) as partial cement replacement

These are **excluded from the initial scope** but documented in `13_SPECIAL_CASES.md`.

---

*Source: SRC-BRE-001*
*Verification Status: CROSS-VERIFIED (multiple Tier 2/3 sources confirm the 5-stage structure)*
*Created: 2026-09-18*
