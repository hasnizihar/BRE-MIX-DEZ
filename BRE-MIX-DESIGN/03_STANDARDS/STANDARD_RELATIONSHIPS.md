# Standard Relationships

> **Purpose:** Document the relationship between BRE BR 331 and current British/European standards.

---

## Critical Distinction

```
BRE MIX DESIGN CALCULATION (proportioning method)
        ≠
CURRENT UK CONCRETE SPECIFICATION (BS 8500 / BS EN 206)
```

These are **related but distinct** activities. They must NOT be conflated.

---

## Standards Timeline

| Year | Event |
|------|-------|
| 1975 | Original DoE mix design method published |
| 1988 | DoE method revised |
| 1997 | BRE BR 331, Second Edition published |
| 2003 | BS 5328 (UK concrete specification) replaced by BS 8500 / BS EN 206 |
| 2006 | BS 8500:2006 published |
| 2015 | BS 8500:2015+A2:2019 |
| 2023 | BS 8500-1:2023 and BS 8500-2:2023 published (current editions) |

---

## What Each Standard Provides

### BRE BR 331 (1997) — SRC-BRE-001

| Aspect | What it provides |
|--------|-----------------|
| **Purpose** | Concrete mix proportioning method |
| **Scope** | Determine quantities of cement, water, and aggregates |
| **Inputs from user** | Strength, workability, materials |
| **Data** | Tables and figures for mix design calculations |
| **Output** | Mix proportions (first approximation) |
| **Durability** | Limited — references historical standards |
| **Exposure classes** | NOT provided (predates current framework) |
| **Compliance** | NOT a compliance standard |

### BS 8500-1:2023 — SRC-BSI-001

| Aspect | What it provides |
|--------|-----------------|
| **Purpose** | Method of specifying concrete / guidance for specifiers |
| **Scope** | How to specify concrete for different applications |
| **Key content** | Exposure classes, strength classes, durability requirements |
| **Key tables** | Minimum cement content and max w/c ratio for exposure classes |
| **Designated mixes** | Standard mix specifications for common applications |
| **Designed mixes** | Framework for specifying concrete by performance |
| **Relationship to BRE** | Provides INPUTS to the BRE method (max w/c, min cement) |

### BS 8500-2:2023 — SRC-BSI-002

| Aspect | What it provides |
|--------|-----------------|
| **Purpose** | Specification for constituent materials and concrete |
| **Scope** | Material requirements, concrete production, conformity |
| **Key content** | Cement types, aggregate requirements, admixtures |
| **Relationship to BRE** | Defines material specifications that feed into BRE inputs |

### BS EN 206 — SRC-BSEN-001

| Aspect | What it provides |
|--------|-----------------|
| **Purpose** | European framework standard for concrete |
| **Scope** | Specification, performance, production, conformity |
| **Key content** | Exposure classes (XC, XD, XS, XF, XA), conformity criteria |
| **Relationship to BS 8500** | BS 8500 is the UK complementary standard to BS EN 206 |
| **Relationship to BRE** | Provides the European context for specification requirements |

---

## Relationship Matrix

| Requirement | BRE BR 331 | BS 8500 | BS EN 206 | Software Relevance |
|------------|-----------|---------|-----------|-------------------|
| Mix proportioning | ✓ PRIMARY | ✗ | ✗ | Core calculation engine |
| Target mean strength | ✓ | Related | Related | Stage 1 |
| w/c ratio (strength) | ✓ | ✗ | ✗ | Stage 1 |
| w/c ratio (durability) | ✗ | ✓ | ✓ | Input constraint |
| Free water content | ✓ | ✗ | ✗ | Stage 2 |
| Min cement content | ✗ | ✓ | ✓ | Input constraint |
| Max cement content | ✗ | Sometimes | ✗ | Input constraint |
| Exposure classes | ✗ | ✓ | ✓ | Future: durability input |
| Aggregate specification | ✗ | ✓ | Related | Material input |
| Cement classification | Related | ✓ | ✓ | Input |
| Conformity criteria | ✗ | ✗ | ✓ | Out of scope |
| Designated mixes | ✗ | ✓ | ✗ | Out of scope |

---

## How Standards Feed Into BRE Mix Design

```
BS 8500 / BS EN 206
        │
        ├── Maximum w/c ratio     ──→  BRE Stage 1 (constraint)
        ├── Minimum cement content ──→  BRE Stage 3 (constraint)
        ├── Strength class         ──→  BRE Stage 1 (f_ck input)
        └── Cement type allowed    ──→  BRE Stage 1 (cement class)
        
BRE BR 331
        │
        ├── f_m calculation
        ├── w/c ratio determination
        ├── Water content
        ├── Cement content
        ├── Aggregate proportioning
        └── Final mix design
```

---

## Items Flagged for Future Implementation

| Item | Standard | Purpose | Priority |
|------|----------|---------|----------|
| Exposure class lookup | BS 8500-1 | Auto-determine max w/c and min cement | Medium |
| Designated mix selection | BS 8500-1 | Alternative to designed mix | Low |
| Cement combination types | BS 8500-2 | Support CEM II, CEM III, etc. | Medium |
| Conformity assessment | BS EN 206 | Production quality control | Low |

---

## Conflicts Between Historical and Current Standards

### CONFLICT-001: Cement Classification

| Field | Value |
|-------|-------|
| **Topic** | Cement strength classification |
| **Source A** | BRE BR 331 (1997) — refers to cement classes of its era |
| **Source B** | BS EN 197-1:2011 — current cement classification |
| **Difference** | The mapping between old OPC/RHPC designations and current 42.5/52.5 classes |
| **Possible Reason** | Standards evolution over time |
| **Recommended Treatment** | Use current BS EN 197-1 classes (42.5, 52.5) as documented in Table 2 of BR 331 second edition |
| **Status** | RESOLVED — BR 331 second edition already uses 42.5/52.5 classification |

---

*Source: SRC-BRE-001, SRC-BSI-001, SRC-BSI-002, SRC-BSEN-001, SRC-CS-001*
*Created: 2026-09-18*
