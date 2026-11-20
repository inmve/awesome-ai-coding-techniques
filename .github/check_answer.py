"""Check a survey answer added by a pull request and merge it.

A pull request that touches anything outside answers/ is not a survey answer and is left alone.
Run locally on a file: python3 .github/check_answer.py --file answers/2026/abcd1234.json
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
# «never-heard» was dropped on 2026-11-19: four answers
ANSWERS = {"not-interested", "want-to-try", "tried-dropped", "do-it"}
PATH = re.compile(r"^answers/2026/[a-f0-9]{8}\.json$")
MAX_BYTES = 20000


def categories():
    """Category id -> practice ids, the same sections as on the site."""
    data = json.loads((ROOT / "data/entries.json").read_text(encoding="utf-8"))
    # a team's copy adds its own practices in docs/team.json; the site shows them in the same sections
    team_file = ROOT / "docs/team.json"
    if team_file.exists():
        known = {e["id"] for e in data["entries"]}
        for practice in json.loads(team_file.read_text(encoding="utf-8")).get("practices") or []:
            if isinstance(practice, dict) and practice.get("id") not in known and practice.get("title") and practice.get("definition"):
                data["entries"].append({"kind": "practice", "stages": [], "group": None, **practice})
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
    if not PATH.match(path):
        return [f"the file must be answers/2026/<8 hex characters>.json, not {path}"]
    if len(raw) > MAX_BYTES:
        return ["the file is larger than an answer can be"]
    try:
        answer = json.loads(raw)
    except ValueError as error:
        return [f"the file is not valid JSON: {error}"]
    # who answered is the author of the pull request, so the file carries no id of its own (2026-11-20)
    if not isinstance(answer, dict) or set(answer) != {"survey", "answeredAt", "answers"}:
        return ["the file must have exactly: survey, answeredAt, answers"]
    if answer["survey"] != SURVEY:
        found.append(f"survey must be {SURVEY}")
    try:
        day = datetime.date.fromisoformat(answer["answeredAt"])
        if day > datetime.date.today() + datetime.timedelta(days=1):
            found.append("answeredAt is in the future")
    except (TypeError, ValueError):
        found.append("answeredAt must be a date like 2026-11-20")
    answers = answer["answers"]
    if not isinstance(answers, dict) or not answers:
        found.append("answers must name at least one practice")
    else:
        surveyed = set().union(*(members for _, members in categories().values()))
        unknown = sorted(set(answers) - surveyed)
        if unknown:
            found.append("practices that are not in the survey: " + ", ".join(unknown))
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
    elif not PATH.match(files[0]["filename"]):
        found = problems(files[0]["filename"], "")  # the path is checked before anything is fetched
    else:
        path = files[0]["filename"]
        raw = gh("api", f"repos/{os.environ['HEAD_REPO']}/contents/{path}?ref={os.environ['HEAD_SHA']}",
                 "-H", "Accept: application/vnd.github.raw")
        found = problems(path, raw)
    if found:
        gh("pr", "comment", number, "--repo", repo, "--body",
           "Thanks for answering. This file could not be accepted:\n\n" + "\n".join(f"- {p}" for p in found))
        sys.exit(1)
    count = len(json.loads(raw)["answers"])
    # merge only the commit that was checked: a commit pushed after the check stops the merge
    gh("pr", "merge", number, "--repo", repo, "--squash", "--match-head-commit", os.environ["HEAD_SHA"],
       "--subject", f"Survey answers: {count} practices")
    print("merged")


if __name__ == "__main__":
    main()
