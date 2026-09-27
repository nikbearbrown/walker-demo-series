# Rhythm-game source audit — 2026-09-13

Preparation only: no adaptation, import, gameplay capture, or film has passed yet.
The preceding 3D film pair still has listening pending in queue.json.

Inspected source: walker/godot-demo-projects/audio/rhythm_game, including
README.md, project.godot, conductor.gd, metronome.gd, note_manager.gd,
and scenes/main/main.gd. Preserve the original checkout.

## Planned code → visible result pairs

- Conductor.get_beat_duration: 60 / bpm → measured note travel against beat timing.
- Filtered versus raw playback → toggle the existing checkbox while notes move.
- NoteManager hit windows (50 ms perfect, 150 ms good) → normal Space input
  producing the corresponding judgment and counter change.
- Input latency setting → existing offset control and visible judgment offset.
- Main restart handler → R resets the chart and counters.
- Pause handler → inspect implementation, then prove pause/resume using normal input.

## Candidate defects to reproduce before changing

1. NoteManager._process calls _miss_old_notes, which can empty _notes, and then
   calls _handle_keypress on a same-frame press. That method indexes _notes[0]
   without another emptiness check. Test a press when the last note expires.
   This is source-based suspicion, not a confirmed runtime failure.
2. Metronome adds cached output latency (seconds) directly to current beat
   (beats). Check units against the conductor's conversion before any fix.
   Its existing comment separately acknowledges audio-mix scheduling imprecision.

## Licensing and capture gates

README attributes the metronome recording to Ludwig Peter Müller, CC0 1.0.
No music/LICENSE* file matched; inspect remaining music metadata and the root
demo license before distributing copied assets or using music in films.
Use actual audio output for synchronization tests; headless/Dummy audio is not
proof of perceived sync. Never silently retime footage. Keep the 15 GB reserve.
Do not claim the two candidate issues are verified until reproductions exist.

### Follow-up inspection, 23:49 UTC

Read the root Godot demo MIT license; preserve its copyright and permission
notice in the adaptation. Music inventory contains the_comeback2.ogg and the
metronome WAV plus import sidecars; track-specific attribution still needs checking.
Read pause_handler.gd: it toggles SceneTree.paused and PauseLabel visibility.
Its comment requires PROCESS_MODE_ALWAYS; verify the scene property before
claiming pause/resume behavior. Queue now records source-audit, not game completion.
