# Inbox: upload a skill without git

This folder is for `.skill` files (a zip of your skill folder, the same thing besci-skill-creator or Claude's export gives you). A bot turns anything dropped here into a proper `skills/<name>/` folder on your pull request.

## How to use it, from the GitHub website

1. Open this folder on GitHub: `inbox/`.
2. Click **Add file** (top right) then **Upload files**.
3. Drag your `.skill` file in (or click "choose your files").
4. In the box at the bottom, type a short message such as `Add decompose-comb-barriers`.
5. Choose **Create a new branch for this commit and start a pull request**. Keep the suggested branch name.
6. Click **Propose changes**, then **Create pull request** on the next page. The pull request template has a checklist; tick what applies.

That is all. You need a GitHub account with write access to this repository (TAF and IL staff in Phase 1). No git, no terminal.

## What the bot does

Within a minute or two of your pull request opening, the inbox workflow:

- unpacks the archive into `skills/<name>/` (the folder name comes from inside the zip),
- deletes the `.skill` file from `inbox/`,
- commits both changes to your pull request branch,
- runs the structure validator and posts a plain-language report as a comment.

If the report lists problems, fix them (re-run besci-skill-creator or edit the files), re-zip the folder, and upload the new `.skill` into `inbox/` **on the same branch** (open your pull request, click the branch name, navigate to `inbox/`, upload again). The bot replaces the folder and re-checks.

## Rules the bot enforces

- Exactly one top-level folder in the zip, containing `SKILL.md`. Zip the folder, not its contents.
- No files other than markdown, text, JSON, YAML, CSV, Python, R, shell, HTML, CSS, JS, and small images.
- 10 MB per archive, 200 files.
- Everything in `docs/skill-spec.md`: frontmatter fields, the eight sections, three evals, a changelog entry.

`__MACOSX` folders and `.DS_Store` files that macOS adds are ignored.

## If this is not for you

- Comfortable with git? Clone, add `skills/<name>/`, run `uv run scripts/besci_validate.py`, open a pull request.
- Not on GitHub at all? Send the `.skill` file to a maintainer in `MAINTAINERS.md` and they will upload it here with you credited.
- Have the contributor key? Use the upload form on the website; it opens the pull request for you.
