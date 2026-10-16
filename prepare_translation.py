"""Preserve source demo in a new sibling; no replacement of existing projects."""
import hashlib,json,shutil,subprocess
from pathlib import Path
base=Path(__file__).resolve().parent.parent
source=base/'walker/godot-demo-projects/gui/translation'
target=base/'walker-gui-translation'
assert not target.exists(),'Existing project must be resumed, never replaced'
assert shutil.disk_usage(base).free>25*1024**3
target.mkdir()
shutil.copytree(source,target/'godot',ignore=shutil.ignore_patterns('.godot','.git'))
shutil.copy2(base/'walker/godot-demo-projects/LICENSE.md',target/'LICENSE.md')
(target/'evidence').mkdir()
files=[]
for f in sorted(source.rglob('*')):
    if not f.is_file() or '.godot' in f.parts or '.git' in f.parts:continue
    rel=f.relative_to(source)
    digest=hashlib.sha256(f.read_bytes()).hexdigest()
    assert hashlib.sha256((target/'godot'/rel).read_bytes()).hexdigest()==digest
    files.append(dict(path=str(rel),sha256=digest))
(target/'evidence/source-copy.json').write_text(json.dumps(dict(source=str(source),files=files),indent=2))
(target/'AGENTS.md').write_text('''# Walker GUI Translation

Preserve source demo and copied runtime, licenses, audio, fonts, imports and all
prior artifacts. Local only: no publishing, push, paid APIs, credentials changes,
sandbox weakening or deletion. Keep15GB reserve. Use isolated normal-input
harnesses for verification. Locale-switch text/resources and CSV/PO scene changes
need actual tests; log output is not proof that audio was heard. Human approval
remains separate from machine checks.
''')
(target/'SOURCES.md').write_text(f'''# Source provenance

Unmodified initial copy of {source}. Official Godot demo collection. Root MIT
LICENSE.md and bundled font license preserved. Image/audio-specific attribution
requires inspection; no new license claims. File hashes in evidence/source-copy.json.
''')
(target/'FRICTIONAL.md').write_text('''# Production evidence

2026-10-05: started item109 while item108 remains blocked at shared Gate T.
All initial source files copied and hashes compared; original checkout untouched.
CSV demo supports English/Spanish/Japanese/Russian, PO supports first three;
locale changes remap flags/audio. PO includes random1–3 plural example. Source
project contains legacy locale paths as well as current internationalization
settings; retain until actual import/run reveals whether they matter.
No behavioral, audio-listening, film or human approval claimed.
''')
with (target/'evidence/import1.log').open('x') as log:
    result=subprocess.run(['/opt/homebrew/bin/godot','--headless','--editor','--path',str(target/'godot'),'--import'],stdout=log,stderr=subprocess.STDOUT,timeout=180)
print(f'Copied {len(files)} files; import exit {result.returncode}; {target}',flush=True)
