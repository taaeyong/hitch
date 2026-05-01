# Raw Ingest Spec

## Scope
- v4 includes raw txt intake in a limited, semi-supported way
- this is not a fully generalized KakaoTalk ingestion engine in MVP

## User Assumption
- the user may dump rough raw relationship material as txt
- Hitch / Atlas should take on the responsibility of structuring and integrating that material over time

## Raw Input Expectation
- raw text may be messy
- the system should still produce value without requiring perfect formatting

## Required Pipeline Shape
raw input should move through:
1. ingest
2. parse
3. episode segmentation
4. signal extraction
5. ontology mapping
6. intermediate structured data
7. pattern induction / relationship summary updates
8. simulation / reporting / graph materialization

## Practical MVP Meaning
- human-assisted or semi-structured extraction is acceptable
- user convenience matters more than universal parser completeness in v4 MVP
