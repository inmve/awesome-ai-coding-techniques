"""Build README.md from data/entries.json as two-column HTML cards (draft of 2026-11-16).

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

    blocks = [("Approaches", [e for e in entries if e["kind"] == "approach"], None)]
    placed = {e["id"] for e in blocks[0][1]}
    for stage in stages:
        if stage["id"] == "general":
            continue
        members = [e for e in entries if e["id"] not in placed and e["kind"] != "concept" and not e.get("group")
                   and (e.get("stages") or [None])[0] == stage["id"]]
        if members:
            blocks.append((stage["title"]["en"], members, None))
            placed |= {e["id"] for e in members}
    for group in groups:
        members = [e for e in entries if e["id"] not in placed and e.get("group") == group["id"]]
        if members:
            prefix = "Concepts: " if group["section"] == "concepts" else "Across stages: "
            if group["id"] == "team":
                prefix = ""
            blocks.append((prefix + group["title"]["en"], members, group.get("description", {}).get("en")))
            placed |= {e["id"] for e in members}
    rest = [e for e in entries if e["id"] not in placed and e.get("seededFrom") == "pre-llm"]
    if rest:
        blocks.append(("Before coding agents", rest, None))
        placed |= {e["id"] for e in rest}
    other = [e for e in entries if e["id"] not in placed]
    if other:
        blocks.append(("Across stages: other", other, None))

    import html as html_module
    esc = html_module.escape
    quoted = sum(1 for e in entries for s in e["sources"] if s.get("quote"))
    out = [
        "<!-- Generated from data/entries.json by scripts/build_readme.py. Do not edit by hand. -->",
        "",
        "<h1>Agentic engineering reference</h1>",
        "",
        "<table><tr>",
        "<td width=\"62%\" valign=\"top\">",
        "<b>Practices for coding agents and the older practices they grew from.</b><br><br>",
        f"{len(entries)} practices. Each has a definition and first-hand sources; every source quote is checked word for word on the live page.",
        "</td>",
        "<td valign=\"top\">",
        f"<b><a href=\"{SITE_URL}\">Open the site</a></b> with the timeline and quotes on hover<br>",
        "<a href=\"data/entries.json\">data/entries.json</a>, the single source<br>",
        f"<a href=\"{SURVEY_TEMPLATE_URL}\">team-survey</a>, the same practices as a survey for your team",
        "</td>",
        "</tr></table>",
        "",
    ]
    out += ["<b>Sections:</b> " + " · ".join(f"<a href=\"#{anchor(title)}\">{esc(title)}</a> ({len(members)})" for title, members, _ in blocks), ""]

    def card(entry):
        date = entry_date(entry, by_id)
        year = f" <sub>{date[:4]}</sub>" if date and date[:4] not in entry["title"]["en"] else ""
        sources = "; ".join(
            f"<a href=\"{esc(s['url'])}\">{esc(s.get('author') or s['url'].split('/')[2])}</a>"
            for s in sorted(entry["sources"], key=lambda s: s.get("n", 0)) if s.get("quote"))
        roots = [by_id[r]["title"]["en"] for r in entry.get("rootsIn") or [] if r in by_id]
        extra = f"<br><sub>Grew from: {esc(', '.join(roots))}</sub>" if roots else ""
        return (f"<td width=\"50%\" valign=\"top\"><b>{esc(entry['title']['en'])}</b>{year}<br>"
                f"{esc(plain_definition(entry))}<br><sub>Sources: {sources}</sub>{extra}</td>")

    for title, members, description in blocks:
        ordered = sorted(members, key=lambda e: sort_key(e, by_id, llm_era_start))
        out += [f"<h2 id=\"{anchor(title)}\">{esc(title)}</h2>", ""]
        if description:
            out += [f"<p><i>{esc(description)}</i></p>", ""]
        out += [f"<details open><summary>{len(ordered)} practices</summary>", "", "<table>"]
        for i in range(0, len(ordered), 2):
            pair = ordered[i:i + 2]
            out.append("<tr>" + "".join(card(e) for e in pair) + ("<td></td>" if len(pair) == 1 else "") + "</tr>")
        out += ["</table>", "</details>", ""]
    out += ["<h2>Contributing</h2>", "",
            "See <a href=\"CONTRIBUTING.md\">CONTRIBUTING.md</a>. Changes go into <code>data/entries.json</code>; then run "
            "<code>python3 scripts/build_readme.py</code>.", ""]
    (ROOT / "README.md").write_text("\n".join(out), encoding="utf-8")
    print("README.md:", len(entries), "entries in", len(blocks), "sections")


if __name__ == "__main__":
    main()
