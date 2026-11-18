"""Build README.md from data/entries.json.

Usage: python3 scripts/build_readme.py
data/entries.json is the source of truth; README.md is generated from it, do not edit README.md by hand.
The README follows the form of the site: the same title and introduction, the same parts in the same order
(by SDLC stage, cross-stage, teams and projects, thematic groups, approaches), oldest practices first inside a
section, and the example schemes as still pictures from figures/ (see scripts/build_figures.py).
"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE_URL = "https://inmve.github.io/software-practices/"
SURVEY_TEMPLATE_URL = "https://github.com/inmve/team-survey"


def plain_definition(entry):
    return re.sub(r"(\s*\[\d+\])+\s*$", "", entry["definition"]["en"]).strip()


def entry_date(entry, by_id):
    appeared = (entry.get("firstAppeared") or {}).get("date")
    if appeared:
        return appeared
    # the date of a quote about what changes with agents is not the date of the practice
    published = [s["published"] for s in entry["sources"] if s.get("published") and s.get("role") != "relevance"]
    return min(published) if published else None


def sort_key(entry, by_id):
    # the order of the site: oldest first, entries without a date last, the same date by title
    return (entry_date(entry, by_id) or "9999", entry["title"]["en"].lower())


def shown_year(entry):
    # the site shows a year only when the date of the practice was checked on a source page (rule 4.7, 2026-11-18);
    # the earliest saved post is the date of our collection, not of the practice, and is used only for the order
    appeared = entry.get("firstAppeared") or {}
    return appeared["date"][:4] if appeared.get("date") and appeared.get("verified") else None


def anchor(title):
    return re.sub(r"[^a-z0-9 -]", "", title.lower()).strip().replace(" ", "-")


def entry_lines(entry, by_id):
    date = shown_year(entry)
    year = f" ({date})" if date and date not in entry["title"]["en"] else ""
    lines = [f"- **{entry['title']['en']}**{year}. {plain_definition(entry)}"]
    sources = []
    for source in sorted(entry["sources"], key=lambda s: s.get("n", 0)):
        who = source.get("author") or source["url"].split("/")[2]
        when = f", {source['published']}" if source.get("published") else ""
        sources.append(f"[{who}{when}]({source['url']})")
    if sources:
        lines.append(f"  Sources: {'; '.join(sources)}.")
    roots = []
    for r in entry.get("rootsIn") or []:
        if r in by_id:
            root_year = shown_year(by_id[r])
            roots.append(by_id[r]["title"]["en"] + (f" ({root_year})" if root_year else ""))
    if roots:
        lines.append(f"  Grew from: {', '.join(roots)}.")
    # the example scheme of the site, as a still picture (scripts/build_figures.py writes the files)
    if (ROOT / "figures" / f"{entry['id']}.svg").exists():
        lines += ["", f'  <img src="figures/{entry["id"]}.svg" width="440" alt="Example scheme: {entry["title"]["en"]}">', ""]
    return lines


def short_lines(entry, by_id):
    date = shown_year(entry)
    year = f" ({date})" if date and date not in entry["title"]["en"] else ""
    return [f"- **{entry['title']['en']}**{year}. {plain_definition(entry)}"]


# The introduction of the site, word for word (index.html, INTRO and INTRO_SOURCES). When one changes, change the other.
INTRO_SOURCES = [
    "https://x.com/karpathy/status/2015883857489522876",
    "https://claude.dev/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models/",
    "https://www.omnea.co/blog/ai-in-our-programming-interviews",
]


def intro(practices, with_root):
    note = lambda n: f"<sup>[[{n}]]({INTRO_SOURCES[n - 1]})</sup>"
    return [
        "In the autumn of 2025 I kept a list of tips and techniques for coding with LLMs, and stopped adding to it that "
        "November. A year later I wouldn’t follow a lot of it myself.",
        "",
        f"That November Opus 4.5 and GPT-5.2 came out, and agents got good enough to write most of the code.{note(1)} "
        "This year Fable and Astra went further and stopped needing most of what my list was for: detailed "
        f"instructions, carefully prepared context, reminders to think hard.{note(2)}",
        "",
        "So I started again from what people who ship software with agents write about their own work. Below are "
        f"{practices} of their practices, each with a quote from the post that describes it.",
        "",
        "Prompting is the part that got less important. The practices that were around long before LLMs went the other "
        "way: I couldn’t find anyone taking back tests, code review or CI, and if anything they carry more weight "
        f"now.{note(3)} {with_root} of the practices on this page grew straight out of one of those older ones, like "
        "continuous integration (1998) or test-driven development (2002). Teams that already had them had less to change. "
        "Even the rubber duck is still here; now it talks back.",
        "",
    ]


def main():
    data = json.loads((ROOT / "data/entries.json").read_text(encoding="utf-8"))
    by_id = {e["id"]: e for e in data["entries"]}
    # older practices appear only as «Grew from» of an agent-era entry, not as entries of their own
    entries = [e for e in data["entries"] if e.get("seededFrom") != "pre-llm"]
    meta = data["meta"]

    # the parts and sections of the site, in its order: (part title, [(section title or None, description, members, repeated)])
    parts = [
        ("By SDLC stage", [(st["title"]["en"], None,
                            [e for e in entries if e["kind"] == "practice" and st["id"] in (e.get("stages") or [])], False)
                           for st in meta["stages"] if st["id"] != "general"]),
        ("Cross-stage", [(g["title"]["en"], g.get("description", {}).get("en"),
                          [e for e in entries if e["kind"] != "approach" and e.get("group") == g["id"]], False)
                         for g in meta["groups"] if g["section"] == "general" and g["id"] != "team"]),
    ]
    # Teams and projects: its line goes under the part title, then its subgroups (data without subgroups: one section)
    part_descriptions = {}
    for g in meta["groups"]:
        if g["section"] == "general" and g["id"] == "team":
            subgroups = [s for s in meta["groups"] if s["section"] == "team"]
            if subgroups:
                part_descriptions[g["title"]["en"]] = g.get("description", {}).get("en")
                parts.append((g["title"]["en"], [(s["title"]["en"], s.get("description", {}).get("en"),
                                                  [e for e in entries if e["kind"] != "approach" and e.get("group") == s["id"]], False)
                                                 for s in subgroups]))
            else:
                parts.append((g["title"]["en"], [(None, g.get("description", {}).get("en"),
                                                  [e for e in entries if e["kind"] != "approach" and e.get("group") == "team"], False)]))
    for theme in meta.get("themes") or []:
        parts.append((theme["title"]["en"], [(None, (theme.get("description") or {}).get("en"),
                                               [e for e in entries if e["id"] in theme["entries"]], True)]))
    parts.append(("Approaches", [(None, None, [e for e in entries if e["kind"] == "approach"], False)]))
    parts = [(title, [section for section in sections if section[2]]) for title, sections in parts]
    parts = [(title, sections) for title, sections in parts if sections]

    quoted = sum(1 for e in entries for s in e["sources"] if s.get("quote"))
    figures = sum(1 for e in entries if (ROOT / "figures" / f"{e['id']}.svg").exists())
    with_root = sum(1 for e in entries if any(r in by_id for r in e.get("rootsIn") or []))
    out = [
        "<!-- Generated from data/entries.json by scripts/build_readme.py. Do not edit by hand. -->",
        "",
        "# Agentic software development reference",
        "",
        "**What agents changed in how software gets built, and what they didn’t**",
        "",
    ]
    out += intro(len(entries), with_root)
    out += [
        f"- **Site:** [{SITE_URL}]({SITE_URL}) (the same reference with a timeline, quotes on hover and schemes that play)",
        "- **Data:** [`data/entries.json`](data/entries.json), the single source; this README is generated from it",
        f"- **Survey for your team:** [team-survey]({SURVEY_TEMPLATE_URL}), a GitHub template that asks the same practices inside your team",
        "",
        f"{len(entries)} practices, {sum(len(e['sources']) for e in entries)} sources, {quoted} of them with a verbatim quote "
        f"stored in the data, {figures} example schemes. Preliminary edition: dates are not verified yet.",
        "",
        "Inside every section the oldest practices come first.",
        "",
        "## Contents",
        "",
    ]
    for title, sections in parts:
        if sections[0][0] is None:
            out.append(f"- [{title}](#{anchor(title)})")
        else:
            out.append(f"- [{title}](#{anchor(title)}): " + " · ".join(f"[{name}](#{anchor(name)})" for name, _, _, _ in sections))
    out.append("")
    for title, sections in parts:
        out += [f"## {title}", ""]
        if part_descriptions.get(title):
            out += [part_descriptions[title], ""]
        for name, description, members, repeated in sections:
            if name:
                out += [f"### {name}", ""]
            if description:
                out += [description, ""]
            if repeated:
                out += ["These practices also stand in their own sections above, with their sources.", ""]
            for entry in sorted(members, key=lambda e: sort_key(e, by_id)):
                out += short_lines(entry, by_id) if repeated else entry_lines(entry, by_id)
            out.append("")
    out += ["## Contributing", "",
            "See [CONTRIBUTING.md](CONTRIBUTING.md). Changes go into `data/entries.json`; then run "
            "`python3 scripts/build_readme.py`.", ""]
    text = re.sub(r"\n{3,}", "\n\n", "\n".join(out))
    (ROOT / "README.md").write_text(text, encoding="utf-8")
    print("README.md:", len(entries), "practices,", figures, "schemes,", sum(len(s) for _, s in parts), "sections")


if __name__ == "__main__":
    main()
