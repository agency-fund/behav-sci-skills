# Site copy review (2026-10-13)

Every visible string the site itself writes, before and after a pass with the humanizer skill and taste-skill's copy audit (§4.9, §9). Skill content from SKILL.md files is out of scope. Strings not listed stay as they are.

What the pass removed: slogans, the five-part "does one thing, cites, asks, says when" list (it was in the hero, About, and Contribute), eyebrow labels, middle-dot strings, em dashes, and "from X to Y" ranges. New strings are for the pages and features added in this round.

Mark anything you want changed; the rest goes in as written.

## Everywhere

| Where | Before | After |
|---|---|---|
| Home `<title>` | Behavioral Science Skills: an open library of atomic AI skills | Behavioral Science Skills |
| Home meta description | An open library of atomic AI skills for behavioral science, by The Agency Fund and Irrational Labs. | Open-source AI skills that run behavioral-science methods for social-sector teams. From The Agency Fund and Irrational Labs. |
| Footer blurb | An open library of small, single-purpose AI skills that put behavioral-science methods into the daily work of social-sector teams. Co-owned by The Agency Fund and Irrational Labs. | AI skills for behavioral-science methods, made by The Agency Fund and Irrational Labs for teams without a behavioral scientist on staff. |
| Footer licenses | Skill content CC BY 4.0 · code MIT · licenses | Skills are CC BY 4.0 and code is MIT. See the licenses. |
| Footer links | agency.fund · irrationallabs.com | (two separate links, no separator) |
| Footer theme | (new) | Match system theme |
| Nav | Skills, Workflows, Install, Contribute, What's new, About | Skills, Map, Workflows, Install, Contribute, About (What's new moves to the footer) |
| Eyebrows ("Catalog", "Install", "By stage", "Start here", "Contribute · step 1", "404" and others) | (on every page head) | Removed |

## Home

| Where | Before | After |
|---|---|---|
| h1 | Behavioral science, one skill at a time. | Behavioral science skills for your AI assistant |
| Lede | Small, single-purpose AI skills that put behavioral-science methods into the daily work of social-sector teams. Each one does one thing a behavioral scientist does, cites its evidence, asks before it answers, and says when to bring in a specialist. | {n} small skills, each running one method, like a COM-B barrier analysis or a cognitive interview script. |
| Buttons | Install → (scrolled to #start) · Browse 74 skills · How it works | Install → (goes to /install/) · Browse skills |
| Demo footnote | Illustrative · outputs abridged, numbers invented | Example conversation, shortened. The program and the numbers are made up. |
| Demo links | The skill → / The workflow → | Open this skill / Open this workflow |
| Demo tool lines | Loaded skill · Measure stage / Step 1 · Define | Loaded skill / Step 1 of 5 |
| Demo field break | interviews in the field | Three weeks of interviews later |
| Stages h2 | Where are you in the project? | (keep) |
| Stages text | Skills are organized by where in a project they are used, from defining a behavior to scaling what worked. Pick a stage to browse its skills. | Skills are grouped by the stage of a project where you'd use them. Pick one to see what's in it. |
| Stage panel kicker | Stage 07 · 6 skills | Removed |
| Stage panel link | Browse all 6 skills → | All 6 Implement skills → |
| Meta line | Plus 3 meta-skills that work on the library itself: … | Three meta-skills look after the library itself: … |
| Map teaser h2 | (new) | See which skills feed into each other |
| Map teaser text | (new) | Some skills produce something another skill takes in. A barrier diagnosis, for example, is what lever selection starts from. The map draws these links for all {n} skills. |
| Map teaser button | (new) | Open the skill map |
| Workflows h2 | (new) | Or follow a workflow |
| Workflows text | (new) | A workflow runs several skills in order for a bigger job and marks where your team has to decide. |
| Workflows links | (new) | All workflows · Build your own |
| Install band h2 | Install the whole library (+ "Start here" eyebrow, three numbered steps) | Install in Claude Code |
| Install band text | One install gives your assistant all 74 skills, across the seven stages plus the meta-skills. A skill stays out of the way until a request matches it. | Two commands install every skill and keep them up to date. |
| Install band link | Want to start small? Install only the navigator and the evaluator, or see every install option. | Using Codex, Cursor, or Claude Desktop? See every install option. |

## Skills

| Where | Before | After |
|---|---|---|
| h1 | All skills | Skills |
| Lede | Every skill is one thing a behavioral scientist does, with its evidence, its output shape, and its escalation point. Switch to the map to see how skills chain: one skill's output is the next one's input. | Each skill handles one method. Filter by stage, or search for the method you need. |
| Map button | (Cards / Map toggle) | Open the map |
| Stage line, nothing selected | Seven stages, from defining a behavior to scaling what worked, plus 3 meta-skills that work on the library itself. | Pick a stage to narrow the list. |
| Search placeholder | Search skills… | Search by name, method, or tag |
| Filters | (five selects, always shown) | More filters |
| Card button | (new) | Add / Step 3 (when added) |

## Map (new page)

| Where | After |
|---|---|
| h1 | Skill map |
| Text | An arrow from one skill to another means the first one produces something the second one uses, as the skills' authors declared it. Follow the arrows to find skills that can run in sequence. They aren't the only order that works. |
| Hint | Click a skill to hold its connections in place. |
| Search placeholder | Find a skill |
| Panel buttons | Open skill page · Add to workflow · Show full map |
| Panel sections | Its output goes to · It takes input from · You can supply |
| No links | This skill has no declared links yet. |
| Narrow screen | The map is wide. Scroll sideways, or use the list on the Skills page. |
| Removed | The "You supply" column and the legend ("one skill's output feeds the next", "something you can supply yourself") |

## Workflows

| Where | Before | After |
|---|---|---|
| h1 | Skills in sequence | Workflows |
| Lede | A workflow is a recommended set of skills for a larger task, with the relationships between them stated: which runs first, which can run in parallel, which are independent, and where a human decides. A workflow can be as light as "use these three, in any order, but A before B". | A workflow is a set of skills for a bigger job. It says which run first, which can run side by side, and where a person has to decide. |
| Footnote | Workflows live in workflows/, never in skills/, because everything in skills/ is atomic. | Want to write one for the library? Start from the workflow template. |
| Build card | (new) | Build your own: pick skills from the list or the map, put them in order, and get the install commands and a prompt to run them. |
| Workflow page | (new) | Install these {n} skills · Open in builder |

## Build a workflow (new page)

| Where | After |
|---|---|
| h1 | Build a workflow |
| Lede | Put your skills in order. Between steps you'll see what each skill passes on, or a note where nothing does. |
| Empty | Nothing here yet. Add skills from the Skills page or the map. |
| Order button | Suggest an order, with the help text "Puts each skill after the skills it takes input from." |
| Hand-offs | Passes on its {artifact}. / Uses the {artifact} from step {k}. / No declared hand-off. Give this step what it needs yourself. |
| Install | Install these skills. The Claude Code plugin already includes all of them. |
| Run | Run it: paste this into your assistant. |
| Prompt | I want to run these behavioral-science skills in order: 1. … Start with step 1. After each step, show me the result and wait for me before going on. Where a step's output fits the next step, use it as that step's input. |
| Share | Copy link / Link copied |
| Propose | Suggest it for the library |
| Replace check | Replace your current workflow ({n} skills) with the one in this link? |
| Tray | Your workflow: {n} skills · Edit order · Build · Clear |

## Install

| Where | Before | After |
|---|---|---|
| h1 | Pick the tool you use | Install |
| Lede | Every path installs the same skills. Claude Code keeps itself updated; the others need a re-run or a re-upload when a skill changes. | Every option installs the same skills. Only Claude Code updates them for you. With the others, you re-run the command or re-upload the file when a skill changes. |
| Claude Code, after the commands | Then just describe what you are trying to do. The navigator fires on behavioral-science questions; individual skills fire when you name their method. Type /besci-navigator to call it directly. | Then describe what you're working on. The navigator answers behavioral-science questions, and a skill runs when you name its method. Type /besci-navigator to call the navigator directly. |
| Updates | (new) | To see what changed recently, check What's new. |

## Contribute, propose, upload

| Where | Before | After |
|---|---|---|
| Contribute lede | A skill is one thing a behavioral scientist does, narrow enough to describe in a sentence without the word "and". It cites its evidence, asks before it answers, shows its output shape, names its failure modes, and says when to bring in a specialist. Read the full spec. | A skill covers one method, narrow enough to describe in a sentence without the word "and". The full spec lists everything else a skill has to include. |
| Contribute step | Submit, three ways | Submit it |

Propose and upload keep their text; only the eyebrows go.

## What's new, About, 404

| Where | Before | After |
|---|---|---|
| What's new h1 | Every change is a version | What's new |
| What's new lede | Each change to a skill bumps its version and adds a changelog entry, so a project can cite exactly what it used. Newest first. Subscribe to the RSS feed to hear about releases. | Recent skill changes, newest first. Each change bumps the skill's version, so a project can cite the exact version it used. The RSS feed announces new releases. |
| About h1 | Behavioral science you can install | About |
| About lede | The Behavioral Science Skills Library is a curated, open-source collection of small, single-purpose AI skills that put behavioral-science methods into the daily work of social-sector teams. It is co-owned by The Agency Fund and Irrational Labs. | The Behavioral Science Skills Library is an open-source set of AI skills for social-sector teams. Each skill covers one behavioral-science method. The Agency Fund and Irrational Labs own it together. |
| About, who it is for | …Each skill is one thing a behavioral scientist does: … It cites the evidence it draws on, asks before it answers, produces a predictable output, records where it goes wrong, and says when to bring in a specialist. | …Each skill covers one method, such as breaking a behavior into COM-B barriers, drafting a cognitive interview script, or designing a measure of agency. It names its sources and asks you questions before it produces anything. It also tells you when the work needs a specialist. |
| About | Skills amplify practitioners; they do not replace experts. | The skills help practitioners. They don't replace experts. |
| About h2 | A folder, a contract, and a test suite | What's in a skill |
| About h2 | Three skills that work on the library itself | Skills for using the library |
| About h2 | From the memorandum of understanding | Principles |
| About panel | Skills are Socratic. They ask before they answer. "Before you start" is a required section. | Skills ask before they answer. Every skill has a "Before you start" section with the questions it asks first. |
| About h2 | Co-owned, openly licensed | Governance |

## Skill pages

| Where | Before | After |
|---|---|---|
| Eyebrow | (dot) Design · v0.1.0 | Removed; the stage and version stay in the badges |
| Callout title | When this skill fires | When this skill runs |
| Draft banner | Draft: this skill has not yet been reviewed by a maintainer. Use with care and send feedback. | Draft. A maintainer hasn't reviewed this skill yet, so check its output carefully. |
| Empty details | — | Not stated |
| New | (none) | See it on the map · Add to workflow |

## Machine-readable files

| Where | Before | After |
|---|---|---|
| llms.txt line | - name [stage, type, status]: what it does — URL | - name [stage, type, status]: what it does (URL) |

Stage descriptions in `taxonomy.yaml` stay as they are.
