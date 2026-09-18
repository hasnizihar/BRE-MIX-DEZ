# Engineering Constants

> **Source:** SRC-BRE-001 — BRE BR 331, Second Edition, 1997

---

## Statistical Constants

### k Factor Values (Proportion Defective)

| ID | Proportion Defective | k Factor | Source | Status |
|----|---------------------|----------|--------|--------|
| CON-001 | 10% | 1.28 | SRC-BRE-001 | CROSS-VERIFIED |
| CON-002 | 5% | 1.64 | SRC-BRE-001 | CROSS-VERIFIED |
| CON-003 | 2.5% | 1.96 | SRC-BRE-001 | CROSS-VERIFIED |
| CON-004 | 1% | 2.33 | SRC-BRE-001 | CROSS-VERIFIED |

These are standard values from the **inverse of the standard normal distribution**.

- k = 1.64 is the most commonly used value (5% defectives, as typically required by UK specifications)
- These values are exact mathematical constants, not empirical data

### Standard Deviation Guidance (STD-BRE-001)

When calculating target mean strength without sufficient prior test data (n < 20), standard deviation values are taken from BRE BR 331 guidance. See [STD-BRE-001](file:///c:/Users/asus/Desktop/Hasni/BRE%20MIX%20DEZ/BRE-MIX-DESIGN/04_ENGINEERING_DATA/TABLES/STD-BRE-001.md) for complete details.

---

## Physical Constants

### Water Density

| ID | Name | Value | Unit | Source | Status |
|----|------|-------|------|--------|--------|
| CON-010 | Density of water | 1000 | kg/m³ | Standard | VERIFIED |

### Cement Density (typical)

| ID | Name | Value | Unit | Source | Status |
|----|------|-------|------|--------|--------|
| CON-011 | Typical density of Portland cement | 3150 | kg/m³ | Standard | VERIFIED |

Note: Cement density is used in volumetric calculations but is typically NOT required as a user input in the BRE method — the method works on mass basis.

---

## Method-Specific Constants

### Mixed Aggregate Weighting

| ID | Name | Fine Aggregate Weight | Coarse Aggregate Weight | Source | Status |
|----|------|-----------------------|------------------------|--------|--------|
| CON-020 | Aggregate type weighting for water content | 2/3 | 1/3 | SRC-BRE-001 | SECONDARY |

When fine and coarse aggregates are different types, the free water content is:
```
W = (2/3 × W_fine_type) + (1/3 × W_coarse_type)
```

---

*Source: SRC-BRE-001*
*Created: 2026-09-18*
