# Walker demo adaptation series

**What it is.** The production ledger for turning every Godot demo project (139 in the local checkout of the official demo collection) into its own standalone `walker-*` project, each with two native-4K films narrated by Liam: a walkthrough and a separate development film.

**Why it is in Walker.** It gives Walker a large, honest body of working Godot projects to teach from and to film, with every source license, asset and provenance record preserved.

**What was found (2026-09-27).** 67 of 139 items are started and 58 have their own sibling folder. One (`walker-pong`) is machine review-ready with both films; one (`walker-3d-platformer`) is in film production; 52 have passed import; 13 are blocked on external hardware or toolchains. Human review is pending for all of them. See [GDD.md](GDD.md) for the series design document and the full project index.

- Repository: https://github.com/nikbearbrown/walker-demo-series
- Series design document: [GDD.md](GDD.md) (recovered 2026-09-27, unapproved; open questions in [design/decisions.md](design/decisions.md))

## Authorization update — 2026-09-27

On 2026-09-27 Nik Bear Brown explicitly authorized creating GitHub repositories and pushing every `walker-*` folder. This supersedes the "no GitHub pushes" line in the series rules below **for that action only**. YouTube publishing remains unauthorized, as do paid APIs and Shorts.

## Series rules

Local production ledger; not part of the public Walker framework.
Inventory every `project.godot` from the source checkout and keep each project
in a separate sibling `walker-*` directory. Initial order: Pong, 3D Platformer,
Audio Rhythm Game, then round-robin through all categories until exhausted.
Pong is `walker-pong`; other names include their source category to avoid collisions.

Each item must progress through source/license inspection, bounded Walker
adaptation, engine import/run and behavior checks, genuine capture, a 4K Liam
Walker walkthrough, and a separate 4K Liam Walker development film. Each focused
code excerpt must immediately precede its visible result. Preserve the regular
outro. Use local Kokoro; no paid APIs, Shorts, GitHub pushes or YouTube publishing
are authorized by this series request. (GitHub pushes: superseded 2026-09-27, see
the authorization update above.)

`queue.json` is the durable status ledger, not evidence of completion. Do not
mark review-ready until both MP4s exist, hashes and native 4K dimensions match,
skill checks pass, and actual film frames/event sequences have been inspected.
Machine review-ready is not human approval. Preserve all existing work, originals,
source licenses, UIDs/import settings, and provenance. Never overwrite an existing
project merely to make the queue advance.

Finish both films before taking the next item unless an external dependency
blocks it. Record that blocker, proceed to the next feasible item, and revisit
blocked items. Hardware-dependent XR/mobile/gamepad demonstrations must remain
explicitly unverified when hardware is unavailable. Preserve C# demos as their
own entries; do not silently relabel GDScript copies as C# demonstrations.

Keep substantive progress and failures in each game's FRICTIONAL.md. Use separate
capture copies, normal input paths, original gameplay speed, and real evidence.
Check disk space before captures; do not delete existing media to create room.
Keep a minimum 15 GB free reserve and budget each capture before launching it.
If that reserve cannot be maintained, record a storage blocker and request a
user-approved output volume rather than deleting, compressing away evidence,
or claiming the remaining films are finished.

Recurring continuation resumes this ledger in the current task; it is not a
promise that a separate renderer runs while the computer or app is unavailable.

## Files

- `queue.json` — the durable status ledger (139 items)
- `STATUS.md` — dated handoff notes, newest first
- `*-preflight.md` — source preflights for items blocked before a copy was made
- `RHYTHM-SOURCE-AUDIT.md` — source audit for the rhythm-game item
- `advance_platformer.py` — one-off script that recorded Pong's verified masters and seeded `walker-3d-platformer`
- `GDD.md`, `design/` — series design document, status and open questions
