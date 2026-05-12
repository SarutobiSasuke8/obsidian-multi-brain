# FAQ

**What if I only have one brand?**
You do not need the multi-brain pattern yet. Use `vault-seed-CLAUDE.md` to bootstrap a solid central vault. When a second brand enters the picture, layer on the parallel-filing system. The two are designed to stack.

**Does this only work with Obsidian?**
The pattern works anywhere notes are plain text files in folders the agent can read and write. Logseq, a folder of `.md` files in VS Code, a plain filesystem. Obsidian is a nice editor on top, not a requirement.

**Does this work with Notion, Roam, or other tools?**
Not directly. Those tools store data in proprietary formats or databases the agent cannot read or write as plain files. The system depends on notes being files you own. If you want to migrate, the pattern works well as a migration target.

**What about images, PDFs, and other attachments?**
Same rules as notes. The agent copies them into the satellite when the note that references them is mirrored. For Pattern C, if an attachment embeds sensitive information (a screenshot of a CRM, a revenue chart) the note referencing it gets the strip treatment and the attachment is dropped from the mirror.

**What if the satellite is a git repo with branches and pull request review?**
Pattern C plus a PR workflow is the right default when the destination has its own publishing pipeline. The agent writes to a feature branch, opens a PR, and the human reviews before merge. You still get the leverage; you keep the gate.

**How do I stop the same note drifting in two places?**
The central vault wins, always. If you edit a satellite copy by hand, the next mirror overwrites it. The rule must be uncompromising or the system rots. If a satellite genuinely needs to author a note directly and that note should not be overwritten, mark it explicitly in the satellite's entry-point note as "satellite-authored, do not overwrite."

**What if the coding agent gets it wrong?**
Update `AGENTS.md`. The agent follows written rules. Wrong behaviour means the rules need a line added. Treat the first two weeks as calibration time: every time the agent does something you did not want, update the contract so it does not happen again.

**How long does setup take?**
A working day for the first satellite. A week to feel comfortable with the strip rules and override commands. Every new brand after that is an afternoon: one config row, one entry-point note, one dry run.

**Is this a CRM, content calendar, or project tracker?**
No. It is the routing layer underneath those. You can run any of them inside this system. The multi-brain pattern is about where notes live, not what they contain.

**What about backups?**
Treat the central vault and every satellite that matters as a git repo. Obsidian vaults are just folders of text files: `git init`, add a `.gitignore` for large attachments, and push to a private GitHub repo. You are treating your notes like code because the system is code-adjacent.

**Can I have more than three satellites?**
Yes. The system scales linearly: one row in the register per satellite, one entry-point note per brand. There is no hard limit. At some point the agent's per-session context will be a practical ceiling but that is a hardware problem, not a design problem.

**What if I want a satellite to be the source of truth for a specific note?**
That is a deliberate, separate decision. Mark the note `satellite only` in the entry-point rules for that satellite. The agent will not overwrite it from the central vault. Use this sparingly: it is an exception to the operating model, and exceptions accumulate.
