# OpenXR Origin Centric Movement preflight — 2026-09-27 22:06 UTC

Item70, source xr/openxr_origin_centric_movement at
a3b5c113112f77291d5f3d1360f33a882fdc52f7. Read README, project config, all three
GDScript files (start_vr/player/black_out), and blackout shader completely. No
XR-specific AGENTS found. Source checkout clean. No sibling copy, import, runtime
or synthetic tracker created for this item. Scenes, action map, asset-specific
license audit remain pending; preserve original root MIT and attribution.

Existing hardware/runtime blocker: inspected actual prior
../walker-xr-openxr-character-centric-movement/runtime-preflight-20260924.log,
which reports OpenXR initialization failure and HMD/required-feature unavailability.
That is earlier environment evidence, not a new run of this demo. Current startup
requires an already initialized OpenXR interface and quits if absent.

Source behavior to verify with genuine hardware:

- Origin-centered smooth rotation around the character body; movement input sums
  left/right controller move vectors. Body heading follows projected camera heading.
- Physical roomscale displacement moves the character body toward neck-projected
  ground position. Unresolved horizontal offset above0.1 starts blackout; fade
  reaches1 at0.2. Controller locomotion is skipped while blocked; gravity still runs.
- Recenter derives origin from body and neck transforms, removes camera tilt and
  resets the body local transform. Test real recenter and obstruction recovery.
- Session lifecycle controls viewport XR, focus pause/resume and physics refresh
  matching. None of these paths, comfort behavior or shader pixels is verified.

No hardware evidence can be inferred from ordinary desktop movement or constructed
poses. Source README platform claims were not independently checked for current
support. Both native4K Liam films remain pending under existing capture/runtime
constraints, as does human review. Proceed next feasible item71 without retirement.
