---
id: "IRP-AAPL-001"
title: "Apple ID & iCloud Account Takeover"
platform: "Apple"
version: "1.0.0"
last_verified: "2026-10-22"
severity_level: "Critical"
target_audience: "Operator & Tech-Savvy Helper"

endpoints:
  account_management: "https://appleid.apple.com/account/manage"
  device_management: "https://appleid.apple.com/account/manage/section/devices"
  security_settings: "https://appleid.apple.com/account/manage/section/security"
  find_devices: "https://www.icloud.com/find"
  icloud_mail_rules: "https://www.icloud.com/mail/" # Requires manual navigation to settings gear > rules

indicators:
  - "Unexpected 'Apple ID Sign In Requested' maps/prompts on trusted devices."
  - "Receipts for App Store or Apple Pay purchases not made by the user."
  - "Devices unexpectedly shifting into 'Lost Mode'."
  - "Notifications that a Trusted Phone Number or Recovery Contact was added/changed."

prerequisites:
  clean_environment_required: true
  prerequisite_warning: "Apple heavily favors recovery via an already-trusted Apple device (iPhone/iPad/Mac) with a passcode. Prioritize using the victim's physical iPhone over a web browser if it remains logged in and uncompromised."
---

# [IRP-AAPL-001] Apple ID & iCloud Account Takeover (ATO)

> **Blast Radius Warning:** An Apple ID compromise grants access to iCloud Keychain (effectively a password manager breach), iMessage interception, Apple Pay, and the ability to permanently brick hardware via Activation Lock / Lost Mode.

---

## Phase 0: Pre-Flight Safety Check

Before taking web-based recovery actions:
- **Locate a Trusted Device:** Does the victim have physical possession of their unlocked iPhone, iPad, or Mac that is still signed into the Apple ID?
  - **Yes:** Perform all password resets and evictions directly on this device via `Settings > [Victim's Name]`. This bypasses most web-based friction.
  - **No (or Locked Out):** You must rely on the web portals or the Apple Support app on a borrowed device.

---

## Phase 1: Emergency Containment (Stop Active Adversary Access)

Objective: Terminate the attacker's sessions and revoke their ability to interact with iCloud data.

1. **Force Primary Credential Rotation**
   * If using a trusted device: Navigate to **Settings > [Name] > Sign-In & Security > Change Password**.
   * If using the web: Navigate to `https://appleid.apple.com/account/manage/section/security` and select **Password**.
   * *Note: Changing the Apple ID password will prompt you to automatically sign out all other devices and web sessions. Select **Sign Out of Other Devices**.*

2. **Evict Rogue Hardware**
   * Navigate to `https://appleid.apple.com/account/manage/section/devices`.
   * Review the list of trusted devices. If the adversary added their own device to bypass 2FA, click it and select **Remove from Account**.
   * *Critical: Removing a device immediately strips its ability to approve future Apple ID sign-in requests.*

3. **Revoke App-Specific Passwords**
   * While in `https://appleid.apple.com/account/manage/section/security`, select **App-Specific Passwords**.
   * Revoke all active passwords to ensure attackers haven't established persistence via third-party mail clients or calendars.

---

## Phase 1B: Recovery & Lockout Bypass (Attacker Changed Credentials)

If the adversary locked the victim out:
1. Use the **Apple Support app** on a *different* (clean) Apple device (like the helper's iPhone).
2. Go to **Support Tools > Reset Password > A different Apple ID**.
3. Follow the prompts using the victim's trusted phone number. This method is often prioritized in Apple's queue over web-based recovery (`iforgot.apple.com`), which can trigger a mandatory multi-day waiting period.

---

## Phase 2: Eradication & Persistence Hunting

Objective: Remove recovery backdoors that the adversary planted to regain access.

### 1. Recovery & Account Contacts Audit
Attackers will often quietly add their own phone number or Apple ID as a recovery mechanism.
* Navigate to `https://appleid.apple.com/account/manage/section/security`.
* **Trusted Phone Numbers:** Verify that *only* the victim's active phone numbers are listed. Delete any unrecognized numbers.
* **Account Recovery Contact:** Verify no unauthorized individuals are listed as Recovery Contacts.
* **Legacy Contact:** Verify no unauthorized individuals are listed to inherit the account data.

### 2. iCloud Mail Forwarding & Rules
If the Apple ID uses an `@icloud.com`, `@me.com`, or `@mac.com` address, attackers will hide reset tokens.
* Navigate to `https://www.icloud.com/mail/`.
* Open the **Settings (Gear Icon) > Rules**. Delete any rules auto-forwarding or trashing incoming mail.
* Check **Settings > Forwarding** and disable unauthorized forwarding addresses.

### 3. Apple Account Access (OAuth)
* Navigate to `https://appleid.apple.com/account/manage/section/security`.
* Select **Sign in with Apple**. Review the list of connected apps and select **Stop Using Apple ID** for any unrecognized services.

---

## Phase 3: Blast Radius Assessment & Downstream Remediation

1. **iCloud Keychain Compromise:** If the attacker had a session active, assume all passwords stored in iCloud Keychain are compromised. Begin rotating passwords for high-value targets (banking, email, primary social media).
2. **Apple Pay / Wallet Audit:** Review recent transactions. Removing an Apple ID or changing the password usually suspends Apple Pay cards, but contact the issuing banks to monitor for unauthorized token provisioning.
3. **iMessage/FaceTime History:** Advise the victim that the attacker may have synced recent iMessage history to their rogue device before being evicted. 

---

## Phase 4: Hardening & Post-Incident Closure

- **Enable Advanced Data Protection (ADP):** Go to `Settings > [Name] > iCloud > Advanced Data Protection`. This end-to-end encrypts iCloud backups, Photos, and Drive, meaning even if Apple is breached or the web session is hijacked, the data requires a trusted device key to decrypt.
- **Generate a Recovery Key:** Enable a 28-character Recovery Key in the Security settings. *Warning: Losing this key and a trusted device simultaneously means permanent loss of the account.*
- **Enforce Hardware Security Keys:** Transition 2FA from standard SMS/trusted-device prompts to FIDO2 hardware keys (e.g., YubiKey) under the **Security Keys** menu.
