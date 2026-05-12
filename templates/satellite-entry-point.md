---
title: "[Brand Name] Satellite Vault Sync"
type: satellite-entry-point
brand: "[Brand Name]"
satellite-root: "[absolute path to the satellite vault or repo]"
pattern: "[A / B / C / D]"
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
| Sync pattern | [A / B / C / D] |
| Audience | [internal / partner-facing / public-facing] |
| Folder shape | [mirrors central vault / has own structure] |

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

## Notes and quirks

[Document any slug conventions, naming differences, or one-off rules for this satellite that the agent needs to know.]

---

## Related

- `AGENTS.md` — operating contract (registered satellites table)
- [[Multi-Brain Management System]] — the human-readable map of the full system
