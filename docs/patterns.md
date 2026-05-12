# The four sync patterns

A quick reference for picking the right pattern when registering a new satellite.

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

---

## Pattern D: Read-only feeder

**Use when:** the satellite needs context from the central vault but should never receive automated writes. A code repo, a partner-controlled space, a research vault for a specialist domain, anywhere commit hygiene or access control matters more than note flow.

**Default behaviour:** the agent reads the satellite for grounding but does not write. Any proposed changes are captured back into the central vault first, then offered for explicit push.

**Typical scope:** context reads only. No auto-mirroring.

**Watch for:** the temptation to gradually turn this into a write target. If you find yourself manually pushing content there regularly, re-evaluate whether it should be Pattern B or C instead.

---

## Choosing between patterns

| Question | If yes |
|---|---|
| Does the satellite have the same folder structure as the central vault? | Pattern A |
| Does the satellite have its own structure and a different audience? | Pattern B |
| Is the satellite one step from public, requiring a strip? | Pattern C |
| Should writes always be human-reviewed before landing? | Pattern D |
| Does the satellite need both a strip AND a PR review? | Pattern C, paired with a branch/PR workflow in the satellite repo |

A satellite can graduate from one pattern to another. If a Pattern B satellite starts receiving near-public content regularly, add Pattern C rules for that content slice. Update `AGENTS.md` and the satellite's entry-point note.
