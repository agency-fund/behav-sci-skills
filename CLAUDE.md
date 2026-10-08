@AGENTS.md

Claude Code specifics: the repo is itself a plugin (`.claude-plugin/`), so `claude plugin validate ./` checks the manifests. Test the plugin locally with `/plugin marketplace add ./` then `/plugin install behav-sci-skills@behav-sci-skills`. The validator warns about this CLAUDE.md being at the plugin root; that is expected.
