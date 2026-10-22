---
id: "IRP-MSFT-001"
title: "Microsoft / Live / Outlook Account Takeover"
platform: "Microsoft"
version: "1.0.0"
last_verified: "2026-10-22"
severity_level: "Critical"
target_audience: "Operator & Tech-Savvy Helper"

endpoints:
  account_dashboard: "https://account.microsoft.com/"
  security_dashboard: "https://account.microsoft.com/security"
  sign_out_everywhere: "https://account.microsoft.com/security" # Under Advanced Security Options
  connected_apps: "https://account.live.com/consent/Manage"
  recent_activity: "https://account.live.com/Activity"
  account_aliases: "https://account.live.com/names/manage"
  outlook_rules: "https://outlook.live.com/mail/0/options/mail/rules"
  outlook_forwarding: "https://outlook.live.com/mail/0/options/mail/forwarding"
  recovery_portal: "https://account.live.com/acsr"

indicators:
  - "Security alerts indicating login from an unfamiliar country/IP."
  - "Contacts receiving spam emails originating from the user's @outlook.com or @hotmail.com address."
  - "Notification that the primary account alias or security phone number was changed."
  - "Purchases on the Microsoft Store / Xbox Live not initiated by the user."

prerequisites:
  clean_environment_required: true
  prerequisite_warning: "Do not execute recovery from a host suspected of session cookie theft or infostealer infection."
---

# [IRP-MSFT-001] Microsoft Account Takeover (ATO)

> **Blast Radius Warning:** A Microsoft account controls Outlook.com, Windows OS sign-in, OneDrive files, Xbox profiles, and linked Microsoft 365 services. Attackers often target the primary alias to permanently orphan the victim's access.

---

## Phase 0: Pre-Flight Safety Check

- [ ] **Confirm Local PC Status:** Is the user signed into their Windows 10/11 PC with this Microsoft account? If the attacker alters the account password, the local PC login will eventually reject offline PINs or lock the desktop out.
- [ ] **Check Sign-In Capability:**
  - **Can Sign In:** Proceed immediately to **Phase 1: Emergency Containment**.
  - **Primary Alias Deleted / Locked Out:** Jump directly to **Phase 1B: Recovery & Lockout Bypass**.

---

## Phase 1: Emergency Containment (Stop Active Adversary Access)

Objective: Terminate attacker sessions and cut off remote access tokens.

1. **Execute "Sign Out Everywhere"**
   * Navigate to: `https://account.microsoft.com/security`
   * Select **Advanced security options**.
   * Scroll down to **Sign out everywhere** and click **Sign out everywhere**.
   * *Note: Microsoft will invalidate all active browser sessions, apps, and tokens within 24 hours (usually effective immediately).*

2. **Force Credential Rotation**
   * Navigate to: `https://account.microsoft.com/security`
   * Select **Change password**. Generate a unique 20+ character passphrase via a password manager.

3. **Audit Trusted 2FA Methods**
   * While in **Advanced security options**, review **Ways to prove who you are**.
   * If the attacker enrolled an unfamiliar Microsoft Authenticator instance or unfamiliar phone number, delete it immediately.

---

## Phase 1B: Recovery & Lockout Bypass (Attacker Changed Alias)

If the adversary has changed the primary login alias:
1. Attackers often add their own address as the primary alias and delete the victim’s original address. If the original address ended in `@hotmail.com` or `@live.com`, **deletion is permanent and cannot be recreated.**
2. Navigate directly to the automated recovery questionnaire: `https://account.live.com/acsr`.
3. Provide previous passwords, exact subject lines of recently sent emails, and billing/credit card details historically attached to the account to clear automated scoring.

---

## Phase 2: Eradication & Persistence Hunting

Objective: Eliminate quiet backdoors left by the attacker inside Outlook and OAuth permissions.

### 1. Outlook Web Mail Forwarding & Rules
* [ ] **Forwarding:** Check `https://outlook.live.com/mail/0/options/mail/forwarding`. Ensure **Enable forwarding** is unticked.
* [ ] **Hidden Inbox Rules:** Check `https://outlook.live.com/mail/0/options/mail/rules`.
  * Search for rules containing "Delete", "Mark as read", or rules targeting keywords like `verification`, `code`, `security`, `invoice`, or `crypto`. Delete unauthorized rules.

### 2. Third-Party App & Consent Grants (OAuth)
Attackers frequently bind an enterprise or rogue consumer app to retain full mailbox access via Microsoft Graph API.
* [ ] Navigate to: `https://account.live.com/consent/Manage`
* [ ] Review **Apps and services you've given access**.
* [ ] Select each suspicious entry and click **Remove these permissions**.

### 3. Alias & Sign-in Preferences Check
* [ ] Navigate to: `https://account.live.com/names/manage`
* [ ] Confirm that all email addresses and phone numbers listed under **Account aliases** belong to the legitimate owner.
* [ ] Verify the **Primary alias** is set to the victim's verified email.

---

## Phase 3: Blast Radius Assessment & Downstream Remediation

1. **OneDrive Audit:** Check `https://onedrive.live.com/` -> **Recycle bin** and **Recent files** to ensure sensitive documents or photo vaults were not wiped or mass-downloaded.
2. **Linked Windows Devices:** Check `https://account.microsoft.com/devices`. If rogue laptops or PCs are enrolled, remove them to revoke auto-syncing of Edge passwords and BitLocker keys.
3. **Downstream Password Resets:** Audit the Outlook inbox trash folder (`inbox > Deleted Items > Recover items deleted from this folder`) for password reset attempts received during the incident window.

---

## Phase 4: Hardening & Post-Incident Closure

- [ ] **Go Passwordless:** In **Advanced security options**, enable **Passwordless account**. This converts authentication strictly to the Microsoft Authenticator app or FIDO2 security keys, neutralizing standard brute force and credential stuffing attacks entirely.
- [ ] **Generate a 25-Character Recovery Code:** Under **Recovery code**, click **Generate a new code**. Print or store this code offline in a physical safe.
