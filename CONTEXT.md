# Behavioral Science Skills Library

A curated, open-source library of small, single-purpose AI skills that put behavioral-science methods into the daily work of social-sector teams. Co-owned by The Agency Fund and Irrational Labs.

## Language

**Skill**:
A folder containing a `SKILL.md` that teaches an AI tool one documented procedure, citing its evidence, stating when it applies, and producing a predictable output.
_Avoid_: prompt, template, tool, agent

**Atomic skill**:
A skill that does one thing a behavioral scientist does, narrow enough to describe in one sentence without the word "and".
_Avoid_: micro-skill, sub-skill

**Meta-skill**:
A skill whose subject is the library itself rather than a behavioral-science method: creating, navigating, or evaluating skills.
_Avoid_: system skill, utility skill

**Trigger rule**:
The statement of which user intents and phrasings should invoke a skill and which adjacent intents should not. The compressed form is the `description` field; the full form is the "When to use it" section.
_Avoid_: activation criteria, use case

**Escalation point**:
The condition under which a skill tells the user the question has outgrown the tool and a human specialist is needed.
_Avoid_: handoff, limit

**Evidence base**:
The frameworks, papers, or practice a skill draws on, with citations, WEIRD skew, and replication status.
_Avoid_: references, sources, literature

**Test case**:
A realistic user prompt paired with the expected shape of output, stored in the skill's `evals/evals.json`, used in review and re-run when the skill changes.
_Avoid_: example, sample prompt

**Version**:
The semver string in a skill's metadata, bumped with every change and described in the skill's `CHANGELOG.md`, so a project can cite the exact skill it used.

**Workflow**:
A recommended set of skills for a larger task, with the relationships between them stated: ordered, parallel, or independent, and where a human decides. Lives in `workflows/`, never in `skills/`.
_Avoid_: stack, pack, bundle, pipeline

**Stage**:
Where in a project a skill is normally used: define, diagnose, design, measure, test, analyze, implement, or other. One per skill, strongly recommended rather than dictated.
_Avoid_: phase, category, step

**Navigator**:
The meta-skill that recommends which skills to run and in what order. In route mode it answers a concrete task with at most one question; in guide mode it interviews the user and drafts a workflow.
_Avoid_: router, assistant, orchestrator

**Catalog**:
The machine-readable list of every skill and workflow, generated from the repository. The site renders it; the navigator carries a dated snapshot of it.
_Avoid_: index, registry, directory

**Inbox**:
The repository folder where a contributor drops a packaged skill through GitHub's web upload so a bot can unpack and check it.
_Avoid_: drop zone, staging, uploads

**Contributor key**:
The shared secret given to TAF and IL staff that lets the website's upload form open a pull request on their behalf during Phase 1.
_Avoid_: password, token, API key
