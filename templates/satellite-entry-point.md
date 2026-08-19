---
title: "[Brand Name] Satellite Vault Sync"
type: satellite-entry-point
brand: "[Brand Name]"
satellite-root: "[absolute path to the satellite vault or repo]"
pattern: "[A / B / C / D]"
authority-model: "[single-owner / mixed-authority]"
mutability: living
created: YYYY-MM-DD
---

# [Brand Name] Satellite Vault Sync

This is the entry-point note for the [Brand Name] satellite. It documents how the central vault syncs into `[satellite root]` and what rules apply.

Reference this note in `AGENTS.md` under the registered satellites table.

---

## Satellite details

| Field | Value |
|---|---|
| Satellite root | `[absolute path]` |
| Sync pattern (outbound) | [A / B / C / C-strict / D] |
| Return path (inbound) | [none / Pattern E] |
| Audience | [internal / team / partner-facing / public-facing / agent fleet] |
| Folder shape | [mirrors central vault / has own structure] |
| Who else writes here | [nobody / named agents / named people / automated exports] |
| Publication owner per path | [one owner per versioned path; list them] |

---

## Mirror scope

What auto-mirrors from the central vault into this satellite:

- [Content type] to `[destination folder in satellite]`
- [Content type] to `[destination folder in satellite]`
- [Add rows as needed]

---

## Exclusions for this satellite

What never auto-mirrors here. Review and ask before mirroring:

- [Excluded content type or folder]
- [Excluded content type or folder]

---

## Stripping pass (Pattern C only)

*Delete this section if not using Pattern C.*

**Remove on the way out:**

- [What gets stripped for this specific satellite]
- [e.g., customer and lead names]
- [e.g., revenue, pricing, deal size]
- [e.g., competitive analysis]
- [e.g., meeting attendees and internal dates]
- [e.g., internal wikilinks to non-public notes]
- [e.g., internal frontmatter fields]

**Preserve:**

- The public claim, voice, and structure
- [Satellite-specific frontmatter fields to carry across]
- Public citations

**Safety valve:** if a note cannot be cleanly stripped without gutting it, do not mirror. Flag for deliberate authoring in the satellite instead.

---

## Folder map

How this brand's main-vault folders map to satellite folders:

| Central vault path | Satellite path |
|---|---|
| `Business/[Brand]/[Folder]/` | `[satellite folder]` |
| [Add rows as needed] | |

---

## Authority zones (Pattern D only)

*Delete this section if not using Pattern D.*

| Zone | Path | Publication or write owner | Allowed flow |
|---|---|---|---|
| Curated context | `Context/public-safe/` | [central publication process] | Derived mirrors flow out; agents read only |
| Agent workspace | `Workspace/[mount]/` | [registered agent or process] | Work artefacts may be authored here; accepted results use Pattern E |
| CRM quarantine | `CRM/Proposals/` | [agents propose; reviewer or importer decides] | Append-only proposals; never direct canonical CRM writes |

### Workspace mount register

| Mount | Purpose | Allowed authorities | Retention / return path |
|---|---|---|---|
| `Workspace/[mount]/` | [bounded work purpose] | [agent ids or process ids] | [retention rule and Pattern E destination] |

Missing mount or authority registration means no write. Context is `public-safe` only; internal context belongs behind a separate access boundary.

### CRM proposal gate

- Required proposal fields: `type: crm-proposal`, `status: proposed`, `source_agent`, `canonical_target`, `created`, `mutability: append-only`.
- Reviewer or importer: [human or process that may accept a proposal].
- Canonical CRM boundary: [path or system that agents cannot write directly].
- Rejected proposal retention: [archive or retention rule].

---

## Return path (Pattern E only)

*Delete this section if nothing other than you writes in this satellite.*

| Field | Value |
|---|---|
| Writable folders to sweep | `[paths]` |
| Folders never swept | `[the outbound mirror paths, so the ingest cannot loop]` |
| Authors and their folders | `[folder]` owned by `[agent or person id]` |
| Ingest ledger | `[path to the ledger note]` |
| Quarantine destination | `[path for ambiguous items]` |

Judge test for this satellite: would a future decision go differently because this exists in the central vault? If no, refuse as residue.

Provenance stamped on every ingested file:

```yaml
source_vault: [this satellite]
source_path: "[exact relative path]"
source_agent: [resolved author]
ingested: YYYY-MM-DD
ingested_by: [ingesting agent]
```

---

## Notes and quirks

[Document any slug conventions, naming differences, or one-off rules for this satellite that the agent needs to know.]

---

## Related

- `AGENTS.md` — operating contract (registered satellites table)
- [[Multi-Brain Management System]] — the human-readable map of the full system
- `docs/patterns.md` — what each pattern means
- `docs/backflow.md` — the return path protocol, if this satellite uses one
