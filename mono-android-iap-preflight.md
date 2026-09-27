# C# Android IAP preflight — 2026-09-24

Queue item 28: `mono/android_iap`, distinct from the GDScript IAP demo.
Read README, project, csproj, plugin descriptor and Main.cs. No source mono
AGENTS.md found. Requires Godot.NET.Sdk/4.7.0 and net8.0. Existing plugin
descriptor points to bundled GodotGooglePlayBilling.1.2.0.release.aar and remote
Android Billing dependency 5.2.1; these are source declarations, not verified
current compatibility or Play eligibility.

This shell still cannot resolve dotnet; /usr/local/share/dotnet,
/usr/share/dotnet and /Users/bear/.dotnet are absent. Applications lists only
Godot.app and its Contents/Resources/GodotSharp is absent. Same bounded local
.NET toolchain blocker as item 15, not a claim no other installation exists.
No misleading import with a non-.NET editor was attempted.

Source README says its end-to-end demo needs export/upload to Google Play.
That is not authorized by this task. Main.cs also automatically acknowledges
unacknowledged purchases after connecting, so merely launching against a real
billing account is not read-only. No billing connection, query, acknowledgement,
consumption, purchase, upload, install or credential change was attempted.

No project copy, build, runtime verification or films created. Retain as
external-setup-pending, not retired. After an appropriate .NET toolchain is
available, safe local build/isolated tests can proceed; real billing workflow
requires separate explicit scope and must not be silently enabled. Continue
next feasible item while retaining both films and human review as pending.
