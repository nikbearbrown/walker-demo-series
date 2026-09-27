# Walker demo series — Series Design Document (recovered)

| | |
|---|---|
| Version | 0.1.0-recovered |
| Date | 2026-09-27 |
| Author | Zelda (agent, silent), for Nik Bear Brown |
| Mode | recovered, silent — series ledger, not a game |
| Revision | 1 |
| Gates | vision ○ · systems ○ · world ○ · scope ○ — gate — unsigned at time of writing |
| Sources read | `README.md`, `STATUS.md`, `queue.json`, `RHYTHM-SOURCE-AUDIT.md`, `advance_platformer.py`, all nine `*-preflight.md`, and the first paragraph of every sibling `walker-*` README |

## Executive summary

**What it is.** The Walker demo series is a production ledger, not a game. It takes every Godot demo project in the local checkout of the official demo collection (139 of them) and turns each into its own standalone `walker-*` project, then into two native-4K films narrated by Liam: a walkthrough and a separate development film. `[OBSERVED README.md; queue.json total=139]`

**Why it is in Walker.** Walker needs a large, honest body of working Godot projects to teach from and to film. Adapting the official demos, with their licenses and assets preserved, gives it that body without inventing games. `[INFERRED from README.md and the sibling READMEs; the purpose is not written in one sentence anywhere — MISSING]`

**What was found.** As of `queue.json` on 2026-09-27: 67 of 139 items have been started; 58 have their own sibling folder. One item (`walker-pong`) is machine review-ready with both films; one (`walker-3d-platformer`) is in film production; 52 have passed import; 13 are blocked on external setup (XR headset, .NET SDK, WebRTC native extension, HDR display, mobile sensors, Android billing). Human review is pending for all 139. Every sibling folder is described in the index below. `[OBSERVED queue.json]`

Provenance tags: `[OBSERVED file]` a file here says this · `[INFERRED]` strongly implied; evidence given · `[MISSING]` nothing in the folder says this. This document describes what exists; it approves nothing.

## 1. Series purpose

- Inventory every `project.godot` from the source checkout; keep each project in a separate sibling `walker-*` directory. `[OBSERVED README.md]`
- Source: `walker/godot-demo-projects` at commit `a3b5c113112f77291d5f3d1360f33a882fdc52f7`; destination: the `books/` folder. `[OBSERVED queue.json source_root, source_commit, destination_root]`
- Order: Pong, 3D Platformer, Audio Rhythm Game, then round-robin through all categories until exhausted. `[OBSERVED README.md]` The queue's 13 categories: 3d 32, 2d 27, gui 15, misc 12, xr 10, audio 9, networking 7, viewport 7, loading 6, mono 6, mobile 4, compute 3, plugins 1. `[OBSERVED queue.json items[].source]`
- Naming: Pong is `walker-pong`; others carry their source category to avoid collisions. `[OBSERVED README.md]`
- Audience for the films. `[MISSING]` No file names the viewer (students, Godot learners, general YouTube). Q-S01.
- Why "Walker" wants 278 films. `[MISSING]` "278 requested films" is recorded `[OBSERVED STATUS.md historical notes]`; the reason, and whether all 278 are still wanted, is not. Q-S02.

## 2. Series rules (these are the pillars)

The series has no pillars under that name, but its README states hard rules that do the same job. `[OBSERVED README.md]`

| ID | Rule | Source |
|---|---|---|
| R-S1 | Real evidence only: genuine capture, normal input paths, original gameplay speed; separate capture copies | README.md, Series rules |
| R-S2 | Machine review-ready is not human approval; `queue.json` is a status ledger, not evidence of completion | README.md, Series rules |
| R-S3 | Preserve everything: existing work, originals, source licenses, UIDs/import settings, provenance; never overwrite a project to advance the queue | README.md, Series rules |
| R-S4 | Hardware-dependent XR/mobile/gamepad demonstrations stay explicitly unverified without hardware | README.md, Series rules |
| R-S5 | C# demos are their own entries; never relabel a GDScript copy as a C# demonstration | README.md, Series rules |
| R-S6 | Keep a 15 GB free-disk reserve; never delete or compress away evidence to make room | README.md, Series rules |
| R-S7 | Local Kokoro only; no paid APIs, Shorts, or YouTube publishing under this series request | README.md, Series rules |
| R-S8 | Each focused code excerpt immediately precedes its visible result; keep the regular outro | README.md, Series rules |

GitHub pushes were also excluded by README.md. On 2026-09-27 Nik Bear Brown explicitly authorized creating GitHub repos and pushing every `walker-*` folder; that supersedes the push exclusion for that action only. YouTube publishing remains unauthorized. `[OBSERVED — authorization recorded in README.md, 2026-09-27]`

## 3. Pipeline (per item)

`[OBSERVED README.md; queue.json stage values; STATUS.md]`

1. **Source and license inspection** — read README, config, all scripts; record licenses and attributions. Blocked items get a `*-preflight.md` here instead of a copy (nine exist).
2. **Bounded Walker adaptation** — an independent copy with a title change; any production fix is named in the project README.
3. **Engine import, run and behavior checks** — Godot 4.7.2 headless import, then normal-input harness checks. Queue stages: `import-passed`, `import-passed-runtime-warning`, or `external-setup-pending`.
4. **Genuine capture** — native 4K, real input, original speed; budget disk first.
5. **4K Liam walkthrough film.**
6. **Separate 4K Liam development film** — code excerpt, then its visible result.
7. **Machine review-ready** — both MP4s exist, hashes and native-4K dimensions match, skill checks pass, actual frames/event sequences inspected. Stage `review_ready`.
8. **Human review** — separate from 7; pending for every item.

Finish both films before taking the next item unless an external dependency blocks it; record the blocker, move on, revisit. `[OBSERVED README.md]` In practice only items 1–2 have reached the film stages; items 3–67 have been advanced through steps 1–3 while films wait. `[INFERRED queue.json: walkthrough=pending for 137 items]` Q-S03.

`advance_platformer.py` is the one-off script that recorded Pong's verified masters (hash, 4K, audio) into `queue.json` and seeded `walker-3d-platformer` without overwriting. `[OBSERVED advance_platformer.py:1-34]`

## 4. Status (from queue.json, 2026-09-27)

| Stage | Count |
|---|---|
| `review_ready` (machine) | 1 — walker-pong |
| `film-production` | 1 — walker-3d-platformer (listening pending) |
| `import-passed` | 50 |
| `import-passed-runtime-warning` | 2 |
| `external-setup-pending` | 13 (4 with a folder, 9 preflight-only) |
| `pending` (not started) | 72 |
| **Human review done** | **0 of 139** |

External blockers by kind: OpenXR headset/runtime (3 xr items), .NET SDK / GodotSharp (5 mono items), native WebRTC extension (2), HDR-capable display (1), physical mobile sensors (1), Android billing plugin (1). A separate visible-capture permission constraint is also recorded in several preflights and READMEs. `[OBSERVED queue.json; *-preflight.md; walker-gui-bidi-and-font-features/README.md]`

## 5. Project index

Every sibling `walker-*` folder under `books/` except the bare `walker` framework folder. Descriptions are condensed from each project's own README first paragraph; the stage column is that project's `queue.json` entry. Repository and GDD links point at `github.com/nikbearbrown/<name>`; a GDD link resolves only once that repository has a root `GDD.md`.

| # | Project | What it is | Queue | Repo | GDD |
|---|---|---|---|---|---|
| 1 | `walker-2d-bullet-shower` | One script moves 500 collision objects through physics-server RIDs and a single draw loop; a teaching demo. | #4 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-2d-bullet-shower) | [GDD.md](https://github.com/nikbearbrown/walker-2d-bullet-shower/blob/main/GDD.md) |
| 2 | `walker-2d-custom-drawing` | Seven-tab gallery of immediate-mode 2D drawing calls; reference for drawing without nodes and for antialiasing vs 2D MSAA. | #17 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-2d-custom-drawing) | [GDD.md](https://github.com/nikbearbrown/walker-2d-custom-drawing/blob/main/GDD.md) |
| 3 | `walker-2d-dodge-the-creeps` | The finished "Your first 2D game" tutorial game: dodge the creeps, score is time survived. | #29 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-2d-dodge-the-creeps) | [GDD.md](https://github.com/nikbearbrown/walker-2d-dodge-the-creeps/blob/main/GDD.md) |
| 4 | `walker-2d-drawable-textures` | Paint on a 2D canvas and see the same texture live on a 3D mesh (`DrawableTexture2D`). | #41 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-2d-drawable-textures) | [GDD.md](https://github.com/nikbearbrown/walker-2d-drawable-textures/blob/main/GDD.md) |
| 5 | `walker-2d-dynamic-tilemap-layers` | Title-only copy of Godot `2d/dynamic_tilemap_layers`; original assets, scripts and license retained. | #52 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-2d-dynamic-tilemap-layers) | [GDD.md](https://github.com/nikbearbrown/walker-2d-dynamic-tilemap-layers/blob/main/GDD.md) |
| 6 | `walker-2d-finite-state-machine` | Local adaptation of Godot `2d/finite_state_machine`; upstream MIT license, README and assets retained. | #62 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-2d-finite-state-machine) | [GDD.md](https://github.com/nikbearbrown/walker-2d-finite-state-machine/blob/main/GDD.md) |
| 7 | `walker-3d-antialiasing` | One scene of 21 rendering specimens for comparing 3D antialiasing modes. | #5 · `import-passed-runtime-warning` | [repo](https://github.com/nikbearbrown/walker-3d-antialiasing) | [GDD.md](https://github.com/nikbearbrown/walker-3d-antialiasing/blob/main/GDD.md) |
| 8 | `walker-3d-csg` | Title-only adaptation of Godot `3d/csg` (constructive solid geometry); checker texture CC0. | #18 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-3d-csg) | [GDD.md](https://github.com/nikbearbrown/walker-3d-csg/blob/main/GDD.md) |
| 9 | `walker-3d-decals` | Title-only adaptation of Godot `3d/decals`; original assets and UIDs retained. | #30 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-3d-decals) | [GDD.md](https://github.com/nikbearbrown/walker-3d-decals/blob/main/GDD.md) |
| 10 | `walker-3d-global-illumination` | Title-only copy of Godot `3d/global_illumination`, bake data retained. | #42 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-3d-global-illumination) | [GDD.md](https://github.com/nikbearbrown/walker-3d-global-illumination/blob/main/GDD.md) |
| 11 | `walker-3d-graphics-settings` | Local adaptation of Godot `3d/graphics_settings`; title change only. | #53 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-3d-graphics-settings) | [GDD.md](https://github.com/nikbearbrown/walker-3d-graphics-settings/blob/main/GDD.md) |
| 12 | `walker-3d-ik` | Local copy of Godot `3d/ik` with a title change and a FABRIK scheduling correction. | #63 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-3d-ik) | [GDD.md](https://github.com/nikbearbrown/walker-3d-ik/blob/main/GDD.md) |
| 13 | `walker-3d-platformer` | Walker adaptation of Godot's official 3D Platformer demo; gameplay and assets retained; films in production. | #2 · `film-production` | [repo](https://github.com/nikbearbrown/walker-3d-platformer) | [GDD.md](https://github.com/nikbearbrown/walker-3d-platformer/blob/main/GDD.md) |
| 14 | `walker-audio-audio-effects` | Tech demo: music, seven sound buttons and 18 effect toggles on the Master bus. | #6 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-audio-audio-effects) | [GDD.md](https://github.com/nikbearbrown/walker-audio-audio-effects/blob/main/GDD.md) |
| 15 | `walker-audio-bpm-sync` | Title-only adaptation of Godot `audio/bpm_sync`. | #19 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-audio-bpm-sync) | [GDD.md](https://github.com/nikbearbrown/walker-audio-bpm-sync/blob/main/GDD.md) |
| 16 | `walker-audio-device-changer` | Title-only adaptation of Godot `audio/device_changer`. | #31 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-audio-device-changer) | [GDD.md](https://github.com/nikbearbrown/walker-audio-device-changer/blob/main/GDD.md) |
| 17 | `walker-audio-generator` | Title-only adaptation of Godot `audio/generator`, plus a local test harness. | #43 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-audio-generator) | [GDD.md](https://github.com/nikbearbrown/walker-audio-generator/blob/main/GDD.md) |
| 18 | `walker-audio-mic-record` | Copy of Godot `audio/mic_record`; title change only. | #54 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-audio-mic-record) | [GDD.md](https://github.com/nikbearbrown/walker-audio-mic-record/blob/main/GDD.md) |
| 19 | `walker-audio-midi-piano` | Copy of Godot `audio/midi_piano` with a title change and MIDI message filtering. | #64 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-audio-midi-piano) | [GDD.md](https://github.com/nikbearbrown/walker-audio-midi-piano/blob/main/GDD.md) |
| 20 | `walker-audio-rhythm-game` | Adaptation in progress of Godot `audio/rhythm_game`: Space hits a note, R restarts, P or Escape pauses. | #3 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-audio-rhythm-game) | [GDD.md](https://github.com/nikbearbrown/walker-audio-rhythm-game/blob/main/GDD.md) |
| 21 | `walker-compute-heightmap` | Title-only adaptation of Godot `compute/heightmap`. | #7 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-compute-heightmap) | [GDD.md](https://github.com/nikbearbrown/walker-compute-heightmap/blob/main/GDD.md) |
| 22 | `walker-compute-post-shader` | Title-only adaptation of Godot `compute/post_shader`. | #20 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-compute-post-shader) | [GDD.md](https://github.com/nikbearbrown/walker-compute-post-shader/blob/main/GDD.md) |
| 23 | `walker-compute-texture` | Local adaptation of Godot `compute/texture`. | #32 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-compute-texture) | [GDD.md](https://github.com/nikbearbrown/walker-compute-texture/blob/main/GDD.md) |
| 24 | `walker-gui-accessibility` | Adaptation of Godot `gui/accessibility`; upstream unchanged. | #8 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-gui-accessibility) | [GDD.md](https://github.com/nikbearbrown/walker-gui-accessibility/blob/main/GDD.md) |
| 25 | `walker-gui-bidi-and-font-features` | Local adaptation of Godot `gui/bidi_and_font_features`. | #21 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-gui-bidi-and-font-features) | [GDD.md](https://github.com/nikbearbrown/walker-gui-bidi-and-font-features/blob/main/GDD.md) |
| 26 | `walker-gui-control-gallery` | One screen showing Godot's Control nodes, each labeled with its name; a tech demo. | #33 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-gui-control-gallery) | [GDD.md](https://github.com/nikbearbrown/walker-gui-control-gallery/blob/main/GDD.md) |
| 27 | `walker-gui-custom-splash-screen` | Title-only copy of Godot `gui/custom_splash_screen`; original branding retained, no endorsement implied. | #44 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-gui-custom-splash-screen) | [GDD.md](https://github.com/nikbearbrown/walker-gui-custom-splash-screen/blob/main/GDD.md) |
| 28 | `walker-gui-drag-and-drop` | Copy of Godot `gui/drag_and_drop`; title change only. | #55 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-gui-drag-and-drop) | [GDD.md](https://github.com/nikbearbrown/walker-gui-drag-and-drop/blob/main/GDD.md) |
| 29 | `walker-gui-gd-paint` | Local adaptation of Godot `gui/gd_paint`; title change only. | #65 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-gui-gd-paint) | [GDD.md](https://github.com/nikbearbrown/walker-gui-gd-paint/blob/main/GDD.md) |
| 30 | `walker-jumpman-clawd` | Not a demo adaptation: Walker's own platformer, iteration 1 of Clawd in the First Steps level. | not in queue | [repo](https://github.com/nikbearbrown/walker-jumpman-clawd) | [GDD.md](https://github.com/nikbearbrown/walker-jumpman-clawd/blob/main/GDD.md) |
| 31 | `walker-loading-autoload` | Adaptation of Godot `loading/autoload`; title changed, upstream unmodified. | #9 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-loading-autoload) | [GDD.md](https://github.com/nikbearbrown/walker-loading-autoload/blob/main/GDD.md) |
| 32 | `walker-loading-load-threaded` | Local copy of Godot `loading/load_threaded`. | #22 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-loading-load-threaded) | [GDD.md](https://github.com/nikbearbrown/walker-loading-load-threaded/blob/main/GDD.md) |
| 33 | `walker-loading-runtime-save-load` | Copy of Godot `loading/runtime_save_load` with local preview, export and error-handling changes. | #34 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-loading-runtime-save-load) | [GDD.md](https://github.com/nikbearbrown/walker-loading-runtime-save-load/blob/main/GDD.md) |
| 34 | `walker-loading-scene-changer` | Two scenes, one button each, switching via `change_scene_to_file()` and `change_scene_to_packed()`; a tech demo. | #45 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-loading-scene-changer) | [GDD.md](https://github.com/nikbearbrown/walker-loading-scene-changer/blob/main/GDD.md) |
| 35 | `walker-loading-serialization` | Local copy of Godot `loading/serialization` with serializer file-error guards. | #56 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-loading-serialization) | [GDD.md](https://github.com/nikbearbrown/walker-loading-serialization/blob/main/GDD.md) |
| 36 | `walker-loading-threads` | Local adaptation of Godot `loading/threads`. | #66 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-loading-threads) | [GDD.md](https://github.com/nikbearbrown/walker-loading-threads/blob/main/GDD.md) |
| 37 | `walker-misc-2-5d` | GDScript adaptation of Godot `misc/2.5d`; title-only initial change. | #10 · `import-passed-runtime-warning` | [repo](https://github.com/nikbearbrown/walker-misc-2-5d) | [GDD.md](https://github.com/nikbearbrown/walker-misc-2-5d/blob/main/GDD.md) |
| 38 | `walker-misc-custom-logging` | Local adaptation of Godot `misc/custom_logging`. | #23 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-misc-custom-logging) | [GDD.md](https://github.com/nikbearbrown/walker-misc-custom-logging/blob/main/GDD.md) |
| 39 | `walker-misc-graphics-tablet-input` | Drawing canvas for pen pressure and tilt, with latency settings in a sidebar; a tech demo. | #35 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-misc-graphics-tablet-input) | [GDD.md](https://github.com/nikbearbrown/walker-misc-graphics-tablet-input/blob/main/GDD.md) |
| 40 | `walker-misc-hdr-output` | Title-only copy of Godot `misc/hdr_output`; third-party art credits retained in its README. | #46 · `external-setup-pending` | [repo](https://github.com/nikbearbrown/walker-misc-hdr-output) | [GDD.md](https://github.com/nikbearbrown/walker-misc-hdr-output/blob/main/GDD.md) |
| 41 | `walker-misc-joypads` | Copy of Godot `misc/joypads`; title change only; source attribution preserved. | #57 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-misc-joypads) | [GDD.md](https://github.com/nikbearbrown/walker-misc-joypads/blob/main/GDD.md) |
| 42 | `walker-misc-large-world-coordinates` | Local adaptation of Godot `misc/large_world_coordinates`. | #67 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-misc-large-world-coordinates) | [GDD.md](https://github.com/nikbearbrown/walker-misc-large-world-coordinates/blob/main/GDD.md) |
| 43 | `walker-mobile-multitouch-cubes` | Local adaptation of Godot `mobile/multitouch_cubes`. | #24 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-mobile-multitouch-cubes) | [GDD.md](https://github.com/nikbearbrown/walker-mobile-multitouch-cubes/blob/main/GDD.md) |
| 44 | `walker-mobile-multitouch-view` | Title-only adaptation of Godot `mobile/multitouch_view`. | #36 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-mobile-multitouch-view) | [GDD.md](https://github.com/nikbearbrown/walker-mobile-multitouch-view/blob/main/GDD.md) |
| 45 | `walker-mobile-sensors` | Title-only copy of Godot `mobile/sensors`. | #47 · `external-setup-pending` | [repo](https://github.com/nikbearbrown/walker-mobile-sensors) | [GDD.md](https://github.com/nikbearbrown/walker-mobile-sensors/blob/main/GDD.md) |
| 46 | `walker-networking-multiplayer-bomber` | Adaptation of Godot `networking/multiplayer_bomber`; upstream untouched. | #12 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-networking-multiplayer-bomber) | [GDD.md](https://github.com/nikbearbrown/walker-networking-multiplayer-bomber/blob/main/GDD.md) |
| 47 | `walker-networking-multiplayer-pong` | Local copy of Godot `networking/multiplayer_pong`. | #25 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-networking-multiplayer-pong) | [GDD.md](https://github.com/nikbearbrown/walker-networking-multiplayer-pong/blob/main/GDD.md) |
| 48 | `walker-networking-webrtc-minimal` | Title-only copy of Godot `networking/webrtc_minimal`. | #37 · `external-setup-pending` | [repo](https://github.com/nikbearbrown/walker-networking-webrtc-minimal) | [GDD.md](https://github.com/nikbearbrown/walker-networking-webrtc-minimal/blob/main/GDD.md) |
| 49 | `walker-networking-websocket-chat` | One window with a WebSocket server panel and three client panels chatting through it; a tech demo. | #58 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-networking-websocket-chat) | [GDD.md](https://github.com/nikbearbrown/walker-networking-websocket-chat/blob/main/GDD.md) |
| 50 | `walker-plugins` | Adaptation of Godot `plugins`: four editor-plugin demonstrations. | #16 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-plugins) | [GDD.md](https://github.com/nikbearbrown/walker-plugins/blob/main/GDD.md) |
| 51 | `walker-pong` | The first series entry: two-player local Pong with upstream gameplay preserved. | #1 · `review_ready` | [repo](https://github.com/nikbearbrown/walker-pong) | [GDD.md](https://github.com/nikbearbrown/walker-pong/blob/main/GDD.md) |
| 52 | `walker-viewport-2d-in-3d` | Adaptation of Godot `viewport/2d_in_3d`. | #13 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-viewport-2d-in-3d) | [GDD.md](https://github.com/nikbearbrown/walker-viewport-2d-in-3d/blob/main/GDD.md) |
| 53 | `walker-viewport-3d-in-2d` | A 3D robot rendered into a `SubViewport` and shown as a 2D sprite; a rendering tech demo. | #26 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-viewport-3d-in-2d) | [GDD.md](https://github.com/nikbearbrown/walker-viewport-3d-in-2d/blob/main/GDD.md) |
| 54 | `walker-viewport-3d-scaling` | Title-only copy of Godot `viewport/3d_scaling`. | #38 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-viewport-3d-scaling) | [GDD.md](https://github.com/nikbearbrown/walker-viewport-3d-scaling/blob/main/GDD.md) |
| 55 | `walker-viewport-dynamic-split-screen` | Title-only copy of Godot `viewport/dynamic_split_screen`. | #49 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-viewport-dynamic-split-screen) | [GDD.md](https://github.com/nikbearbrown/walker-viewport-dynamic-split-screen/blob/main/GDD.md) |
| 56 | `walker-viewport-gui-in-3d` | Copy of Godot `viewport/gui_in_3d` with local input-routing changes. | #59 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-viewport-gui-in-3d) | [GDD.md](https://github.com/nikbearbrown/walker-viewport-gui-in-3d/blob/main/GDD.md) |
| 57 | `walker-xr-mobile-vr-interface-demo` | Title-only copy of Godot `xr/mobile_vr_interface_demo`. | #14 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-xr-mobile-vr-interface-demo) | [GDD.md](https://github.com/nikbearbrown/walker-xr-mobile-vr-interface-demo/blob/main/GDD.md) |
| 58 | `walker-xr-openxr-binding-modifier-demo` | Title-only adaptation of Godot `xr/openxr_binding_modifier_demo`. | #27 · `import-passed` | [repo](https://github.com/nikbearbrown/walker-xr-openxr-binding-modifier-demo) | [GDD.md](https://github.com/nikbearbrown/walker-xr-openxr-binding-modifier-demo/blob/main/GDD.md) |
| 59 | `walker-xr-openxr-character-centric-movement` | XR tech demo: the body follows the tracked head; a blocked body blacks out the view. Imports; no headset to run it. | #39 · `external-setup-pending` | [repo](https://github.com/nikbearbrown/walker-xr-openxr-character-centric-movement) | [GDD.md](https://github.com/nikbearbrown/walker-xr-openxr-character-centric-movement/blob/main/GDD.md) |

## 6. Open questions

Kept in [design/decisions.md](design/decisions.md): Q-S01 audience · Q-S02 are all 278 films still wanted · Q-S03 films-first vs import-first · Q-S04 hardware for the 13 blocked items · Q-S05 visible-capture permission · Q-S06 who performs human review, and what "approved" means · Q-S07 GitHub repo scope and visibility now that pushes are authorized · Q-S08 is `walker-jumpman-clawd` part of this series.

## Zelda's notes (silent mode; what I would have said out loud)

1. **The ledger is honest; the plan is not the practice.** The README says finish both films before the next item. The queue shows 65 items advanced through import while two films exist. That may be the right call — imports are cheap, films are not — but it is a change of plan that nobody has written down. Write it down (Q-S03).
2. **Zero human reviews across 139 items is the real bottleneck,** not import throughput. A second machine review-ready pair adds nothing until a person watches the first one.
3. **Thirteen items are waiting on hardware or toolchains, not on work.** Group them by blocker and decide once per blocker (Q-S04), rather than rediscovering the same OpenXR failure in each XR preflight.
4. **Pushing 59 repositories is now authorized. Publishing is not.** Keep those two things visibly separate in every README, as this one now does.
5. **First fix:** name the audience (Q-S01). It decides whether the remaining ~270 films are worth making at all.
