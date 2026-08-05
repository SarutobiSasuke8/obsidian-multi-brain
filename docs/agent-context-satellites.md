# Agent-context satellites

Patterns A to D assume a human opens the satellite. A fifth kind of satellite exists and it behaves differently enough to need its own rules: a satellite whose reader is a fleet of agents.

You build one when you have agents running somewhere other than your laptop, in a chat app, on a server, in a scheduled job, and they need to know things about your business without you pasting context into a prompt every time.

The central brain is still the source of truth. The agent-context satellite is a **retrieval surface** built from it.

---

## The three properties that make it different

### 1. It is tiered by blast radius, not by topic

Do not organise agent context by subject. Organise it by what happens if the content escapes.

| Tier | Test | Who receives it |
|---|---|---|
| `public-safe` | Would survive being quoted word for word by an agent in a public group chat | Any agent, including externally-facing ones |
| `internal` | Operator-only. Business state, priorities, constraints | Agents that only ever talk to you |
| Not exported | Credentials, exact financials, health, family, unrestricted contact data | Nothing. These stay behind a brokered lookup or stay out entirely |

The public-safe test is absolute and it is a blast-radius test, not a taste test. Assume the content will be repeated verbatim in the worst possible room. If you hesitate, it is not public-safe.

An agent that talks to strangers gets exactly one tier. Do not build an agent that decides for itself which tier to quote from.

### 2. It is fail-closed

Anything that could carry personal or commercial exposure is excluded unless a field explicitly permits it.

For contact or entity records, put an access field on the record itself:

- unset or `none`: never exported. **This is the default.**
- `index`: non-sensitive identity context only
- `contact`: an allowlisted operational card, no note body
- `full`: the whole note

Missing metadata means no export. Not "export cautiously". No export. The moment the rule is "export unless flagged sensitive" you have built a leak with extra steps, because the flag is the thing you forget.

Two consequences people miss:

- **A place in a review queue is not an access grant.** Records queued for classification stay unexported until classified.
- **Retrieved context reaches your model provider.** Anything an agent can pull, it can put in a prompt, and that prompt goes to whoever runs the model. Choose the narrowest tier that does the job.

### 3. It is derived, never authored

Context files are distilled copies. The rule is uncompromising:

1. Substance is written and edited in the central brain.
2. A distillation pass produces the satellite copy, assigns its tier, and stamps the sync date.
3. A validator checks the pack before anything is pushed.
4. The push refuses if validation fails, and installs read-only at the destination.
5. If context is wrong or stale, **fix the master and re-push.** Hand-editing a satellite copy is a contract violation, and it is the single most common way this system rots.

---

## Frontmatter contract

Every context file carries:

```yaml
type: agent-context
tier: public-safe        # or internal
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

---

## Validate before you push

The validator is the thing that makes this safe to automate. It should check:

- required frontmatter is present and well formed
- the file sits in the tier folder its `tier` field claims
- the master note actually exists at the recorded path
- review and expiry dates have not passed
- file hashes match, so a hand-edited satellite copy is detected
- the total bundle is within a sane size

The push refuses on any failure. A validator you can override by habit is a validator you do not have.

---

## Progressive retrieval

The satellite is a retrieval surface, not one large prompt. Layer it:

1. a small identity and authority core, always loaded
2. current goals and priorities, when relevant
3. the specific venture or domain pack the task needs
4. one approved entity or contact record
5. a governed workspace artefact or handoff

Never load an entity-scale dataset into default context. A CRM is a thing you query, not a thing you paste.

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
