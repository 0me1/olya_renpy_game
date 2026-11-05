"""Rebuild copies with the visible lower cut below the 1080px viewport."""
from pathlib import Path
import hashlib
import json
import math
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
LANDMARKS = json.loads((ROOT / 'tools/art_landmarks.json').read_text())
PROFILES = json.loads((ROOT / 'tools/framing_profiles.json').read_text())
CANVAS = (1600, 1600)
EYE_X = 800
sources = {}
for name in LANDMARKS:
    source = ROOT / 'game/images' / name
    image = Image.open(source).convert('RGBA')
    bounds = image.getchannel('A').point(lambda a: 255 if a >= 32 else 0).getbbox()
    sources[name] = (image, bounds, source)

# One multiplier and eye line per character/costume, NOT per menu interaction.
solutions = {}
for group, profile in PROFILES.items():
    members = [n for n in LANDMARKS if n.rsplit('/', 1)[0] == group]
    eye_y = profile['eye_y']
    while True:
        multiplier = max(1.0, max((profile['cut_y'] - eye_y) /
                         ((sources[n][1][3] - LANDMARKS[n]['eye_center'][1]) * LANDMARKS[n]['scale'])
                         for n in members))
        multiplier = math.ceil(multiplier * 1000) / 1000
        if all(eye_y - (LANDMARKS[n]['eye_center'][1] - sources[n][1][1]) * LANDMARKS[n]['scale'] * multiplier >= profile['head_margin'] for n in members):
            break
        eye_y += 2
        assert eye_y < 600, group
    solutions[group] = (eye_y, multiplier)

records = {}
for relative, spec in LANDMARKS.items():
    image, alpha_bbox, source = sources[relative]
    group = relative.rsplit('/', 1)[0]
    target_y, multiplier = solutions[group]
    scale = spec['scale'] * multiplier
    eye_x, eye_y = spec['eye_center']
    offset = (round(EYE_X - eye_x * scale), round(target_y - eye_y * scale))
    left, top, right, bottom = alpha_bbox
    assert left * scale + offset[0] >= 0, relative
    assert right * scale + offset[0] <= CANVAS[0], relative
    assert top * scale + offset[1] >= 24, relative
    pixel = '/minecraft/' in relative or relative.startswith('cast/villager/')
    resampling = Image.Resampling.NEAREST if pixel else Image.Resampling.LANCZOS
    resized = image.resize((round(image.width * scale), round(image.height * scale)), resampling)
    canvas = Image.new('RGBA', CANVAS)
    canvas.paste(resized, offset)
    visible = canvas.getchannel('A').point(lambda a: 255 if a >= 32 else 0).getbbox()
    assert visible[3] >= 1120, (relative, visible)
    # Verify side clearance in actual left/right staging, including the pickaxe.
    stage_x = 1920 * (0.30 if relative.startswith('olya/') else 0.72) - EYE_X
    assert stage_x + visible[0] >= 24, (relative, 'left edge')
    assert stage_x + visible[2] <= 1896, (relative, 'right edge')
    destination = ROOT / 'game/images_normalized' / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(destination, optimize=True)
    records[relative] = dict(spec, scale=scale, reference_scale=spec['scale'],
                            group_multiplier=multiplier, target_eye=[EYE_X, target_y], canvas=CANVAS,
                            source_alpha_bbox=alpha_bbox, derived_alpha_bbox=visible,
                            offset=offset, resampling='nearest' if pixel else 'lanczos',
                            source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                            derived_sha256=hashlib.sha256(destination.read_bytes()).hexdigest())
(ROOT / 'game/art_layout.json').write_text(json.dumps(records, indent=2) + '\n')
print(f'Normalized {len(records)} poses. Every visible lower cut is at least 40px below the frame; originals unchanged.')
print('Group eye lines and multipliers:', solutions)
