# OpenXR Hand Tracking preflight — 2026-09-27 09:06 UTC

Item 60: `xr/openxr_hand_tracking_demo`, source commit
`a3b5c113112f77291d5f3d1360f33a882fdc52f7`. Read README, project configuration
and all seven GDScript files. No XR AGENTS.md found. No copy, import, runtime,
fake tracker or source modification performed. Scene/action-map and asset-specific
license audits remain pending; retain original attribution and assets.

Existing hardware/runtime blocker applies: the actual earlier
`walker-xr-openxr-character-centric-movement/runtime-preflight-20260924.log`
records OpenXR initialization failure. This project's startup also requires an
initialized OpenXR interface. This is source preflight, not new runtime evidence.

Required actual evidence includes optical/controller tracking transitions,
palm-to-grip fallback, skeleton finger motion, confidence/source display,
nearest-object highlighting, pickup and release. Pickup uses 0.6/0.4 hysteresis;
objects are frozen/reparented on pickup and restored/unfrozen on release. The
fallback skeleton uses controller trigger/grip, not optical tracking. These
paths have been read, not behaviorally verified. Do not label synthetic tracking
as hardware verification or real footage. Runtime/vendor support described in
the source README has not been independently checked for current availability.

Known capture permission constraint remains. Both native-4K Liam films and human
review remain pending. Proceed next feasible item without retiring this pair.
