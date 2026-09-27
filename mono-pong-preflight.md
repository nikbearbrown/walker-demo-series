# C# Pong preflight — 2026-09-27 09:06 UTC

Item 61: `mono/pong`, source commit
`a3b5c113112f77291d5f3d1360f33a882fdc52f7`. Read README, project.godot, csproj
and all four C# scripts; full scene and asset/license audit still pending.
No mono AGENTS.md found. Source remains untouched; no copy or build attempted.

The project explicitly requires Godot.NET.Sdk/4.7.0 and targets net8.0.
`command -v dotnet` returned no executable; file inventory beneath the installed
Godot.app found no GodotSharp/dotnet entries. This repeats the known C# toolchain
blocker, not a new failure. No SDK installation or package restore performed.

Source inspection identifies a candidate bug to reproduce once runnable:
Paddle._Process clamps position.Y using GetViewportRect().Size.X instead of Y,
although the configured viewport is 640 by 400. No fix or behavior claim made
without a runnable C# project. Verify both input mappings, bottom/top bounds,
ball acceleration, paddle/wall collision and reset after installing a suitable
toolchain. Do not substitute the completed GDScript Pong as evidence for this item.

Both native-4K Liam films and human review remain pending, also subject to the
existing capture constraint. Proceed to item 62, finite-state-machine, without
retiring this entry. Initial glob-based read failed because scripts are in Logic;
the subsequent explicit Logic/*.cs read succeeded.
