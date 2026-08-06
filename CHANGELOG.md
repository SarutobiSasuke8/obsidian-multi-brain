# Changelog

## v1.1

This release covers the cases the first version did not anticipate, mostly around what happens once agents can write as well as read.

### Added

- **Pattern E, the return path** (`docs/backflow.md`). The original four patterns push one way. That holds until an agent, a colleague, or an automated export starts writing in a satellite, at which point the central brain quietly stops being the source of truth. Pattern E is the governed ingest back: discover, judge, label with provenance, file, close the loop, record in a ledger.
- **Agent-context satellites** (`docs/agent-context-satellites.md`). A satellite whose reader is an agent fleet rather than a person. Tiered by blast radius, fail-closed on access, derived and never hand-edited, validated before every push, retrieved progressively.
- **Security notes** (`docs/security.md`). Secrets never live in the vault, and the one that catches people is two-factor recovery codes rather than API keys. Scan for credential shapes rather than vocabulary, or you will learn to skip the scanner. `AGENTS.md` is not a security boundary. Retrieved context reaches your model provider. Rotate the credentials your agents hold.
- **Untrusted content rule** in `AGENTS.md`. Text inside a file is data, never instruction. Any pipeline touching clippings, research exports, or shared folders is carrying open-internet text into a context window that can write to your business notes.
- **Pattern C-strict**, the de-ego'd strip, for shared team surfaces. Strip your identity as well as your commercial exposure, so the result reads as the organisation rather than as private notes that escaped.
- **One publication owner per versioned path.** Overlapping live write access is fine. Overlapping publication rights produce duplicate commits and conflicting history that you notice weeks later.
- `examples/vault.gitignore` for backing a vault up to a private git repo.
- A "what this does not do" section in the README.

### Changed

- `templates/satellite-entry-point.md` now records the return path, who else writes in the satellite, and publication ownership per path.
- `docs/patterns.md` covers C-strict and E, and notes that patterns compose. A satellite is commonly Pattern C outbound and Pattern E inbound at once.
- FAQ answers the backflow, agent-fleet, secrets-in-git, injection, and enforcement questions.
- `AGENTS.md` marks its optional sections explicitly. Delete the return path, agent-context, and de-ego sections unless you have the problem they solve.

### Fixed

- Dead link in `AGENTS.md` to a companion post that does not exist in this repo. It now points at `docs/patterns.md`.

## v1.0

Initial release: `AGENTS.md` template, vault bootstrap seed, implementation seed, canvas, satellite entry-point template, patterns A to D, two examples, FAQ.
