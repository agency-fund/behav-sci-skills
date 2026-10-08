# Disclosure: what happens to your data, and ours

This library is a set of open-source text files. Using them inside a commercial AI product is a different matter, and the partnership behind the library wants both users and contributors to understand that distinction before they rely on it.

## For users

**A skill runs inside whatever AI product you load it into.** When you use a skill in Claude, ChatGPT, Codex, or any other assistant, everything you type in that conversation, including documents you upload and details about your program, participants, and organization, is sent to that product's provider under that provider's terms. The skill does not change those terms, and the library's maintainers never see your conversations.

**Do not paste sensitive data without checking the terms.** Personal data about participants, unpublished results, proprietary program designs, and anything covered by a data-protection agreement should not go into an AI product unless you have confirmed what the provider does with it: whether it is retained, used for training, or shared. Many providers offer plans with stronger guarantees; your organization may already have one. If in doubt, anonymize or summarize before you paste.

**You can use the library without an AI product.** Every skill is written so a person can read the procedure, follow it by hand, and keep their own notes. If your organization is not comfortable transferring work into an AI system, read the skills as a methods manual, practice the method with the AI on non-sensitive examples, and then apply the procedure in your own workflow.

**Skills do not replace specialists.** Each skill says where it stops and a specialist starts. Please read that section before acting on an output in a high-stakes setting.

## For contributors

**Your skill will be processed by third-party AI systems.** When someone uses your published skill, its full text is sent to that person's AI provider as part of their conversation. That is the mechanism by which a skill works. If you include knowledge you consider proprietary, or methods you would otherwise share only under contract, understand that publishing it here places it in that flow.

**You choose what to include.** The partnership's principle is that contributors set their own terms: you decide what goes in, you can revise it, and you can deprecate your own skill at any time through a pull request. Your authorship is recorded in the skill's metadata and changelog.

**Attribution travels with the content.** Skill content is CC BY 4.0, so anyone reusing it must credit you. Nothing here stops a frontier model provider from processing the content when a user loads it, and nothing here stops them from using such conversations according to their own terms with that user.

**The repository is public.** Pull requests, issues, and review comments are visible to anyone.

## For both

The library is a joint project of The Agency Fund and Irrational Labs. Neither organization sells, trains on, or collects your conversation data; neither has access to it. Questions about this disclosure go to the maintainers listed in `MAINTAINERS.md`.
