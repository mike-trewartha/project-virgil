---
id: "IRP-META-001"
title: "Meta (Facebook & Instagram) Account Takeover"
platform: "Meta"
version: "1.0.0"
last_verified: "2026-10-22"
severity_level: "High"
target_audience: "Operator & Tech-Savvy Helper"

endpoints:
  accounts_center: "https://accountscenter.meta.com/"
  sessions: "https://accountscenter.meta.com/passwords_and_security/logged_in_sessions"
  password_change: "https://accountscenter.meta.com/passwords_and_security/password"
  two_factor: "https://accountscenter.meta.com/passwords_and_security/two_factor"
  personal_details: "https://accountscenter.meta.com/personal_info"
  facebook_apps: "https://www.facebook.com/settings?tab=applications"
  facebook_hacked: "https://www.facebook.com/hacked"
  instagram_hacked: "https://www.instagram.com/hacked"
  business_manager: "https://business.facebook.com/"

indicators:
  - "Direct messages sent to friends requesting money, crypto, or 'help with a contest'."
  - "Profile picture, bio, or cover photo changed to cryptocurrency or investment branding."
  - "Unexpected password reset emails or alerts of a login from a new device."
  - "Charges on linked credit cards for Meta Ads."

prerequisites:
  clean_environment_required: true
  prerequisite_warning: "Infostealers frequently target Facebook session cookies to bypass 2FA. Do not attempt recovery from a device suspected of malware infection."
---

# [IRP-META-001] Meta (Facebook & Instagram) Account Takeover (ATO)

> **Blast Radius Warning:** Meta accounts are highly interconnected via the Accounts Center. An attacker compromising an Instagram account can often pivot to the linked Facebook account, and more destructively, access linked Business Manager accounts to run fraudulent ad campaigns.

---

## Phase 0: Pre-Flight Safety Check

Before taking web-based recovery actions:
- **Establish Clean Device:** Perform all subsequent steps from a clean smartphone or secondary computer.
- **Check Access Status:** Can the legitimate owner still sign in?
  - **Yes:** Proceed directly to **Phase 1: Emergency Containment**.
  - **No (Locked Out):** Jump immediately to **Phase 1B: Recovery & Lockout Bypass**.

---

## Phase 1: Emergency Containment (Stop Active Adversary Access)

Objective: Terminate the attacker's sessions across the Meta ecosystem.

1. **Terminate Remote Sessions**
   * Navigate directly to: `https://accountscenter.meta.com/passwords_and_security/logged_in_sessions`
   * Select the compromised account. Review all active sessions.
   * Click **Select devices to log out** and select all unrecognized sessions. (When in doubt, log out of everything except the current device).

2. **Force Primary Credential Rotation**
   * Navigate to: `https://accountscenter.meta.com/passwords_and_security/password`
   * Change the password using a dedicated password manager. Ensure the new password has never been used on another site.

3. **Secure Two-Factor Authentication**
   * Navigate to: `https://accountscenter.meta.com/passwords_and_security/two_factor`
   * Review enrolled 2FA methods. If the attacker added their own authenticator app or phone number, remove it immediately.

---

## Phase 1B: Recovery & Lockout Bypass (Attacker Changed Credentials)

If the adversary has locked the victim out by changing the password and email:
1. **Facebook:** Navigate to `https://www.facebook.com/hacked` and select "My account is compromised."
2. **Instagram:** Navigate to `https://www.instagram.com/hacked`.
3. **Execution Context:** Perform these steps from a device (like the victim's smartphone) and a Wi-Fi network that was previously used to access the accounts. Meta's risk engine heavily weights familiar IP addresses and device fingerprints during account recovery.
4. **Video Selfie / ID Verification:** If the attacker enabled 2FA, select "Try another way" or "Get support" to trigger the identity verification flow. The victim will need to upload a government-issued ID or record a video selfie.

---

## Phase 2: Eradication & Persistence Hunting

Objective: Remove backdoors that allow the adversary to retain access after a password change. This is the most critical phase for Meta compromises.

### 1. The Accounts Center Pivot (Rogue Linked Profiles)
Attackers frequently link their own Instagram or Meta accounts to the victim's Accounts Center. This grants them a persistent backdoor that survives a password reset.
* Navigate to: `https://accountscenter.meta.com/`
* Look under **Profiles**. Verify that every profile listed belongs to the victim.
* If a rogue account is present, click on it and select **Remove from Accounts Center**.

### 2. Contact Points Audit
* Navigate to: `https://accountscenter.meta.com/personal_info`
* Review **Contact info**. Attackers will add their own email address or phone number here to intercept future password resets.
* Delete any email or phone number that the victim does not exclusively control.

### 3. App & Website OAuth Consent (Facebook)
* Navigate to: `https://www.facebook.com/settings?tab=applications`
* Review the list of active apps and websites. Attackers often grant access to rogue third-party apps to maintain API access to the account.
* Click **Remove** on any unrecognized or suspicious applications.

### 4. Meta Business Manager / Ad Accounts
* Navigate to: `https://business.facebook.com/`
* Check if the personal account is tied to any Ad Accounts or Business Portfolios.
* Check **Billing** for any active, unauthorized ad campaigns or newly added payment methods. If unauthorized ads are running, pause the campaigns immediately and contact Meta Business Support.

---

## Phase 3: Blast Radius Assessment & Downstream Remediation

1. **Third-Party SSO:** Did the victim use "Log in with Facebook" for other services (Spotify, Tinder, AirBnb)? If so, the attacker may have pivoted. Audit and rotate credentials for those linked services.
2. **Social Engineering Containment:** Warn close contacts.
   * Post a plain-text status update on Facebook/Instagram: *"My account was compromised on [Date]. Please ignore any messages asking for money, crypto, or votes. I have regained control."*
3. **Financial Audit:** Review connected credit cards in Facebook Pay/Meta Pay and check bank statements for unauthorized charges.

---

## Phase 4: Hardening & Post-Incident Closure

- **Enforce Authenticator App:** In `https://accountscenter.meta.com/passwords_and_security/two_factor`, transition away from SMS-based 2FA and use an Authenticator App (e.g., Google Authenticator, Aegis, Authy).
- **Enable Login Alerts:** Under Passwords and Security, go to **Login alerts** and ensure in-app and email notifications are enabled for unrecognized logins.
- **Generate Recovery Codes:** Download or write down the 2FA recovery codes and store them safely offline.
