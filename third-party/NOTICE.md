# Third-party skill notices

The vendored skill-directory files are preserved without content changes. The source revisions below describe the imported snapshots, not this repository's commit.

## Felix Shi — GitHub Profile Polish

- Repository: https://github.com/shi-felix/skills
- Original path: `github-profile-polish`
- Revision: `d2e4717b7b71d9dff1c2269cc9327bc5acf8ecd9`
- License: MIT, Copyright (c) 2026 Felix Shi
- The complete upstream root license is included at `skills/github-profile-polish/LICENSE`. This is a local addition to the skill folder so a standalone install keeps the copyright and permission notice.

## Jeff Allan — claude-skills

- Skills: `playwright-expert`, `sql-pro`, `typescript-pro`
- Repository: https://github.com/Jeffallan/claude-skills
- Original paths: `skills/playwright-expert`, `skills/sql-pro`, `skills/typescript-pro`
- Revision: `882ef55e377dbf9a4dbe496bb41ac6ccd0e555cf`
- License: MIT, Copyright (c) 2025
- Complete license: [LICENSE-JeffAllan-MIT.txt](LICENSE-JeffAllan-MIT.txt)

Each of these three imported skill folders also contains a local `LICENSE` addition with the same license text. These `LICENSE` files were added during consolidation; they were not present inside the original vendored skill-directory snapshots.

## Vercel — React Best Practices

- Local name: `vercel-react-best-practices`
- Repository: https://github.com/vercel-labs/agent-skills
- Original path: `skills/react-best-practices`
- Revision: `063bee94c3f4df8453406c830b0a7df0f2860278`
- License: MIT, declared in the skill's retained `SKILL.md` frontmatter and the upstream repository README.
- Pinned declaration: https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/README.md#license

All original `SKILL.md`, `AGENTS.md`, metadata and rule files are retained. The pinned repository root has no standalone LICENSE file; this import does not add an invented upstream copyright notice.

Three local Markdown compatibility entries (`async-defer-await.md`, `async-cheap-condition-before-await.md`, `server-hoist-static-io.md`) point to their full `rules/` files. They repair root-relative links in the retained `AGENTS.md` without changing any upstream file.

## Local workflow entry

`workspace-delivery` is the existing locally authored workspace workflow entry. It is copied intact and is not attributed to either upstream project above.

## Import additions

This notice and the MIT license copies are consolidation metadata. Original file hashes and local source locations are recorded only in the ignored local import record, not in this public repository.
