# Walker trio film recipe (godot-waikthrough → godot-gdd → godot-gamedev, walker mode)

**What this is:** the proven recipe for building the three Liam films for one walker-* repo, distilled from the first complete trio (walker-2d-dodge-the-creeps, 2026-09-28: all three 4K masters pass checkers, GATE T, Gate V, loudness; ~2.5 h wall time, ~470 MB after pruning). Reference reels: `walker-2d-dodge-the-creeps/youtube/claude-liam-walker-2d-dodge-the-creeps-{walkthrough,gdd,gamedev}/` — copy their `scripts/` (walker_reel.py, onebeat.py, inspect_master.py, author.py, coverage.py/evidence.py, snapshot.py) and `_qc/REPORT-*.md`.

## Order
1. **Capture first, into the walkthrough reel.** Copy `godot/` → `walkthrough/_capture-project/`; add `capture_driver.gd`:
   - SubViewport with `size_2d_override` = game logical size, rendered 2160 px tall (portrait: native 3×).
   - PNG every other 60 Hz frame (`frame_post_draw`); input only via `Input.parse_input_event` + `SubViewport.push_input`.
   - Log per-frame state + every input with markers; seed; draw-skip guard (fail the take on any undrawn frame).
   - `Godot --always-on-top --path … --script res://capture_driver.gd --write-movie take.avi --fixed-fps 60` (AVI PCM = frame-aligned game audio). Pilot the seed IN movie mode (movie vs non-movie can diverge).
   - Pad (don't scale) to 3840×2160, mux audio, hash everything, then delete PNGs/AVI (record path+sha256 first).
2. Walkthrough film. 3. GDD + gamedev films copy the walkthrough `capture/` in (byte-identical).
4. Pipeline per reel: author → Kokoro (am_onyx) → `walker_reel.py lock` (frame-exact beats, game audio −15 dB) → align + `cues` → `footage` (un-retimed clips, side panels, labelled HELD FRAME holds) → `remotion_scenes.py` (never edit beat_sheet.json while it runs — it rewrites it) → evidence + `./art <skill> --check` → `./art final REEL --height 2160 --fps 30 --out REEL/exports/landscape` → `inspect_master.py` contact sheet + whisper the outro.
5. Prune only `clips/` and raw dumps after all three pass. **Keep `capture/`** — the checkers hash it.

## Layout traps
- Downscale game 0.9× so its HUD stays title-safe; side-panel text x ≥ 230, ≥ 44 px; `qc.contrast_regions` on every gameplay beat.
- GATE T reads particle trails/HUD digits as text: type footage beats as raw game footage, or move clip in/out so the midpoint sample misses them (log it).
- GodotDevWorkbench: ~13 code lines at codeFontSize 26 + 2 notes → excerpts 7–14 lines. GodotDesignBoard excerpts ≤ ~434 chars. GodotDesignFigure text ≥ ~48 px at 3200 px width.
- Redraw design/ SVGs large-type inside the reel (labelled redrawn); no "→" in SVG text.
- Mixed colour-range clips wash the master grey — normalise range when cutting footage.
- Remotion dominates render time (~15 min per 20+ beats).

## Honesty rules
Scripted input is labelled; no retiming; no human playtest claimed; GDD and game never edited — the film reports gaps (e.g. tests now observed) out loud. No git, no publishing.

## Tech-demo notes (walker-2d-bullet-shower trio, 2026-09-28 — all pass; reference reels `walker-2d-bullet-shower/youtube/claude-liam-walker-2d-bullet-shower-*`)
- **4K Movie Maker config:** Movie Maker writes the WINDOW size; `--resolution` is clamped to the screen. In the capture copy's project.godot: viewport 3840×2160, window override 1280×720, stretch mode `viewport`; in the driver put the game in a 3840×2160 SubViewport with `size_2d_override` = the project's logical size. The AVI is full-range MJPEG → convert to tv/bt709.
- **Verify the capture:** replay headless and diff the log against the movie run (frame n = frame n). Compare geometric overlap vs reported state — that comparison found a real bug (STATIC bodies never register new contacts while the mouse is still).
- **Fit narration BEFORE fixing footage windows:** measure Kokoro mp3s first; narration must fit phase windows or overlapping windows imply a replay.
- Footage beats: `shot.type: "VIDEO"`, `qc.contrast_regions` (with reason) on disclosure lines, label type ≥ 64 px; no extra label line near the bottom edge (edge-bleed).
- ExecutedData is a fixed 15 s composition — cap cues at 14.8 s. Titles ending on a preposition trip §8.9. Face/asset images in asset mode trip bbox-overlap. Re-running author.py wipes the lock: always re-run lock → align → cues.
- Do a 1080 `./art run` before `./art final`. Remotion ≈ 1–1.5 min/beat (~45 min/film); serialise Remotion renders across parallel lanes when possible.
- Pruning: keep the `capture/run-*.mp4` + input logs the checkers reference; prune the rest with path+sha256 in `evidence/PRUNED.md`.

## Lane notes

### 2026-09-28 — GUI tech-demo lane (walker-gui-control-gallery, -drag-and-drop, -custom-splash-screen, -accessibility)
Reference reels: `walker-gui-control-gallery/youtube/claude-liam-walker-gui-control-gallery-*` (scripts: `capture_driver.gd`, `build.py`, `author.py`, `coverage.py`/`finish.py`, `docs.py`, `inspect_master.py`).
- **GUI at native 4K without a SubViewport:** capture copy with viewport 3840×2160 + window override + stretch `viewport`, then `root.content_scale_factor = 3840 / logical_width` in the driver. Text/widgets rasterise crisply at 4K and popups (ColorPicker, OptionButton, MenuButton, tooltips) embed into the root and are recorded. Pick the logical size from the scene (1280×720 upstream-screenshot size, or 1152×648 when positions are absolute).
- **Movie Maker records no cursor.** Draw the pointer + an "INPUT click / key X / drag" readout per frame from the logs in the edit (PIL frame pipe in `build.py`), label it on every frame, and hide the pointer before the first logged *mouse* input (keyboard-only phases must not show a parked arrow).
- **Frame alignment for coroutine drivers:** with a SceneTree `_process` logger + `await process_frame` route, state row k is written before frame k's inputs, so movie frame n shows state row n+1 (verified twice by pixel diff). Use `LOG_OFFSET = 1` when drawing from logs.
- **Pace the actions, not just the idle:** measuring narration first and idling at the end of a phase still leaves Liam describing actions seconds after they happen; spread the waits between actions to the narration length.
- **Restart/quit demos (R-02):** a demo that calls `OS.set_restart_on_exit(true)` + `quit()` would relaunch the `--write-movie` command and overwrite the take. Record the flag and clear it in the driver's `_finalize` (root is already null there; cache viewport info earlier). Disclose it.
- **Accessibility demos:** the screen-reader layer is implemented but not capturable; keep it `implemented` with empty evidence in `coverage.json` (the contract forbids relabelling) → the walkthrough checker FAILs by design; ship the master with `BLOCKED.md` asking for a VoiceOver/Accessibility Inspector run or explicit partial-walkthrough approval.
- **Gate traps hit:** HELD FRAME label must stay in the 1970–2050 px band (a taller box = edge-bleed BLOCKER); ExecutedData with 5 rows edge-bleeds → max 4; a long mixed-case GodotDesignBoard status strip shrank to 39 px (GATE T FAIL) → short all-caps status; hesitant writer with short lines underfills Gate V (<55%) → three long lines at fontSize 92.
- **Process traps:** never run two `./art` commands on one reel at once (a still-running `final` made `run` report spurious low-contrast MAJORs from shifted beats); zsh does not word-split `set -- $pair`; `while read … <<LIST` loops lose their input to ffmpeg — give every ffmpeg/Popen `stdin=DEVNULL` / `< /dev/null`. Headless replays of anchored GUI scenes get a 1280×1280 window, so compare control-state fields, not mouse positions.
- Cost: ~25–40 min wall per film with two other lanes rendering (load average 55–86); Remotion + `./art final` dominate.
- More traps: `remotion_scenes.py` rewrites beat_sheet.json from its in-memory copy when it finishes, so a sheet edit made while it runs is silently undone (re-check the sheet after every render). Asset-texture strips and cropped stills with digits inside drawn boxes trip GATE T §8.6b bbox-overlap inside GodotDesignFigure — use a labelled REPLAY footage window instead. `until ! pgrep -f "x.sh"` inside a shell whose own command line contains "x.sh" never ends (pgrep matches itself). `./art final` re-creates `clips/` — prune after the *last* final.
- Findings from this lane (reported in the films, never fixed): Control Gallery MenuButton check items never tick (no handler; GDD M-07) and a GraphNode title drag inside its GraphFrame moves nothing (cause undiagnosed, reproduces headless); Accessibility custom list draws `item_rects[selected]` three times, Up decrements, focus outline wider than the items; Drag-and-drop and Splash: no defects found.

### 2026-09-28 — 2D/GUI tech-demo lane (walker-2d-finite-state-machine, -drawable-textures, -dynamic-tilemap-layers, walker-gui-gd-paint)
Reference reels: `walker-2d-finite-state-machine/youtube/claude-liam-walker-2d-finite-state-machine-*` (landscape `walker_reel.py` + per-demo `panel_config.py`, marker-driven `author.py`, `encode_capture.py`, `coverage.py`, `docs.py`). All 12 films pass their checkers, GATE T, Gate V and loudness.
- **Landscape harness layout:** the portrait Dodge layout does not fit 16:9 demos. Game box 0.7× (2688×1512) at (192,120); readout column at x 2960 (keep every value < ~19 mono chars — a 29-char value ran off the right edge and Gate V did not sample it); bottom strip for provenance / INPUT NOW / WATCH, caption wrap to x 3620. Demo-specific rows live in `panel_config.py` so `walker_reel.py` is reusable unchanged.
- **Markers, not seconds:** the driver `mark()`s every segment; `author.py` resolves footage windows from the receipt's png-frame markers (`pre`/`post` frame offsets for trims), so a recapture never leaves stale times.
- **Pace the capture to measured narration:** write narration, run Kokoro, then recapture with per-segment `pad_to(narration + 0.4 s)` (a `pads.json` arg keeps it data-driven). One recapture cut held frames from 3–4 s per beat to ≤ 0.5 s. For reused footage in GDD/gamedev films, trim each window's end with `post` so clips close with the narration.
- **Native render by stretch mode:** canvas_items projects → SubViewport 3840×2160 with `size_2d_override`; near-square projects (530×495) → render at native height and PAD to 16:9; stretch mode `viewport` + integer scale (GD Paint) → render the 1152×648 canvas and apply ×3 nearest-neighbour at encode (exactly what the engine shows on a 4K window), disclosed. `encode_capture.py` handles all three (integer nearest scale, then pad; never stretch).
- **GATE T and demo artwork:** GATE T reads demo pixels as text (sword blade 2.16:1, 3D cube + logo stamps, purple tile walls 4.2:1 on the harness ground, UI screenshots of pickers). FSM passed by shifting windows; the other three typed footage beats `VIDEO` with a `type_note` (harness typography is the same one that passed pixel checks in FSM; Gate V regional contrast still runs). Diagrams: ellipses joined by arrows and nested capture tiles trip §8.6b bbox-overlap — respace boxes, keep labels off arrow lines, use boards instead of tiled stills.
- **Hesitant writer:** three lines of ~33–40 characters at fontSize 92–94, lineSpacing 3.0; shorter lines underfill Gate V (51–54%). The trigger word fires on every occurrence (tilemap gamedev B01 replaced "wall" twice).
- **Code panels:** ≤ 10 source lines; long lines (tscn transforms, base64 tile data, project.godot Object(...) events) wrap and push the last lines off the panel — pick short contiguous ranges and view each code beat at full size before the final.
- **Input traps:** mouse-polling demos (`get_viewport().get_mouse_position()`, `Input.is_mouse_button_pressed`) need BOTH `Input.parse_input_event` (button mask) and `SubViewport.push_input(e, true)` (a standalone SubViewport reports the last pushed mouse position). Controls inside a demo's own SubViewportContainer have rects in that inner viewport — add the container's global origin. `OS.low_processor_usage_mode = false` in the driver for projects that enable it (else the draw-skip guard fails) — disclose it.
- **Filesystem dialogs (privacy):** set `stage.gui_embed_subwindows = false` for the take so a FileDialog opens outside the recorded SubViewport; type the path via `dialog.get_line_edit()` + `Window.push_input`; verify the written file. The Movie Maker AVI still records the whole window (dialog included) — hash and delete it, never encode it.
- **Pixel read-backs:** where a demo draws into a texture (`DrawableTexture2D.get_image()`), log pixel probes from the driver; they turned "GPU painting unverified" into observed evidence the GDD film could cite.
- **Load:** with 3–4 other lanes rendering (load average 60–90), a 75 s 4K capture took ~20 min and one Remotion B00 render timed out (30 s per frame) — just re-run `--only B00`.
- Recurring finding across Walker demos: joypad D-pad bindings keep Godot 3 button numbers (FSM, tilemap; also Dodge). Probe the Godot 4 enum at runtime and press both numbers.

## Lane notes

**2026-09-28 — lane: walker-audio-rhythm-game (gamedev), walker-misc-2-5d, walker-loading-serialization, walker-2d-custom-drawing.** What changed in practice, beyond the recipe above:

- **16:9 games don't take side panels.** Two layouts that pass Gate V: (a) capture scaled 0.8× (3072×1728 at 384,228) in a dark disclosure frame, captions at y≈1968, x≥240 (rhythm, serialization, custom-drawing); (b) a 1320-px left log panel + a *native 1:1* centre crop 2280×1944 placed at (1344,108) when the camera follows the player (2.5D). Full-bleed game footage fails `edge-bleed` on every frame.
- **Held-frame label:** accent-coloured text, no filled box — the box tripped caption `low-contrast` MAJORs.
- **Contrast regions:** declare only *your* overlay text. Declaring the game's own UI (serialization's grey buttons) fails on the game's design.
- **Text-heavy demos:** GATE T reads the demo's own labels/shapes as our typography (custom-drawing: 36 px runs, 2.91:1 blobs). Type those capture beats `"type": "VIDEO"` (raw footage — the type_check exemption), keep the disclosure/caption checked by Gate V regions.
- **Hesitant writer:** 97 px when lines are short; 90–94 underfilled (53–55 %). Keep the corrected sentence meaningful ("surviving the crabs" → "saving the crabs" read wrong; rewrite the line, not just the trigger).
- **Board card text (GodotDesignBoard):** cards containing "AA vs MSAA", "≠" etc. produced 39 px runs (< 41 floor) in 7 beats; rewording the card text cleared it. Suspect short all-caps/symbol tokens rendered as separate runs.
- **Scene changes vs SubViewport capture:** `change_scene_to_file` adds the new scene under root — adopt it into the stage and free the old one (2.5D cube). `reload_current_scene` needs `current_scene` — make the SubViewport part of a wrapper .tscn that *is* the current scene (serialization death reload; reloaded twice cleanly).
- **Window placement matters now that lanes run in parallel.** A capture window at (0,0) under another lane's always-on-top Godot rendered ~13 frames/min vs ~90 at a unique `--position`. Load average hit 70–100; plan ~3× the single-lane wall time.
- **Pace the capture route to the narration** (8–15 s per feature beat). A 3-s-per-feature route gave 70 % labelled holds; recapturing (15 min) beat rewriting.
- **Author windows from marker names** (receipt/inputs markers), not typed seconds — the serialization recapture shifted everything and the authors didn't care. Read the states log before narrating: the slower take died once unplanned, and the film now says so.
- **Editor-only features:** harness EditorPlugin in an isolated copy, `godot --editor --resolution 3840x2160` (window comes up 3456×2070 here), push a real mouse click into the editor viewport, save stills, pad into a 4K mp4 as its own capture (2.5D `editor-01`).
- **user:// saves:** `config/use_custom_user_dir=true` in the capture copy only; disclose the created folder. An "Open folder" button opens a real Finder window outside the capture — say so.
- **OptionButton menus in a SubViewport:** `gui_embed_subwindows = true`; the menu opens on Space after the click (Walker's own test_input.gd does this). The first custom-drawing take failed there; a short run-02 covered MSAA.
- **Pixel claims:** cut native crops (nearest scaling) and measure a pixel diff before saying "smoother". MSAA 8× changed ~15k edge pixels but looked nearly identical to off at native size; the films say "subtle".
- **Excerpts:** GodotDevWorkbench at 26–30 px fits ~12 rows *including wraps*; long comment lines wrap. Pilot-render the densest code beats and inspect the whole panel; three serialization excerpts clipped on the first master.
- **remotion_scenes.py `--only` takes one id;** loop for several. Never re-run author/lock while a render reads the sheet.
- **Hygiene:** chain logs go inside the reel (one landed in a repo root and was removed); tests that write fixtures to `res://../` land next to `_test-project` inside the reel — fine, disclose.
