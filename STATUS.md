# Current work

## September 29, 2026 UTC — kinematic moving-platform route

Item 96's normal-input left+jump route now lands on MovingPlatform2 and rides it.
An assertion run measures matching −36 px player/platform Y over 120 physics
frames with floor contact and stable offset. The shorter failed route is
preserved. This is engine-state behavioral evidence, not visible footage or
human play. One-way traversal, Princess win and both films remain pending.

## September 29, 2026 UTC — kinematic controls follow-up

Item 96's second normal-input diagnostic now passes braking and left movement;
engine-state observations confirm MovingPlatform1 position and Circle rotation
change over time. The first parse failure and one incorrect displacement check
remain logged. This does not verify player carry, one-way traversal, Princess
win or visible gameplay. Those and both films stay pending; no new review-ready
pair, no source-checkout edit and no capture worker launched.

## September 29, 2026 UTC — round-robin continuation

WebXR item 95 source preflight retained in `walker-xr-webxr-preflight.md`:
immersive browser/headset/controller behavior cannot be claimed from a desktop
preview. Queue keeps it at external-setup-pending, not retired. Created the
separate `walker-2d-kinematic-character` copy for item 96 with upstream MIT
notice and provenance. Godot 4.7.2 reimport after the local display-name change
passes. Headless real-scene input probe passes landing, rightward movement and
Space jump; preserved four failed diagnostic logs before the passing probe.
Platform carry, one-way traversal, rotating obstacle, Princess win, rendered
capture and both films remain unverified/pending. No original demo change.

## September 29, 2026 UTC — rhythm film audit

Both Rhythm Game native-4K landscape masters and matching ready receipts now
exist. Walkthrough skill check passes 17 implemented features/20 evidence
intervals; gamedev check passes 15 exact adjacent code/result pairs. Actual
contact sheets and recorded event-sequence reviews were inspected. Queue stage
corrected from stale `import-passed` to `film-production`. Heard synchronization,
full audio-transition listening and Bear's review remain pending; do not mark
the pair review-ready. Platformer remains on the same listening hold. No duplicate
render was launched and no original or failed artifact was removed.

## September13 19:19UTC — newest handoff

QA session72313 completed. Platformer gamedev actual master: all29contacts with
342samples inspected, plus native material-code frame. Source checker PASS18pairs,
134files; audio -26.4LUFS/-3dBFS. Visual report in gamedev/qc/master-20260913.
No render/QA workers remain. Listening unavailable, human review pending; don't
claim those passed. Next: continue audio/rhythm_game source inspection and separate
adaptation while external listening remains pending; retain platformer follow-up.
Factory47ready/2retrying/1building/12pending. New hash/audio/native4K pairs verified:
audit-review-queue, fill-slates, generate-audio-kokoro. All verticals exceed3min.

## September13 18:47UTC — current handoff (supersedes older notes)

Platformer gamedev master completed: native4K,625.133333s, receipt hash matches.
QA session72313 running check_final_gamedev.py; clip frames and action clocks
passed, actual-frame extraction active. Resume, never duplicate into existing
qc/master-20260913. Inspect contacts/native code and rerun source/skill checks.
Listening/human review pending; pair not ready. 71GiB free, no compiler active.
Factory44ready/3retrying/1building/14pending, supervisor running. New verified
4K landscape+vertical pairs: brand-variant, build-cli-d3-reels, capture-sim.
All three verticals exceed180s; not Shorts-ready. Notify for review, not approval.

B04F audio completed:7.36s, fits8s clip. Trim session21697 may still be running;
resume it before mixing. Full listening review remains pending.

## Latest — September 12, 2026, 12:16 EDT

Capture-fall-stepped-02 PASSES actual fall825/recovery826, no reset input.1801
decoded frames/1800 distinct/maxrepeat2/zero full-scalePCM. Inspected11–16s
sequence: approach, fall into mist, return to original ground. Added B04F draft
afterB04, selecting source10–18s unretimed; source copy and prior sheet preserved.
Local Liam audio job43612 and8s trim job just started; check sessions/files before
writers. Next verify voice fits8s, mix original game audio, add clip/mix manifests
and fall coverage, disclosure labels, fullQC. Factory resumed command-todo worker;
30ready, no newly verified pair yet. No final/publish/push.

## Latest — September 12, 2026, 11:46 EDT

Fixed60 cell-centerX=-5 route PASSES fall+recovery without reset input. Fresh
capture-fall-stepped-02 started using that exact driver; check latest capture
session and run/report before claiming success. Prior failed30s take retained.
Next decoded motion/audio and actual fall-frame inspection, then integrate beat.

## Latest — September 12, 2026, 11:42 EDT

Recorded stepped01 FAILED despite earlier real-time headless success. Crucial
diagnostic: headless --fixed-fps60 reproduces the captured final position exactly.
Use this cheap deterministic mode for future route tests; no more capture until
it passes. Landed-waypoint variant also fails at northern ledge nearZ-15.6/Y-4.
Testing cell-centerX=-5 instead of boundaryX=-6: fixed60-x5 probe running (see
latest exec session). Original capture and reports preserved.23GiB free.
Factory unchanged30 ready/running/usage-limited. No finished film or notification.

## Latest — September 12, 2026, 11:12 EDT

Stepped probe01 PASSES: falls below-12 at frame1309 and recovers1310; reset input
false throughout. Actual report preserved; headless shutdown resource warnings
remain. Started fresh native4K capture-fall-stepped-01, session80718, using same
ordinary-input waypoints and forced draw/lower gain.24GiB free beforehand; budget
~1.5GB for30s take retains15GB reserve. Check session/report/decoded motion/audio
before integrating. No final film yet. Next capture QA, integrate fall beat,
disclosure framing/mix/QC, then gamedev. No publication/push.

## Latest — September 12, 2026, 11:08 EDT

SE/SW/NE diagonal headless probes also hit terrain, no automatic reset; reports
preserved. Expanded read-only terrain inventory with local cell-height rows to
identify a stepped northern approach near X=-6. Stepped ordinary-input probe01
running session11914 (30 seconds simulated); inspect report before any4K capture.
No large capture/render running. Factory unchanged30 ready, usage pause, alive.

## Latest — September 12, 2026, 10:37 EDT

Two further cheap held-jump routes (negative Z, negative X) fail honestly against
terrain; reports saved, no video generated. Both stop near Y=-4 with repeated
shutdown resource warnings. Read-only inspect_terrain.gd shows GridMap cell size2,
position(-16,-6,-12), occupied-cell bounds(-3,-1,-8)..(40,8,19). Straight cardinal
routes meet walls: jumping rise3.6 cannot clear a4-unit ledge. Next inspect a
stepped/diagonal route rather than repeating cardinal probes. All bookends done;
fall evidence, disclosure framing and complete film QC still pending. No workers
running; no new factory pair (30 ready, running, usage-limited).

## Latest — September 12, 2026, 10:05 EDT

B08 regular outro rendered; inspected 2-second frame: readable title/handle and
crisp mascot. All bookends rendered, full QC pending. No jobs running. Two cheap
headless positive-X jump probes failed, ending against terrain nearX7.6/Y-8.
Corrected held jump input before second probe; reports retained. Second run had
shutdown resource-leak warnings. No large new captures. Next inspect terrain for
a reachable fall route, add disclosure framing, coverage/mix/QC, then gamedev.
Factory unchanged30 ready/running/usage-limited; no new notification.

## Latest — September 12, 2026, 09:33 EDT

Touch03 integration completed; verified current B05 video and mixed-audio hashes
against the integration receipt. Refreshed both main manifests to the 8-second
button take; old entries/media remain in history/touch-buttons-v1. No final film
yet. Next B08, disclosure framing, cheap fall-route probes before another capture,
coverage and final QC, then the separate code-to-consequence development film.
Factory remains running, usage-limited, 30 ready. Scene-index has new September12
exports; check receipts and native4K/audio before notifying. No publishing or push.

## Latest — September 12, 2026, 08:27 EDT

B07 rendered;13s prompt frame inspected/readable. Fall02 also fails: reaches
lower terrainY=-8, not reset threshold. Stop blind recording; inspect level route
or probe directions cheaply before another4K attempt. Both failed takes retained.
Integrating verified8s touch03 into B05 (session31059); prior sheet/media/mix/ledgers
backed up in history/touch-buttons-v1. Wait before another sheet writer. Integration
writes coverage and receipt; main clip/mix manifests need refreshed B05 entries
afterward (old versions remain backed up). Next B08, disclosure framing, fall gap,
final QC. Factory29 ready; icon-build/scenes are September9 revalidations, no alert.

## Latest — September 12, 2026, 07:55 EDT

B06 rendered; inspected12s frame, readable verdict with explicit limits.
Fall01 failed honestly: negativeX route stops against terrain atX=-11.599/Y=-4.
Fall02 tests positiveZ direction, session17689; preserve failed take. B07 viewer
prompt rendering session20127; avoid sheet edits until renderer finishes.
Next integrate touch03, resolve fall evidence, finish B08/labels/coverage/QC.
Factory27 ready. New art --list pair verified: landscape191.08s,vertical196.92s,
both native4K/audio and matching ready hashes. Notify pair; vertical NOT Shorts.
Icons revalidated September9 exports, not new. No publication.

## Latest — September 12, 2026, 07:22 EDT

B01 rendered;9s frame shows completed finished→playable correction, readable.
Touch03 passes synthetic joystick/jump/shoot outcomes; inspected jump/projectile
sequence.481frames,480 distinct,zero full-scale PCM; hardware remains unverified.
Need replace B05 with this longer take and update mix/coverage (keep old artifacts).
New input-only fall route capture-fall-01 running session59705; no reset input or
state injection, success not yet known. B06 verdict rendering session76993;
don't duplicate either job or write beat sheet concurrently with its renderer.
Factory25 ready; Riff newly ready with fresh vertical234.54s, existing landscape,
hashes/audio/native4K verified. Your Turn is old exports revalidated. Notify only
Riff pair; vertical exceeds3min, not Shorts-ready. Nothing published.

## Latest — September 12, 2026, 06:50 EDT

B00 opening rendered successfully; inspected12s frame, text readable and suggested
prompt/reconstruction disclosure visible. Not a complete frame audit. B01 now
rendering, session99680; don't launch another sheet writer while active.
Extended isolated touch driver to press/release actual jump/shoot buttons via
viewport-local events, recording action and player/Bullet outcomes. Fresh capture
touch03 running session68745; original takes/drivers preserved. Check outcome,
never claim button success from UI appearance alone. Fall-reset gap remains.
Factory unchanged23 ready/usage-limited; no new film pair to notify.

## Latest — September 12, 2026, 06:17 EDT

Walkthrough coverage.json and exact source snapshot written. Checker intentionally
fails on unshown automatic-fall-reset; touch jump/shoot button-event behavior also
remains unshown. Both stay implemented with empty evidence, not falsely planned.
Existing coin route minimumY=-8.0016 does not establish the below-12 reset path.
Read parent explainer/Remotion/motion and visual-QC references. Started B00 opening
render through the normal wrapper; check active exec session before duplicating.
B00 render session26252. Next resolve two coverage gaps, inspect B00, continue
remaining bookends, add disclosure labels and verify final sync/audio/frame QC.
No final yet. Factory unchanged23 ready, usage-limited; no new notification.

## Latest — September 12, 2026, 05:45 EDT

Media prep finished: four exact60fps clips with game audio and independent source
copies; hash manifest exists. Mixed each with padded Liam at original duration,
game gain-12dB below captured audio, explicit0.95 limiter. Originals retained.
Stock slug-seeded outro attached; pre-mix sheet backed up. Full listening pending.
FACTCHECK.md, SHOTLIST.md and PROMPTS.md drafted. Next coverage/source ledgers,
disclosure labels, bookend render and actual-frame/sync QC. No active workers here.
Factory unchanged23 ready, usage-limited. No new pair to notify.

## Latest — September 12, 2026, 05:12 EDT

Shortened walkthrough B05 to “Synthetic touch preview, not a hardware test.”
Original narration preserved as beat-B05-original-long.mp3; regenerated only B05
at3.22s, now within4s source interval. Initial unsupported --force invocation
failed harmlessly; corrected to documented --only. All body speech now fits.
Started prepare_walkthrough_media.py, exec session56273: independent capture/log
copies and exact60fps trims with original game sound retained. Check existing
session/clip-manifest before resuming; don't start a second writer. Next padded
Liam/game audio mix, evidence paperwork and bookend renders. No final film yet.
Factory unchanged23 ready, usage-limited; no new notification.

## Latest — September 12, 2026, 04:39 EDT

Platformer walkthrough now has a nine-beat source-bound draft and BUILD-PROMPT.md
under youtube/claude-liam-walker-3d-platformer-walkthrough. Four capture intervals
mapped without retiming; touch is explicitly diagnostic. Started free local Liam
Kokoro generation, exec session11498. Check that session/files before resuming;
do not launch a duplicate audio writer. Next measure narration against intervals,
Audio completed successfully:8 beats,$0.00,no writer running. B05 narration4.33s
exceeds its4s diagnostic clip: shorten speech or explicitly hold outside action,
never slow the clip. Other body narration fits the assigned intervals (B02 8.36s
within10s;B03 7.25s within9.5s;B04 18.60s within30s). B01 is10.82s.
complete coverage/evidence paperwork, preserve game audio and render bookends.
No final film yet. Factory unchanged23 ready/2 retrying/37 pending, usage-limited.

## Latest — September 12, 2026, 04:06 EDT

Platformer diagnostic touch preview02 passes: synthetic viewport-local drag gives
0.75 right-action strength and release. Real UI exposed on non-touch desktop;
explicitly NOT physical hardware evidence. Failed take01 retained. Native4K60,
241frames,zero full-scale PCM; event sequence inspected. No render running.
Next finish source ledger/coverage and author film beat sheets/audio.

Factory23 ready,2 retrying,37 pending; usage-limit pause, supervisor alive.
New SRI explainer pair281.75s verified hashes/audio/native4K both aspects.
Art help has new vertical177s and existing landscape177s, both verified.
These pairs notified for review; SRI vertical exceeds180s so NOT Shorts-ready.

## Latest — September 12, 2026, 03:32 EDT

Platformer jump comparison captured and inspected:6vs60 held ticks yield measured
rises1.5300vs3.6031 in this location. Native4K60,721frames,zero full-scale PCM.
Scene inspection records actual animations/resources and GridMap2921 cells/18
library entries. RESOURCE-NOTES.md drafted. Material distance fade explains the
near-camera translucent robot; terrain obstruction remains a separate limit.
No renders/checkers running now; no narrated films yet. Next remaining touch UI
and source coverage, then beat sheets/audio. Factory running21 ready; no new pair.

## Latest — September 12, 2026, 03:00 EDT

Inspected basic capture03 at2fps: movement, jump, shots and reset visible; source
checks remain4/4. Created Platformer youtube/PRODUCTION.md and RIFF-DRAFT.md from
actual event sequences. Lists code→result units and remaining truthful coverage
(touch UI, release-height comparison, patrol, resources). No film render started.
Factory21 ready/1 retrying/1 building/39 pending; screen-clean is a September8
export revalidated, not a new film. Riff worker actively repairing its own QC.

## Latest — September 12, 2026, 02:27 EDT

Platformer capture-route-02 verified: native4K60, two coins and enemy hit,
1800 distinct images/1801 frames, zero full-scale audio samples after capture-only
-9dB Master gain. Actual event sequence inspected; camera obstruction remains.
Basic input harness now maintains held actions; fresh low-gain basic capture next.
Started that capture as capture-pilot-03 (exec session77831); check run.json and
report.json before resuming, never launch a duplicate into the same directory.
Completed: exit0, all four assertions pass, 600 distinct images/608 frames,
maximum repeat7, zero full-scale PCM. Seven Texture RID warnings persist.
No capture or metric checker remains running. Next inspect its jump/reset frames
and author the two film plans using current full skill instructions.
29GiB free at launch. Queue JSON parses. Git diff check unavailable because this
standalone project has not been initialized as a Git repository.
No narrated Platformer films yet. Factory running:20 ready,1 retrying,1 building,
40 pending; logo-motion/NBB/nopunt are September8 exports revalidated, not new films.

## Latest — September 12, 2026, 01:22 EDT

Platformer feature route now collects two coins and hits an enemy through ordinary
inputs. Actual native4K/60fps30s capture exists;1800 distinct images/1801 frames,
coin frame257/enemy275, inspected event sequence. Failed routes retained. Original
PCM has full-scale peaks; recapture with lower master gain before final mixing.
GDD.md now describes inspected build and limitations. No narrated films yet.
Factory unchanged: running but usage-limited,17 ready/45 pending. No new alert.

## Latest — September 12, 2026, 00:46 EDT

Platformer capture defect resolved in isolated driver: pilot01 had239 consecutive
identical frames while state moved; pilot02 forces rendering each capture step
and yields600 distinct images across608 frames, longest repeat7. Inspected actual
motion/shoot/reset sequence. Source game untouched and failed take retained.
Next coin/enemy input route and complete coverage; no narrated films yet.
Factory unchanged: running but usage-limited,17 ready/45 pending; no notification.

## Latest — September 12, 2026, 00:12 EDT

Platformer native4K Movie Maker pilot is recorded and one actual frame inspected.
608 decoded frames/60fps,10.1333sec with PCM game audio;4/4 normal-input assertions
pass. Engine summary contradicts decoded count (67); investigate timing before
final-use certification. Seven Texture RID shutdown leaks, audio near0dBFS peak.
No narrated film yet. Capture details and preserved evidence in Platformer/CAPTURE.md.

Factory unchanged: supervisor running,17 review_ready,45 pending, waiting for
Claude usage reset. No new verified pair or user-action blocker to notify.

## Latest — September 11, 2026, 22:47 EDT

Platformer probe04: four ordinary-input behavior checks pass, CoreAudio with
normal wall-clock timing, exit0 and empty stderr. Accelerated Dummy-audio
probe03 still reports playback-resource shutdown leaks despite test teardown.
Both records preserved; no gameplay change. Next visual pilot and remaining
coin/enemy/camera/audio coverage before films. Still one completed game pair.

Brutalist supervisor running,17 review_ready,2 retrying,43 pending; temporarily
waiting on Claude usage reset. Newly ready logo/HAI entries are old exports
revalidated, not new films. No repeat or routine notification needed.

## Latest — September 11, 2026, 22:15 EDT

3D Platformer now has two actual 600-frame normal-input probe reports. Four
assertions pass: movement, jump, projectile creation and reset. No injected
gameplay state. Headless shutdown still leaks audio playback/randomizer resources;
verbose run narrows the warnings to WAV playback. Continue coin/enemy/camera/
audio checks and a real rendered capture; neither film exists yet.

Factory produced a genuinely refreshed godot-gamedev skill pair at 21:22/21:23,
matching ready receipt hashes, both 4K with audio, 3:51.83 each. The vertical is
over the user's three-minute Shorts ceiling: a full vertical review cut, not a
Shorts-ready deliverable. Notification must make that distinction. No publishing.

## Update — September 11, 2026

Pong's two films are exported and were delivered in the preceding user turn:
150.6-second walkthrough and 374.43-second development film, both native4K with
audio and matching final receipts. Eight exact code/result pairs pass. Development
master: 44 sampled frames, zero blockers/majors after fixing speed-label margins.
Queue records actual paths/hashes; human review remains separate.

Current: walker-3d-platformer, separate source-preserving copy with project-name
change only. Upstream hashes/license retained. Godot4.7.2 import succeeded. All
eight GDScript files read. Headless 180-frame smoke exited0 but forced teardown
reported five ObjectDB leaks and one resource in use. No behavioral test or film
yet. Next: inspect resources, build normal-input harness with orderly teardown,
verify motion/jump/shoot/coin/reset/camera, then capture real4K with game sound.
Touch/gamepad hardware unverified. 34GB free; keep15GB reserve.

Factory running: 11 review_ready, one retrying, one building,49 pending. Finance
revalidated old September8 exports, not new films. No new notification warranted.

## Historical notes (superseded by update above)

- Inventory: 139 separate source demos; 278 requested films, none yet completed
  by this series. Queue contains unique category-qualified IDs, except walker-pong.
- Current: walker-pong, created outside the framework at ../walker-pong.
- Import: successful with Godot 4.7.2 regular / Compatibility.
- Tests: ten normal-input checks passed at 60 FPS and 30 FPS. Not a human playtest.
- Native 4K framing pilot inspected: original 16:10 playfield retained with side margins.
- Full engine capture finished in walker-pong/evidence/capture-production at 30 FPS:
  2,400 PNGs, 80 seconds, its own ten-check passing report. Encoded unchanged
  action speed to walker-pong-route-4k.mp4 (3840×2160, video only; source is silent).
  Neither the capture nor encoder is still running. Preserve those frames.
- Individual source frames at first paddle contact, floor rebound and reset
  agree with the event log. A contact-sheet preview initially looked misleading;
  actual full frames show one ball, not duplicate game objects. A pixel/log
  comparison script adds independent sampled-frame verification.
- The two-film shot/teaching plan is walker-pong/youtube/PRODUCTION.md.
- Both narrated films remain pending. No MP4 here is a completed narrated film.
- Next games: walker-3d-platformer, then walker-audio-rhythm-game.
- Existing thread heartbeat now includes active Walker continuation every 30 minutes,
  while retaining read-only monitoring of the separate Brutalist playlist factory.

## Resume the first film pair

Read walker-pong/AGENTS.md, CAPTURE.md, GDD.md, SOURCES.md, FRICTIONAL.md, all
runtime source, evidence/source-snapshot.json and youtube/PRODUCTION.md.
Check evidence/capture-production/pixel-log-verification.json; do not rerun
the verifier over its existing report (it deliberately refuses overwrite).
Inspect full event sequences, then prepare evidence-preserving reel-contained
media intervals. Final beats, voice and both films remain to be produced.

Use brutalist.art's current skills/make/godot-waikthrough/SKILL.md (alias
godot-walkthrough), godot-gamedev/SKILL.md, riff/SKILL.md, ai-explainer/SKILL.md
and all required references. These skills were inspected while setting up
the series, but each continuation must follow the current full instructions.
Reuse GodotDevWorkbench for exact readable code→immediate actual-result pairs;
do not run the unrelated Brutalist playlist factory to make these game films.
Liam/am_onyx, Walker bookends, regular stock outro, no captions, no publishing.
Read the parent explainer/Remotion/QC references before rendering components.

The source Pong has no score, menus, winner, AI opponent or audio. Do not invent
any of those to fill a film. Its gamepad bindings remain hardware-unverified.
Source gameplay scripts/scene are unchanged; the Walker name and documentation
are new. Failed harness/capture pilots are retained and clearly non-deliverables.

Keep 15 GB free, do not delete existing artifacts, and record status/evidence
updates here and in queue.json. Do not mark a game or pair done from filenames,
worker claims, or successful import alone.
