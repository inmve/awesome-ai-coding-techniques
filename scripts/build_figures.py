"""Build figures/<entry id>.svg for the README from the example schemes of the site.

Usage: python3 scripts/build_figures.py /path/to/software-practices

The site keeps its schemes in two forms: figures/motion.json (schemes that play step by step, with a still
`poster` step) and figures/<id>.svg (still schemes). A README cannot run the player, so every scheme in motion
is written here as its poster step: parts that are off on that step are dropped, frames take the red or green
tone of that step, moved parts take their position on that step. Still schemes are copied. Every file gets a
white background, so that it reads on a dark page too.
"""
import json
import pathlib
import re
import sys
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent.parent
STYLE = ("text{font:13px ui-monospace,'SF Mono',Menlo,monospace}"
         ".move{transform-box:fill-box;transform-origin:left center}")
RED, GREEN = "#c0392b", "#2a7d3f"


def steps(element, name):
    return (element.get(name) or "").split()


def poster_svg(spec):
    poster = str(spec["poster"])
    root = ET.fromstring(spec["svg"])

    def prune(parent):
        for child in list(parent):
            if child.get("data-on") is not None and poster not in steps(child, "data-on"):
                parent.remove(child)
                continue
            classes = (child.get("class") or "").split()
            hot, good = poster in steps(child, "data-hot"), poster in steps(child, "data-good")
            if "box" in classes and (hot or good):
                child.set("stroke", RED if hot else GREEN)
                child.set("stroke-width", "1.6")
            if "fillbar" in classes and hot:
                child.set("fill", RED)
            if child.get("data-t"):
                # the position on the poster step: the last listed step that is not after it
                value = None
                for item in child.get("data-t").split(";"):
                    step, transform = item.split(":", 1)
                    if value is None or int(step) <= int(poster):
                        value = transform
                child.set("style", f"transform:{value}")
            for name in ("data-on", "data-hot", "data-good", "data-t"):
                child.attrib.pop(name, None)
            child.set("class", " ".join(c for c in classes if c == "move")) if "move" in classes else child.attrib.pop("class", None)
            prune(child)

    prune(root)
    body = "".join(ET.tostring(child, encoding="unicode") for child in root)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{root.get("viewBox")}" role="img">'
            f'<style>{STYLE}</style><rect width="100%" height="100%" fill="#fff"/>{body}</svg>\n')


def with_white_background(svg_text):
    return re.sub(r"(<svg\b[^>]*>)", r'\1<rect width="100%" height="100%" fill="#fff"/>', svg_text, count=1)


def main():
    site = pathlib.Path(sys.argv[1]).expanduser() / "figures"
    data = json.loads((ROOT / "data/entries.json").read_text(encoding="utf-8"))
    entry_ids = {e["id"] for e in data["entries"]}
    motion = json.loads((site / "motion.json").read_text(encoding="utf-8"))
    captions = json.loads((site / "index.json").read_text(encoding="utf-8"))
    out = ROOT / "figures"
    out.mkdir(exist_ok=True)
    for old in out.glob("*.svg"):
        old.unlink()
    written = []
    for entry_id, spec in motion.items():
        if entry_id in entry_ids:
            (out / f"{entry_id}.svg").write_text(poster_svg(spec), encoding="utf-8")
            written.append(entry_id)
    for entry_id in captions:
        if entry_id in entry_ids and entry_id not in motion and (site / f"{entry_id}.svg").exists():
            (out / f"{entry_id}.svg").write_text(
                with_white_background((site / f"{entry_id}.svg").read_text(encoding="utf-8")), encoding="utf-8")
            written.append(entry_id)
    skipped = sorted((set(motion) | set(captions)) - entry_ids)
    print(f"figures: {len(written)} written;", "not in the data:", skipped or "none")


if __name__ == "__main__":
    main()
