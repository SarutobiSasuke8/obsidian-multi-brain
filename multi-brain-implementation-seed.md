---
title: "Multi-Brain Implementation Seed"
type: agent-seed
version: "1.0"
---

# Multi-Brain Implementation Seed

*Drop this file into a vault alongside `CLAUDE.md` (or `AGENTS.md`) when you want a coding agent to build out a multi-brain parallel-filing system from scratch. The agent reads this file and uses it as the spec.*

---

## What this file is

This is a seed for a coding agent. It describes the shape of a multi-brain management system in enough detail that an agent can scaffold one inside a fresh Obsidian vault, wire it into the operating contract, and leave the user with a working setup.

Drop this file at the vault root. Open a terminal in the vault. Start a coding agent session. Tell the agent: "implement the multi-brain system per this seed."

The agent should follow the protocol below.

---

## Protocol for the agent

### Phase 0: read the room

Before writing anything, the agent reads:

1. This seed
2. Any existing `AGENTS.md` or `CLAUDE.md` at the vault root
3. The top-level folder structure of the vault
4. Any folders that look like they could be brand or business homes (anything under `Business/`, `Brands/`, `Companies/`, `Clients/`, or named after a known brand)

The agent then produces a short situation report:

- What brands or scopes currently live in the central vault
- Where each one's main-vault home is
- Whether any satellite vaults or repos already exist that should be registered
- What is missing

Do not write any files yet. Confirm the picture with the user.

### Phase 1: gather the satellite register

Ask the user, one question at a time:

1. "What is the central brain? Confirm the vault root path."
2. "Which brands or scopes have a separate workspace, vault, or repo that this central brain should sync into?"
3. For each satellite the user names:
   - Path to the satellite root
   - Purpose in one sentence (dogfood vault, content production repo, public brain, etc.)
   - Audience (internal only, partner-facing, public-facing)
   - Whether it has its own folder structure or mirrors the central brain
4. "Are there any folders or content types in the central brain that should never be auto-mirrored anywhere?"

Use the answers to build the satellite register.

### Phase 2: pick a pattern per satellite

For each satellite, propose one of the four patterns based on what the user said. State the recommendation with the reasoning. Get explicit confirmation before locking it in.

**Pattern A — full mirror.** The satellite mirrors the central brain's folder shape. Notes get straight-copied with slug adjustment. Use when the satellite is a structural twin (e.g., a demo or dogfood operating vault).

**Pattern B — narrow mirror.** The satellite has its own folder structure. Public-facing material mirrors freely; internal strategy stays central-only. Use when the satellite is a dedicated brand brain with a different audience.

**Pattern C — stripped mirror.** Every write runs through a stripping pass that removes unsafe material. Use when the satellite is one step from public (content production repo, partner workspace, near-publish surface).

**Pattern D — mixed-authority agent bridge.** The central vault publishes curated `public-safe` context into `Context/public-safe/`; registered agents may write only inside named `Workspace/<mount>/` paths; relationship changes are append-only proposals under `CRM/Proposals/`. Use when an agent fleet needs shared grounding and bounded work without access to the private vault or canonical CRM.

### Phase 3: define the stripping pass

If any satellite uses Pattern C, the agent must define a stripping pass with the user. Ask:

- "What kinds of names should never appear in this destination?" (customers, leads, partners, counterparties)
- "What financial data should be stripped?" (revenue, pricing, ARPU, deal size, runway, pipeline)
- "What internal context should be stripped?" (meeting attendees, internal dates, internal commentary, 1-1 notes, personnel commentary)
- "What internal frontmatter should be dropped?" (owners, reviewers, internal mutability flags)
- "What should always be preserved?" (the public claim, voice, structure, public citations, destination-repo frontmatter conventions)

Document the answers in the satellite's entry-point note. The agent runs this pass on every Pattern C write.

The safety valve: if a note cannot be cleanly stripped without gutting it, the agent does not mirror. It flags the note for deliberate authoring in the destination instead.

### Phase 3b: define Pattern D authority zones

If any satellite uses Pattern D, configure all three zones before enabling writes:

- `Context/public-safe/`: identify the central publication owner and the curated source notes. Internal context is not co-located in the shared bridge.
- `Workspace/<mount>/`: name every writable mount, its purpose, allowed agent identities, retention rule, and Pattern E destination. Missing registration means no write.
- `CRM/Proposals/`: define the proposal schema, reviewer or importer, canonical CRM boundary, and retention rule. Agents may propose; they never apply canonical relationship changes.

Confirm that filesystem or repository permissions match the written boundary where possible. A folder name and `AGENTS.md` are operating controls, not a security boundary.

### Phase 4: write the operating contract

Create `AGENTS.md` at the vault root if it does not exist. Add a section titled **Parallel filing into satellite vaults** that contains:

- A short statement of intent (one paragraph)
- A markdown table of registered satellites: brand, main-vault home, satellite root, pattern, stance
- Per-satellite mirror scope (what gets auto-filed)
- Universal exclusions (what never auto-files anywhere)
- The stripping pass spec for any Pattern C satellites
- The context publisher, authorised workspace mounts, and CRM proposal gate for any Pattern D bridge
- Override commands the user can speak in chat: `main only`, `satellite only`, `parallel file this`, `preview`
- Agent behaviour: a numbered list of what the agent does on every write inside a brand-scoped folder

Keep the section under 200 lines. It is a contract, not a manual.

### Phase 5: write the entry-point notes

For each satellite, create an entry-point note inside the brand's main-vault home. The note should contain:

- The satellite's root path
- The pattern in use
- The mirror scope for this satellite specifically
- The exclusions for this satellite specifically
- For Pattern C: the strip and preserve lists
- For Pattern D: the three authority zones, publication owner, workspace mount allowlist, and proposal-import gate
- Any quirks (slug differences, folder remapping, conventions)

Name the note something like `[Brand] Satellite Vault Sync` or `Satellite Vault Import Notes`.

### Phase 6: write the human map

Create a single human-facing reference note at `Obsidian Vault Management/Systems/Multi-Brain Management System.md` (or equivalent path). This is the readable version of the system: prose explanation, the table of satellites, the patterns, the stripping pass, the override commands.

This note is for the user. The contract in `AGENTS.md` is for the agent.

### Phase 7: build the canvas

Create a canvas (`.canvas` file) at `Obsidian Vault Management/Multi-Brain Management System.canvas` that visualises:

- The central brain at the top
- The operating contract and motivation on either side
- One node per pattern (A / B / C / D) under the central brain
- Mechanics for each pattern below its header
- The stripping pass as a dedicated node connected to Pattern C
- Universal exclusions and override commands on the sides
- Agent behaviour and the payoff at the bottom

Use Obsidian Canvas JSON format. Use colour codes consistently (one colour per pattern).

### Phase 8: dry run

Pick one note in one of the brand-scoped folders. Show the user:

- Which satellite it would mirror to
- What the destination path would be
- What transforms would apply (slug adjustment, stripping, link rewriting)
- The resulting stripped or copied content if applicable

Do not write the mirror until the user approves the dry run.

### Phase 9: turn defaults on

After the user signs off:

- Note in `AGENTS.md` that parallel filing is now the default
- Confirm the override commands are documented
- Suggest the user live with it for two weeks and revisit the contract based on actual friction

---

## File scaffolding the agent should produce

```
[vault root]/
  AGENTS.md                              ← operating contract (created or extended)
  Obsidian Vault Management/
    Systems/
      Multi-Brain Management System.md   ← human-readable map
    Multi-Brain Management System.canvas ← visual map
  [Brand A home]/
    [Brand A] Satellite Vault Sync.md    ← entry-point note
  [Brand B home]/
    [Brand B] Satellite Vault Sync.md    ← entry-point note
  ... one entry-point per registered satellite
```

The satellite vaults themselves are not created by the agent. The user owns those paths and is responsible for the destination's existence.

---

## Universal exclusions the agent should default to

Even before asking the user, the agent should seed the universal-exclusions list with these defaults and confirm them:

- Founder-private notes, journal, reflection
- Vault-management material itself
- Raw research and unverified clippings
- Meeting notes with confidential counterparty material
- Competitive analysis, pricing internals, revenue and pipeline data
- Risk registers, governance internals
- Live customer, lead, or partner names
- Anything tagged `internal-only`, `partner-confidential`, or `pre-disclosure`
- Notes flagged `mutability: review-first` without explicit approval

The user can add or remove from this list. The defaults are conservative on purpose.

---

## Agent behaviour the contract should encode

On every write inside a brand-scoped folder, the agent:

1. Detects which brand the note belongs to (by folder path)
2. Resolves the equivalent destination in the registered satellite
3. If the destination folder does not exist in the satellite, pauses and proposes the structure rather than creating it silently
4. Runs the pattern-specific transform: copy with slug adjustment (A), scope check (B), stripping pass (C), or authority-zone check (D)
5. Writes to both locations when appropriate
6. Reports both paths explicitly in the response
7. If the content falls in an excluded zone, previews both possible destinations and asks before proceeding
8. Respects override commands spoken in chat

---

## What the agent must not do

- Do not delete satellite content that does not have a central source. The satellite may have content the user authored directly there.
- Do not rename notes across satellites without confirming the wikilink impact.
- Do not silently create folders in satellite vaults. Always propose first.
- Do not mirror notes flagged `mutability: review-first`, `internal-only`, `partner-confidential`, or `pre-disclosure` without explicit user approval.
- Do not assume the central brain is wrong if a satellite disagrees. The central brain wins by default.
- Do not attempt to invert the system later by treating a satellite as the source of truth. If the user wants to move authorship to a satellite, that is a separate, deliberate decision.
- Do not let a Pattern D workspace write outside its registered mount, hand-edit published context, or apply a CRM proposal directly to the canonical record.

---

## Tone for the build session

The user is investing a real chunk of time in this setup. Match that with care:

- Use plain language. Skip jargon.
- One question at a time during the configuration phases.
- Summarise back before writing anything.
- Show, do not tell, during the dry run.
- Be explicit about what each file is for so the user can maintain it without you.

If the user already runs a working note-taking practice, do not impose new conventions on top. Map the system onto their existing structure.

---

## After the build

Once the system is live, the agent's job in future sessions is:

- Read `AGENTS.md` on session start
- Honour the satellite register and the patterns it defines
- Run the right transforms on every write
- Surface friction back to the user so the contract can evolve

The system gets sharper every time the user pushes back on its behaviour. Treat the contract as a living document, not a one-time spec.

---

*Multi-Brain Implementation Seed v1.0 — drop this file beside `CLAUDE.md` to brief a coding agent on building a parallel-filing system from scratch.*
