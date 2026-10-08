---
status: accepted
date: 2026-10-08
---
# Flat `skills/<name>/` layout with the taxonomy in metadata, not in directory names

Skills could be grouped by category directory (`skills/<category>/<name>/`) as Matt Pocock's repository does. We chose a flat layout, atomic and meta skills alike, with stage and type in frontmatter metadata, and a separate top-level `workflows/` directory for chained sets of skills.

The taxonomy will move: the MOU anticipates navigator variants by theoretical framework and a stage model crosswalked to three different lifecycle frameworks. With flat folders a reclassification is a one-line metadata edit; with category directories it is a `git mv` that breaks every install link and URL. Meta-skills are skills in every technical sense, so they live in `skills/` with `type: meta`. Workflows are a different kind of thing, a recipe rather than a skill, and keeping them out of `skills/` preserves the rule that everything in `skills/` is atomic. Both the Claude Code plugin loader and the `npx skills` CLI discover either layout, so the choice carries no install cost.
