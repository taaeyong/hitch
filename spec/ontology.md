# Ontology and Graph Spec

## Layer Separation
Treat these as distinct but related layers:
- intermediate structured schema
- ontology
- visualization surface

Final visualization should be ontology-based, not a raw dump of the intermediate schema.

## Core Node Types (v1)
1. person
2. relationship
3. episode
4. need
5. preference
6. expression
7. reception
8. mismatch
9. repair
10. question

## Core Edge Vocabulary (v1)
1. has_relationship
2. involves
3. expresses
4. receives
5. prefers
6. needs
7. contains_mismatch
8. resolved_by
9. raises
10. informs

## Pre-Visualization Data Requirement
There must be a structured intermediate representation between raw text and final graph rendering.
That layer should support:
- simulated relationship reasoning
- daily/weekly interpretation bootstrapping
- graph-ready visualization later
