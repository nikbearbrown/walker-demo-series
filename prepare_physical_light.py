"""Copy only into a new sibling and retain hashes; bounded import, no source edits."""
import hashlib
import json
import shutil
import subprocess
from pathlib import Path

base = Path(__file__).resolve().parent.parent
source = base / 'walker/godot-demo-projects/3d/physical_light_camera_units'
target = base / 'walker-3d-physical-light-camera-units'
assert not target.exists(), 'Resume existing project; never overwrite'
assert shutil.disk_usage(base).free > 25 * 1024**3
target.mkdir()
shutil.copytree(source, target / 'godot', ignore=shutil.ignore_patterns('.godot', '.git'))
shutil.copy2(base / 'walker/godot-demo-projects/LICENSE.md', target / 'LICENSE.md')
(target / 'evidence').mkdir()
manifest = []
for path in sorted(source.rglob('*')):
    if not path.is_file() or '.godot' in path.parts or '.git' in path.parts:
        continue
    relative = path.relative_to(source)
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    assert hashlib.sha256((target / 'godot' / relative).read_bytes()).hexdigest() == digest
    manifest.append({'path': str(relative), 'sha256': digest})
(target / 'evidence/source-copy.json').write_text(json.dumps({'source': str(source), 'files': manifest}, indent=2))
print(f'Copied and hash-verified {len(manifest)} files', flush=True)
with (target / 'evidence/import1.log').open('x') as log:
    result = subprocess.run(['/opt/homebrew/bin/godot', '--headless', '--editor', '--path', str(target / 'godot'), '--import'], stdout=log, stderr=subprocess.STDOUT, timeout=180)
print(f'Import exit {result.returncode}', flush=True)
