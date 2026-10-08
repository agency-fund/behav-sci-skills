---
status: accepted
date: 2026-10-08
---
# One validator, in Python, bundled unchanged into the meta-skills and the upload endpoint

Authors check a skill locally inside `besci-skill-creator`, CI checks it on the pull request, and the site's upload function checks it before opening a pull request. Three implementations of the same rules would drift and authors would pass locally and fail on upload.

`scripts/besci_validate.py` is the single implementation. It depends only on PyYAML, runs on Python 3.8 and later, and is copied byte-for-byte into `skills/besci-skill-creator/scripts/` and `skills/besci-eval/scripts/`; `scripts/check_sync.py` fails CI if a copy drifts. Python was chosen over Node because it runs in claude.ai's sandbox, in Claude Code, in GitHub Actions, and in a Vercel function, and because TAF and IL scientists can read it. The whole toolchain (site builder, packager, snapshot) is Python for the same reason, with a little browser JavaScript on the site.
