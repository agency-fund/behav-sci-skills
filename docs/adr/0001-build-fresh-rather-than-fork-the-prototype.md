---
status: accepted
date: 2026-10-08
---
# Build the repository fresh rather than fork Joe Speed's prototype

Joe Speed's `behavioural-skills` prototype (September 2026) already had sixteen skills, a JSON schema, a validator, a static catalog with a workflow builder, and CI. We decided to build this repository from scratch and treat the prototype as its own project, porting individual skills later one at a time.

The prototype's frontmatter put nested custom fields (`evidence_base`, `weird_context`, `inputs`, `outputs`) at the top level, outside the Agent Skills spec, which would have needed a rewrite of every skill anyway. It also lacked test cases, dual licensing, plugin packaging, the meta-skills, and the MOU's governance and disclosure material. Starting clean let the structure follow the spec and the MOU from the first commit; the cost is re-creating the catalog tooling, which was small. Continuity with the prototype's ideas (controlled taxonomy, typed inputs and outputs for chaining, a generated catalog) is kept by design, not by code.
