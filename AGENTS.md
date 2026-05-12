# AGENTS.md — Multi-Brain Operating Contract (Public Template)

*This is a generalised, public version of the operating contract I run at the root of my own Obsidian vault. Drop it into your own vault, replace the placeholders, delete sections you do not use, and live with it for two weeks before tuning. Companion to the [Multi-Brain Management System post](./Multi-Brain%20Management%20System.md) and the [canvas](./Multi-Brain%20Management%20System.canvas).*

---

## What this file is

This is the operating contract between any coding agent (Claude Code, Codex, or similar) and this Obsidian vault. The agent reads it at the start of every session. The rules live in this file, not in your memory.

Treat this file as living. Update it when the agent's behaviour drifts, when a new brand enters the system, or when a rule turns out to be wrong in practice.

---

## What this vault is

This vault is a personal operating system for:

- business building and operator work
- portfolio and project coordination
- applied AI research and tooling
- personal CRM and relationship memory
- journalling, reflection, and planning
- task capture and execution
- public-facing content production across multiple brands

The vault helps `[[Owner Name]]` think, build, decide, remember, and follow through. Favour practical organisation and project momentum over a perfect taxonomy.

### Canonical self note

`[[Owner Name]]` is the canonical self-note. Use it as the default identity anchor for owner fields, founder references, and cross-project ownership. Treat handles and platform-specific names as aliases unless the note is specifically about that public persona.

---

## Primary vault areas

The main mental map. Adjust the list to your own setup.

| Area | Location | Purpose | Agent stance |
|---|---|---|---|
| Business | `Business/` | Ventures, offers, strategy, operating work | Active collaborator |
| Portfolio | `Portfolio/` | Cross-project tracking and ownership | Active collaborator |
| Tasks | `Tasks/` | Task capture, triage, execution | Active collaborator |
| People | `People/` | Personal CRM and relationship notes | Careful; preserve tone and privacy |
| Journal | `Journal/` | Daily, weekly, reflection | Respectful; preserve voice |
| Knowledge Base | `Knowledge Base/` | Curated research and structured reports | Read-mostly unless explicitly asked |
| Companies | `Companies/` | Company notes, market observations | Active collaborator |
| Content | `Content/` | Drafts, finished pieces, calendars | Active collaborator |
| Personal Brand | `Personal Brand/` | Public identity, positioning | Active collaborator |
| Vault Management | `Vault Management/` | Vault structure, conventions, workflows | Active collaborator for vault design |
| Templates | `Templates/` | Reusable note templates | Edit when improving workflows |
| Clippings | `Clippings/` | Captured external material | Source layer; do not rewrite unless asked to import or clean |

---

## Operating principles

1. Start from the user's actual goal, not the cleverest system.
2. Prefer the folder the request naturally belongs to.
3. Keep notes useful inside Obsidian: clear titles, stable links, simple frontmatter when needed.
4. Preserve the user's voice in personal, journal, people, and project notes.
5. When a source is speculative, generated, or social-media-derived, mark uncertainty clearly rather than laundering it into confident notes.
6. Prefer small, meaningful improvements over large reorganisations.
7. When an idea is about to become a folder, project, or repo, preview the structure and ask before creating it.

---

## Session startup checklist

1. Read this file.
2. Identify the user's requested work area from the top-level folders.
3. Inspect the relevant folder before giving broad opinions.
4. Report the practical state of that area: what exists, what looks active, what is stale, what next action would create momentum.

For a general "vault state" request, sample the main operating folders first.

---

## Editing rules

- Do not delete or rename notes without explicit confirmation.
- Do not rewrite raw or clipped source material unless the task is to import or clean it.
- For personal, journal, and people notes, preserve tone and avoid over-structuring.
- Prefer extending the most relevant existing note over creating a parallel duplicate.
- If a note has frontmatter or a local format, follow it.

### Mutability classes

Use `mutability:` frontmatter when a note's edit policy matters.

| Class | Use for | Agent behaviour |
|---|---|---|
| `immutable` | Source records, raw research reports, imported snapshots | Do not rewrite. Create linked synthesis or follow-up notes instead. |
| `append-only` | Logs, meeting notes, dispatches, audit trails | Add dated appendices only. Do not restructure previous text. |
| `review-first` | Personal notes, people notes, strategy, verified facts, public-facing claims, health, legal, financial | Preview proposed changes before writing. |
| `living` | Dashboards, indexes, task notes, synthesis notes, project hubs | Safe-write allowed when relevant. |

If a note has no `mutability:` field, infer from the folder and note type. When uncertain, treat as `review-first`.

---

## Task handling

- Use markdown checkbox tasks: `- [ ]`.
- Use `#task` for actionable tasks.
- Use `#inbox` when the task has not been triaged.
- Add `[project:: Project Name]` when the task belongs to a known project.
- Use `#next` only for immediate next actions.
- Keep wording concrete enough to act on later.

---

## Idea to folder handling

When the user asks to turn an idea into a folder, project, repo, or durable operating area:

1. Pause before creating the structure.
2. Check for an existing relevant project or folder first.
3. Identify candidate templates from `Templates/`.
4. Preview the destination, template candidates, and the files and folders that would be created.
5. Ask the user before proceeding.

---

## Meeting note handling

- File in the most specific project `Meetings/` folder when one exists.
- Use `[[Call Notes]]` frontmatter and `mutability: append-only`.
- Normalise into: Executive summary, topic sections, Decisions, Open questions, Action items, Related.
- Convert action items into markdown checkbox tasks.
- Use `[[Owner Name]]` as the canonical self link. Link people, projects, tools, related notes.

---

## Parallel filing into satellite vaults

Some brands have their own dedicated satellite vault or repo outside the main vault. When a note belongs to that brand's operating surface, the agent parallel-files it into the satellite by default so both stay in sync. The main vault wins any disagreement.

### Registered satellite vaults

| Brand | Main-vault home | Satellite root | Pattern |
|---|---|---|---|
| `Brand A` | `Business/Brand A/` | `[path to Brand A vault or repo]` | A (full mirror) |
| `Brand B` | `Business/Brand B/` | `[path to Brand B vault or repo]` | B (narrow mirror) |
| `Brand C` | `Business/Brand C/` | `[path to Brand C vault or repo]` | C (stripped mirror) |
| `Brand D` | `Business/Brand D/` | `[path to Brand D repo]` | D (read-only feeder) |

Add a row when a new satellite is stood up. Pick a pattern. Write a brand-specific entry-point note documenting the scope and any stripping rules. See the [companion post](./Multi-Brain%20Management%20System.md) for what the patterns mean.

### What auto-mirrors by default

For Pattern A satellites:

- Marketing content and drafts
- Offers and public positioning
- Methodology and process docs
- Project briefs and plans the satellite treats as canonical
- Publish logs, content calendars, operating registers

For Pattern B satellites (public brain with its own structure):

- Blog posts, articles, narrative material
- Brand, voice, language guidelines
- Marketing collateral, campaigns, social drafts, tutorials
- Public product or protocol explainers

For Pattern C satellites (near-publish surface, stripped):

- Blog drafts and finished posts
- Email drafts and sequences
- Landing-page and pillar copy
- Tutorials, use-case write-ups, public methodology
- Style and identity material that is already public-safe

For Pattern D satellites: nothing auto-mirrors. The agent may read for grounding only.

### Universal exclusions

Never auto-mirror to any satellite. Preview and ask, or keep central-only:

- Founder-private notes, journal, reflection
- Vault-management material itself
- Raw research and unverified clippings
- Meeting notes with confidential counterparty material
- Competitive analysis, pricing internals, revenue and pipeline data
- Risk registers, governance internals
- Live customer, lead, or partner names
- Anything tagged `internal-only`, `partner-confidential`, or `pre-disclosure`
- Notes flagged `mutability: review-first` without explicit approval

### The stripping pass (Pattern C satellites)

Before writing any note into a Pattern C satellite, run a stripping pass. The mirrored version is a sibling, not the same artefact.

**Remove or generalise:**

- Customer, lead, partner, counterparty names
- Meeting attendees, internal dates, internal commentary
- Revenue, pricing, ARPU, deal size, runway, pipeline
- Competitive analysis, internal vs-competitor framing
- Personnel commentary, 1-1 context
- Internal-only wikilinks (drop the link, keep the surrounding text)
- Frontmatter exposing internal owners, reviewers, mutability flags, routing metadata
- TODOs and open questions not fit for a near-public surface

**Preserve:**

- The public-facing claim and content itself
- Voice, structure, substance
- Citations and source links that are already public
- The destination repo's frontmatter conventions

**Safety valve:** if a note cannot be cleanly stripped without gutting it, do not mirror. Flag it for a deliberate authoring pass in the destination instead.

### How to parallel-file

1. Resolve the equivalent destination path in the satellite. Mirror the satellite's existing folder shape; do not invent a new one.
2. If the destination folder does not exist yet, pause and propose it rather than creating it silently.
3. Apply the pattern-specific transform: copy with slug adjustment (A), scope check (B), stripping pass (C), or read-only context fetch (D).
4. If the satellite has a publish log or content calendar, add a draft entry there too.
5. In responses, report both destinations explicitly so the user can verify.

### Override commands

- `main only` — skip the satellite copy
- `satellite only` — write to the satellite without filing centrally (use sparingly)
- `parallel file this` — explicit mirror of an existing note
- `preview` — show both destinations before writing anything

When unsure whether a note should be parallel-filed, preview both destinations and ask.

---

## Vault ingest router

Plain `ingest` is a smart vault intake command, not a single-destination workflow.

### Command meanings

- `ingest this` — smart router; preview first if destination is ambiguous
- `research ingest this` — apply the research-report ingestion checklist
- `brief ingest this` — normalise generated briefing material
- `task ingest this` — extract markdown checkbox tasks from the source
- `normalise this` — clean formatting only
- `file this` — put content in the right vault area with minimal processing
- `enrich this` — improve connected living vault surfaces after intake; check `mutability` first
- `auto-enrich preview` — generate proposed changes only
- `auto-enrich apply safe` — write only to `mutability: living` notes and approved index surfaces

### Routing defaults

- Deep research reports go near the relevant domain folder
- Action lists go to `Tasks/Inbox.md` unless the project is obvious
- Raw clipped material stays in `Clippings/` unless the user asks for synthesis
- Personal, journal, or people material previews first and preserves voice

### Preview-first rule

For broad or ambiguous ingests, show source(s), intended destination(s), whether raw content will be preserved, and whether tasks or new notes will be created. If the user gives an explicit destination, proceed.

### Enrich vs ingest

Ingestion files or normalises new material. Enrichment turns material into useful vault residue: tasks, dashboards, indexes, synthesis notes, open-question notes, decision-support notes.

Enrichment must not directly rewrite raw sources, original research reports, imported snapshots, verified facts without primary-source evidence, or personal, people, journal, health, legal, financial, or client-facing notes without preview approval.

---

## Confidence and evidence

Use plain confidence language in normal notes:

- `high` — primary source or strongly corroborated
- `medium` — single reliable source or plausible synthesis
- `low` — speculative, generated, contradicted, or not yet checked

For business, health, financial, legal, or public-facing claims, prefer primary sources and make uncertainty visible.

---

## What not to do

- Do not convert the whole vault into a rigid schema.
- Do not over-normalise personal notes until they stop feeling like the user's notes.
- Do not create duplicate pages when an existing note should be extended.
- Do not silently rewrite human-maintained areas in a way that changes meaning, tone, or ownership.
- Do not treat generated briefs or social threads as verified facts.
- Do not invert the system: a satellite never becomes the source of truth without a deliberate, separate decision.

---

## Customising this file

This template is conservative on purpose. Things to tune for your own setup:

- The folder map at the top
- The satellite register (delete brands you do not have; add the ones you do)
- The exclusions list (your sensitive material is not mine)
- The stripping pass (your destination repo has its own rules)
- The override commands (these are mine; pick what you say naturally)
- The ingest router commands (delete the ones you do not use)

If a rule in this file does not match what the agent actually does after a week, fix the file. The contract is the source of truth.

---

*AGENTS.md template v1.0 — based on a working multi-brand vault. Companion to [Multi-Brain Management System](./Multi-Brain%20Management%20System.md), [the canvas](./Multi-Brain%20Management%20System.canvas), and [the implementation seed](./Multi-Brain%20Implementation%20Seed.md).*
