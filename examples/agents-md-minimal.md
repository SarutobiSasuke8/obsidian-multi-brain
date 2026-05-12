# AGENTS.md — Minimal one-satellite example

*This is the smallest working version of a multi-brain operating contract. One central vault, one satellite, Pattern A (full mirror). Use it as a starting point and grow from here.*

---

## What this vault is

This vault is a personal operating system for `[[Your Name]]`. It holds thinking, planning, projects, tasks, and personal CRM.

The vault helps `[[Your Name]]` decide, remember, and follow through. Favour practical organisation over a perfect taxonomy.

---

## Primary areas

| Area | Location | Purpose |
|---|---|---|
| Business | `Business/` | Ventures, clients, strategy |
| Projects | `Projects/` | Active work |
| Tasks | `Tasks/` | Capture and triage |
| People | `People/` | Contacts and relationship notes |
| Journal | `Journal/` | Daily and weekly notes |
| Content | `Content/` | Drafts, published, calendar |

---

## Operating principles

1. Start from the user's actual goal.
2. Preserve the user's voice in personal, journal, and people notes.
3. Prefer extending an existing note over creating a duplicate.
4. Mark uncertainty in generated or speculative content.

---

## Session startup

1. Read this file.
2. Identify the work area from the top-level folders.
3. Inspect the relevant folder before giving opinions.

---

## Editing rules

- Do not delete or rename notes without confirmation.
- Treat personal and journal notes as `review-first` by default.

### Mutability classes

| Class | Agent behaviour |
|---|---|
| `immutable` | Do not rewrite. Create linked outputs instead. |
| `append-only` | Add dated entries only. |
| `review-first` | Preview before writing. |
| `living` | Safe-write when relevant. |

---

## Parallel filing

One satellite is registered.

| Brand | Main-vault home | Satellite root | Pattern |
|---|---|---|---|
| My Business | `Business/My Business/` | `[absolute path to satellite vault]` | A (full mirror) |

### What auto-mirrors (Pattern A)

- Marketing content and drafts
- Offers and public positioning docs
- Project briefs the satellite treats as canonical
- Publish logs and operating registers

### What never auto-mirrors

- Journal, personal reflection, founder-private notes
- Raw research and clippings
- Meeting notes with confidential counterparty material
- Revenue, pricing, or competitive analysis

### How to parallel-file

1. Resolve the equivalent destination path in the satellite.
2. If the destination folder does not exist, pause and propose it.
3. Copy the note with slug adjustment if needed.
4. Report both destinations in the response.

### Override commands

- `main only` — skip the satellite copy
- `parallel file this` — explicit mirror of an existing note
- `preview` — show both destinations before writing

---

## Task handling

- Use `- [ ]` for checkboxes.
- Add `#task` to actionable items.
- Add `#inbox` when not yet triaged.
- Add `[project:: Project Name]` when the project is known.
- Use `#next` for immediate next actions only.

---

## What not to do

- Do not create duplicates when an existing note should be extended.
- Do not rewrite personal notes until they stop sounding like the user.
- Do not treat generated content as verified facts.
- Do not silently create satellite folders.

---

*Minimal AGENTS.md v1.0 — based on the [obsidian-multi-brain](https://github.com/SarutobiSasuke8/obsidian-multi-brain) template.*
