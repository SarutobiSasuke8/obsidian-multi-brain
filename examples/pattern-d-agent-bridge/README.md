# Pattern D fixture

This example is a complete, non-private Pattern D bridge. It demonstrates the authority split without relying on a real person's vault, contacts, machine paths, or credentials.

```text
central/
  Public/Product Overview.md                 canonical source
satellite/
  Context/public-safe/product-overview.md    derived, centrally published mirror
  Workspace/research/brief.md                bounded agent-authored work
  CRM/Proposals/contact-update.md             quarantined relationship proposal
satellite-entry-point.md                      authority register
```

The fixture is checked by [`scripts/validate.py`](../../scripts/validate.py). Run it from the repository root:

```bash
python scripts/validate.py
```

The example is intentionally generic. Copy the entry-point template rather than editing this fixture for a live vault.
