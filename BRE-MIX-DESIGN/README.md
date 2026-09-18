# BRE Mix Design — Engineering Knowledge Base

## Project Overview

This repository contains the **complete engineering knowledge base** for a BRE/DoE concrete mix-design desktop application.

### Purpose

Provide a verified, traceable, structured engineering blueprint that enables a software developer to implement the BRE concrete mix-design calculation engine **without having to guess any engineering rule**.

### Primary Method

| Attribute | Value |
|-----------|-------|
| Method | BRE / DoE Concrete Mix Design |
| Reference | BRE BR 331, *Design of Normal Concrete Mixes* |
| Edition | Second Edition, 1997 |
| ISBN | 1-86081-172-8 |
| Publisher | Building Research Establishment |
| Application | Normal-weight concrete mix design |

### Current Phase

```
RESEARCH + ENGINEERING DOCUMENTATION + DATA STRUCTURING + VALIDATION PREPARATION
```

**No application code is contained in this repository.**

---

## Repository Structure

| Directory | Purpose |
|-----------|---------|
| `00_PROJECT/` | Project scope, roadmap, requirements, terminology, decisions, changelog |
| `01_SOURCES/` | Source register, primary/secondary sources, source review notes |
| `02_BRE_METHOD/` | Complete BRE method documentation (13 steps + traceability) |
| `03_STANDARDS/` | Current British standards context and relationships |
| `04_ENGINEERING_DATA/` | Data dictionary, constants, tables, graphs, equations, lookup data |
| `05_CALCULATIONS/` | Calculation pipeline, equations, interpolation, rounding, units, errors |
| `06_VALIDATION/` | Validation plan, golden test cases, unit cases, boundary cases |
| `07_SOFTWARE_SPEC/` | Future application architecture, UI, database, engine, reports |
| `08_AI_AGENT/` | Agent workflow, rules, guardrails, templates, checklists |
| `09_ARCHIVE/` | Archived and superseded material |

---

## Key Documents

- **[AGENTS.md](AGENTS.md)** — Project rules for AI coding agents
- **[00_PROJECT/PROJECT_SCOPE.md](00_PROJECT/PROJECT_SCOPE.md)** — Project scope definition
- **[01_SOURCES/SOURCE_REGISTER.md](01_SOURCES/SOURCE_REGISTER.md)** — Authoritative source catalog
- **[02_BRE_METHOD/00_OVERVIEW.md](02_BRE_METHOD/00_OVERVIEW.md)** — BRE method overview
- **[04_ENGINEERING_DATA/DATA_DICTIONARY.md](04_ENGINEERING_DATA/DATA_DICTIONARY.md)** — Complete data dictionary
- **[05_CALCULATIONS/CALCULATION_PIPELINE.md](05_CALCULATIONS/CALCULATION_PIPELINE.md)** — Deterministic calculation workflow
- **[06_VALIDATION/VALIDATION_PLAN.md](06_VALIDATION/VALIDATION_PLAN.md)** — Validation strategy

---

## Engineering Authority

All engineering data in this repository follows the authority hierarchy defined in [AGENTS.md](AGENTS.md).

Every equation, table, constant, and engineering rule is traceable to a specific source document with edition and location.

**No engineering data has been invented or assumed without explicit documentation.**

---

*Created: 2026-09-18*
