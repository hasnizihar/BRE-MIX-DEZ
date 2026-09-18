# BRE Mix Design — Scope, Assumptions & Limitations

> **Source:** SRC-BRE-001 — BRE BR 331, Design of Normal Concrete Mixes, Second Edition, 1997

---

## Scope of the BRE Method

The method is intended for the design of **normal concrete mixes** using:

- Portland cement (or Portland cement with approved additions)
- Natural or crushed aggregates of normal weight
- Water
- Admixtures (limited guidance)

## Applicability

| Parameter | BRE Method Applicability |
|-----------|------------------------|
| Concrete type | Normal-weight concrete |
| Cement types | Portland cement classes 42.5 and 52.5 |
| Aggregate types | Crushed and uncrushed (natural/gravel) |
| Maximum aggregate sizes | 10 mm, 20 mm, 40 mm |
| Strength range | Typically 20–60+ N/mm² (28-day characteristic) |
| Workability range | Very low to high (0–180 mm slump) |
| Curing | Standard (moist curing at 20°C assumed for table data) |

## Assumptions

### A1: Normal distribution of strength results

The statistical treatment (k × s margin) assumes concrete strength test results follow a **normal (Gaussian) distribution**.

- **Source:** SRC-BRE-001
- **Status:** VERIFIED — standard assumption in concrete technology
- **Engineering note:** This assumption is generally valid for well-controlled concrete production with sufficient test data.

### A2: Standard curing conditions

The compressive strength values in Table 2 and Figure 4 are based on **standard curing conditions** (water-cured specimens at approximately 20°C).

- **Source:** SRC-BRE-001
- **Status:** VERIFIED
- **Engineering note:** Site conditions may differ; trial mixes should use appropriate curing regimes.

### A3: SSD aggregate basis

All aggregate quantities are calculated on a **Saturated Surface-Dry (SSD)** basis. Corrections are required for actual moisture conditions.

- **Source:** SRC-BRE-001
- **Status:** VERIFIED

### A4: Free water (not total water)

The method uses **free water** — the water available for cement hydration and workability, excluding water absorbed by aggregates.

- **Source:** SRC-BRE-001
- **Status:** VERIFIED
- **Engineering note:** This distinction is critical. Total water = Free water + Absorbed water.

### A5: First approximation

The method produces a **first approximation** of mix proportions. Trial mixes are required to verify performance.

- **Source:** SRC-BRE-001
- **Status:** VERIFIED
- **Engineering note:** The method is not intended to produce a final mix without verification.

### A6: 28-day strength as primary design age

The primary design age is **28 days**. Table 2 provides strengths at 3, 7, 28, and 91 days, but the w/c ratio determination procedure typically targets 28-day strength.

- **Source:** SRC-BRE-001
- **Status:** CROSS-VERIFIED

### A7: Cube specimens

Strength values in the method are based on **cube specimens** (typically 150 mm cubes), which is standard UK practice.

- **Source:** SRC-BRE-001
- **Status:** INFERRED — standard UK testing practice at time of publication
- **Engineering note:** If cylinder strengths are used, a conversion factor would be required. This is outside the scope of the initial implementation.

## Limitations

### L1: Not applicable to special concretes

The method is **NOT** designed for:
- Lightweight concrete
- Heavyweight concrete
- Self-compacting concrete
- High-performance concrete
- Fibre-reinforced concrete
- Sprayed concrete (shotcrete)

### L2: Limited to documented cement types

The table data covers cement classes 42.5 and 52.5. Other cement types or combinations require the modification procedures described in the special cases section.

### L3: Limited aggregate sizes

Data is provided for 10 mm, 20 mm, and 40 mm maximum aggregate sizes only.

### L4: Graphical data limitations

Figures 4, 5, and 6 are graphical relationships. Values between data points require interpolation, which introduces approximation. The accuracy of software implementation depends on the quality of digitization of these charts.

### L5: Historical publication

The method was published in 1997. The UK concrete specification framework has since evolved (BS 5328 → BS 8500 / BS EN 206). Durability requirements and exposure classes should be obtained from current standards, not from the BRE method alone.

### L6: Aggregate variability

The method provides typical values for "crushed" and "uncrushed" aggregates. Actual aggregate properties (shape, texture, grading) may significantly affect mix performance.

### L7: Temperature effects

The method does not account for the effects of ambient temperature on concrete properties or workability loss during transport and placing.

## Exclusions (from initial software implementation)

| Item | Reason |
|------|--------|
| Air-entrained concrete | BRE provides guidance but excluded from initial scope |
| PFA modifications | BRE provides guidance but excluded from initial scope |
| GGBS modifications | BRE provides guidance but excluded from initial scope |
| Admixtures (chemical) | Limited guidance in BRE; significant current practice evolution |
| Durability design | Requires BS 8500; outside BRE method scope |
| Structural design | Entirely separate discipline |
| Multi-age strength design | Initial focus on 28-day; other ages documented for reference |

---

*Source: SRC-BRE-001*
*Verification Status: CROSS-VERIFIED*
*Created: 2026-09-18*
