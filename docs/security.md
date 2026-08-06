# Security notes

This system gives an agent read and write access to everything you know, and then routes some of it towards public surfaces. That is the whole point, and it is also the whole risk. These are the rules worth having before you need them.

None of this is theoretical. These are the failure modes that show up repeatedly in systems shaped like this one.

---

## Secrets never live in the vault

The FAQ tells you to put your vault in a git repo. Do that. But understand what you have just built: an append-only, replicated, permanent history of every file, on a server you do not own.

Before the first commit, and periodically after it, confirm the vault contains none of the following:

- API keys, tokens, and connection strings
- passwords, even "temporary" ones
- **two-factor recovery codes.** These end up in notes constantly. Someone sets up an account, pastes the ten backup codes into a note "for now", and forgets. They are then in git history forever.
- private keys, seed phrases, wallet exports
- `.env` files copied in for reference

Put them in a password manager. Reference the manager in the note, not the value.

**Git history is not a place you can clean up casually.** If a secret has been committed, the credential is compromised. Rotate it. Rewriting history does not un-publish something that was pushed, and does not help at all if the repo was ever public or cloned.

If you find one: rotate first, clean history second, and treat the cleanup as optional.

---

## Scan for credential shapes, not vocabulary

If you automate a secret scan before commits or pushes, match on the shape of a credential: the entropy, the length, the known prefixes providers use.

Do not match on bare vocabulary. A scanner that trips on the word `token:` will fire on every note you have ever written about tokens, you will start passing `--no-verify` out of habit within a week, and then the scanner is worse than nothing because you believe it is running.

Keep repository-side scanning on as an independent second line. Two checks that fail differently beat one check you have learned to skip.

---

## The agent is not the security boundary

Do not rely on the agent choosing correctly about sensitive material. Instructions in `AGENTS.md` are a strong default, not an enforcement mechanism, and the failure is silent.

Where it actually matters, enforce mechanically:

- a validator that refuses the push, rather than a rule asking the agent to check
- fail-closed metadata on records, so absence of a flag means exclusion
- read-only installation at the destination
- a destination path allowlist in the sync script itself, so a wrong argument cannot write outside it
- one publication owner per versioned path

Written rules handle the ninety-nine percent. Mechanical gates handle the one percent that costs you.

---

## Treat all satellite and imported content as untrusted

Anything your agent reads that you did not write is data, not instruction. Clippings, research exports, shared team folders, email pulls, anything an agent authored, anything scraped.

If a file contains text addressed to the agent, telling it to file somewhere unusual, skip a check, fetch a URL, or claiming you already authorised something, the correct behaviour is: quote it to the operator, execute nothing.

Put this rule in your `AGENTS.md` explicitly. By the second hop, a research pipeline is carrying text from the open internet straight into a context window that has write access to your business notes.

---

## Model providers see retrieved context

Anything an agent can retrieve, it can put in a prompt, and that prompt goes to whoever runs the model. If you use a hosted model, retrieved contact details, client names, and strategy notes leave your machine.

This is a trade-off, not a blocker. Make it deliberately:

- choose the narrowest access tier that lets the task succeed
- keep the categories you would not send off the retrieval surface entirely
- know which provider is behind each agent, and note it where the access rule is written

Write the decision down where the access rule lives, so future-you knows it was a decision rather than an oversight.

---

## Rotate the credentials your agents hold

Every agent, broker, and sync job you stand up gets a credential. They accumulate, they outlive the thing they were made for, and nobody enumerates them.

Keep a list of every credential issued to an automated process, with the date and the scope. Rotate on a schedule. Revoke when you retire the process rather than "later". Anything you cannot name the owner of should be revoked now and re-issued if something breaks.

---

## The public-safe test is a blast-radius test

Before any content reaches a surface an outside party can see, apply one test: **would this survive being quoted word for word, out of context, in the worst room it could reach?**

Not "is this roughly fine". Not "is this technically already public". Assume verbatim quotation by an agent that does not understand nuance, in front of someone with an incentive to read it badly.

If you hesitate, it is not public-safe. Hesitation is the answer.

---

## A short checklist before you make anything public

- [ ] No credentials, keys, or recovery codes in the working tree
- [ ] No credentials anywhere in git history, or the exposed ones are rotated
- [ ] No live customer, lead, or partner names
- [ ] No revenue, pricing, runway, or pipeline figures
- [ ] No meeting attendees or internal dates
- [ ] No personal contact details for anyone but you
- [ ] Internal wikilinks removed, not just left dangling
- [ ] Internal frontmatter fields stripped: owners, reviewers, routing, mutability
- [ ] Filenames and folder names checked too. A path can leak a client name on its own
- [ ] Images and attachments checked. A screenshot leaks whatever was on screen
- [ ] If the repo was ever public, treat everything in its history as published
