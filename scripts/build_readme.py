"""Build README.md from data/entries.json.

Usage: python3 scripts/build_readme.py
data/entries.json is the source of truth; README.md is generated from it, do not edit README.md by hand.
Order inside every block: newest first; entries without a date after dated ones; practices from before
coding agents last.
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


def sort_key(entry, by_id, llm_era_start):
    date = entry_date(entry, by_id)
    before_agents = entry.get("seededFrom") == "pre-llm" or (date is not None and date < llm_era_start)
    if before_agents:
        return (2, "" if date is None else "".join(chr(255 - ord(c)) for c in date))
    if date is None:
        return (1, "")
    return (0, "".join(chr(255 - ord(c)) for c in date))


def anchor(title):
    return re.sub(r"[^a-z0-9 -]", "", title.lower()).strip().replace(" ", "-")


def entry_lines(entry, by_id):
    date = entry_date(entry, by_id)
    year = f" ({date[:4]})" if date and date[:4] not in entry["title"]["en"] else ""
    lines = [f"- **{entry['title']['en']}**{year}. {plain_definition(entry)}"]
    sources = []
    for source in sorted(entry["sources"], key=lambda s: s.get("n", 0)):
        who = source.get("author") or source["url"].split("/")[2]
        when = f", {source['published']}" if source.get("published") else ""
        sources.append(f"[{who}{when}]({source['url']})")
    if sources:
        lines.append(f"  Sources: {'; '.join(sources)}.")
    roots = [by_id[r]["title"]["en"] for r in entry.get("rootsIn") or [] if r in by_id]
    if roots:
        lines.append(f"  Grew from: {', '.join(roots)}.")
    descendants = [e["title"]["en"] for e in by_id.values() if entry["id"] in (e.get("rootsIn") or [])]
    if descendants:
        lines.append(f"  Led to: {', '.join(descendants)}.")
    return lines


def main():
    data = json.loads((ROOT / "data/entries.json").read_text(encoding="utf-8"))
    entries = data["entries"]
    by_id = {e["id"]: e for e in entries}
    llm_era_start = data["meta"]["llmEraStart"]
    stages = data["meta"]["stages"]
    groups = data["meta"]["groups"]

    blocks = [("Approaches", [e for e in entries if e["kind"] == "approach"])]
    placed = {e["id"] for e in blocks[0][1]}
    for stage in stages:
        if stage["id"] == "general":
            continue
        members = [e for e in entries if e["id"] not in placed and e["kind"] != "concept" and not e.get("group")
                   and (e.get("stages") or [None])[0] == stage["id"]]
        if members:
            blocks.append((stage["title"]["en"], members))
            placed |= {e["id"] for e in members}
    for group in groups:
        members = [e for e in entries if e["id"] not in placed and e.get("group") == group["id"]]
        if members:
            prefix = "Concepts: " if group["section"] == "concepts" else "Across stages: "
            blocks.append((prefix + group["title"]["en"], members))
            placed |= {e["id"] for e in members}
    rest = [e for e in entries if e["id"] not in placed and e.get("seededFrom") == "pre-llm"]
    if rest:
        blocks.append(("Before coding agents", rest))
        placed |= {e["id"] for e in rest}
    other = [e for e in entries if e["id"] not in placed]
    if other:
        blocks.append(("Across stages: other", other))

    quoted = sum(1 for e in entries for s in e["sources"] if s.get("quote"))
    out = [
        "<!-- Generated from data/entries.json by scripts/build_readme.py. Do not edit by hand. -->",
        "",
        "# Software Practices",
        "",
        "An open reference of software development practices, from code inspection to work with coding agents.",
        "For each practice: a definition, when it appeared, where it grew from, and the sources that describe it.",
        "",
        f"- **Site:** [{SITE_URL}]({SITE_URL}) (the same data, with a timeline and quotes on hover)",
        "- **Data:** [`data/entries.json`](data/entries.json), the single source; this README is generated from it",
        f"- **Survey for your team:** [team-survey]({SURVEY_TEMPLATE_URL}), a GitHub template that asks the same practices inside your team",
        "",
        f"{len(entries)} entries, {sum(len(e['sources']) for e in entries)} sources, {quoted} of them with a verbatim quote "
        "stored in the data. Preliminary edition: dates are not verified yet.",
        "",
        "Inside every section the newest entries come first; practices from before coding agents come last.",
        "",
        "## Contents",
        "",
    ]
    out += [f"- [{title}](#{anchor(title)})" for title, _ in blocks]
    out.append("")
    for title, members in blocks:
        out += [f"## {title}", ""]
        for entry in sorted(members, key=lambda e: sort_key(e, by_id, llm_era_start)):
            out += entry_lines(entry, by_id)
        out.append("")
    out += ["## Contributing", "",
            "See [CONTRIBUTING.md](CONTRIBUTING.md). Changes go into `data/entries.json`; then run "
            "`python3 scripts/build_readme.py`.", ""]
    (ROOT / "README.md").write_text("\n".join(out), encoding="utf-8")
    print("README.md:", len(entries), "entries in", len(blocks), "sections")


if __name__ == "__main__":
    main()
