"""Check a survey answer added by a pull request and merge it.

A pull request that touches anything outside answers/ is not a survey answer and is left alone.
Run locally on a file: python3 .github/check_answer.py --file answers/2026/req-plan/abcd1234.json
"""
import datetime
import json
import os
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SURVEY = "agentic-software-development-2026"
ANSWERS = {"never-heard", "not-interested", "want-to-try", "tried-dropped", "we-do-it"}
PATH = re.compile(r"^answers/2026/([a-z0-9-]+)/([a-z0-9]{8})\.json$")
MAX_BYTES = 20000


def categories():
    """Category id -> practice ids, the same sections as on the site."""
    data = json.loads((ROOT / "data/entries.json").read_text(encoding="utf-8"))
    practices = [e for e in data["entries"] if e.get("seededFrom") != "pre-llm"]
    result = {}
    for stage in data["meta"]["stages"]:
        members = {e["id"] for e in practices if e.get("kind") == "practice" and stage["id"] in (e.get("stages") or [])}
        if members:
            result[f"stage-{stage['id']}"] = (stage["title"]["en"], members)
    for group in data["meta"]["groups"]:
        members = {e["id"] for e in practices if e.get("kind") != "approach" and e.get("group") == group["id"]}
        if members:
            result[f"group-{group['id']}"] = (group["title"]["en"], members)
    return result


def problems(path, raw):
    """Everything wrong with one answer file; an empty list means it is accepted."""
    found = []
    match = PATH.match(path)
    if not match:
        return [f"the file must be answers/2026/<category>/<8 letters or digits>.json, not {path}"]
    if len(raw) > MAX_BYTES:
        return ["the file is larger than an answer can be"]
    try:
        answer = json.loads(raw)
    except ValueError as error:
        return [f"the file is not valid JSON: {error}"]
    if not isinstance(answer, dict) or set(answer) != {"survey", "category", "answeredAt", "answers"}:
        return ["the file must have exactly: survey, category, answeredAt, answers"]
    if answer["survey"] != SURVEY:
        found.append(f"survey must be {SURVEY}")
    known = categories()
    category = answer["category"]
    if category not in known:
        found.append(f"unknown category {category}")
    elif re.sub(r"^(stage|group)-", "", category) != match.group(1):
        found.append("the folder does not match the category")
    try:
        day = datetime.date.fromisoformat(answer["answeredAt"])
        if day > datetime.date.today() + datetime.timedelta(days=1):
            found.append("answeredAt is in the future")
    except (TypeError, ValueError):
        found.append("answeredAt must be a date like 2026-11-20")
    answers = answer["answers"]
    if not isinstance(answers, dict) or not answers:
        found.append("answers must name at least one practice")
    elif category in known:
        unknown = sorted(set(answers) - known[category][1])
        if unknown:
            found.append("practices that are not in this category: " + ", ".join(unknown))
        wrong = sorted({str(v) for v in answers.values()} - ANSWERS)
        if wrong:
            found.append("answers must be one of " + ", ".join(sorted(ANSWERS)) + "; got " + ", ".join(wrong))
    return found


def gh(*args):
    return subprocess.run(["gh", *args], check=True, text=True, capture_output=True).stdout


def main():
    if "--file" in sys.argv:
        path = sys.argv[sys.argv.index("--file") + 1]
        found = problems(path, (ROOT / path).read_text(encoding="utf-8"))
        print("accepted" if not found else "rejected: " + "; ".join(found))
        sys.exit(1 if found else 0)
    repo, number = os.environ["GITHUB_REPOSITORY"], os.environ["PR_NUMBER"]
    files = json.loads(gh("api", f"repos/{repo}/pulls/{number}/files", "--paginate"))
    if any(not f["filename"].startswith("answers/") for f in files):
        print("not a survey answer: left for a person")
        return
    found = []
    if len(files) != 1 or files[0]["status"] != "added":
        found.append("a survey pull request adds exactly one new file")
    else:
        path = files[0]["filename"]
        raw = gh("api", f"repos/{os.environ['HEAD_REPO']}/contents/{path}?ref={os.environ['HEAD_SHA']}",
                 "-H", "Accept: application/vnd.github.raw")
        found = problems(path, raw)
    if found:
        gh("pr", "comment", number, "--repo", repo, "--body",
           "Thanks for answering. This file could not be accepted:\n\n" + "\n".join(f"- {p}" for p in found))
        sys.exit(1)
    title = categories()[json.loads(raw)["category"]][0]
    gh("pr", "merge", number, "--repo", repo, "--squash", "--subject", f"Survey answers: {title}")
    print("merged")


if __name__ == "__main__":
    main()
