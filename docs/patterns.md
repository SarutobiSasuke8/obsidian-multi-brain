# The sync patterns

A quick reference for picking the right pattern when registering a new satellite.

Patterns A to D are the original four and they all push one way. Pattern E is the return path, added once satellites started producing material of their own. Start with A to D. Add E only when something other than you is writing in a satellite.

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

## Pattern D: Read-only feeder

**Use when:** the satellite needs context from the central vault but should never receive automated writes. A code repo, a partner-controlled space, a research vault for a specialist domain, anywhere commit hygiene or access control matters more than note flow.

**Default behaviour:** the agent reads the satellite for grounding but does not write. Any proposed changes are captured back into the central vault first, then offered for explicit push.

**Typical scope:** context reads only. No auto-mirroring.

**Watch for:** the temptation to gradually turn this into a write target. If you find yourself manually pushing content there regularly, re-evaluate whether it should be Pattern B or C instead.

---

## Pattern E: Return path

**Use when:** something other than you writes in the satellite. An agent with write access, a colleague, a research tool depositing exports, a review queue aimed at you.

**Default behaviour:** a governed ingest, not a sync. One deliberate, logged, refusable operation per run. Material comes back into the central brain carrying provenance frontmatter that records the satellite, the exact source path, the authoring agent or person, and the ingest date.

**Typical scope:** agent proposals awaiting a verdict, research output, intelligence and signals, work product authored in the satellite.

**Watch for:** treating it as bidirectional sync. It is not. The central brain still wins every disagreement; the ingest changes what the central brain knows, not who decides. Also watch for the loop: never discover from the folders you mirror outbound, or you will re-ingest your own material into itself.

Full protocol in [backflow.md](./backflow.md).

---

## The agent-context satellite

Not a sync pattern so much as a different kind of destination: a satellite whose reader is a fleet of agents rather than a person. Tiered by blast radius, fail-closed on access, validated before every push, and never hand-edited. See [agent-context-satellites.md](./agent-context-satellites.md).

Most people will never need this. You need it when agents run somewhere other than your laptop and need to know things about your business without you pasting context each time.

---

## Choosing between patterns

| Question | If yes |
|---|---|
| Does the satellite have the same folder structure as the central vault? | Pattern A |
| Does the satellite have its own structure and a different audience? | Pattern B |
| Is the satellite one step from public, requiring a strip? | Pattern C |
| Is the satellite a shared team surface where your voice should not appear? | Pattern C-strict |
| Should writes always be human-reviewed before landing? | Pattern D |
| Does the satellite need both a strip AND a PR review? | Pattern C, paired with a branch/PR workflow in the satellite repo |
| Does anything other than you write in the satellite? | Add Pattern E on top of whatever else applies |
| Is the reader an agent rather than a person? | Agent-context satellite |

Patterns compose. A satellite can be Pattern C outbound and Pattern E inbound at the same time, and usually is once agents are involved.

A satellite can also graduate. If a Pattern B satellite starts receiving near-public content regularly, add Pattern C rules for that content slice. Update `AGENTS.md` and the satellite's entry-point note.

---

## One publication owner per path

Independent of pattern: if two processes can commit to the same folder in a satellite, you will get duplicate writes and conflicting history, and you will notice weeks later.

Overlapping live write access is fine. Overlapping publication rights are not. Give every versioned path exactly one owner and write it down in the entry-point note.
