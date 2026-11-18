# Contributing

This repository is an open reference of software development practices. Every entry in
[`data/entries.json`](data/entries.json) has a definition, a date and sources; `README.md` and the
[site](https://inmve.github.io/dev-with-agents/) are built from that file.

## What an entry needs

- **A practice:** a repeatable way of working that someone could start tomorrow. Tools, products and
  opinions without an action are not entries.
- **What changes with coding agents.** An older practice is included when it is the root of a newer one.
- **A first-hand source:** the author describes their own work or their company's process. Content
  marketing, listicles and rewrites of someone else's post are not sources.
- **A verbatim quote** from that source, 1 to 2 sentences, that states the practice itself. It is shown
  on the site when the reader hovers or clicks a footnote.
- **A neutral definition** in the third person: what practitioners do, without "you", without advice,
  without claims the source does not make.

## How to contribute

- [Open an issue](https://github.com/inmve/awesome-ai-coding-techniques/issues/new) with the practice,
  the link to the source and the quote; or
- open a pull request that edits `data/entries.json` and run `python3 scripts/build_readme.py`.

Reports of a wrong date, a dead link or a quote that is no longer on the page are as welcome as new entries.
