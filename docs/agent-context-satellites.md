# Pattern D: mixed-authority agent bridges

Patterns A to C assume that publication is the main job of a satellite. Pattern D exists for a different boundary: the reader and partial author is a fleet of agents.

You build one when you have agents running somewhere other than your laptop, in a chat app, on a server, in a scheduled job, and they need to know things about your business without you pasting context into a prompt every time.

The central brain is still the source of truth. The bridge exposes a **retrieval surface**, one or more bounded **workspaces**, and a quarantined **proposal queue** without handing agents authority over the private vault.

---

## The four properties that make it different

### 1. It is tiered by blast radius, not by topic

Do not organise agent context by subject. Organise it by what happens if the content escapes.

| Tier | Test | Who receives it |
|---|---|---|
| `public-safe` | Would survive being quoted word for word by an agent in a public group chat | Any agent, including externally-facing ones |
| Not exported | Internal business state, credentials, exact financials, health, family, unrestricted contact data | Nothing in the shared bridge. Keep it local or behind a separate brokered lookup. |

The public-safe test is absolute and it is a blast-radius test, not a taste test. Assume the content will be repeated verbatim in the worst possible room. If you hesitate, it is not public-safe.

An agent that talks to strangers gets exactly one tier. Do not build an agent that decides for itself which tier to quote from. If a trusted operator-only agent genuinely needs internal context, give it a separate access boundary rather than co-locating that material in the shared bridge.

### 2. It is fail-closed

Anything that could carry personal or commercial exposure is excluded unless a field explicitly permits it.

For contact or entity records, put an access field on the record itself:

- unset or `none`: never exported. **This is the default.**
- `index`: non-sensitive identity context only
- `contact`: an allowlisted operational card, no note body
- `full`: the whole note

Every permitted record still has to pass the `public-safe` test. `full` means the whole approved public-safe note; it is not a bypass for private contact details. Missing metadata means no export. Not "export cautiously". No export. The moment the rule is "export unless flagged sensitive" you have built a leak with extra steps, because the flag is the thing you forget.

Two consequences people miss:

- **A place in a review queue is not an access grant.** Records queued for classification stay unexported until classified.
- **Retrieved context reaches your model provider.** Anything an agent can pull, it can put in a prompt, and that prompt goes to whoever runs the model. Choose the narrowest tier that does the job.

### 3. Context is derived, never authored

Context files are distilled copies. The rule is uncompromising:

1. Substance is written and edited in the central brain.
2. A distillation pass produces the satellite copy, assigns its tier, and stamps the sync date.
3. A validator checks the pack before anything is pushed.
4. The push refuses if validation fails, and installs read-only at the destination.
5. If context is wrong or stale, **fix the master and re-push.** Hand-editing a satellite copy is a contract violation, and it is the single most common way this system rots.

### 4. Write authority is path-scoped

Pattern D has three physically separate zones:

| Zone | May write | Rule |
|---|---|---|
| `Context/public-safe/` | The central publication process | Agents read derived context. They never edit it in place. |
| `Workspace/<mount>/` | Agents explicitly registered for that mount | Agents may create and update work artefacts without per-note approval, but cannot escape the mount. |
| `CRM/Proposals/` | Registered agents | Agents submit append-only proposals. A separate human or importer validates and applies accepted changes. |

The folder name is not the permission system by itself. Enforce the boundary with filesystem or repository permissions when possible, and keep a machine-readable register of writable mounts and their owners. An unregistered path is fail-closed.

Workspace output is not canonical by default. Bring durable results back through the governed Pattern E process: preserve provenance, refuse residue, compare collisions, and record the decision. Likewise, a CRM proposal is evidence for a possible update, not permission to mutate the relationship record.

---

## Frontmatter contracts

### Published context

Every context file carries:

```yaml
type: agent-context
tier: public-safe
master: "path/to/source/note.md"   # plain path, not a wikilink
sync: push
last_synced: YYYY-MM-DD
mutability: mirror
```

Use a plain path for `master`, not a wikilink. Wikilinks in a satellite cannot resolve into the central vault, so the pointer breaks the moment someone clicks it.

Anything describing current state should also carry:

```yaml
review_after: YYYY-MM-DD
valid_until: YYYY-MM-DD    # when the claim must expire
```

Context without an expiry date becomes a confidently wrong agent about four months later. That is worse than an agent with no context, because you stop checking it.

### Authorised workspace artefacts

Every workspace artefact identifies its mount and authoring authority:

```yaml
type: agent-workspace
workspace_scope: research
authority: agent-example
created: YYYY-MM-DD
mutability: living
```

The entry-point note maps `workspace_scope` to a concrete `Workspace/<mount>/` path and names the agents allowed to write there. Unknown scope or authority means quarantine, not best-effort filing.

### CRM proposals

CRM proposals are append-only and cannot be mistaken for canonical records:

```yaml
type: crm-proposal
status: proposed
source_agent: agent-example
canonical_target: "People/example-contact.md"
created: YYYY-MM-DD
mutability: append-only
```

An importer may add review metadata, but only an explicit acceptance step may update `canonical_target`. Rejected proposals remain auditable or are archived according to the bridge's retention policy; agents never rewrite history to make a rejected proposal disappear.

---

## Validate before you push

The validator is the thing that makes this safe to automate. It should check:

- required frontmatter is present and well formed
- the file sits in the tier folder its `tier` field claims
- the master note actually exists at the recorded path
- review and expiry dates have not passed
- file hashes match, so a hand-edited satellite copy is detected
- the total bundle is within a sane size
- every `Workspace/` file names a registered scope and authority
- every CRM item is a `status: proposed`, append-only record under `CRM/Proposals/`
- files do not contain private machine paths, unresolved unsafe placeholders, or credential-shaped values

The push refuses on any failure. A validator you can override by habit is a validator you do not have.

---

## Progressive retrieval

The satellite is a retrieval surface, not one large prompt. Layer it:

1. a small identity and authority core, always loaded
2. current goals and priorities, when relevant
3. the specific venture or domain pack the task needs
4. one approved entity or contact record
5. a governed workspace artefact or handoff

Never load an entity-scale dataset into default context. A CRM is a thing you query through an access-controlled interface, not a thing you paste. Pattern D's proposal queue is a write quarantine, not a bulk read grant.

---

## Refresh cadence

Re-distil when a master note materially changes, or monthly, whichever comes first. Review `last_synced` drift as part of your vault review: context older than about six weeks gets refreshed or deliberately retired.

Retiring stale context is a real option and often the correct one. A missing pack makes an agent ask. A stale pack makes it assert.

---

## One publication owner per path

If more than one process can commit to the same folder in the satellite, you will get duplicate writes and conflicting history, and you will find out weeks later.

Give every versioned path exactly one publication owner. Overlapping live write access is fine. Overlapping publication rights are not.

---

## What never goes in, at any tier

- credentials, tokens, keys, recovery codes
- exact financial internals: revenue, valuation, runway, deal terms
- named counterparties, pipeline records, pricing history
- journal, health, family, and personal-relationship material
- meeting records
- unverified claims presented as fact

The last one matters more than it looks. An agent will repeat a speculative claim from your notes with total confidence, and it will do so to a customer.
