# Source Register

> **Purpose:** Catalog every authoritative source used in this project.
> Every engineering calculation, table value, constant, and engineering rule must be traceable to a source in this register.

---

## Source Register Rules

1. Primary sources control engineering calculations.
2. Secondary sources may clarify but cannot override primary sources.
3. Every implemented table must have a source.
4. Every implemented equation must have a source.
5. Every engineering assumption must be documented.
6. Every software implementation must be traceable to an engineering source.
7. Tier 4 sources (blogs, forums, AI-generated) may only be used for discovery — never as authority.

---

## SRC-BRE-001

| Field | Value |
|-------|-------|
| **Title** | Design of Normal Concrete Mixes |
| **Author / Organization** | D.C. Teychenné, R.E. Franklin, H.C. Erntroy; Building Research Establishment |
| **Publication** | BRE Report BR 331 |
| **Edition** | Second Edition |
| **Publication Year** | 1997 |
| **Publisher** | Construction Research Communications Ltd (BRE) |
| **ISBN** | 1-86081-172-8 |
| **Document Type** | Technical guidance / design method |
| **Authority Tier** | Tier 1 — Primary |
| **URL / Identifier** | https://bregroup.com/documents/311572/1990118/327970.pdf |
| **Relevant Sections** | Entire document — Sections 1–8, Tables 1–8, Figures 1–6, Appendices |
| **Purpose** | Primary engineering method for normal concrete mix proportioning |
| **Used By** | All BRE method files, all equations, all tables, all graphs |
| **Verification Status** | `VERIFIED` — PDF obtained from official BRE Group website |
| **Notes** | First published 1975 (DoE method). Revised 1988. Second edition 1997. Supersedes earlier editions. Historical method — predates current BS 8500/BS EN 206 framework. |

---

## SRC-BSI-001

| Field | Value |
|-------|-------|
| **Title** | Concrete — Complementary British Standard to BS EN 206. Part 1: Method of specifying and guidance for the specifier |
| **Author / Organization** | British Standards Institution (BSI) |
| **Publication** | BS 8500-1 |
| **Edition** | 2023 |
| **Publication Year** | 2023 (published 30 November 2023) |
| **Publisher** | BSI |
| **Document Type** | National standard |
| **Authority Tier** | Tier 1 — Primary |
| **URL / Identifier** | BSI Shop / standards.bsigroup.com |
| **Relevant Sections** | Exposure classes, minimum cement content, maximum w/c ratio, strength classes |
| **Purpose** | Current UK concrete specification framework — defines durability and specification requirements |
| **Used By** | `03_STANDARDS/`, context for future durability inputs |
| **Verification Status** | `VERIFIED` — current edition confirmed via BSI, Concrete Centre, Concrete Society |
| **Notes** | Complementary standard to BS EN 206. Replaced BS 5328 in 2003. Updated 2023 to support lower-carbon cements. Commercially published — content not reproduced here. |

---

## SRC-BSI-002

| Field | Value |
|-------|-------|
| **Title** | Concrete — Complementary British Standard to BS EN 206. Part 2: Specification for constituent materials and concrete |
| **Author / Organization** | British Standards Institution (BSI) |
| **Publication** | BS 8500-2 |
| **Edition** | 2023 |
| **Publication Year** | 2023 (published 30 November 2023) |
| **Publisher** | BSI |
| **Document Type** | National standard |
| **Authority Tier** | Tier 1 — Primary |
| **URL / Identifier** | BSI Shop / standards.bsigroup.com |
| **Relevant Sections** | Constituent materials, cement types, aggregate requirements, admixtures |
| **Purpose** | Current UK specification for constituent materials and concrete |
| **Used By** | `03_STANDARDS/`, material input context |
| **Verification Status** | `VERIFIED` — current edition confirmed |
| **Notes** | Complementary to BS EN 206 and BS 8500-1. |

---

## SRC-BSEN-001

| Field | Value |
|-------|-------|
| **Title** | Concrete — Specification, performance, production and conformity |
| **Author / Organization** | CEN / BSI |
| **Publication** | BS EN 206 |
| **Edition** | Current applicable edition (BS EN 206:2013+A2:2021 at time of research) |
| **Publication Year** | 2013 (with amendments) |
| **Publisher** | BSI / CEN |
| **Document Type** | European standard (adopted as British Standard) |
| **Authority Tier** | Tier 1 — Primary |
| **URL / Identifier** | BSI Shop |
| **Relevant Sections** | Exposure classes, conformity criteria, specification methods |
| **Purpose** | European framework standard for concrete specification |
| **Used By** | `03_STANDARDS/`, relationship documentation |
| **Verification Status** | `VERIFIED` — existence and general scope confirmed |
| **Notes** | BS 8500 is the UK complementary standard to BS EN 206. The BRE mix design method (1997) predates the current BS EN 206 framework. |

---

## SRC-BSEN-002

| Field | Value |
|-------|-------|
| **Title** | Cement — Part 1: Composition, specifications and conformity criteria for common cements |
| **Author / Organization** | CEN / BSI |
| **Publication** | BS EN 197-1 |
| **Edition** | BS EN 197-1:2011 |
| **Publication Year** | 2011 |
| **Publisher** | BSI / CEN |
| **Document Type** | European standard |
| **Authority Tier** | Tier 1 — Primary |
| **URL / Identifier** | BSI Shop |
| **Relevant Sections** | Cement strength classes (32.5, 42.5, 52.5), cement types |
| **Purpose** | Defines cement classification used as input to BRE method |
| **Used By** | `02_BRE_METHOD/04_WATER_CEMENT_RATIO.md`, Table 2 |
| **Verification Status** | `VERIFIED` — cement classes confirmed |
| **Notes** | BRE BR 331 (1997) uses cement classes that align with BS EN 197-1 classification (42.5, 52.5). The 1997 edition refers to the then-current cement classification. |

---

## SRC-BSEN-003

| Field | Value |
|-------|-------|
| **Title** | Aggregates for concrete |
| **Author / Organization** | CEN / BSI |
| **Publication** | BS EN 12620 |
| **Edition** | BS EN 12620:2002+A1:2008 |
| **Publication Year** | 2002 (amended 2008) |
| **Publisher** | BSI / CEN |
| **Document Type** | European standard |
| **Authority Tier** | Tier 1 — Primary |
| **URL / Identifier** | BSI Shop |
| **Relevant Sections** | Aggregate grading, aggregate sizes, properties |
| **Purpose** | Defines aggregate classification relevant to BRE aggregate inputs |
| **Used By** | `02_BRE_METHOD/` aggregate-related files |
| **Verification Status** | `VERIFIED` — existence confirmed |
| **Notes** | BRE method uses aggregate size (10, 20, 40 mm) and type (crushed/uncrushed) as inputs. |

---

## SRC-CS-001

| Field | Value |
|-------|-------|
| **Title** | Concrete Society — BS 8500 Concrete Technical Guidance |
| **Author / Organization** | The Concrete Society |
| **Publication** | Website technical guidance |
| **Edition** | Current (accessed 2026) |
| **Publication Year** | Ongoing |
| **Publisher** | Concrete Society |
| **Document Type** | Technical guidance |
| **Authority Tier** | Tier 2 — Technical |
| **URL / Identifier** | https://www.concrete.org.uk/fingertips/bs-8500-concrete/ |
| **Relevant Sections** | BS 8500 overview, historical context, BS 5328 replacement |
| **Purpose** | Understanding the transition from BS 5328 to BS 8500/BS EN 206 |
| **Used By** | `03_STANDARDS/STANDARD_RELATIONSHIPS.md` |
| **Verification Status** | `VERIFIED` — accessed and reviewed |
| **Notes** | Confirms BS 8500 and BS EN 206 replaced BS 5328 in 2003. |

---

## SRC-TRID-001

| Field | Value |
|-------|-------|
| **Title** | TRID Record — Design of Normal Concrete Mixes, 2nd Edition |
| **Author / Organization** | Transportation Research Board (TRB) |
| **Publication** | TRID database record |
| **Edition** | N/A (database entry) |
| **Publication Year** | N/A |
| **Publisher** | TRB / National Academies |
| **Document Type** | Bibliographic record |
| **Authority Tier** | Tier 3 — Supporting |
| **URL / Identifier** | https://trid.trb.org/View/473650 |
| **Relevant Sections** | Publication metadata |
| **Purpose** | Confirms ISBN, edition, authorship of BRE BR 331 |
| **Used By** | Source verification |
| **Verification Status** | `VERIFIED` |
| **Notes** | Independent confirmation of BRE BR 331 publication details. |

---

## SRC-UNI-001

| Field | Value |
|-------|-------|
| **Title** | Eastern Mediterranean University — BRE Mix Design Lecture Notes |
| **Author / Organization** | Eastern Mediterranean University (EMU), Civil Engineering Department |
| **Publication** | University lecture materials |
| **Edition** | Various |
| **Publication Year** | Various |
| **Publisher** | EMU |
| **Document Type** | Educational material |
| **Authority Tier** | Tier 3 — Supporting |
| **URL / Identifier** | https://www.emu.edu.tr |
| **Relevant Sections** | BRE method worked examples, tables, procedure explanation |
| **Purpose** | Cross-verification of BRE method steps, worked examples for validation |
| **Used By** | Validation cases, cross-checking |
| **Verification Status** | `SECONDARY` — university source, not primary BRE publication |
| **Notes** | Useful for cross-checking extracted values and understanding method application. Values must be verified against primary source. |

---

## SRC-CC-001

| Field | Value |
|-------|-------|
| **Title** | Concrete Centre — Technical Guidance and Publications |
| **Author / Organization** | The Concrete Centre (MPA) |
| **Publication** | Website and technical publications |
| **Edition** | Current |
| **Publication Year** | Ongoing |
| **Publisher** | Mineral Products Association |
| **Document Type** | Technical guidance |
| **Authority Tier** | Tier 2 — Technical |
| **URL / Identifier** | https://www.concretecentre.com |
| **Relevant Sections** | BS 8500 guidance, concrete specification |
| **Purpose** | Understanding current UK concrete specification practice |
| **Used By** | `03_STANDARDS/` |
| **Verification Status** | `VERIFIED` |
| **Notes** | Confirms BS 8500-1:2023 and BS 8500-2:2023 as current editions. |

---

## Summary Table

| ID | Source | Edition | Tier | Purpose | Status |
|----|--------|---------|------|---------|--------|
| SRC-BRE-001 | BRE BR 331 | 1997, 2nd Ed. | 1 | Mix design procedure | VERIFIED |
| SRC-BSI-001 | BS 8500-1 | 2023 | 1 | UK specification/durability | VERIFIED |
| SRC-BSI-002 | BS 8500-2 | 2023 | 1 | Materials/concrete | VERIFIED |
| SRC-BSEN-001 | BS EN 206 | 2013+A2:2021 | 1 | European specification | VERIFIED |
| SRC-BSEN-002 | BS EN 197-1 | 2011 | 1 | Cement classification | VERIFIED |
| SRC-BSEN-003 | BS EN 12620 | 2002+A1:2008 | 1 | Aggregate specification | VERIFIED |
| SRC-CS-001 | Concrete Society | Current | 2 | BS 8500 guidance | VERIFIED |
| SRC-TRID-001 | TRID/TRB | N/A | 3 | BRE metadata verification | VERIFIED |
| SRC-UNI-001 | EMU Lecture Notes | Various | 3 | Worked examples | SECONDARY |
| SRC-CC-001 | Concrete Centre | Current | 2 | Current standards guidance | VERIFIED |

---

*Last updated: 2026-09-18*
