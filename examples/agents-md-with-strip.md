# AGENTS.md — Pattern C stripping example

*This example shows the full stripping pass configuration for a near-public satellite (Pattern C). Assumes you already have the base structure from the minimal example. Only the parallel-filing section is shown here.*

---

## Parallel filing

Two satellites registered.

| Brand | Main-vault home | Satellite root | Pattern |
|---|---|---|---|
| My Business | `Business/My Business/` | `[path to internal business vault]` | A (full mirror) |
| Content Repo | `Business/My Business/Content/` | `[path to near-public content repo]` | C (stripped mirror) |

---

### Pattern A: My Business (full mirror)

**What auto-mirrors:**

- All marketing content and drafts
- Offers, methodology, public positioning
- Project briefs and plans
- Publish logs, registers, calendars

**What never auto-mirrors:**

- Journal, personal reflection, founder-private notes
- Raw research and clippings
- Meeting notes with confidential counterparty material
- Revenue, pricing, pipeline, competitive analysis

---

### Pattern C: Content Repo (stripped mirror)

The content repo is one step from public. Every write runs through a stripping pass. The main vault is the source of truth; the content repo receives derived, de-risked siblings.

**What auto-mirrors (after stripping):**

- Blog drafts and finished posts to `Blog/`
- Email drafts and sequences to `Emails/`
- Landing-page and pillar copy to `Pages/`
- Social posts intended for publication to `Social/`
- Tutorials and explainers to `Tutorials/`
- Use-case write-ups to `Use-Cases/`
- Public brand, voice, style material to `Style/`
- Publishable methodology to `Methodology/`

**What never auto-mirrors here:**

- Competitive analysis, pricing, revenue, pipeline
- Customer, lead, or partner profiles
- Meeting notes, session logs, 1-1s
- Internal strategy, risk registers, governance
- Anything with live counterparty names
- Raw research and unverified claims

**The stripping pass — mandatory on every write:**

Remove or generalise:

- Customer, lead, partner, counterparty names (replace with role descriptors only if the sentence requires it)
- Meeting attendees, internal dates, internal commentary, decisions-made-in-meeting context
- Revenue, pricing, ARPU, deal size, runway, or any financial internals
- Competitive analysis, internal positioning vs named competitors
- Internal team commentary or 1-1 context
- Wikilinks that point to internal-only vault notes (remove the link, keep the surrounding text)
- Frontmatter fields exposing internal owners, reviewers, or internal status (mutability, routing, review-first flags)
- TODOs and open questions not appropriate for a near-public surface

Preserve:

- The public-facing claim, content, and narrative
- Voice, structure, substance
- Public citations and source links
- The content repo's own frontmatter conventions (title, tags, status, type)

Safety valve: if a note cannot be cleanly stripped without gutting it, do not mirror. Flag it for a deliberate authoring pass in the content repo instead.

Show the stripped version in the response before writing if anything non-trivial was removed, so the user can verify the cut.

---

### How to parallel-file

1. Detect the brand folder the note belongs to.
2. Resolve the equivalent destination in the satellite.
3. If destination folder is missing, pause and propose it.
4. For Pattern C: run the stripping pass. Show removed material in the response.
5. Write to both locations.
6. Report both paths explicitly.
7. If content is in an excluded zone, preview and ask.

### Override commands

- `main only` — skip satellite copy
- `satellite only` — write to satellite only (use sparingly)
- `parallel file this` — explicit mirror of an existing note
- `preview` — show both destinations before writing

---

*Pattern C example — based on the [obsidian-multi-brain](https://github.com/SarutobiSasuke8/obsidian-multi-brain) template.*
