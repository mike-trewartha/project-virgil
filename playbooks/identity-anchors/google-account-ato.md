---
id: "IRP-GOOG-001"
title: "Google / Gmail Account Compromise & ATO"
platform: "Google"
version: "1.0.0"
last_verified: "2026-10-22"
severity_level: "Critical"  # Critical (Identity Anchor) | High (Financial/Social) | Medium (Isolated)
target_audience: "Operator & Tech-Savvy Helper"

endpoints:
  account_security: "https://myaccount.google.com/security"
  active_sessions: "https://myaccount.google.com/device-activity"
  third_party_access: "https://myaccount.google.com/connections"
  mail_forwarding: "https://mail.google.com/mail/u/0/#settings/fwdandpop"
  mail_filters: "https://mail.google.com/mail/u/0/#settings/filters"
  security_checkup: "https://myaccount.google.com/security-checkup"

indicators:
  - "Unauthorized outgoing emails or drafts observed."
  - "Unexpected password reset emails from linked financial or social services."
  - "Security alerts indicating a new device login or session token created."
  - "Two-factor authentication prompts received without user initiation."

prerequisites:
  clean_environment_required: true
  prerequisite_warning: "DO NOT run password resets from a machine suspected of running infostealer malware. Use a separate smartphone or known clean device."
---

# [IRP-GOOG-001] Google / Gmail Account Takeover (ATO)

> **Blast Radius Warning:** A Google account is an **Identity Anchor**. Compromise of this account compromises all secondary accounts using it for password resets or Google OAuth (SSO).

---

## Phase 0: Pre-Flight Safety Check

Before taking any recovery actions:
- **Establish Clean Device:** Verify whether the incident originated from a compromised PC (e.g., game mod, pirated software, cracked executable). If infostealer malware is suspected, power down the infected device immediately. Perform all subsequent steps from an unaffected smartphone or secondary computer.
- **Check Access Status:** Can the legitimate owner still sign in?
  - **Yes:** Proceed directly to **Phase 1: Emergency Containment**.
  - **No (Locked Out):** Jump immediately to **Phase 1B: Recovery & Lockout Bypass**.

---

## Phase 1: Emergency Containment (Stop Active Adversary Access)

Objective: Kill existing attacker sessions and secure the perimeter credentials.

1. **Terminate Remote Sessions**
   * Navigate directly to: `https://myaccount.google.com/device-activity`
   * Select any unrecognized hardware, browser sessions, or remote IP locations.
   * Click **Sign out** for every session except your current clean device.

2. **Force Primary Credential Rotation**
   * Change password via: `https://myaccount.google.com/signinoptions/password`
   * Generate a unique, random 20+ character password using a dedicated password manager.
   * *Note: Changing the password invalidates most existing OAuth session refresh tokens.*

3. **Purge Passkeys & Hardware Keys**
   * Navigate to: `https://myaccount.google.com/signinoptions/passkeys`
   * Review all enrolled passkeys. Revoke any passkey not created on your verified devices.

---

## Phase 1B: Recovery & Lockout Bypass (Attacker Changed Credentials)

If the adversary has altered the primary password or recovery email:
1. Navigate directly to account recovery: `https://accounts.google.com/signin/recovery`
2. **Execute from a Familiar Network:** Perform this step from a home Wi-Fi network or IP address frequently used with this account to pass Google's automated risk scoring.
3. If MFA fails, choose **"Try another way"** to fall back to pre-existing backup codes, SMS (if carrier SIM is uncompromised), or hardware tokens.

---

## Phase 2: Eradication & Persistence Hunting

Objective: Remove backdoors that allow the adversary to retain access after a password change.

### 1. Mailbox Routing & Snooping Controls
Attackers frequently configure silent rules to harvest password reset tokens while hiding them from the victim.
* **Forwarding Addresses:** Check `https://mail.google.com/mail/u/0/#settings/fwdandpop`. Ensure no unknown email address is listed under **Forwarding**. Remove unauthorized destinations.
* **Hidden Inbox Filters:** Check `https://mail.google.com/mail/u/0/#settings/filters`. Search for rules containing `to:`, `subject: (verification OR code OR reset OR statement)`, or rules that trigger **"Skip the Inbox"** / **"Mark as read"** / **"Delete it"**. Delete malicious filters.
* **Delegated Accounts:** Check `https://mail.google.com/mail/u/0/#settings/accounts`. Look under **"Grant access to your account"** to confirm no secondary account is delegated.

### 2. OAuth App Consent & API Tokens
* Navigate to: `https://myaccount.google.com/connections`
* Review **"Third-party apps with account access"**.
* Select and click **Delete all connections** for any app granting full Google Drive, Gmail, or profile access that you do not explicitly recognize.

### 3. Recovery Safeguard Verification
* Navigate to: `https://myaccount.google.com/security`
* **Recovery Phone:** Verify the number is correct.
* **Recovery Email:** Verify the email address has not been switched to an attacker inbox.

---

## Phase 3: Blast Radius Assessment & Downstream Remediation

Because this account functions as a central identity anchor, evaluate linked dependencies in order of risk:
1. **Audit Trash/Spam for Intercepted Resets:** 
   * Search `in:trash` and `in:spam` for password reset emails requested during the compromise window.
2. **Prioritize Downstream Accounts:**
   * Immediately rotate master credentials for critical services associated with this email (Banks, PayPal, Apple ID, Amazon, Primary Password Manager).

---

## Phase 4: Hardening & Post-Incident Closure

- **Generate Emergency Backup Codes:** Print or write down 10 single-use recovery codes from `https://myaccount.google.com/signinoptions/two-step-verification` and store them physically offline.
- **Enforce FIDO2 / Passkeys:** Transition authentication from SMS 2FA to hardware keys (YubiKey) or system passkeys.
- **Run Security Checkup:** Complete `https://myaccount.google.com/security-checkup` to confirm no residual warnings persist.
