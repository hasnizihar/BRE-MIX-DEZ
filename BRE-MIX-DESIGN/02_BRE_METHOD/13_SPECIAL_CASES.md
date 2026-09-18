# BRE Mix Design — Special Cases

> **Source:** SRC-BRE-001 — BRE BR 331, Second Edition, 1997

---

## Purpose

Document special cases and modifications described in BRE BR 331 that are outside the initial scope but documented for completeness and future implementation.

---

## 1. Air-Entrained Concrete

### Status: EXCLUDED FROM INITIAL SCOPE — Future implementation

### BRE Guidance

The BRE method provides the following modifications for air-entrained concrete:

#### Water Content Adjustment

When air-entraining agents are used, workability increases for a given water content. The BRE method suggests:

```
Reduce the target free water content by selecting
a workability level one step lower in Table 3
```

> **VERIFICATION STATUS: SECONDARY** — consistently reported across Tier 2/3 sources

#### Density Adjustment

Air-entrained concrete has a lower wet density because entrained air displaces material. The estimated wet density should be reduced:

```
D_wet_air = D_wet × (1 - air_content / 100)
```

Where air_content is the target air content as a percentage.

> **VERIFICATION STATUS: INFERRED** — physical principle, but exact BRE formulation requires verification

#### Strength Adjustment

Entrained air reduces compressive strength. A commonly cited rule of thumb:

```
Each 1% of air content reduces strength by approximately 5–6%
```

> **VERIFICATION STATUS: SECONDARY** — general concrete engineering principle, not specific BRE values

---

## 2. PFA (Pulverised-Fuel Ash) Modifications

### Status: EXCLUDED FROM INITIAL SCOPE — Future implementation

### BRE Guidance

BRE BR 331 includes guidance on partial replacement of Portland cement with PFA (fly ash).

Key modifications:
- The w/c ratio is replaced by a **water/(cement+PFA) ratio**
- PFA affects the rate of strength development (lower early strength, potentially higher later strength)
- PFA generally improves workability, potentially reducing water demand
- The proportion of PFA typically ranges from 15% to 40% of total cementitious material
- The **cementing efficiency factor (k-factor for PFA)** must be applied

> **VERIFICATION STATUS: SECONDARY** — PFA modifications are documented in BR 331 but exact values require verification from the publication

---

## 3. GGBS (Ground Granulated Blastfurnace Slag) Modifications

### Status: EXCLUDED FROM INITIAL SCOPE — Future implementation

### BRE Guidance

BRE BR 331 includes guidance on partial replacement of Portland cement with GGBS.

Key modifications:
- Similar approach to PFA — replace cement content with cement+GGBS combination
- GGBS affects strength development (typically slower early strength)
- GGBS can improve sulfate resistance and reduce heat of hydration
- The proportion of GGBS typically ranges from 20% to 70% of total cementitious material

> **VERIFICATION STATUS: SECONDARY** — GGBS modifications are documented in BR 331 but exact values require verification

---

## 4. Design for Ages Other Than 28 Days

### Status: SUPPORTED (Table 2 provides data at 3, 7, 28, 91 days)

The method primarily targets 28-day strength but Table 2 provides reference strengths at other ages. The same Figure 4 procedure can be applied using the appropriate reference strength for the desired age.

> **VERIFICATION STATUS: CROSS-VERIFIED**

---

## 5. Combined Aggregate Types

### Status: PARTIALLY SUPPORTED

When fine and coarse aggregates are different types (e.g., natural sand with crushed coarse aggregate), the water content is adjusted using the weighted average formula documented in `05_WATER_CONTENT.md`.

> **VERIFICATION STATUS: SECONDARY**

---

## Summary of Special Cases

| Case | BRE Coverage | Initial Scope | Future Scope | Verification |
|------|-------------|---------------|--------------|-------------|
| Air-entrained concrete | Modifications documented | ❌ | ✓ | SECONDARY |
| PFA replacement | Modifications documented | ❌ | ✓ | SECONDARY |
| GGBS replacement | Modifications documented | ❌ | ✓ | SECONDARY |
| Design for other ages | Table 2 data available | Partial | ✓ | CROSS-VERIFIED |
| Mixed aggregate types | Water adjustment formula | ✓ | ✓ | SECONDARY |
| Lightweight concrete | NOT covered | ❌ | ❌ | N/A |
| Heavyweight concrete | NOT covered | ❌ | ❌ | N/A |
| Self-compacting concrete | NOT covered | ❌ | ❌ | N/A |

---

*Source: SRC-BRE-001*
*Verification Status: SECONDARY (most special case details)*
*Created: 2026-09-18*
