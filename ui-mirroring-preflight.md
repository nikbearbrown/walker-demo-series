# Item112 — UI mirroring preliminary source check

2026-10-06 14:14UTC. Read-only preflight while item111's two films remain
blocked by the shared native-gameplay GateT class. Item111 is retained, not retired.
No destination project, import, gameplay verification or films created yet.

Source: walker/godot-demo-projects/gui/ui_mirroring. Destination
walker-gui-ui-mirroring does not yet exist. README, project configuration and
complete short script read; scene node/signal inventory inspected, full scene
and font resources still require reading before adaptation.

Compatibility renderer, canvas_items/expand. Main scene ui_mirroring.tscn.
Normal Swap locale button switches TranslationServer locale between ar and en
and updates the locale label. Initial label reads the environment's locale;
do not assume it begins en. Fixed LTR/RTL panels coexist with locale-dependent
controls. Other buttons are demonstration controls, not navigation destinations
unless source/runtime evidence establishes that behavior.

Retain upstream MIT license and bundled LICENSE.Noto.txt (SIL OFL1.1), both font
files/import settings, original strings, UIDs and screenshots. Do not invent
translation quality, change Arabic strings, or claim human-language approval.
Required input trial: press the actual locale button twice, observe label and
layout recovery, and verify fixed-direction panels remain fixed. Show current
engine frames, not upstream screenshots as present-run evidence.
