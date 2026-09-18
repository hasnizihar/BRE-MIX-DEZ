# BRE Mix Design — Field Corrections

> **Source:** SRC-BRE-001 — BRE BR 331, Second Edition, 1997

---

## Purpose

Convert the SSD-basis mix design quantities into **actual batch quantities** by correcting for the moisture content and absorption of aggregates.

---

## Engineering Principle

The mix design calculates aggregate quantities on an **SSD (Saturated Surface-Dry) basis**. In practice, aggregates are rarely in the SSD condition. They may be:

- **Wetter than SSD** — free moisture on the surface
- **Drier than SSD** — aggregate has not absorbed its full capacity

The free moisture must be subtracted from the batch water, and the aggregate mass must be increased to account for the water it carries.

---

## Equations

### EQ-BRE-007: Adjusted Batch Water

```
W_batch = W - FA_SSD × (MC_FA - Abs_FA) / 100 - CA_SSD × (MC_CA - Abs_CA) / 100
```

Where:
| Variable | Meaning | Unit |
|----------|---------|------|
| W_batch | Actual water to add at the mixer | kg |
| W | Design free water content | kg/m³ |
| FA_SSD | Fine aggregate (SSD basis from design) | kg/m³ |
| CA_SSD | Coarse aggregate (SSD basis from design) | kg/m³ |
| MC_FA | Total moisture content of fine aggregate (as delivered) | % |
| MC_CA | Total moisture content of coarse aggregate (as delivered) | % |
| Abs_FA | Absorption of fine aggregate (to reach SSD from oven-dry) | % |
| Abs_CA | Absorption of coarse aggregate (to reach SSD from oven-dry) | % |

### EQ-BRE-008: Adjusted Fine Aggregate Mass

```
FA_batch = FA_SSD × (1 + MC_FA / 100)
```

### EQ-BRE-009: Adjusted Coarse Aggregate Mass

```
CA_batch = CA_SSD × (1 + MC_CA / 100)
```

> **VERIFICATION STATUS: CROSS-VERIFIED**
> These moisture correction equations are standard concrete batching practice and are confirmed by multiple Tier 2/3 sources. The exact form used in BR 331 should be verified.

---

## Procedure

```
Step 1: Obtain SSD-basis quantities from mix design:
        W, C, FA_SSD, CA_SSD
         ↓
Step 2: Determine actual moisture content of aggregates:
        MC_FA (%), MC_CA (%)
         ↓
Step 3: Determine absorption values:
        Abs_FA (%), Abs_CA (%)
         ↓
Step 4: Calculate free moisture in each aggregate:
        Free moisture FA = MC_FA - Abs_FA (can be negative if dry)
        Free moisture CA = MC_CA - Abs_CA (can be negative if dry)
         ↓
Step 5: Adjust batch water:
        W_batch = W - FA_SSD × (MC_FA - Abs_FA)/100 - CA_SSD × (MC_CA - Abs_CA)/100
         ↓
Step 6: Adjust aggregate masses for actual moisture:
        FA_batch = FA_SSD × (1 + MC_FA/100)
        CA_batch = CA_SSD × (1 + MC_CA/100)
         ↓
Step 7: Cement content remains unchanged: C_batch = C
         ↓
Step 8: Apply batch volume scaling if needed
```

## Engineering Notes

1. If aggregates are **wetter than SSD** (MC > Abs), the free moisture reduces the batch water and increases the aggregate mass.
2. If aggregates are **drier than SSD** (MC < Abs), the aggregates will absorb water from the mix, so additional batch water is needed and aggregate mass is lower.
3. The sum of batch quantities should approximately equal the design quantities when accounting for water redistribution.
4. Moisture content and absorption should be determined by testing (BS EN 1097-5 or BS 812).
5. Cement content is NOT adjusted for moisture — cement is always batched as-is.

---

## Batch Volume Scaling

To convert from per-cubic-metre quantities to a specific batch volume:

```
Material_batch = Material_per_m³ × V_batch
```

Where V_batch is in cubic metres.

---

*Source: SRC-BRE-001*
*Verification Status: CROSS-VERIFIED*
*Created: 2026-09-18*
