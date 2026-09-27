"""Record verified Pong masters and seed the next standalone demo without overwrites."""
from pathlib import Path
import json, hashlib, shutil, subprocess
base = Path(__file__).resolve().parent
books = base.parent
queue = json.loads((base/'queue.json').read_text())
outputs = {}
for kind in ('walkthrough', 'gamedev'):
    reel = books/'walker-pong/youtube'/f'claude-liam-walker-pong-{kind}'
    state = json.loads((reel/'build-state.json').read_text())
    master = Path(state['output'])
    assert state['status'] == 'ready' and master.is_file()
    sha = hashlib.sha256(master.read_bytes()).hexdigest()
    assert sha == state['sha256']
    probe = json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-of','json',str(master)]))
    assert any(s.get('width') == 3840 and s.get('height') == 2160 for s in probe['streams'])
    assert any(s['codec_type'] == 'audio' for s in probe['streams'])
    outputs[kind] = dict(path=str(master), sha256=sha, duration_s=state['duration_s'])
pong = queue['items'][0]
pong.update(stage='review_ready', walkthrough='review_ready', gamedev='review_ready',
    outputs=outputs, human_review='pending', next_action='Both native 4K films exported and inspected; human review remains separate. Delivered in the preceding user turn.')
dest = books/'walker-3d-platformer'
src = books/'walker/godot-demo-projects/3d/platformer'
if not dest.exists():
    dest.mkdir()
    shutil.copytree(src, dest/'godot', ignore=shutil.ignore_patterns('.godot','.git','.DS_Store'))
    shutil.copy2(books/'walker/godot-demo-projects/LICENSE.md',dest/'LICENSE.md')
    (dest/'evidence').mkdir()
    files = [{ 'path':str(p.relative_to(src)), 'sha256':hashlib.sha256(p.read_bytes()).hexdigest() }
             for p in sorted(src.rglob('*')) if p.is_file() and '.godot' not in p.parts and '.git' not in p.parts and p.name != '.DS_Store']
    (dest/'evidence/upstream-snapshot.json').write_text(json.dumps(dict(source=str(src),commit=queue['source_commit'],files=files),indent=2)+'\n')
queue['items'][1].update(stage='source-inspection',next_action='Read runtime system, import local adaptation and verify behavior before recording. No films yet.')
(base/'queue.json').write_text(json.dumps(queue,indent=2)+'\n')
print('Pong masters hash/4K/audio verified; next demo copied without overwriting originals.')
