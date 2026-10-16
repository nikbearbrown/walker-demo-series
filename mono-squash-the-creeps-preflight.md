# C# Squash the Creeps preflight — 2026-09-27 22:36 UTC

Item71, source mono/squash_the_creeps at
a3b5c113112f77291d5f3d1360f33a882fdc52f7. Read README, all four C# files,
csproj and full fonts/LICENSE.txt. No Mono-specific AGENTS found. Source clean;
no sibling copy, compilation, import or runtime claimed. Scenes/project/input-map
and model provenance audit remain pending.

Known toolchain blocker reconfirmed: command -v dotnet found no executable;
installed /Applications/Godot.app/Contents inventory has no GodotSharp/dotnet
files. Project requires Godot.NET.Sdk/4.7.0 and net8.0. Do not substitute a
GDScript version and call it C# verification. No toolchain installation attempted.

Read-only source findings to verify once runnable:

- Player normalizes movement, jumps only when grounded, squashes on upward
  collision normals above0.1, and bounces. Collision checks precede this frame's
  MoveAndSlide; no claim about observed timing or gameplay correctness yet.
- Main randomly selects a spawn-path position; mob speed is integer10–18 by
  default. Mob squashing emits a score signal before queue-free. Player death
  stops spawn timer and shows retry; ui_accept then reloads current scene.
- Mob animation SpeedScale uses randomSpeed / MinSpeed with integer operands.
  At default10–18 over10 this evaluates to1, so it does not express a fractional
  speed ratio. Candidate adaptation fix requires runnable regression evidence;
  no source change or unverified repair made here.

Retain original root MIT, asset provenance and explicit separate notices:
README attributes House In a Forest Loop.ogg to HorrorPen (2012), CC-BY3.0,
with its source link. Montserrat Medium has the supplied full OFL1.1 notice,
copyright2011 The Montserrat Project Authors. Do not erase these in later copies
or imply root MIT replaces the separate notices.

Actual C# behavior, heard audio, capture and both native4K Liam films remain
pending under established toolchain/capture constraints. Proceed next feasible
item72 without retiring this entry; human approval remains pending.
