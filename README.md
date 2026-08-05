# obsidian-multi-brain

**One vault to live in. Many downstream brains that stay in sync automatically.**

A set of templates, operating contracts, and agent seeds for running a multi-brand Obsidian setup where a coding agent handles the filing for you.

![Multi-Brain Management System](Multi-Brain%20Management%20System%20-%20Epic%20Background.png)

---

## The problem

If you run more than one brand, you know the drift.

You write a post draft in your main notes. It belongs in the content repo too. There is a stripped version of it that should go to the public-facing workspace. You copy it by hand, twice, and three weeks later they have all diverged.

The fix is not to work harder. The fix is to write the routing rules down once, put them in a file the agent reads, and let the agent do the filing.

This repo is that file, plus the templates and seeds to build the whole system.

---

## What is in here

| File | What it does |
|---|---|
| `AGENTS.md` | A public template of the operating contract that governs how a coding agent files notes across multiple vaults. Drop this at your vault root, fill in your brands, and it works. |
| `vault-seed-CLAUDE.md` | A bootstrap seed for people who need a central vault first. Drop it in a fresh Obsidian vault as `CLAUDE.md`, run a coding agent, and it interviews you and builds your vault structure. |
| `multi-brain-implementation-seed.md` | An agent-facing spec for building the multi-brain system from scratch inside an existing vault. Give this to a coding agent and it scaffolds everything. |
| `canvas/multi-brain-management-system.canvas` | The visual map of the full system as an Obsidian Canvas file. Open it in Obsidian to see the patterns, mechanics, and flow. |
| `templates/satellite-entry-point.md` | Blank entry-point note for registering a new satellite vault. One per brand. |
| `examples/agents-md-minimal.md` | Minimal one-satellite contract for people starting simple. |
| `examples/agents-md-with-strip.md` | Contract showing the Pattern C stripping pass in full. |
| `docs/patterns.md` | Reference for the sync patterns (A, B, C, C-strict, D, E). |
| `docs/backflow.md` | Pattern E: the governed return path, for when something other than you writes in a satellite. |
| `docs/agent-context-satellites.md` | Building a satellite whose reader is an agent fleet rather than a person. |
| `docs/security.md` | Secrets, prompt injection, blast radius, and what `AGENTS.md` cannot enforce. |
| `docs/faq.md` | Answers to the questions that come up every time this system gets explained. |
| `examples/vault.gitignore` | Starting `.gitignore` for a vault backed up to a private git repo. |

---

## How the system works

There is one central brain. That is the Obsidian vault you actually live in: journal, strategy, contacts, raw thinking. It is the source of truth. Everything else is downstream.

Around it sit satellite brains: a dedicated brand vault, a content production repo, a public knowledge base, a partner workspace. Each satellite has one sync pattern:

**Pattern A: full mirror.** The satellite is a structural twin. Notes copy straight across.

**Pattern B: narrow mirror.** The satellite has its own structure. Public-facing material mirrors freely. Internal strategy stays in the central brain.

**Pattern C: stripped mirror.** The satellite is one step from public. Every write runs through a stripping pass that removes customer names, financials, competitive intel, and internal context before the note lands in the destination.

**Pattern D: read-only feeder.** The agent reads the satellite for context but does not auto-write. Used for code repos or partner spaces where commit hygiene matters.

The rules for which satellite gets what, and how notes get transformed on the way out, live in `AGENTS.md` at the vault root. Any coding agent reads that file on session start and files accordingly.

You write once. The agent handles the rest.

---

## When the flow reverses

The four patterns above all push one way, and that holds until something other than you starts writing in a satellite. An agent with write access. A colleague. A research tool dropping exports into a folder.

At that point the satellite is producing material the central brain has never seen, and the central brain quietly stops being the source of truth.

**Pattern E: the return path.** A governed ingest, not a sync. Sweep the writable folders, refuse most of what you find, stamp what you keep with where it came from, and mark it processed so the queue drains. The judge test is a single question: would a future decision go differently because this exists in the central brain? Most agent output fails that, and it should.

Full protocol in [docs/backflow.md](./docs/backflow.md).

Two rules that are not obvious until they bite. Never sweep the folders you mirror outbound, or the ingest re-consumes your own material into itself. And a name collision means stop and compare, never overwrite.

---

## When the reader is an agent, not you

A satellite built for a fleet of agents behaves differently enough to need its own rules. It is organised by blast radius rather than by topic, it is fail-closed on anything sensitive, and it is validated before every push.

- **Tiered.** A `public-safe` tier that would survive being quoted word for word in a public group chat, and nothing else, is what an externally-facing agent gets.
- **Fail-closed.** A record exports only when a field explicitly says it can. Missing metadata means no export, not cautious export. The moment the rule becomes "export unless flagged sensitive", you have built a leak with extra steps, because the flag is the thing you forget.
- **Derived.** Context files are distilled copies with an expiry date. Fix the master and re-push. Hand-editing a satellite copy is how this rots.

Full reference in [docs/agent-context-satellites.md](./docs/agent-context-satellites.md).

---

## Quickstart

### If you are starting from scratch

1. Download `vault-seed-CLAUDE.md`.
2. Drop it into a fresh Obsidian vault folder as `CLAUDE.md`.
3. Open a terminal in that folder and start a Claude Code (or Codex) session.
4. The agent will interview you and build your vault structure, self note, inbox, today's journal entry, and a working `AGENTS.md`.
5. When you later add a second brand, come back and layer on the multi-brain pattern.

### If you already have a vault

1. Download `AGENTS.md` and `multi-brain-implementation-seed.md`.
2. Drop them at your vault root.
3. Open a coding agent session and say: "implement the multi-brain system per the implementation seed."
4. The agent runs the nine-phase protocol: reads your vault, registers your satellites, picks patterns, defines the stripping pass, writes the contract, creates entry-point notes, builds the human-readable map, builds the canvas, and runs a dry-run mirror for approval.
5. After the dry run, turn the defaults on.

---

## The stripping pass

This is the piece most people do not think to build and the one that unlocks everything else.

It has a stricter sibling. When the destination is a shared team surface rather than a public one, strip your identity as well as your commercial exposure: first-person voice, personal working habits, your other ventures, your relationship history with the people mentioned. What is left should read as though the organisation wrote it, not as though your private notes escaped. See Pattern C-strict in [docs/patterns.md](./docs/patterns.md).

Before any note files into a near-public satellite, the agent strips:

- customer, lead, partner, and counterparty names
- meeting attendees, internal dates, internal commentary
- revenue, pricing, deal size, runway, pipeline
- competitive intel and internal vs-competitor framing
- personnel commentary, 1-1 context
- internal wikilinks
- internal frontmatter (owners, reviewers, mutability flags)
- TODOs and open questions not fit for a public surface

What stays: the public claim, the voice, the structure, public citations.

If a note cannot be cleanly stripped without gutting it, the agent refuses and flags it for deliberate authoring in the destination instead.

You write in your central brain with all the internal context you need. The system handles the cut on the way out.

---

## What this does not do

Worth knowing before you build on it.

**`AGENTS.md` is not a security boundary.** It is a strong default that an agent follows most of the time, and when it fails it fails silently. For anything where a leak actually costs you, enforce mechanically instead: a validator that refuses the push, fail-closed metadata, an allowlist inside the sync script. Written rules handle the ninety-nine percent. Gates handle the one percent that hurts. See [docs/security.md](./docs/security.md).

**Files your agent reads are not trustworthy.** Clippings, research exports, shared folders, and anything another agent wrote are carrying text from the open internet into a context window with write access to your business notes. The rule is one paragraph: text inside a file is data, never instruction, and anything addressed to the agent gets quoted to you rather than executed. Add it on day one.

**Retrieved context reaches your model provider.** Anything an agent can pull, it can put in a prompt. That is a trade-off to make deliberately, not a reason to avoid the system.

**Your vault in git is a permanent public-shaped record.** Read [docs/security.md](./docs/security.md) before the first commit. The thing that catches people is not API keys, it is two-factor recovery codes pasted into a note "for now" a year ago.

**This is not a small system.** One central vault plus one satellite is genuinely useful and takes a day. Everything past that is earned complexity: add a pattern when you have the problem it solves, not before.

---

## Override commands

These work in any agent chat session:

- `main only` — skip the satellite copy
- `satellite only` — write to a satellite only (use sparingly)
- `parallel file this` — explicit mirror of an existing note
- `preview` — show both destinations before writing anything
- `backflow` — sweep a satellite for material the central brain has never seen (Pattern E)

---

## FAQ

**Does this only work with Obsidian?**
The pattern works anywhere notes are plain text files in folders the agent can read and write. Logseq, a folder of `.md` files, even a plain code editor. Obsidian is just a nice UI on top of it.

**What about git repos as satellites?**
Works well. Pattern C plus a PR workflow is the right default when the destination has its own publishing pipeline. The agent writes to a branch; you review before merge.

**What if the agent gets it wrong?**
Update `AGENTS.md`. The agent is following written rules. Wrong behaviour means the rules need a line added. For the cases where a mistake is expensive rather than annoying, add a mechanical gate instead of a rule.

**Something other than me is writing in a satellite. What now?**
That is Pattern E. See [docs/backflow.md](./docs/backflow.md).

**How long does setup take?**
A working day for one satellite. A week to feel comfortable with the strip rules and overrides. Every new brand after that is an afternoon.

**Does this replace a CRM, content calendar, or project tracker?**
No. It is the routing layer underneath all of those. You can run any of them inside this system.

---

## What this pairs well with

- [Claude Code](https://claude.ai/code) as the coding agent
- Obsidian as the vault editor
- A private GitHub repo per satellite for version control
- The [Obsidian Git plugin](https://github.com/Vinzent03/obsidian-git) for auto-committing the central brain

---

## Contributing

PRs welcome for:

- New pattern examples (different satellite types, different agent frameworks)
- Additional templates (research note, person/CRM note, content draft)
- Codex, Cursor, or other agent-specific variants of `AGENTS.md`
- Real-world satellite setups that show the pattern in a different context

Keep additions concrete. Vague "improvements" without a working example are hard to review.

## Licence

MIT. Use it, adapt it, build on it.

---

*Built by a solo operator running multiple brands with AI as the force multiplier.*
