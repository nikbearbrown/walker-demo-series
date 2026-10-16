# WebXR demo preflight — 2026-09-29 UTC

Queue item 95; upstream `xr/webxr` at Godot demo commit
`a3b5c113112f77291d5f3d1360f33a882fdc52f7` (repository MIT license).
The source README calls for a Web export with WebXR polyfills. `main.gd`
requests an `immersive-vr` session, a floor reference space and controller
events. A desktop Godot import or non-XR viewport cannot verify that real
session, headset rendering or controller input. No headset/browser session or
Web export was exercised in this preflight; no footage or film exists.

Keep the item pending external WebXR setup. Preserve the source checkout and
do not represent a desktop fallback or scripted tracker as played VR. Continue
to the next feasible round-robin item, `walker-2d-kinematic-character`.
