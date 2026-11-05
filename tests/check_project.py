"""Static project contracts; runtime paths live in game/*_tests.rpy."""
from pathlib import Path
import ast
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / "docs/handoff_v2/ASSETS.json").read_text())
for row in manifest["images"]:
    asset = ROOT / row["path"]
    assert asset.is_file(), row["path"]
    assert hashlib.sha256(asset.read_bytes()).hexdigest() == row["sha256"], row["path"]
assert len(manifest["images"]) == 89
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
print(f"PASS: 89 scene PNGs; 65 UI PNGs; {len(labels)} labels; all static jump/call targets exist; Russian spelling and portable paths checked.")

from fontTools.ttLib import TTFont
font_manifest = json.loads((ROOT / "docs/handoff_v2/FONT_MANIFEST.json").read_text())
for row in font_manifest:
    font = TTFont(ROOT / row["path"])
    assert "fvar" not in font
    chars = font.getBestCmap()
    assert all(c in chars for c in list(range(0x410, 0x450)) + [0x401, 0x451])
    assert (ROOT / row["license"]).exists()
landmarks = json.loads((ROOT / "game/art_layout.json").read_text())
assert len(landmarks) == 74
for relative, spec in landmarks.items():
    assert hashlib.sha256((ROOT / "game/images" / relative).read_bytes()).hexdigest() == spec["source_sha256"]
    assert hashlib.sha256((ROOT / "game/images_normalized" / relative).read_bytes()).hexdigest() == spec["derived_sha256"]
baseline = json.loads((ROOT / "tests/story_choices_v1.json").read_text())
for name, expected in baseline.items():
    actual = re.findall(r'^\s{8}"([^"\n]+)":$', (ROOT / name).read_text(), re.M)
    assert actual == expected, name
assert not re.search(r"strange (?:doubtful|thinking|skeptical)", (ROOT / "game/assets.rpy").read_text())
assert (ROOT / "game/audio/music/office_airport_lounge.ogg").exists()
print("PASS: 74 derived poses, 7 static Cyrillic fonts, licenses and unchanged story choices.")

from PIL import Image
assert (ROOT / 'icon.ico').read_bytes() == (ROOT / 'art_sources/icon/game_icon.ico').read_bytes()
with Image.open(ROOT / 'icon.ico') as icon:
    assert icon.ico.sizes() == {(n, n) for n in (16, 24, 32, 48, 64, 128, 256)}
source_icon = Image.open(ROOT / 'art_sources/icon/game_icon.png').convert('RGBA').resize((256, 256), Image.Resampling.LANCZOS)
assert source_icon.tobytes() == Image.open(ROOT / 'game/gui/window_icon.png').convert('RGBA').tobytes()
groups = {}
for relative, spec in landmarks.items():
    image = Image.open(ROOT / 'game/images_normalized' / relative).convert('RGBA')
    actual = image.getchannel('A').point(lambda a: 255 if a >= 32 else 0).getbbox()
    assert list(actual) == spec['derived_alpha_bbox']
    assert actual[3] >= 1120 and actual[1] >= 24, relative
    group = relative.rsplit('/', 1)[0]
    value = (spec['target_eye'][1], spec['group_multiplier'])
    assert groups.setdefault(group, value) == value, group
for relative in ['cast/kyle/neutral.png', 'cast/cartman/proud.png']:
    assert landmarks[relative]['derived_alpha_bbox'][1] > landmarks['olya/southpark/neutral.png']['derived_alpha_bbox'][1] + 200
print('PASS: icon source/ICO sizes; actual silhouette bounds below 1080+40; fixed group framing; children below adults.')
