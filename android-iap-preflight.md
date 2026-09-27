# Android IAP preflight — 2026-09-21 03:35UTC

Read local mobile/android_iap README, project.godot, store.gd, item.gd and
setup_instructions.gd. No execution, purchase, account changes or uploads.

Local source does not contain addons/GodotGooglePlayBilling although the project
enables that plugin and store.gd requires BillingClient/JNISingleton. An ls of
the source root confirms no addons directory. This is a missing dependency,
not proof of a broken installed Android app.

Upstream also requires Android Gradle setup, a Play Console application/product
and a suitable test-device/account installation. None of these were verified or
provisioned. Current automation prohibits account changes, uploads and paid APIs;
do not perform a billing transaction or configure Play Console automatically.

Keep this item pending external setup, not retired and not review-ready. No
Walker copy or fabricated billing client was created. A standalone item-card UI
test could be done later but must not be presented as real billing verification.
Return when dependency/device testing is explicitly available; meanwhile continue
the next feasible queue item. All earlier film capture blockers remain in effect.
