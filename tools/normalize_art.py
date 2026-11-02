"""Build reproducible dialogue crops without modifying supplied PNG originals."""
from pathlib import Path
import hashlib
import json
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
LANDMARKS = json.loads((ROOT / 'tools/art_landmarks.json').read_text())
records = {}
for relative, spec in LANDMARKS.items():
    source = ROOT / 'game/images' / relative
    image = Image.open(source).convert('RGBA')
    alpha_bbox = image.getchannel('A').point(lambda a: 255 if a >= 32 else 0).getbbox()
    scale = spec['scale']
    eye_x, eye_y = spec['eye_center']
    target_x, target_y = spec['target_eye']
    offset = (round(target_x - eye_x * scale), round(target_y - eye_y * scale))
    # No crop at the hair, hat, hand or side of the tool. The bottom is the
    # intended dialogue crop; Carrie/Miranda legs are left in original files.
    left, top, right, bottom = alpha_bbox
    assert left * scale + offset[0] >= 0, relative
    assert right * scale + offset[0] <= spec['canvas'][0], relative
    assert top * scale + offset[1] >= 0, relative
    pixel = '/minecraft/' in relative or relative.startswith('cast/villager/')
    resampling = Image.Resampling.NEAREST if pixel else Image.Resampling.LANCZOS
    resized = image.resize((round(image.width * scale), round(image.height * scale)), resampling)
    canvas = Image.new('RGBA', tuple(spec['canvas']))
    canvas.paste(resized, offset)
    destination = ROOT / 'game/images_normalized' / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(destination, optimize=True)
    records[relative] = dict(spec, source_alpha_bbox=alpha_bbox,
                            offset=offset, resampling='nearest' if pixel else 'lanczos',
                            source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                            derived_sha256=hashlib.sha256(destination.read_bytes()).hexdigest())
(ROOT / 'game/art_layout.json').write_text(json.dumps(records, indent=2) + '\n')
print(f'Normalized {len(records)} real poses; source PNGs unchanged.')
