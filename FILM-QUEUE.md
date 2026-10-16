# Walker trio film queue (godot-waikthrough / godot-gdd / godot-gamedev, walker mode)

Status as of 2026-09-28. Recipe: FILM-RECIPE.md.

## Done
- walker-jumpman-clawd (pre-existing trio)
- walker-pong, walker-3d-platformer (gdd added; gamedev+walkthrough pre-existing)
- walker-2d-dodge-the-creeps, walker-2d-bullet-shower
- walker-gui-control-gallery, walker-gui-drag-and-drop, walker-gui-custom-splash-screen
- walker-gui-accessibility — walkthrough rendered but checker FAILS by design (screen-reader output uncaptured; see its BLOCKED.md — needs Bear: VoiceOver recording, Accessibility Inspector dump, or approve keyboard-only partial)
- walker-3d-csg — trio done 2026-09-28 (Forward+ 4K Movie Maker + a Compatibility take); finding: a wheel notch (press+release) zooms 0.25 = 2× ZOOM_SPEED, test sends presses only
- walker-3d-decals — trio done 2026-09-28 (Forward+ 4K, game in a SubViewport so the P-key ray follows the scripted pointer); findings: stamp set red renders white (fade track overwrites modulate), filter menu starts on 4 while the renderer starts on 5, wheel notch 0.25 = 2× ZOOM_SPEED; CC-BY/CC-BY-SA texture credits burned into those clips (licence review Q-07 still open)

- walker-2d-finite-state-machine, walker-2d-drawable-textures, walker-2d-dynamic-tilemap-layers
- walker-gui-gd-paint — Save shown once, dialog kept out of frame (GDD Q-06); if Bear wants no Save on film, drop walkthrough B13–B14 + GDD B18
- walker-audio-rhythm-game (gamedev added — trio complete), walker-misc-2-5d, walker-loading-serialization, walker-2d-custom-drawing

## In progress
- lane 6: walker-loading-autoload, walker-loading-scene-changer, walker-loading-threads, walker-loading-load-threaded
- lane 5: walker-audio-audio-effects, walker-audio-bpm-sync, walker-audio-generator, walker-audio-midi-piano
- lane 4: walker-3d-ik, walker-3d-antialiasing

## Queued
- 3d: global-illumination, graphics-settings
- audio: device-changer, mic-record (both need real devices — likely partial)
- compute: heightmap, post-shader, texture
- gui: bidi-and-font-features (private repo — font licence open)
- loading: runtime-save-load
- misc: custom-logging, graphics-tablet-input, hdr-output, joypads
- mobile: multitouch-cubes, multitouch-view, sensors
- networking: multiplayer-bomber, multiplayer-pong, webrtc-minimal (runtime blocked: WebRTC extension missing), websocket-chat
- plugins
- viewport: 2d-in-3d, 3d-in-2d, 3d-scaling, dynamic-split-screen, gui-in-3d
- xr (last; no headset): mobile-vr-interface-demo, openxr-binding-modifier-demo, openxr-character-centric-movement

## Skipped
- walker-demo-series (ledger, not a game)
