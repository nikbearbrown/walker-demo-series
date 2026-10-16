# XR spectator view preflight — 2026-09-28

Item90 retains the existing XR runtime/headset dependency. Read source README,
project.godot, start_vr.gd and spectator.gd. No nested XR AGENTS found.

Desktop main scene is spectator.tscn; Android uses main.tscn instead. Startup
quits without initialized OpenXR. Spectator modes select third-person,
stabilized first-person, or compatibility-renderer left/right eye textures.
Tracked-camera option additionally requires the README's SteamVR/Vive tracker
setup. This is source inspection, not a claim those devices are available or
that any tracked view has run. Headless synthetic cameras cannot verify the
headset/spectator relationship or actual eye images.

No sibling created, source changed, dependencies installed or hardware test
claimed. Both films remain pending, not retired. Proceed to feasible item91.
Existing XR dependency class does not warrant another user-action alert.
