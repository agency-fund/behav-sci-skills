# Workflows

A **workflow** is a recommended set of skills for a task too big for one skill, with the relationships between the skills stated: which comes after which, which can run in parallel, which are independent, and where a human has to decide before the next step. Even "use these three, in any order, but A before B" is a workflow.

Workflows live here as single markdown files, one per workflow, following `WORKFLOW-TEMPLATE.md`. They are not skills and are never placed in `skills/`. The site draws each one as a graph at https://besci-skills.vercel.app/workflows/.

| Workflow | File |
|---|---|
| From a vague goal to a piloted intervention | `diagnose-to-pilot.md` |
| Design, size, and test a reminder or message program | `design-and-test-an-sms-program.md` |
| Diagnose and shift a social norm | `change-a-social-norm.md` |
| Bring a survey instrument into a new language and mode | `adapt-a-survey-instrument.md` |

To add one, copy `WORKFLOW-TEMPLATE.md` to `workflows/<name>.md` and open a pull request. `besci-navigator` drafts a workflow in guide mode whenever a user's goal spans several stages, and the site's [workflow builder](https://besci-skills.vercel.app/workflows/build/) turns a list of skills you pick into a proposal. From 2027, invited expert organizations are asked to contribute the workflows they actually use.
