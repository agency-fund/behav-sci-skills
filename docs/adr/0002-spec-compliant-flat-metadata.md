---
status: accepted
date: 2026-10-08
---
# Catalog facets live in spec-compliant flat `metadata` strings, not custom frontmatter keys

The catalog, the validator, and the navigator need machine-readable facets for every skill: type, stage, version, status, authors, org, WEIRD status, tags, and optional typed inputs and outputs. The Agent Skills spec allows only `name`, `description`, `license`, `compatibility`, `allowed-tools`, and a `metadata` map of string to string.

We put every facet under `metadata` as plain strings, with lists as comma-separated text, and keep structured prose (evidence base with citations, output template, failure modes, escalation point) in mandated body sections that the validator checks by heading. The alternatives were a sidecar YAML file per skill, which drifts, or nested top-level keys, which some loaders and validators reject. The cost is that a list like `tags: "com-b, wise-interventions"` is a string the tooling splits; the benefit is that every skill loads unchanged in every tool that follows the spec.
