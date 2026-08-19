# The sync patterns

A quick reference for picking the right pattern when registering a new satellite.

Patterns A to C are outbound publication patterns. Pattern D is a mixed-authority bridge for agent fleets, and Pattern E is the governed return path for material authored outside the central brain. Start with the smallest pattern that solves the actual boundary problem.

---

## Pattern A: Full mirror

**Use when:** the satellite is a structural twin of the central vault. Same folder shape, similar conventions. Typically a dogfood or demo operating vault for a business you run.

**Default behaviour:** straight copy with slug adjustment. Internal wikilinks are rewritten where the target exists in the satellite, dropped where it does not.

**Typical scope:** marketing content, offers and positioning, methodology, project briefs, publish logs, operating registers.

**Watch for:** the satellite accumulating notes that were authored directly there and do not have a central source. Those notes are satellite-only and the agent should not overwrite them.

---

## Pattern B: Narrow mirror

**Use when:** the satellite is a dedicated brain for one brand, with its own folder structure and a different audience. A public knowledge base, a brand narrative vault, a protocol documentation brain.

**Default behaviour:** public-facing material mirrors freely using the satellite's folder shape, not the central vault's. Internal strategy, competitive analysis, pricing, governance, and operating state stay in the central vault.

**Typical scope:** blog posts and articles, brand and narrative guidelines, go-to-market collateral, social drafts, public product or protocol explainers.

**Watch for:** notes that sit on the boundary between public and internal. When in doubt, preview and ask rather than auto-filing.

---

## Pattern C: Stripped mirror

**Use when:** the satellite is one step from public. A content production repo, a near-publish workspace, a partner-shared surface where customer names or financial data must never appear.

**Default behaviour:** every write runs through a stripping pass before the note lands in the destination. The stripped version is a sibling of the vault note, not the same artefact.

**Typical scope:** blog drafts and posts, email sequences, landing-page copy, tutorials, use cases, public methodology and identity, publishable personas.

**Watch for:** notes that cannot be cleanly stripped without gutting the content. When the stripping pass would remove more than it keeps, do not mirror. Flag for deliberate authoring in the destination instead.

### Pattern C-strict: the de-ego'd variant

**Use when:** the satellite is a shared knowledge base that colleagues, a team, or partners read. Not public, but not yours either.

Standard Pattern C strips commercial exposure: names, money, competitive framing. C-strict strips **you** as well.

Remove on top of the normal strip:

- first-person voice and personal narrative
- your own opinions marked as opinions, unless the note exists to record a position
- personal working preferences and habits
- references to your other ventures and projects
- your relationship history with the people mentioned
- anything that only makes sense if the reader knows how you think

What is left should read as though the organisation wrote it, not as though someone shared their private notes with the team. This is a harder edit than the commercial strip and it fails more often. When it fails, author directly in the destination.

**Watch for:** the tempting middle ground where you strip the money but keep the voice. It reads as an internal memo that escaped, and colleagues treat it as your opinion rather than as shared reference material.

---

## Pattern D: Mixed-authority agent bridge

**Use when:** an agent fleet needs stable context plus a bounded place to work, but must not receive the private vault or write directly into canonical knowledge and relationship records.

**Default behaviour:** split the satellite into three authority zones. Each zone has one owner and one permitted flow:

| Zone | Authority | Flow |
|---|---|---|
| `Context/public-safe/` | Central publisher only | Curated, derived mirrors flow out from the central vault. Agents read but do not edit. |
| `Workspace/` | Registered agents within named mounts | Agents may create and update work artefacts without per-note approval. Valuable outputs return through Pattern E review. |
| `CRM/Proposals/` | Agents propose; a human or importer decides | Contact changes are append-only proposals. They remain quarantined until validated and explicitly imported into the canonical CRM. |

Everything outside an authorised zone is read-only or unavailable. Missing path registration, access metadata, or publication ownership means no write.

**Typical scope:** public product and identity context, bounded research or delivery work, handoffs, and structured relationship-update proposals. Credentials, exact financials, private relationship history, unrestricted contact data, health, family, and confidential meetings never enter the bridge.

**Watch for:** authority creep. A writable `Workspace/` is not permission to edit `Context/`; a CRM proposal is not a CRM update; a useful agent output is not canonical until the return-path review accepts it. Keep each zone physically separate and validate before publication or import.

---

## Pattern E: Return path

**Use when:** something other than you writes in the satellite. An agent with write access, a colleague, a research tool depositing exports, a review queue aimed at you.

**Default behaviour:** a governed ingest, not a sync. One deliberate, logged, refusable operation per run. Material comes back into the central brain carrying provenance frontmatter that records the satellite, the exact source path, the authoring agent or person, and the ingest date.

**Typical scope:** agent proposals awaiting a verdict, research output, intelligence and signals, work product authored in the satellite.

**Watch for:** treating it as bidirectional sync. It is not. The central brain still wins every disagreement; the ingest changes what the central brain knows, not who decides. Also watch for the loop: never discover from the folders you mirror outbound, or you will re-ingest your own material into itself.

Full protocol in [backflow.md](./backflow.md).

---

## The agent-context satellite

Pattern D is the concrete form of an agent-context satellite: a retrieval surface plus bounded work and proposal zones. Context is tiered by blast radius, fail-closed on access, validated before every push, and never hand-edited. See [agent-context-satellites.md](./agent-context-satellites.md).

Most people will never need this. You need it when agents run somewhere other than your laptop and need to know things about your business without you pasting context each time.

---

## Choosing between patterns

| Question | If yes |
|---|---|
| Does the satellite have the same folder structure as the central vault? | Pattern A |
| Does the satellite have its own structure and a different audience? | Pattern B |
| Is the satellite one step from public, requiring a strip? | Pattern C |
| Is the satellite a shared team surface where your voice should not appear? | Pattern C-strict |
| Does an agent fleet need public-safe context plus a bounded writable workspace? | Pattern D |
| Should contact changes remain proposals until separately validated and imported? | Pattern D |
| Does the satellite need both a strip AND a PR review? | Pattern C, paired with a branch/PR workflow in the satellite repo |
| Does anything other than you write in the satellite? | Add Pattern E on top of whatever else applies |
| Is the reader an agent rather than a person? | Agent-context satellite |

Patterns compose. A satellite can be Pattern C outbound and Pattern E inbound at the same time. Pattern D normally uses Pattern E for accepted workspace artefacts and CRM proposals, without granting the agent write access to the central brain.

A satellite can also graduate. If a Pattern B satellite starts receiving near-public content regularly, add Pattern C rules for that content slice. Update `AGENTS.md` and the satellite's entry-point note.

---

## One publication owner per path

Independent of pattern: if two processes can commit to the same folder in a satellite, you will get duplicate writes and conflicting history, and you will notice weeks later.

Overlapping live write access is fine. Overlapping publication rights are not. Give every versioned path exactly one owner and write it down in the entry-point note.
