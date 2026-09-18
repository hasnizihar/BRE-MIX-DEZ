# BRE Mix Design Project — Agent Rules

> This file is the **permanent project constitution**.
> Every AI coding agent (Codex, Claude Code, Antigravity, or other) must read and obey this file before performing any work on this project.

---

## 1. Project Purpose

This project implements a **BRE/DoE concrete mix-design desktop application** based on:

```
Primary Method:   BRE / DoE Method
Primary Reference: BRE BR 331, Design of Normal Concrete Mixes, Second Edition, 1997
ISBN:              1-86081-172-8
Publisher:         Building Research Establishment (BRE)
```

The application is an **engineering calculation aid**, not a standards-compliance tool.

---

## 2. Engineering Authority

### Source Hierarchy

| Priority | Tier | Source Type | Usage |
|----------|------|------------|-------|
| 1 | Tier 1 — Primary | BRE BR 331, BSI standards (BS 8500, BS EN 206), official government publications | Defines engineering calculations |
| 2 | Tier 2 — Technical | Concrete Society, engineering institutions, university publications | Clarifies and interprets |
| 3 | Tier 3 — Supporting | Textbooks, academic papers, worked examples | Validates and cross-checks |
| 4 | Tier 4 — Discovery | Blogs, forums, YouTube, AI-generated content | Locates information only |

**Rule: Tier 4 material must NEVER define an engineering calculation, table value, constant, or limit.**

### Engineering Data Authority

The verified engineering data in `/02_BRE_METHOD/` and `/04_ENGINEERING_DATA/` is the authoritative source for all software implementation. The AI agent does not become the engineering authority.

---

## 3. Critical Engineering Rules

### NEVER:

1. Invent an engineering equation, table value, constant, interpolation rule, or engineering limit
2. Modify verified engineering data without full traceability and explicit approval
3. Silently change source editions
4. Silently select values that should be user inputs
5. Silently modify source values
6. Combine incompatible editions or methods (BRE/ACI/IS/Eurocode)
7. Treat internet summaries as authoritative sources
8. Assume old BRE procedures automatically satisfy current UK requirements
9. Convert UNVERIFIED status to VERIFIED without evidence
10. Resolve engineering conflicts by guessing

### IF INFORMATION IS MISSING:

```
STOP
  ↓
Document the uncertainty
  ↓
Identify the missing source/information
  ↓
Mark the item as UNVERIFIED
  ↓
Report to the user
```

---

## 4. Source Traceability

Every engineering calculation must reference:

- Source document (e.g., SRC-BRE-001)
- Edition/year
- Section/page where available
- Equation/Table/Graph ID (e.g., EQ-BRE-001, TBL-BRE-002, GRAPH-BRE-001)

Every engineering change must update:

- Source register (`01_SOURCES/SOURCE_REGISTER.md`)
- Traceability matrix (`07_SOFTWARE_SPEC/TRACEABILITY_MATRIX.md`)
- Validation tests
- Changelog (`00_PROJECT/CHANGELOG.md`)

---

## 5. Coding Rules (for future development)

### Architecture

```
Desktop UI
     ↓
Application Services
     ↓
BRE Calculation Engine
     ↓
Engineering Data
     ↓
Validation
```

Engineering calculations must be **independent of UI code**.

The calculation engine must be testable without launching the UI.

### Naming

- Use engineering variable names, not abstract names
- `characteristic_strength` not `x1`
- `water_cement_ratio` not `factor_a`
- `free_water_content` not `water2`

### Units

All internal engineering calculations must use explicit SI units:

| Quantity | Unit |
|----------|------|
| Strength | N/mm² |
| Mass per volume | kg/m³ |
| Mass | kg |
| Volume | m³ |
| Density | kg/m³ |
| Ratio | dimensionless |

### Calculations in Code

- Never place engineering calculations directly in UI components
- Every engineering function must have a source reference comment
- Every engineering function must handle its own input validation
- Intermediate values must be available for inspection (calculation trace)

---

## 6. Testing Rules

### Every engineering function requires:

1. Unit test — verifies the equation produces correct output for known inputs
2. Boundary test — verifies behavior at limits of valid input ranges
3. Validation case — verifies against a BRE worked example

### Golden Tests

BRE worked examples in `06_VALIDATION/GOLDEN_CASES/` are **authoritative validation cases**.

**Rules:**
- Never modify expected values simply to make a test pass
- Never remove tests to make the build pass
- If a test fails, the calculation is wrong — not the test
- If the source is wrong, create a CONFLICT record

### Test Coverage

The calculation engine must pass all golden tests before UI development begins.

---

## 7. Validation Rules

### Verification Statuses

| Status | Meaning |
|--------|---------|
| `VERIFIED` | Source directly confirms the value |
| `CROSS-VERIFIED` | Confirmed by multiple reliable sources |
| `SECONDARY` | Found only in secondary sources |
| `INFERRED` | Derived from source but not explicitly stated |
| `UNVERIFIED` | Cannot currently be confirmed |
| `ENGINEERING REVIEW REQUIRED` | Requires human engineering judgment |

### Conflict Resolution

If two sources disagree:
1. Do NOT choose one silently
2. Create a CONFLICT-XXX record
3. Document both sources and the difference
4. Flag for engineering review
5. Do not implement until resolved

---

## 8. Change Control

### Before modifying any file in these directories:

- `02_BRE_METHOD/`
- `04_ENGINEERING_DATA/`
- `05_CALCULATIONS/`
- `06_VALIDATION/`

The agent must:

1. Document the reason for the change
2. Identify the source authority for the change
3. Update all affected traceability records
4. Run all existing tests
5. Update the changelog

### Forbidden without explicit approval:

- Removing existing functionality
- Modifying engineering data
- Changing validation expected values
- Changing source editions
- Removing tests

---

## 9. Documentation Rules

- Every engineering assumption must be explicitly documented
- Every limitation must be documented
- Every exclusion must be documented
- Comments and docstrings related to engineering must never be removed
- README files in each directory must be maintained

---

## 10. Uncertainty Handling

Unknown information must be **flagged, not guessed**.

```
Known and verified     → implement with confidence
Known but unverified   → implement with UNVERIFIED flag
Unknown                → STOP and report
Conflicting            → create CONFLICT record
```

---

## 11. Method Boundaries

### This application implements:

```
BRE MIX DESIGN METHOD (BR 331, 1997)
```

### This application does NOT claim to implement:

```
BS 8500 compliance verification
BS EN 206 conformity assessment
Structural design
Durability design (beyond BRE method scope)
```

### The distinction must be maintained:

```
BRE MIX DESIGN CALCULATION
        ≠
CURRENT UK CONCRETE SPECIFICATION COMPLIANCE
```

Where current standards provide relevant inputs or checks for the mix design, those relationships are documented in `03_STANDARDS/STANDARD_RELATIONSHIPS.md`.

---

## 12. File Structure

```
BRE-MIX-DESIGN/
├── AGENTS.md                    ← this file
├── README.md
├── 00_PROJECT/                  ← project management
├── 01_SOURCES/                  ← authoritative sources
├── 02_BRE_METHOD/               ← engineering method documentation
├── 03_STANDARDS/                ← current standards context
├── 04_ENGINEERING_DATA/         ← tables, graphs, equations, data
├── 05_CALCULATIONS/             ← calculation specifications
├── 06_VALIDATION/               ← test cases and validation
├── 07_SOFTWARE_SPEC/            ← software requirements
├── 08_AI_AGENT/                 ← agent governance
└── 09_ARCHIVE/                  ← archived/superseded material
```

---

*Last updated: 2026-09-18*
*Version: 1.0.0*
