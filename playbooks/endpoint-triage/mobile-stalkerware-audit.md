---
id: "IRP-EP-MOB-001"
title: "Mobile Stalkerware & Surveillance Audit (iOS & Android)"
platform: "Mobile (iOS & Android)"
version: "1.0.0"
last_verified: "2026-10-22"
severity_level: "High"
target_audience: "Operator & Tech-Savvy Helper"

indicators:
  - "Battery draining exceptionally fast or phone feeling warm while idle."
  - "Unprompted location, microphone, or camera access icons appearing in the status bar."
  - "Unexplained high background data consumption."
  - "A partner, acquaintance, or third party demonstrates knowledge of private chats, locations, or calls."

prerequisites:
  clean_environment_required: false
  prerequisite_warning: "SAFETY WARNING: If dealing with domestic abuse or coercive control, removing stalkerware immediately may alert the abuser. Coordinate with the victim and ensure an offline safety plan is in place before making device changes."
---

# [IRP-EP-MOB-001] Mobile Stalkerware & Surveillance Audit

> **Operational Warning:** Stalkerware often relies on native device sharing features (Find My, Google Location Sharing, Family Sharing) rather than exotic malware. Always audit built-in platform sharing mechanisms before hunting for clandestine binaries.

---

## Phase 1: Built-in Sharing Audit (The Low-Hanging Fruit)

Attackers with physical access to an unlocked phone frequently abuse native features:

### 1. iOS (Apple) Audit
* **Find My Sharing:** Open the **Find My** app > **People** tab. Verify who can see the device location. Stop sharing with unauthorized individuals.
* **Family Sharing:** Check **Settings > [User Name] > Family Sharing**. Ensure the user is not part of an unauthorized family group that enforces location tracking or screen time restrictions.
* **Safety Check (iOS 16+):** Navigate to **Settings > Privacy & Security > Safety Check**.
  * Use **Emergency Reset** to immediately sever all location sharing, Bluetooth access, and app permissions with all people and apps.

### 2. Android Audit
* **Google Location Sharing:** Open **Google Maps** > Tap the profile icon > **Location Sharing**. Check for active, continuous location links and stop unauthorized sharing.
* **Device Admin Apps:** Navigate to: **Settings > Security > More security settings > Device admin apps** (path varies slightly by vendor). Ensure no unknown apps have administrator privileges (which prevents standard uninstallation).

---

## Phase 2: App and Profile Persistence Hunting

### 1. Configuration Profiles (iOS)
Commercial stalkerware often installs Mobile Device Management (MDM) profiles to bypass Apple's security sandbox.
* Navigate to: **Settings > General > VPN & Device Management**.
* If any profile exists that was not placed there by an employer or school, **Remove the Profile immediately**.

### 2. Sideloaded / Sideloading Permissions (Android)
* Navigate to: **Settings > Apps > Special app access > Install unknown apps**.
* Ensure no browser, file manager, or untrusted utility has permission to install APKs.
* Open the **Google Play Store > Profile > Play Protect > Scan**. Check if Play Protect was deliberately disabled.

---

## Phase 3: Eradication

* [ ] **The Definitive Fix:** **Full Factory Reset**
  * Stalkerware modifications, hidden child-monitoring utilities (e.g., mSpy, eyeZy), and rogue enterprise certificates rarely survive a clean device factory reset.
  * **Critical:** When restoring after the reset, **do not restore from a full cloud backup** made during the period of suspected compromise. Restore only synced contacts, photos, and basic files. Reinstall apps manually from the official App Store or Google Play Store.

---

## Phase 4: Hardening & Post-Audit Verification

- [ ] **Rotate Device Passcode:** Change the lock screen PIN/passcode to an alphanumeric string the abuser cannot guess. Avoid birthdays, anniversaries, or simple 4-digit PINs.
- [ ] **Secure the Identity Anchor:** Change the password for the Apple ID or primary Google account tied to the mobile device. Enable passkeys or authenticator apps.
- [ ] **SIM PIN:** Set up a SIM card lock PIN under cellular settings to prevent the SIM card from being moved to another device for unauthorized SMS interception.
