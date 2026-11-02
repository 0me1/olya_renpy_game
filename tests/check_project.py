"""Static project contracts; runtime paths live in game/*_tests.rpy."""
from pathlib import Path
import ast
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / "docs/brief/ASSETS.json").read_text())
for row in manifest["images"]:
    assert (ROOT / row["path"]).is_file(), row["path"]
assert len(manifest["images"]) == 49
assert len(list((ROOT / "game/gui/worlds").rglob("*.png"))) == 65
scripts = list((ROOT / "game").rglob("*.rpy"))
labels = set()
targets = set()
dialogue = []
for path in scripts:
    text = path.read_text(encoding="utf-8-sig")
    assert "\u0451" not in text and "\u0401" not in text, path
    assert "/workspace" not in text, path
    labels.update(re.findall(r"^label (\w+)", text, re.M))
    targets.update(re.findall(r"^\s*(?:jump|call) (?!screen\b|expression\b)(\w+)", text, re.M))
    if path.name.endswith("_tests.rpy") or path.name == "test_support.rpy":
        continue
    for line in text.splitlines():
        match = re.match(r'^\s*(?:\w+ )?(".*")\s*$', line)
        if match:
            try:
                dialogue.append(ast.literal_eval(match[1]))
            except (ValueError, SyntaxError):
                pass
assert not targets - labels, targets - labels
for ending in ["housewives", "manhattan", "southpark", "minecraft", "sims", "marvel"]:
    assert (ROOT / f"game/chapters/0{['housewives','manhattan','southpark','minecraft','sims','marvel'].index(ending)+1}_{ending}.rpy").exists()
print(f"PASS: 49 scene PNGs; 65 UI PNGs; {len(labels)} labels; all static jump/call targets exist; Russian spelling and portable paths checked.")
