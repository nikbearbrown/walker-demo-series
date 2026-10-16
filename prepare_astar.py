"""Non-overwriting sibling copy and bounded engine import; originals untouched."""
import hashlib,json,shutil,subprocess
from pathlib import Path
base=Path(__file__).resolve().parent.parent
src=base/'walker/godot-demo-projects/2d/navigation_astar'
dst=base/'walker-2d-navigation-astar'
assert not dst.exists(),'Resume existing package, never replace it'
assert shutil.disk_usage(base).free>25*1024**3
dst.mkdir();shutil.copytree(src,dst/'godot',ignore=shutil.ignore_patterns('.godot','.git'))
shutil.copy2(base/'walker/godot-demo-projects/LICENSE.md',dst/'LICENSE.md')
(dst/'evidence').mkdir()
files=[]
for f in sorted(src.rglob('*')):
    if not f.is_file() or '.godot' in f.parts or '.git' in f.parts:continue
    rel=f.relative_to(src);digest=hashlib.sha256(f.read_bytes()).hexdigest()
    assert hashlib.sha256((dst/'godot'/rel).read_bytes()).hexdigest()==digest
    files.append(dict(path=str(rel),sha256=digest))
(dst/'evidence/source-copy.json').write_text(json.dumps(dict(source=str(src),files=files),indent=2))
(dst/'AGENTS.md').write_text('''# Walker AStar Navigation

Preserve source, runtime, licenses, prior artifacts and user projects. Local only;
no publishing, push, paid APIs, credential changes, sandbox weakening or deletion.
Keep15GB free reserve. Use isolated normal-input harnesses. Right-click teleport
is a real built-in control: label it as teleport, never evidence of path traversal.
Do not seed character positions or bypass normal pathfinding for gameplay claims.
Machine checks are not human approval. Finish both films unless externally blocked.
''')
(dst/'SOURCES.md').write_text(f'# Source provenance\n\nUnmodified initial copy of {src}. Official Godot demo collection; root MIT license retained. Asset-specific attribution remains to inspect. Hash manifest in evidence/source-copy.json.\n')
(dst/'FRICTIONAL.md').write_text('''# Production evidence

2026-10-05 20:08UTC: item110 started while109 retains both partial films blocked
by shared GateT native PO text-size checks. No item retired. Initial source files
copied/hash-compared. Two scripts read: normal left-click path following,
right-click built-in teleport, obstacle/out-of-bounds rejection, path markers,
arrival clearing and steering. Teleport must be explicitly identified, never
passed off as path traversal. Godot physics120Hz; speed200, mass10, arrival10.
No behavior, capture, film or human approval claimed yet.
''')
with (dst/'evidence/import1.log').open('x') as log:
    result=subprocess.run(['/opt/homebrew/bin/godot','--headless','--editor','--path',str(dst/'godot'),'--import'],stdout=log,stderr=subprocess.STDOUT,timeout=180)
print(f'Copied {len(files)} files; import exit{result.returncode}; {dst}',flush=True)
