# BRE Mix Design — Final Mix

> **Source:** SRC-BRE-001 — BRE BR 331, Second Edition, 1997

---

## Purpose

Assemble the complete mix design output including all design quantities, batch quantities, and supporting information.

---

## Final Mix Design Output

### Design Quantities (per m³, SSD basis)

| Material | Symbol | Unit |
|----------|--------|------|
| Free water content | W | kg/m³ |
| Cement content | C | kg/m³ |
| Fine aggregate (SSD) | FA | kg/m³ |
| Coarse aggregate (SSD) | CA | kg/m³ |
| **Total** | - | kg/m³ |

### Design Parameters

| Parameter | Symbol | Unit |
|-----------|--------|------|
| Free water/cement ratio | w/c | dimensionless |
| Target mean strength | f_m | N/mm² |
| Characteristic strength | f_ck | N/mm² |
| Margin | M | N/mm² |
| Fine aggregate proportion | P_fine | % |
| Estimated wet density | D_wet | kg/m³ |

### Batch Quantities (corrected for moisture)

| Material | Symbol | Unit |
|----------|--------|------|
| Batch water | W_batch | kg/m³ |
| Cement | C | kg/m³ |
| Fine aggregate (wet) | FA_batch | kg/m³ |
| Coarse aggregate (wet) | CA_batch | kg/m³ |

---

## Engineering Checks

The following checks should be applied to the final mix:

| Check | Rule | Severity |
|-------|------|----------|
| Total mass ≈ wet density | Sum of materials should be close to estimated wet density | WARNING if >2% deviation |
| w/c ratio ≤ specified maximum | Durability check | ERROR if exceeded |
| Cement ≥ specified minimum | Durability check | ERROR if not met |
| Cement ≤ specified maximum | Practical check | WARNING if exceeded |
| Batch water > 0 | Moisture correction check | ERROR if negative |
| Fine aggregate proportion reasonable | Typically 25–50% | WARNING if outside |
| Cement content reasonable | Typically 240–500 kg/m³ | WARNING if outside |

---

## Mix Design Summary Report Content

The final mix design should be presented as:

```
═══════════════════════════════════════════════
           BRE MIX DESIGN SUMMARY
═══════════════════════════════════════════════

PROJECT: [name]
MIX REF: [reference]
DATE:    [date]
ENGINEER: [name]

METHOD:  BRE BR 331, Second Edition, 1997

───────────────────────────────────────────────
 DESIGN REQUIREMENTS
───────────────────────────────────────────────

 Characteristic strength:     XX N/mm²
 Target mean strength:        XX N/mm²
 Margin (k × s):              XX N/mm²
 Cement class:                42.5 / 52.5
 Aggregate type (coarse):     Crushed / Uncrushed
 Aggregate type (fine):       Crushed / Uncrushed
 Maximum aggregate size:      XX mm
 Required slump:              XX mm
 w/c ratio:                   0.XX

───────────────────────────────────────────────
 MIX PROPORTIONS (per m³, SSD basis)
───────────────────────────────────────────────

 Cement:              XXX kg/m³
 Free water:          XXX kg/m³
 Fine aggregate:      XXX kg/m³
 Coarse aggregate:    XXX kg/m³
 ─────────────────────────────
 Total:              XXXX kg/m³

 Estimated wet density:       XXXX kg/m³

───────────────────────────────────────────────
 BATCH QUANTITIES (corrected for moisture)
───────────────────────────────────────────────

 Cement:              XXX kg/m³
 Water (added):       XXX kg/m³
 Fine aggregate:      XXX kg/m³
 Coarse aggregate:    XXX kg/m³

───────────────────────────────────────────────
 ENGINEERING CHECKS
───────────────────────────────────────────────

 [✓] w/c ratio ≤ specified maximum
 [✓] Cement ≥ specified minimum
 [✓] Mix total ≈ wet density

───────────────────────────────────────────────
 TABLES & FIGURES USED
───────────────────────────────────────────────

 TBL-BRE-002: Compressive strengths at w/c 0.5
 TBL-BRE-003: Free water contents
 GRAPH-BRE-001: w/c ratio vs strength (Figure 4)
 GRAPH-BRE-002: Estimated wet density (Figure 5)
 GRAPH-BRE-003: Fine aggregate proportion (Figure 6)

───────────────────────────────────────────────
 EQUATIONS USED
───────────────────────────────────────────────

 EQ-BRE-001: f_m = f_ck + M
 EQ-BRE-002: M = k × s
 EQ-BRE-003: C = W / (w/c)
 EQ-BRE-004: A_total = D_wet − C − W
 EQ-BRE-005: FA = A_total × P_fine
 EQ-BRE-006: CA = A_total − FA

═══════════════════════════════════════════════
 SOFTWARE VERSION: X.X.X
 ENGINEERING DATA VERSION: BRE-1997-DATA-1.0
═══════════════════════════════════════════════
```

---

*Source: SRC-BRE-001*
*Created: 2026-09-18*
