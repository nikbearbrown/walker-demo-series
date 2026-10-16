"""Create a new isolated package without touching the upstream demo."""
import hashlib,json,shutil,subprocess
from pathlib import Path
base=Path(__file__).resolve().parent.parent
src=base/'walker/godot-demo-projects/gui/ui_mirroring'
dst=base/'walker-gui-ui-mirroring'
assert not dst.exists()
assert shutil.disk_usage(base).free>15*1024**3
shutil.copytree(src,dst/'godot',ignore=shutil.ignore_patterns('.godot','.git'))
(dst/'evidence').mkdir()
shutil.copy2(base/'walker/godot-demo-projects/LICENSE.md',dst/'LICENSE.md')
manifest=[]
for f in sorted((dst/'godot').rglob('*')):
    if not f.is_file():continue
    rel=f.relative_to(dst/'godot');digest=hashlib.sha256(f.read_bytes()).hexdigest()
    assert digest==hashlib.sha256((src/rel).read_bytes()).hexdigest()
    manifest.append(dict(path=rel.as_posix(),sha256=digest))
(dst/'evidence/source-copy.json').write_text(json.dumps(dict(source=str(src),files=manifest),indent=2))
for name,args in [('import1.log',['--headless','--editor','--import']),('run-smoke1.log',['--headless','--quit-after','120'])]:
    with (dst/'evidence'/name).open('x') as log:
        proc=subprocess.run(['/opt/homebrew/bin/godot','--path',str(dst/'godot'),*args],stdout=log,stderr=subprocess.STDOUT,timeout=180)
    print(name,proc.returncode,flush=True)
    assert proc.returncode==0,name
print('New package copied and headless checks completed; no visual or behavioral approval.',flush=True)
