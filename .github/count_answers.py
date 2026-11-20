"""Count the survey answers: one vote per GitHub account, its latest merged pull request.

Who answered is the author of the pull request that added the answer file; the file itself carries no id.
A later send by the same account replaces its earlier answers in the count, so nothing is counted twice.

Usage, in a clone of the repository:
  python3 .github/count_answers.py                       ask GitHub for the merged pull requests (needs gh)
  python3 .github/count_answers.py --prs prs.json        the same, from a saved `gh pr list` answer
  python3 .github/count_answers.py --out results.json    also write the counts to a file
The answer files are read from this clone, so pull main first.
"""
import collections
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
ANSWERS_DIR = "answers/2026/"
ANSWERS = ["not-interested", "want-to-try", "tried-dropped", "do-it"]


def merged_pull_requests():
    if "--prs" in sys.argv:
        return json.loads(pathlib.Path(sys.argv[sys.argv.index("--prs") + 1]).read_text(encoding="utf-8"))
    # no repository is named: gh takes the one this clone belongs to, so a team's copy counts its own answers
    out = subprocess.run(["gh", "pr", "list", "--state", "merged", "--limit", "5000",
                          "--json", "number,author,mergedAt,files"], check=True, text=True, capture_output=True,
                         cwd=ROOT).stdout
    return json.loads(out)


def latest_answer_per_account(pull_requests):
    """GitHub login -> (merged at, path of its answer file), the latest merged answer of each account."""
    latest = {}
    for pr in pull_requests:
        files = [f["path"] for f in pr.get("files") or []]
        if len(files) != 1 or not files[0].startswith(ANSWERS_DIR):
            continue  # not a survey answer (the bot merges only pull requests that add exactly one answer file)
        login = pr["author"]["login"].lower()
        if login not in latest or pr["mergedAt"] > latest[login][0]:
            latest[login] = (pr["mergedAt"], files[0])
    return latest


def count(latest):
    per_practice = collections.defaultdict(collections.Counter)
    missing = []
    for login, (_, path) in sorted(latest.items()):
        file = ROOT / path
        if not file.exists():
            missing.append(path)
            continue
        for practice, answer in json.loads(file.read_text(encoding="utf-8"))["answers"].items():
            per_practice[practice][answer] += 1
    return per_practice, missing


def main():
    latest = latest_answer_per_account(merged_pull_requests())
    per_practice, missing = count(latest)
    result = {"accounts": len(latest) - len(missing),
              "practices": {p: {a: c[a] for a in ANSWERS} for p, c in sorted(per_practice.items())}}
    if missing:
        print("not in this clone (pull main first):", ", ".join(missing), file=sys.stderr)
    print(f"{result['accounts']} accounts answered")
    for practice, counts in result["practices"].items():
        print(f"  {practice}: " + ", ".join(f"{a} {n}" for a, n in counts.items() if n))
    if "--out" in sys.argv:
        pathlib.Path(sys.argv[sys.argv.index("--out") + 1]).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
