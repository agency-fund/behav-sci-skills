---
name: besci-skill-creator
description: >-
  Use when someone wants to create a new skill for the Behavioral Science
  Skills Library, turn a method, framework, paper, playbook, or checklist
  into a skill, revise an existing library skill, or check a draft skill
  against the library's spec. Trigger on "create a besci skill", "turn this
  method into a skill", "write a SKILL.md for the behavioral science
  library", "contribute a skill", "is my skill atomic", "check my skill
  draft". Do not use for skills outside this library (Anthropic's
  skill-creator handles general skills). Not for evaluating a finished
  skill across models (besci-eval) or for finding which skill to use
  (besci-navigator).
license: CC-BY-4.0
metadata:
  title: Behavioral science skill creator
  type: meta
  stage: other
  version: "0.1.0"
  status: draft
  authors: "Zezhen Wu"
  org: TAF
  weird: not-applicable
  tags: "meta, authoring"
  produces: "skill-draft"
---

## What it does

Interviews an author about one behavioral-science method until every part of a library skill is clear, then drafts the complete skill folder.

The library's spec has eight sections, three or more test cases, and a changelog. Most authors know their method well and the spec poorly, so the interview does the translating: it asks the questions a careful reviewer would ask, one at a time, with a recommended answer each time, and only writes files once the answers hold up.

## When to use it

### Use it when
- "I want to turn the saying-is-believing technique into a skill for the library"
- "Help me write a SKILL.md for COM-B barrier decomposition"
- "Here's a playbook chapter; make it a besci skill"
- "Is this idea atomic enough to be one skill?"
- "Check my draft skill against the library spec"
- "Revise my skill; the reviewer said the trigger rule is too vague"
- "Contribute a skill" or "claim a skill" for the behav-sci-skills repo

### Do not use it when
- The skill is not for this library (a PDF tool, a coding workflow); use Anthropic's general skill-creator
- The author wants to test a finished skill across models or score its outputs; use besci-eval
- The user wants to know which existing skill fits their problem; use besci-navigator
- The user wants to write a workflow (an ordered set of skills); use the workflow template in the repo, with besci-navigator's guide mode

## Before you start

Ask these first, one at a time, unless already answered.

1. **Required.** In one sentence, what does the skill do? Watch for "and": if the sentence needs one, there are probably two skills. Do not write anything until this sentence is clean.
2. **Required.** Who are you (name, organization) and who is the skill for? The library's default user is a program designer or M&E lead at an NGO with no behavioral scientist in the room.
3. **Required.** Where are we working? If files can be written (Claude Code or a sandbox with a filesystem), the skill folder is created directly and the validator runs. If not (Claude Desktop, claude.ai without code execution), the files are produced as text blocks plus a downloadable zip where possible, and the checklist in `references/checklist.md` replaces the validator.
4. Optional. Is there source material: a paper, a playbook, an existing prompt, notes from practice? Ask for it now; it anchors the evidence base and the procedure.
5. Optional. Is this a revision of an existing skill? If so, read the current folder before asking anything else, and interview only about what is changing.

## What it draws on

- The library's skill specification, bundled as `references/skill-spec.md` (source: `docs/skill-spec.md` in the repo). It is the contract the validator enforces.
- The Agent Skills specification (https://agentskills.io/specification) for frontmatter and folder rules, and Anthropic's skill-creator guidance on progressive disclosure, pushy descriptions, and realistic test prompts.
- The interview discipline of the grill-me pattern: one question at a time, a recommended answer with each, walk every branch, do not write until the branch is resolved.
- The partnership's principles: skills are Socratic (they ask before they answer), they cite what they draw on, they say where they stop and a specialist starts, and their content may be processed by third-party AI systems when others use them, which the author must know before contributing.

**WEIRD skew:** Not a concern for this skill itself. It does require every atomic skill it drafts to state its own WEIRD skew and replication status.

**Replication status:** Not applicable; this is a procedure, not an empirical claim.

## How to do it

Work through the phases in order. One question per turn. Offer a recommended answer with every question so the author can say "yes" instead of composing from scratch. Keep the author's wording where it is good. Never invent a citation; if a reference cannot be confirmed, mark it "unverified, author to confirm" in the draft. The detailed question bank with good and bad examples is in `references/interview-guide.md`; read it before the first question.

**Phase 1: Atomicity gate.** Get the one-sentence "What it does". Test it: one verb, no "and", one input, one output. If it fails, propose the split (two or three skills) and ask which one to build now. Record the others as future skills.

**Phase 2: Name and trigger rule.** Propose a verb-first kebab-case name from the taxonomy's verb list (`define-`, `decompose-`, `draft-`, `design-`, `measure-`...). Then collect the trigger rule: at least three phrasings a real user would type that should fire the skill, and at least two adjacent intents that should not, each with where to send them instead. Draft the `description` from these: a "Use when" clause, the phrasings, and a "Do not use when" clause, under 1024 characters, a little pushy.

**Phase 3: Before you start.** Ask what the skill must know before it can produce a good output, and what it should assume if an answer is missing. Three to six questions is typical. If the author says it needs nothing, push once: "What is the most common way a user gives too little context, and what goes wrong?" Accept "Not applicable" only with a real reason, which goes into the section verbatim.

**Phase 4: Evidence base.** Ask what the method rests on: framework, paper, playbook, or the author's own practice. Get full citations. Then ask the two flags: where does the evidence come from (WEIRD skew), and has it replicated. If the author does not know, say so in the draft rather than guessing.

**Phase 5: Procedure.** Walk the method step by step. For each step ask why it matters and what the model is likely to get wrong. Decide what goes in `SKILL.md` and what moves to `references/` (question banks, long tables, worked examples).

**Phase 6: Output template.** Ask what a finished output looks like. Draft it as a fenced markdown block with angle-bracket placeholders. Check that a reviewer could tell from the template alone whether a run succeeded.

**Phase 7: Failure modes.** Ask "when have you seen this method go wrong in practice?" and "what would a model do with this that an expert would never do?" Get at least three. Add out-of-scope cases.

**Phase 8: Escalation point.** Ask when a user should stop and bring in a specialist, what kind, and what to bring them. Push on "Not applicable" the same way as in Phase 3.

**Phase 9: Test cases.** Draft at least three evals in the user's voice: one complete request that should produce the full output, one that is missing context so the skill should ask, one that approaches the escalation point. Add a fourth that should not fire if the adjacent intents are easy to confuse. Each has an `expected_output` describing the shape of a good answer, not the answer itself. Show them to the author and adjust.

**Phase 10: Metadata.** Confirm stage (recommend from the seven; `other` is allowed), tags, optional `consumes` and `produces` from the taxonomy's io types, authors, org, weird status, version `0.1.0`, status `draft`, license `CC-BY-4.0`.

**Phase 11: Draft the folder.** Write `SKILL.md`, `evals/evals.json`, `CHANGELOG.md`, and any `references/` files, using `assets/skill-template/` as the skeleton. Keep `SKILL.md` under 500 lines.

**Phase 12: Validate.** With a filesystem: run `python scripts/besci_validate.py <skill-folder>` from this skill's folder and fix every error; warnings need a decision, not silence. Without a filesystem: walk `references/checklist.md` against the draft and report what passes and what does not.

**Phase 13: Self-test.** For each eval, act as a fresh user sending that prompt to a model that has only the drafted skill, produce the response, and compare it with `expected_output`. Show the author the three outputs side by side with one line each on what matched and what did not. Offer one revision pass. Do not loop more than twice; deeper testing belongs to besci-eval.

**Phase 14: Package and hand off.** With a filesystem: run `python scripts/package_skill.py <skill-folder>` to produce `<name>.skill`. Then tell the author the three ways to submit (hand the file to a maintainer; upload it into `inbox/` on GitHub with "Create a new branch and start a pull request"; or clone and open a pull request), and remind them that a maintainer reviews content, not just structure. Point them to besci-eval for cross-model testing.

## Output template

The deliverable is the skill folder. Report it like this:

```markdown
# Skill drafted: <name> (v0.1.0, draft)

**What it does:** <the one sentence>
**Stage:** <stage>  **Evidence:** <frameworks, n citations, k unverified>

## Files
skills/<name>/
├── SKILL.md            (<n> lines)
├── evals/evals.json    (<n> cases)
├── CHANGELOG.md
└── references/<file>.md

## Validator
<PASS / FAIL with the report, or the checklist result>

## Self-test
| Eval | Matched expected shape | Gap |
|---|---|---|
| 1 | yes / partly / no | <one line> |

## Open items for the author
- <unverified citation, undecided split, a "Not applicable" to reconsider>

## Submit
<the path that fits this author, in two lines>
```

## Where it goes wrong

- **Accepting a skill that is a workflow.** "Design a behavior change program" is five skills. The atomicity gate exists to catch this; do not skip it to be agreeable.
- **Writing the description as a summary.** "This skill helps teams decompose barriers" fires on nothing. The description is intents and phrasings, with a "do not use when".
- **Inventing citations.** A plausible-looking reference that does not exist is the worst failure this skill can have. Mark anything unconfirmed.
- **Asking everything at once.** A wall of twelve questions gets twelve thin answers. One question, one recommendation, one turn.
- **Letting "Not applicable" through without a reason.** Both optional sections need a sentence that would satisfy a reviewer.
- **Leading test prompts.** Evals written in the skill's vocabulary pass trivially. Write them the way a tired program officer types at 11pm.
- **Over-long SKILL.md.** Reference material belongs in `references/`; the body should fit in one read.
- Out of scope: evaluating skills at scale, writing workflows, general-purpose skills.

## When to bring in a specialist

Tell the author to bring in a domain expert before submitting when:
- The method has no published evidence base and the author is not themselves a practitioner of it.
- The skill touches clinical, safety, legal, or child-protection decisions, where a wrong procedure causes harm.
- The author cannot answer the WEIRD-skew or replication questions and the skill will be used outside the evidence's context.

Bring them: the one-sentence description, the evidence list, and the "Where it goes wrong" draft. A maintainer from TAF or IL reviews every skill's content before merge regardless.
