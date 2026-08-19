---
title: "Example Studio Agent Bridge"
type: satellite-entry-point
brand: "Example Studio"
satellite-root: "./satellite"
pattern: "D"
authority-model: "mixed-authority"
mutability: living
created: 2026-08-19
---

# Example Studio Agent Bridge

This entry point registers a generic bridge for demonstration. The central fixture is canonical; the satellite has three zones with separate authority.

## Authority zones

| Zone | Path | Owner | Rule |
|---|---|---|---|
| Curated context | `Context/public-safe/` | `central-publisher` | Derived mirrors only; agents read |
| Research workspace | `Workspace/research/` | `agent-example` | Bounded research artefacts; accepted results use Pattern E |
| CRM quarantine | `CRM/Proposals/` | `agent-example` proposes; `crm-importer` decides | Append-only proposals; no direct CRM writes |

Missing path or authority registration means no write. No internal context is published into this shared bridge.

## Flow

- [`central/Public/Product Overview.md`](./central/Public/Product%20Overview.md) is the source for [`satellite/Context/public-safe/product-overview.md`](./satellite/Context/public-safe/product-overview.md).
- [`satellite/Workspace/research/brief.md`](./satellite/Workspace/research/brief.md) is agent-authored and remains non-canonical until reviewed through Pattern E.
- [`satellite/CRM/Proposals/contact-update.md`](./satellite/CRM/Proposals/contact-update.md) is a proposal, not a canonical relationship record.

See [the Pattern D reference](../../docs/agent-context-satellites.md) for the full contract.
