# Item108 — initial source preflight

Read-only inspection on2026-10-04. Source `../walker/godot-demo-projects/3d/particles`;
no sibling exists yet. README, project.godot, tester.gd and checker.LICENSE.md
read. Full1090-line scene/resource and remaining asset/license audit still pending.

Forward+ showcase includes CPU/GPU particles, collision, attractors, trails
and subemitters. Do not silently substitute Compatibility and claim GPU coverage.
Script accepts normal left/right actions and Previous/Next buttons, clamps
selector to available testers, updates label and disabled boundary buttons.
Mouse wheel changes zoom0.125 per event, clamped1.5–4; drag with any main mouse
button adjusts yaw/pitch via screen_relative, pitch clamped−90°–0°. Camera
smoothly follows selected tester onZ. These are source facts, not verified runs.

Checker texture credits Kenney CC0. Preserve original license and audit smoke
texture and baked collision data provenance before copying. Next: finish source
and instruction reads, create a separate local sibling without touching source,
import/run Forward+, then normal-input selector/camera checks and real particle
behavior capture. No actual game tests, films or human approvals yet.
