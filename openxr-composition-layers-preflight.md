# OpenXR Composition Layers preflight — 2026-09-26 22:06 UTC

Queue item 50, source `xr/openxr_composition_layers` at commit
`a3b5c113112f77291d5f3d1360f33a882fdc52f7`. Read README, project configuration
and all four GDScript files. No source XR AGENTS.md found. Original source,
attribution and assets remain untouched; no copy or runtime started this turn.

The existing XR blocker remains applicable: earlier actual runtime evidence in
walker-xr-openxr-character-centric-movement/runtime-preflight-20260924.log
reports OpenXR initialization failure with HMD/required feature unavailable.
This demo exits when OpenXR is not initialized. No new physical runtime was
configured and no fake trackers/controllers were supplied. This is preflight,
not a claim of fresh runtime or behavior verification for this project.

Actual behavior requires tracked aim/select input, active-hand switching,
ray-to-viewport conversion, UI interaction, pointer pulse and controller haptics.
Main startup picks the right hand; either select handler switches active hand.
Full scenes, action map and shader audit remain pending. Pointer release outside
the layer is a specific behavior to test; the current code resets was_pressed
on a ray miss without dispatching a release event. No bug fix made without test.

Capture caveat from the source README: compositor layers are composed by the
XR runtime and omitted from an ordinary spectator view. Therefore a desktop
mirror alone cannot establish the central visual result. A supported headset
capture path must verify actual layer content; do not substitute a fake overlay
or present fallback rendering as native compositor evidence.

A Remotion ffmpeg encoder was visible in the process list this turn. Its output
was a temporary native-4K pre-encode file, not a verified Walker film. Left it
untouched and launched no duplicate writer. Both film tasks remain pending the
existing hardware/capture constraints. Proceed next feasible item without
retiring this pair; no user approval, publishing or account changes performed.
