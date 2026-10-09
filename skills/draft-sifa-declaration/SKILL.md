---
name: draft-sifa-declaration
description: >-
  Use when writing up a report, paper, intervention design, or other
  deliverable and the team must disclose how people and AI tools each
  contributed. Also use when a journal, funder, or organizational policy
  asks for an AI-use disclosure and the current answer is "we used ChatGPT
  a bit for drafting", or when a team wants its human-AI division of labor
  inspectable before anyone asks. Produces a SIFA declaration (Statement of
  Intellectual Fellowship and Accountability): for each CRediT contributor
  role, who did the work, which AI tool helped, how much on a
  none/some/extensive scale, and the audit note behind that rating. It
  records what happened; it does not judge whether the AI use was
  acceptable. Do not use to examine the team's prior beliefs about the
  target population; that is audit-researcher-bias, which runs before the
  work. Not for ruling on whether a level of AI use passes a journal's or
  funder's policy, and not for evaluating an AI product (choose-ai-eval-level).
license: CC-BY-4.0
metadata:
  title: Write an AI-use disclosure statement
  type: atomic
  stage: implement
  version: "0.1.0"
  status: draft
  authors: "Joe Speed"
  org: IL
  weird: likely-generalizes
  tags: "research-transparency, credit, ai-disclosure"
  consumes: "ai-use-account"
  produces: "sifa-declaration"
---

## What it does

Turns a team's account of who did what into a SIFA declaration of where AI tools were involved in producing a piece of work.

For each relevant role in CRediT (a standard list of research contributor roles), it records the people involved, any AI tool used, how much the AI contributed (none, some, or extensive), and a short audit note explaining that rating. Accountability stays with the named human authors throughout.

## When to use it

### Use it when
- A report, paper, intervention design, or other deliverable is being finalized and the team needs a standardized statement of where AI tools were involved in producing it
- A journal, funder, or organizational policy asks for an AI-use disclosure and the team's current answer is an unstructured paragraph ("we used ChatGPT a bit for drafting")
- A team wants to make its human-AI division of labor inspectable before someone else asks; SIFA's framing is a deliberate, voluntary disclosure, not a compliance response
- Someone asks "how do we say which parts the AI did?" or "do we have to disclose that it fixed our grammar?"

### Do not use it when
- The team wants to examine its prior beliefs about the target population; that is `audit-researcher-bias`, which runs before the work, where this skill runs after it
- The request is for a ruling on whether a level of AI involvement is acceptable or "will pass the journal's policy"; the declaration records what happened, and the ruling belongs to the journal, funder, or organization
- The subject is an AI product's quality or impact rather than AI tools used in producing a piece of work; `choose-ai-eval-level` and `design-golden-dataset` cover that

## Before you start

Ask these before producing anything. Do not ask anything the user has already answered.

1. **Required.** The work being declared: its title, its type (report, paper, design document, dataset), and the human authors who will be accountable for it.
2. **Required.** The team's raw, honest account of how the work was produced: who did which parts, which AI tools were used where (name and model or version), and roughly how heavily each contributed. Ask specifically about small uses teams tend to drop: grammar passes, debugged scripts, first drafts of charts, literature sweeps.
3. **Required.** Anything the team is unsure whether to disclose. Those items go in the table; small ratings with honest notes are what make the large ratings credible.
4. Optional. The declaration date, and whether a specific venue's disclosure format must be produced alongside the SIFA form.

If 1 or 2 is missing, ask and stop. If the answer to 3 is "nothing", proceed, but ask once about the roles most often omitted (review and editing, visualization, software). If 4 is missing, date the declaration today and produce the SIFA form only.

## What it draws on

- Schomerus, M., & Saleh, E. SIFA: Statement of Intellectual Fellowship and Accountability. Busara. Browser-based declaration tool mapping AI involvement onto CRediT contributor roles. https://mareikeschomerus-ctrl.github.io/sIfA/
- Brand, A., Allen, L., Altman, M., Hlava, M., & Scott, J. (2015). Beyond authorship: attribution, contribution, collaboration, and credit. *Learned Publishing*, 28(2), 151-155.

SIFA (Schomerus & Saleh, Busara) maps AI involvement onto the CRediT contributor-role taxonomy (Brand et al., 2015), the same 14 roles (Conceptualization, Methodology, Investigation, Formal analysis, Writing – original draft, Writing – review & editing, Visualization, and so on) that major journals already use for human contributors. That mapping is the core move this skill preserves: instead of one vague project-level sentence, AI involvement is declared role by role, on SIFA's three-point scale (none, some, extensive), each rating carrying a brief audit note saying what the tool actually did. Using an established taxonomy makes declarations comparable across projects and journals rather than bespoke prose.

Two SIFA principles are load-bearing and this skill enforces them. First, accountability stays human: an AI tool is never listed as a contributor alongside people; it appears only inside a role a named human is accountable for. Second, the audit note is the substance: a bare "2" next to Writing – original draft tells a reader almost nothing, while "first draft of sections 2 to 4 generated from our outline, then substantially restructured by the authors" tells them exactly what to weigh.

Judgment call the source does not fully specify: SIFA is a self-report tool, and so is this skill. It structures what the team says happened; it has no way to detect an omitted tool or an understated rating. The output therefore states on its face that it is a self-declaration.

**WEIRD skew:** The declaration practice itself is procedural and travels: it makes no claims about human behavior, only about disclosure. What is culturally specific is the CRediT taxonomy's origin in Western academic publishing. Its 14 roles assume a journal-article division of labor, and authorship and credit norms differ across research cultures and sectors. Teams outside that context should treat the role list as a checklist to adapt (dropping or renaming roles that do not exist in their workflow) rather than a form to force their work into.

**Replication status:** Not applicable: SIFA is a disclosure procedure and CRediT a contributor taxonomy, so there is no effect to replicate. CRediT is adopted by many publishers; SIFA is a recent tool, and whether declarations made with it are complete or consistent across teams has not, to the authors' knowledge, been studied.

## How to do it

1. **Write the header.** Name the work, the human authors accountable for it, and every AI tool used anywhere in it (tool plus version or model, one line each; "none" is a valid answer). Add the declaration-basis line: self-reported by the authors on the date, a disclosure and not an external audit. This line is mandatory and unhedged.
2. **Walk all 14 CRediT roles against the account.** Only roles that apply to the work are listed, but every role where any AI involvement occurred must appear, including ones the team considers trivial: "it just fixed our grammar" is a Writing – review & editing disclosure. Roles with no AI involvement and no ambiguity may be grouped in a single 0 row.
3. **Rate each listed role on SIFA's scale:** 0 none, 1 some, 2 extensive. Anchor the scale to SIFA, not to the team's comfort: if the tool produced the first version of the artifact, that role is a 2 however heavily it was edited afterward.
4. **Write the audit note for each row:** what the tool concretely did and what the humans did around it. The test is whether a skeptical reader could tell what the tool produced versus what the humans produced. "AI was used responsibly" fails that test.
5. **Keep the tool out of the contributor column.** It appears only in the AI tool column of a role a named human answers for. Do not write audit notes in which the tool "decided" or "concluded".
6. **List the roles not applicable to this work** and why, one line each, so an omission reads as a judgment rather than an oversight.
7. **Write the accountability paragraph:** the claims, analysis, and errors in the work are the named authors' responsibility regardless of the ratings above.
8. **If the account asks for a declaration shaped to pass a policy,** structure what happened anyway and say plainly that whether it passes is the venue's call. Shading notes toward a desired ruling is the failure the tool exists to prevent.

See `references/worked-example.md` for a complete declaration on a two-author field study report.

## Output template

```markdown
# SIFA declaration: <work title>

**Human authors accountable for this work:** <names; accountability for every role below, including AI-assisted ones, rests with these people>
**AI tools used anywhere in the work:** <tool + version/model, one line each; "none" for a clean-hands declaration is also a valid output>
**Declaration basis:** Self-reported by the authors on <date>. This statement records the authors' own account; it is a disclosure, not an external audit.

## Role-by-role declaration
| CRediT role | Human contributor(s) | AI tool | AI involvement (0-2) | Audit note |
|---|---|---|---|---|
| <role> | <names> | <tool or none> | <0/1/2> | <what the tool concretely did, and what the humans did around it> |

<one row per applicable role; roles with no AI involvement and no ambiguity may be grouped in a single 0 row for brevity>

## Roles not applicable to this work
<CRediT roles omitted and why, one line each, so an omission reads as a judgment, not an oversight>

## What the humans remain accountable for
<one short paragraph: the claims, analysis, and errors in this work are the named authors' responsibility regardless of the tool ratings above>
```

## Where it goes wrong

- **The vague-virtue declaration.** Audit notes like "AI was used responsibly throughout" rate everything a 1 and explain nothing. The note's test: could a skeptical reader tell what the tool concretely produced versus what the humans produced? If not, the declaration is reassurance, not disclosure.
- **Laundering through the scale.** Rating extensive first-drafting as "1, some" because 2 feels embarrassing. The scale anchors are SIFA's, not the team's comfort: if the tool produced the first version of the artifact, that role is a 2 no matter how heavily it was edited after.
- **The AI as author.** Listing the tool in the contributor column, or writing audit notes in which the tool "decided" or "concluded". SIFA's accountability principle is the opposite: tools appear only inside roles a named human answers for.
- **Trivial-use omission.** Dropping the grammar pass or a debugged script because "that's not really AI use". Any role the tool touched appears in the table; small ratings with honest notes are exactly what makes the big ratings credible.
- **Treating the output as verification.** This is self-report. A team that omits a tool produces a clean-looking declaration; nothing in this skill can catch that, which is why the declaration-basis line is mandatory and unhedged.
- **Out of scope: policy rulings.** An input like "declare our AI use in a way that will pass the journal's policy" asks the declaration to answer an acceptability question. Structure what happened; whether it passes is the journal's call, and shading notes toward a desired ruling is the failure the tool exists to prevent.

## When to bring in a specialist

Tell the user to take the question to the venue's editor, their organization's research integrity officer, or legal counsel when:
- The question is whether a given level of AI involvement is acceptable under a journal's, funder's, or organization's policy; the declaration is the input to that ruling, not the ruling itself
- Contributors disagree about who performed a role, or about whether someone qualifies as an author at all; CRediT roles do not settle authorship disputes, and an integrity officer or the venue's authorship policy does
- AI tools processed confidential, participant, or third-party material, raising questions of consent, data protection, or copyright that go beyond disclosure; those belong with counsel or a data protection officer

Bring them: the completed declaration, the raw AI-use account, and the text of the policy in question.
