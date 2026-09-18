Yes. For this project, I would **not start by asking an AI agent to code the desktop application**. The first project is to build a **verified engineering knowledge base** containing the BRE/DoE mix-design method, equations, tables, charts, assumptions, standards, inputs, outputs, worked examples, and validation cases.

Then the coding agent uses that knowledge base as the specification.

One important terminology point first: the method you're referring to is generally the **BRE/DoE method, documented in *Design of Normal Concrete Mixes* (BRE BR 331)**. The second edition was published in 1997, following the earlier 1975 method and 1988 revision. ([BRE Group][1])

Also, don't mix the **BRE mix-design procedure** with the much newer **BS 8500 / BS EN 206 specification framework**. They are related but serve different purposes. BS 8500-1:2023 and BS 8500-2:2023 are current UK complementary standards to BS EN 206, while the historical BRE BR 331 is the source for the normal concrete mix proportioning procedure you're trying to implement.

# 1. The overall project

I recommend structuring the project as **five layers**:

```text
                    BRE MIX DESIGN DESKTOP APP
                              │
              ┌───────────────┴───────────────┐
              │                               │
       ENGINEERING KNOWLEDGE             APPLICATION
              │                               │
       ┌──────┴──────┐                ┌───────┴────────┐
       │             │                │                │
   BRE Method    Standards       Calculation Engine    UI
       │             │                │                │
   Equations      BS/EN/BRE        Validation       Reports
   Tables         References       Tests            Export
   Charts         Limitations
   Examples
```

The critical principle is:

> **AI writes the software. AI does not become the authority for the engineering method.**

The authoritative engineering data should be extracted, checked, structured, and versioned first.

---

# 2. Phase 0: Define exactly what version you are implementing

Create this first:

```text
BRE-Mix-Design/
│
├── 00_PROJECT/
│   ├── PROJECT_SCOPE.md
│   ├── PROJECT_ROADMAP.md
│   ├── REQUIREMENTS.md
│   ├── TERMINOLOGY.md
│   └── DECISIONS.md
│
├── 01_SOURCES/
├── 02_BRE_METHOD/
├── 03_STANDARDS/
├── 04_ENGINEERING_DATA/
├── 05_CALCULATIONS/
├── 06_VALIDATION/
├── 07_SOFTWARE_SPEC/
├── 08_AI_AGENT/
└── 09_ARCHIVE/
```

Your first scope document should explicitly say something like:

```text
Project:
BRE Concrete Mix Design Desktop Application

Primary Method:
BRE / DoE Method

Primary Reference:
BRE BR 331
Design of Normal Concrete Mixes
Second Edition, 1997

Initial Scope:
Normal-weight concrete mix design.

Initial Exclusions:
- Lightweight concrete
- Heavyweight concrete
- Self-compacting concrete
- High-performance concrete
- Fibre-reinforced concrete
- Special concretes
- Pumped concrete unless explicitly supported
- Air-entrained concrete unless explicitly implemented
- Automatic material optimization

Future Scope:
Additional mix-design methods and standards.
```

The original BRE publication itself states that the method is intended for most normal concrete applications and describes limitations and modifications for special cases. ([TRID][2])

---

# 3. Phase 1: Build the source library

This is the **most important stage**.

Your AI agent should collect sources into:

```text
01_SOURCES/
│
├── PRIMARY/
│   ├── BRE_BR331/
│   ├── BS_8500/
│   ├── BS_EN_206/
│   └── OTHER_PRIMARY/
│
├── SECONDARY/
│   ├── University_Notes/
│   ├── Technical_Guides/
│   ├── Worked_Examples/
│   └── Research_Papers/
│
└── SOURCE_REGISTER.md
```

## Source hierarchy

Give every source a priority.

### Tier 1: Primary

Use these for actual engineering implementation.

* BRE BR 331
* Relevant BSI standards
* BS EN standards
* BRE publications
* Official government/engineering guidance

### Tier 2: Technical interpretation

* University lecture notes
* Engineering institution documents
* Government technical documents
* Established engineering organizations

### Tier 3: Supporting material

* Research papers
* textbooks
* worked examples
* engineering websites

### Tier 4: Discovery only

* random blogs
* forums
* YouTube
* Scribd
* AI-generated explanations

**Never allow Tier 4 material to define a calculation.**

---

# 4. Important source discovery

I already checked the web for the core material.

The official BRE-hosted copy of **Design of Normal Concrete Mixes, Second Edition** is available and identifies the publication as BR 331. ([BRE Group][1])

The publication metadata confirms:

* first published: 1975
* revised: 1988
* second edition: 1997
* BRE / Transport Research Laboratory / British Cement Association involvement
* ISBN: 1-86081-172-8 ([TRID][2])

There is also a current UK standards context you need to document separately. BSI lists **BS 8500-1:2023** and **BS 8500-2:2023** as current editions, with BS 8500 complementing BS EN 206.

The Concrete Society also notes that BS 8500 and BS EN 206 replaced BS 5328 in 2003, so your documentation needs to distinguish **historical BRE/DoE mix design** from the **current UK concrete specification framework**. ([Concrete Society][3])

---

# 5. Source Register

Create:

```text
01_SOURCES/SOURCE_REGISTER.md
```

Use this structure:

```markdown
# Source Register

| ID | Source | Edition | Type | Authority | Used For | Status |
|----|--------|---------|------|-----------|----------|--------|
| SRC-001 | BRE BR 331 | 1997 | Primary | BRE | Mix design procedure | Verified |
| SRC-002 | BS 8500-1 | 2023 | Primary | BSI | UK specification/durability | Verified |
| SRC-003 | BS 8500-2 | 2023 | Primary | BSI | Materials/concrete | Verified |
| SRC-004 | BS EN 206 | Current applicable edition | Primary | BSI/CEN | Concrete specification | Pending |
| SRC-005 | University worked example | Various | Secondary | University | Validation | Pending |

## Rules

1. Primary sources control engineering calculations.
2. Secondary sources may clarify but cannot override primary sources.
3. Every implemented table must have a source.
4. Every implemented equation must have a source.
5. Every engineering assumption must be documented.
6. Every software implementation must be traceable to an engineering source.
```

This will become extremely valuable later.

---

# 6. Phase 2: Extract the BRE method

Now tell the AI agent:

> Don't code anything. Read the primary BRE document and convert the entire methodology into structured engineering documentation.

Create:

```text
02_BRE_METHOD/
│
├── 00_OVERVIEW.md
├── 01_SCOPE.md
├── 02_INPUT_REQUIREMENTS.md
├── 03_TARGET_MEAN_STRENGTH.md
├── 04_WATER_CEMENT_RATIO.md
├── 05_WATER_CONTENT.md
├── 06_CEMENT_CONTENT.md
├── 07_TOTAL_AGGREGATE.md
├── 08_FINE_AGGREGATE.md
├── 09_COARSE_AGGREGATE.md
├── 10_ADJUSTMENTS.md
├── 11_FIELD_CORRECTIONS.md
├── 12_FINAL_MIX.md
├── 13_SPECIAL_CASES.md
├── 14_WORKED_EXAMPLES.md
└── 99_METHOD_TRACEABILITY.md
```

---

# 7. Map the complete calculation workflow

Your AI agent should extract the BRE workflow into a deterministic pipeline.

A high-level representation is:

```text
USER REQUIREMENTS
       ↓
Characteristic strength
       ↓
Percentage defectives
       ↓
Standard deviation
       ↓
Target mean strength
       ↓
Select water/cement ratio
       ↓
Select free-water content
       ↓
Calculate cement content
       ↓
Estimate concrete density
       ↓
Calculate total aggregate
       ↓
Determine fine aggregate proportion
       ↓
Calculate fine aggregate
       ↓
Calculate coarse aggregate
       ↓
Check durability requirements
       ↓
Apply moisture / absorption corrections
       ↓
Determine batch quantities
       ↓
Generate final mix
       ↓
Validation
       ↓
Report
```

This is supported by published summaries of the BRE procedure, which identify target mean strength, water/cement ratio, water content, cement content, total aggregate, fine/coarse aggregate proportions and final adjustments as core stages. ([Scribd][4])

---

# 8. Do NOT let the AI agent invent equations

This needs to be a hard rule.

For every equation create a record:

```markdown
# Equation: Target Mean Strength

ID:
EQ-BRE-001

Name:
Target Mean Strength

Equation:
[verified equation]

Variables:
- f_m = ...
- f_ck = ...
- M = ...

Source:
BRE BR 331, Second Edition, relevant section/page

Units:
N/mm²

Valid Range:
[documented]

Notes:
[engineering interpretation]

Software Function:
calculate_target_mean_strength()

Validation:
VAL-001
VAL-002
```

Do the same for **every calculation**.

---

# 9. Build an Engineering Data Dictionary

Create:

```text
04_ENGINEERING_DATA/DATA_DICTIONARY.md
```

Example:

| Variable | Meaning                             |  Unit | Input/Output        | Source |
| -------- | ----------------------------------- | ----: | ------------------- | ------ |
| `fck`    | Characteristic compressive strength | N/mm² | Input               | BRE    |
| `fm`     | Target mean strength                | N/mm² | Calculated          | BRE    |
| `s`      | Standard deviation                  | N/mm² | Input/selected      | BRE    |
| `k`      | Statistical factor                  |     - | Selected            | BRE    |
| `w_c`    | Free water/cement ratio             |     - | Calculated/selected | BRE    |
| `W`      | Free water content                  | kg/m³ | Calculated          | BRE    |
| `C`      | Cement content                      | kg/m³ | Calculated          | BRE    |
| `FA`     | Fine aggregate                      | kg/m³ | Calculated          | BRE    |
| `CA`     | Coarse aggregate                    | kg/m³ | Calculated          | BRE    |

Don't allow the programming agent to use mysterious variables like:

```python
x1
x2
factor_a
water2
```

Use engineering names.

---

# 10. Tables need their own database

This is extremely important.

Don't simply put tables inside Markdown and expect the AI to correctly reproduce them in code.

Create:

```text
04_ENGINEERING_DATA/TABLES/
│
├── table_01_strength.md
├── table_02_wc_ratio.md
├── table_03_water_content.md
├── table_04_fine_aggregate.md
├── table_05_density.md
└── README.md
```

Each table:

```markdown
# BRE Table XXX

## Metadata

ID:
TBL-BRE-XXX

Source:
BRE BR 331

Edition:
1997

Page:
XX

Purpose:
[description]

## Data

| Parameter | Value |
|---|---:|
| ... | ... |

## Interpolation

Allowed:
YES/NO

Method:
[exact interpolation rule]

## Software Representation

Data structure:
...

## Validation

Test:
...
```

---

# 11. Graphs are even more important

The BRE method contains relationships represented by graphs/charts.

**Do not ask the coding agent to visually estimate points from a graph.**

Instead:

```text
Graph
  ↓
Digitize/reference original values
  ↓
Create structured dataset
  ↓
Document interpolation method
  ↓
Validate against original graph
  ↓
Only then implement
```

For example:

```text
04_ENGINEERING_DATA/GRAPHS/

GRAPH-BRE-001.md
GRAPH-BRE-002.md
GRAPH-BRE-003.md

data/
    GRAPH-BRE-001.csv
    GRAPH-BRE-002.csv
```

---

# 12. Worked examples become your golden tests

This is where the project becomes powerful.

Take the worked examples from the BRE publication.

For each:

```text
06_VALIDATION/
│
├── CASE-001/
│   ├── input.json
│   ├── expected.json
│   ├── calculation.md
│   └── verification.md
│
├── CASE-002/
│
├── CASE-003/
│
└── CASE-004/
```

The structure should be:

```json
{
  "case_id": "BRE-EXAMPLE-001",

  "inputs": {},

  "expected": {
    "water": null,
    "cement": null,
    "fine_aggregate": null,
    "coarse_aggregate": null
  },

  "tolerance": {},

  "source": {
    "document": "BRE BR 331",
    "edition": "1997",
    "page": "..."
  }
}
```

These become **golden tests**.

If the AI writes code and the output doesn't match the verified example, the agent must stop.

---

# 13. Build a calculation specification BEFORE coding

Create:

```text
05_CALCULATIONS/
│
├── CALCULATION_PIPELINE.md
├── EQUATIONS.md
├── CONSTANTS.md
├── TABLE_LOOKUPS.md
├── INTERPOLATION.md
├── ROUNDING_RULES.md
├── UNIT_HANDLING.md
└── ERROR_HANDLING.md
```

The AI coding agent should eventually be able to read these and implement the calculation engine without guessing.

---

# 14. Engineering validation architecture

I strongly recommend three levels.

### Level 1: Equation tests

```text
Input → Equation → Expected output
```

### Level 2: Component tests

```text
Inputs
 ↓
water/cement ratio
 ↓
water
 ↓
cement
 ↓
aggregates
```

### Level 3: Complete BRE examples

```text
Complete input
 ↓
Entire calculation engine
 ↓
Expected final mix
```

Only when all three pass should the UI be developed seriously.

---

# 15. Software architecture

Once the engineering knowledge base is complete, **then** start the desktop application.

I'd structure it like:

```text
BRE-Mix-Designer/
│
├── app/
│   ├── ui/
│   ├── services/
│   ├── calculations/
│   ├── models/
│   ├── validation/
│   ├── reports/
│   └── database/
│
├── engineering/
│   ├── equations/
│   ├── tables/
│   ├── charts/
│   ├── constants/
│   └── rules/
│
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── validation/
│   └── golden/
│
├── docs/
│
└── data/
```

---

# 16. Desktop technology

For your particular project, I would seriously consider:

### Option A

**Python + PySide6**

```text
PySide6
   +
Python calculation engine
   +
SQLite
   +
Pydantic
   +
Matplotlib
   +
ReportLab
```

This gives you:

* proper desktop UI
* engineering calculations
* charts
* PDF reports
* local database
* easy testing
* relatively easy AI-agent development

### Option B

**C# + WPF/WinUI**

Better if you want a very Windows-native commercial engineering application.

For your AI-agent workflow, however, Python is likely easier to iterate rapidly.

---

# 17. Separate UI from engineering calculations

This rule should be absolute:

```text
UI
 ↓
Application Service
 ↓
BRE Calculation Engine
 ↓
Engineering Data
```

Never:

```text
Button clicked
 ↓
300 lines of engineering equations
 ↓
database
```

Instead:

```python
result = bre_engine.design_mix(input_data)
```

The UI shouldn't know how BRE calculations work.

---

# 18. The application workflow

Eventually the user should see something like:

```text
NEW MIX DESIGN
       ↓
Project Information
       ↓
Concrete Requirements
       ↓
Material Properties
       ↓
Strength Parameters
       ↓
Workability
       ↓
Aggregate Information
       ↓
Cement Information
       ↓
Durability / Specification
       ↓
BRE Calculation
       ↓
Engineering Checks
       ↓
Trial Mix
       ↓
Corrections
       ↓
Final Mix
       ↓
Report
```

---

# 19. Input validation

The software needs engineering validation, not just ordinary form validation.

For example:

```text
❌ Missing characteristic strength
❌ Invalid aggregate size
❌ Impossible water/cement ratio
❌ Missing specific gravity
❌ Incompatible material selection
❌ Missing fine aggregate grading information
❌ Values outside documented BRE range
```

The software should distinguish:

### ERROR

Cannot calculate.

### WARNING

Calculation possible, but engineering attention required.

### INFORMATION

Useful engineering note.

Example:

```text
ERROR
Specific gravity of coarse aggregate is required.

WARNING
Input lies outside the normal range represented in the
selected BRE data table.

INFORMATION
The selected value was obtained by interpolation.
```

---

# 20. Don't hide the calculations

This is an engineering application.

The user should be able to click:

> **Show Calculation**

and see:

```text
Target mean strength

fₘ = fck + margin

fck = XX N/mm²
margin = XX N/mm²

Therefore:

fₘ = XX N/mm²
```

Then:

```text
Water/Cement Ratio

Selected relationship:
BRE Table / Figure XXX

Required value:
X.XX
```

Then continue through the calculation.

This gives the application **engineering transparency**.

---

# 21. Add a calculation trace

Every result should have a trace:

```text
CALCULATION TRACE

Design ID: BRE-2026-0001

Method:
BRE BR 331

Edition:
1997

Inputs:
...

Tables used:
TBL-001
TBL-002
TBL-003

Equations:
EQ-001
EQ-002
EQ-003

Adjustments:
...

Final result:
...

Software version:
0.1.0
```

This is much more valuable than simply showing:

```text
Cement = 350 kg/m³
```

---

# 22. AI agent development workflow

Now we get to the fun part.

Don't give Claude Code / Codex / Antigravity one giant prompt:

> "Build my BRE mix design software."

That will create a beautiful train wreck.

Instead, use an **agent-controlled development pipeline**.

---

# 23. Create an AGENTS.md

At the root:

```text
AGENTS.md
```

Put rules such as:

```markdown
# BRE Mix Design Project Rules

## Engineering Authority

The primary engineering authority is the verified
BRE BR 331 documentation contained in /02_BRE_METHOD
and /04_ENGINEERING_DATA.

## Critical Rule

Never invent an engineering equation, table value,
constant, interpolation rule, or engineering limit.

If required information is missing:
STOP and report the missing information.

## Source Traceability

Every engineering calculation must reference:
- source
- edition
- section/page where available
- equation/table ID

## Calculation Engine

Engineering calculations must not be implemented
inside UI components.

## Testing

Every engineering function requires:
1. unit test
2. boundary test
3. validation case

## Golden Tests

BRE worked examples are authoritative validation cases.

Never modify expected values simply to make a test pass.

## Units

All internal engineering calculations must use
explicit SI units.

## Changes

Do not modify engineering data without updating:
- source register
- traceability
- validation tests
- change log
```

This file becomes the agent's constitution.

---

# 24. Add an AI workflow document

Create:

```text
08_AI_AGENT/
│
├── AGENT_WORKFLOW.md
├── AGENT_RULES.md
├── TASK_TEMPLATE.md
├── REVIEW_CHECKLIST.md
├── ENGINEERING_GUARDRAILS.md
└── CHANGE_PROTOCOL.md
```

---

# 25. Every AI task should follow this cycle

```text
READ
 ↓
UNDERSTAND
 ↓
PLAN
 ↓
IMPLEMENT
 ↓
TEST
 ↓
COMPARE
 ↓
REVIEW
 ↓
DOCUMENT
 ↓
COMMIT
```

Not:

```text
PROMPT → CODE → DONE
```

---

# 26. Give the agent small missions

Example:

### Mission 001

```text
Read:
02_BRE_METHOD/03_TARGET_MEAN_STRENGTH.md

Task:
Implement target mean strength calculation.

Requirements:
- no UI changes
- no database changes
- create unit tests
- use typed inputs
- document source
- run existing tests

Do not implement any other calculation.
```

Then Mission 002:

```text
Implement BRE water/cement ratio selection.
```

Then:

```text
Implement free water calculation.
```

Then:

```text
Implement cement calculation.
```

And so on.

---

# 27. Agent task structure

Use:

```markdown
# TASK-001

## Objective

Implement target mean strength calculation.

## Read First

- AGENTS.md
- 02_BRE_METHOD/03_TARGET_MEAN_STRENGTH.md
- 05_CALCULATIONS/EQUATIONS.md

## Allowed Changes

- calculations/
- tests/

## Forbidden Changes

- UI
- database
- engineering source data

## Requirements

1. Implement equation.
2. Use SI units.
3. Validate inputs.
4. Add unit tests.
5. Add boundary tests.
6. Add source reference.
7. Run full test suite.

## Acceptance Criteria

- [ ] Equation matches engineering specification.
- [ ] Tests pass.
- [ ] No unrelated files changed.
- [ ] Source traceability exists.
```

This works extremely well with coding agents.

---

# 28. Use multiple agents strategically

You don't need one AI agent doing everything.

Use roles.

### Agent 1: Research Agent

```text
Find and organize engineering sources.
```

### Agent 2: Engineering Analyst

```text
Extract equations/tables/procedures.
```

### Agent 3: Verification Agent

```text
Check extracted information against sources.
```

### Agent 4: Software Architect

```text
Design application architecture.
```

### Agent 5: Coding Agent

```text
Implement only verified specifications.
```

### Agent 6: Test Agent

```text
Try to break the calculation engine.
```

### Agent 7: Documentation Agent

```text
Keep engineering/software documentation synchronized.
```

---

# 29. The most important agent: the auditor

Have a separate agent review the coding agent's work.

For example:

```text
CODING AGENT
     ↓
implementation
     ↓
TEST AGENT
     ↓
ENGINEERING AUDITOR
     ↓
PASS / FAIL
```

The auditor should ask:

```text
Does equation match source?
Does table match source?
Are units correct?
Is interpolation correct?
Are rounding rules correct?
Are boundary conditions handled?
Are worked examples reproduced?
Did the developer accidentally change engineering data?
```

---

# 30. Build a traceability matrix

Create:

```text
07_SOFTWARE_SPEC/TRACEABILITY_MATRIX.md
```

Example:

| Requirement          | Engineering Source | Software Module | Test     |
| -------------------- | ------------------ | --------------- | -------- |
| Target mean strength | BRE BR331          | `strength.py`   | TEST-001 |
| W/C ratio            | BRE Table/Figure   | `wc_ratio.py`   | TEST-002 |
| Water content        | BRE table          | `water.py`      | TEST-003 |
| Cement content       | BRE equation       | `cement.py`     | TEST-004 |
| Fine aggregate       | BRE table          | `aggregate.py`  | TEST-005 |
| Coarse aggregate     | BRE method         | `aggregate.py`  | TEST-006 |
| Final mix            | BRE procedure      | `mix_design.py` | TEST-007 |

This means you can eventually answer:

> "Why did the software produce this number?"

That's crucial.

---

# 31. Create a knowledge graph of the method

This sounds fancy, but it's actually simple.

```text
Characteristic Strength
        │
        ├── Standard Deviation
        │
        └── k factor
              ↓
       Target Mean Strength
              ↓
         W/C Ratio
              ↓
        Free Water
              ↓
           Cement
              ↓
      Total Aggregate
          /       \
         /         \
      Fine        Coarse
```

Each node should link to:

```text
equation
source
table
inputs
outputs
validation
software function
```

This will make your AI agents dramatically more reliable.

---

# 32. Build a machine-readable engineering specification

Markdown is great for humans.

But the application should eventually have structured data too.

For example:

```text
engineering/
│
├── tables/
│   ├── bre_water_content.json
│   ├── bre_wc_ratio.json
│   └── bre_aggregate_ratio.json
│
├── equations/
│   └── bre_equations.json
│
└── metadata/
    └── sources.json
```

So you have:

```text
Human documentation
        +
Machine-readable engineering data
```

---

# 33. Version engineering data separately from software

For example:

```text
Engineering Dataset Version:
BRE-1997-DATA-1.0

Calculation Engine:
1.0.0

Application:
0.5.0
```

This prevents a future change from silently altering old calculations.

---

# 34. Save every design

Eventually the application should store:

```text
Project
 └── Mix Design
      ├── Inputs
      ├── Material properties
      ├── Calculation trace
      ├── Trial mixes
      ├── Corrections
      ├── Final mix
      ├── Notes
      └── Report
```

SQLite is enough initially.

---

# 35. Reports

Eventually generate:

```text
BRE MIX DESIGN REPORT

Project Information

Concrete Requirements

Material Properties

Design Parameters

BRE Calculation

Target Mean Strength

Water/Cement Ratio

Water Content

Cement Content

Aggregate Content

Moisture Corrections

Final Mix

Mix Proportions

Calculation Trace

Engineering Checks

Warnings

Source References

Software Version
```

PDF generation should be deterministic.

---

# 36. Your complete development roadmap

I would use this order:

```text
PHASE 01
Project definition
        ↓
PHASE 02
Source collection
        ↓
PHASE 03
BRE methodology extraction
        ↓
PHASE 04
Equation extraction
        ↓
PHASE 05
Table extraction
        ↓
PHASE 06
Graph/data extraction
        ↓
PHASE 07
Worked examples
        ↓
PHASE 08
Independent verification
        ↓
PHASE 09
Engineering specification
        ↓
PHASE 10
Software architecture
        ↓
PHASE 11
Calculation engine
        ↓
PHASE 12
Automated tests
        ↓
PHASE 13
Desktop UI
        ↓
PHASE 14
Reports
        ↓
PHASE 15
Database/project management
        ↓
PHASE 16
Full engineering validation
        ↓
PHASE 17
Beta version
        ↓
PHASE 18
Real-world validation
        ↓
PHASE 19
Release
```

---

# 37. The actual MD structure I recommend

Ultimately your repository should look approximately like this:

```text
BRE-MIX-DESIGN/
│
├── AGENTS.md
├── README.md
│
├── 00_PROJECT/
│   ├── PROJECT_SCOPE.md
│   ├── PROJECT_ROADMAP.md
│   ├── REQUIREMENTS.md
│   ├── TERMINOLOGY.md
│   ├── DECISIONS.md
│   └── CHANGELOG.md
│
├── 01_SOURCES/
│   ├── SOURCE_REGISTER.md
│   ├── PRIMARY/
│   ├── SECONDARY/
│   └── SOURCE_NOTES/
│
├── 02_BRE_METHOD/
│   ├── 00_OVERVIEW.md
│   ├── 01_SCOPE.md
│   ├── 02_INPUT_REQUIREMENTS.md
│   ├── 03_TARGET_MEAN_STRENGTH.md
│   ├── 04_WATER_CEMENT_RATIO.md
│   ├── 05_WATER_CONTENT.md
│   ├── 06_CEMENT_CONTENT.md
│   ├── 07_TOTAL_AGGREGATE.md
│   ├── 08_FINE_AGGREGATE.md
│   ├── 09_COARSE_AGGREGATE.md
│   ├── 10_ADJUSTMENTS.md
│   ├── 11_FIELD_CORRECTIONS.md
│   ├── 12_FINAL_MIX.md
│   ├── 13_SPECIAL_CASES.md
│   └── 99_TRACEABILITY.md
│
├── 03_STANDARDS/
│   ├── BS_8500/
│   ├── BS_EN_206/
│   ├── MATERIAL_STANDARDS/
│   └── STANDARD_RELATIONSHIPS.md
│
├── 04_ENGINEERING_DATA/
│   ├── DATA_DICTIONARY.md
│   ├── CONSTANTS.md
│   ├── TABLES/
│   ├── GRAPHS/
│   ├── EQUATIONS/
│   └── LOOKUP_DATA/
│
├── 05_CALCULATIONS/
│   ├── CALCULATION_PIPELINE.md
│   ├── EQUATIONS.md
│   ├── INTERPOLATION.md
│   ├── ROUNDING_RULES.md
│   ├── UNIT_RULES.md
│   └── ERROR_RULES.md
│
├── 06_VALIDATION/
│   ├── VALIDATION_PLAN.md
│   ├── GOLDEN_CASES/
│   ├── UNIT_CASES/
│   ├── BOUNDARY_CASES/
│   └── VALIDATION_RESULTS/
│
├── 07_SOFTWARE_SPEC/
│   ├── ARCHITECTURE.md
│   ├── UI_SPEC.md
│   ├── DATABASE_SPEC.md
│   ├── CALCULATION_ENGINE_SPEC.md
│   ├── REPORT_SPEC.md
│   └── TRACEABILITY_MATRIX.md
│
├── 08_AI_AGENT/
│   ├── AGENT_WORKFLOW.md
│   ├── AGENT_RULES.md
│   ├── TASK_TEMPLATE.md
│   ├── ENGINEERING_GUARDRAILS.md
│   ├── REVIEW_CHECKLIST.md
│   └── CHANGE_PROTOCOL.md
│
├── 09_ARCHIVE/
│
└── src/
    ├── calculations/
    ├── models/
    ├── services/
    ├── ui/
    ├── database/
    ├── reports/
    └── validation/
```

---

# 38. Your AI-agent workflow in one picture

```text
                 YOU
                  │
                  ▼
          PROJECT REQUIREMENT
                  │
                  ▼
        ┌───────────────────┐
        │   RESEARCH AGENT  │
        └─────────┬─────────┘
                  │
                  ▼
            SOURCE LIBRARY
                  │
                  ▼
        ┌───────────────────┐
        │ ENGINEERING AGENT │
        └─────────┬─────────┘
                  │
                  ▼
       EQUATIONS + TABLES + RULES
                  │
                  ▼
        ┌───────────────────┐
        │ VERIFICATION AGENT│
        └─────────┬─────────┘
                  │
             VERIFIED?
             /       \
           NO         YES
           │           │
           └──→ FIX    ▼
                ┌───────────────┐
                │ CODING AGENT  │
                └───────┬───────┘
                        │
                        ▼
                 CALCULATION ENGINE
                        │
                        ▼
                  TEST AGENT
                        │
                        ▼
               ENGINEERING AUDITOR
                        │
                   PASS / FAIL
                        │
                        ▼
                      UI
                        │
                        ▼
                    REPORTS
                        │
                        ▼
                 REAL TEST CASES
                        │
                        ▼
                  RELEASE VERSION
```

---

# 39. How I'd use Codex / Claude Code / Antigravity

Don't choose the AI tool first.

**The repository structure and engineering specification come first.**

Then the agents become interchangeable.

You could use:

```text
Codex
   ↓
software architecture + implementation

Claude Code
   ↓
large-scale repository work + auditing

Antigravity
   ↓
UI / application workflow / agentic development
```

The important thing is that **all three obey the same `AGENTS.md`, engineering specification, source register and validation system**.

That means you can switch agents without losing the project's engineering brain.

---

# 40. The first 10 tasks I would give the agent

Don't start coding yet.

### TASK 001

Create project directory structure.

### TASK 002

Create `SOURCE_REGISTER.md`.

### TASK 003

Locate and catalogue authoritative BRE BR 331 material.

### TASK 004

Create complete BRE method outline.

### TASK 005

Extract every required input.

### TASK 006

Extract every equation.

### TASK 007

Extract every table and graph.

### TASK 008

Extract all worked examples.

### TASK 009

Create engineering traceability matrix.

### TASK 010

Create validation cases from the worked examples.

**Only after TASK 010 passes should you start writing the calculation engine.**

---

# 41. And one critical issue for your project

Because you want this for **real engineering work**, we should not simply say:

> "This software follows British Standards."

That would be too broad.

We need to define exactly:

```text
METHOD
BRE BR 331

EDITION
1997

APPLICATION
Normal concrete mix design

STANDARDS
Relevant material/specification standards

LIMITATIONS
Explicitly documented

DATA SOURCE
Verified engineering tables

CALCULATION ENGINE
Version controlled

VALIDATION
BRE worked examples + independent cases

STATUS
Engineering calculation aid
```

The current UK framework has evolved considerably since the BRE publication. BS 8500-1:2023 and BS 8500-2:2023 are current BSI publications, and BSI describes them as complementary to BS EN 206.  So our research phase should explicitly establish **which historical BRE calculations remain appropriate for your intended application and which current specification/durability requirements need to sit around them**, rather than blindly mixing editions.

---

## The immediate next step

I recommend we make **Phase 1 itself an AI-agent research project**.

The first deliverable should be:

```text
BRE-MIX-DESIGN/
│
├── 00_PROJECT/
├── 01_SOURCES/
├── 02_BRE_METHOD/
├── 03_STANDARDS/
├── 04_ENGINEERING_DATA/
├── 05_CALCULATIONS/
├── 06_VALIDATION/
├── 07_SOFTWARE_SPEC/
├── 08_AI_AGENT/
└── AGENTS.md
```

and the agent's **first mission should be research only**, with **zero application code**.

If you want, I can next build the **actual master AI-agent prompt/workflow for this Phase 1**, specifically written so you can paste it into **Codex / Claude Code / Antigravity**, including the exact commands, research tasks, MD templates, source-verification rules, and stopping conditions.

[1]: https://bregroup.com/documents/311572/1990118/327970.pdf/0b770ceb-b9c9-1f81-5028-9f65f7eedfad?t=1732262342868&version=1.0&utm_source=chatgpt.com "DESIGN OF NORMAL CONCRETE MIXES"
[2]: https://trid.trb.org/View/473650?utm_source=chatgpt.com "DESIGN OF NORMAL CONCRETE MIXES. 2ND EDITION - TRID"
[3]: https://www.concrete.org.uk/fingertips/bs-8500-concrete/?utm_source=chatgpt.com "BS 8500 - Concrete | Concrete Society"
[4]: https://www.scribd.com/document/788227658/final-IESL-DOE?utm_source=chatgpt.com "Below Grade Concrete Mix Design Guide | PDF | Concrete | Cement"
