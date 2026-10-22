---
id: "IRP-SOC-001"
title: "X (Twitter) Account Takeover"
platform: "X / Twitter"
version: "1.0.0"
last_verified: "2026-10-22"
severity_level: "High"
target_audience: "Operator & Tech-Savvy Helper"

endpoints:
  password_reset: "https://x.com/i/flow/password_reset"
  sessions: "https://x.com/settings/sessions"
  connected_apps: "https://x.com/settings/connected_apps"
  account_access: "https://x.com/settings/account"
  hacked_support: "https://help.x.com/en/forms/account-access/regain-access/hacked-or-compromised"

indicators:
  - "Unexpected Tweets or Direct Messages containing crypto links, airdrop announcements, or 'exclusive giveaways'."
  - "Profile picture (NFT/Bored Ape) or bio changes."
  - "Notifications that your email address or password was changed."

prerequisites:
  clean_environment_required: true
  prerequisite_warning: "Infostealers are a primary vector for X takeovers. Verify the user's PC is clean before attempting recovery. If the attacker compromised the linked email address, secure the email first."
---

# [IRP-SOC-001] X (Twitter) Account Takeover (ATO)

> **Blast Radius Warning:** X accounts are heavily targeted by automated networks to pump cryptocurrency scams. If the victim has a large follower count or a "verified" checkmark, the account is highly valuable to attackers and will be aggressively monetized via malicious links.

---

## Phase 1: Emergency Containment

1. **Force Credential Rotation**
   * Navigate to: `https://x.com/i/flow/password_reset`
   * Enter the username or email. Check the associated email inbox for the reset link.
   * *Note: Changing the password on X automatically terminates all active sessions except the one performing the reset.*
2. **Review Two-Factor Authentication (2FA)**
   * Navigate to `https://x.com/settings/account` > **Security and account access** > **Security** > **Two-factor authentication**.
   * If the attacker enabled 2FA to lock you out, or added their own authenticator, disable it immediately.

---

## Phase 1B: Recovery & Lockout Bypass

If the adversary locked the victim out:
1. Navigate to: `https://help.x.com/en/forms/account-access/regain-access/hacked-or-compromised`
2. Submit a Support request. You will need to provide the username and the last date you successfully accessed the account. 

---

## Phase 2: Eradication & Persistence Hunting

### 1. Connected Apps (OAuth Audit)
Attackers frequently authorize malicious third-party apps to retain the ability to tweet or DM even after a password change.
* Navigate to: `https://x.com/settings/connected_apps`
* Review the list of authorized apps. Look for generic names (e.g., "Web App", "Social Manager") or apps with Read/Write/Direct Message permissions.
* Click **Revoke app permissions** on anything unrecognized.

### 2. Verify Contact Information
* Navigate to: `https://x.com/settings/account` > **Account information**.
* Ensure the **Phone** and **Email** belong solely to the victim. Delete any attacker-added phone numbers.

---

## Phase 3: Blast Radius Assessment

1. **Delete Fraudulent Posts:** Navigate to the victim's profile and delete any Tweets or Retweets made by the attacker.
2. **Warn Direct Message Contacts:** If the attacker sent DMs containing phishing links, send follow-up messages warning contacts not to click the links.
3. **Review Muted/Blocked Words:** Attackers sometimes mute words like "hacked", "scam", or "fake" so the victim doesn't see warnings from their followers. Check `https://x.com/settings/muted_keywords`.

---

## Phase 4: Hardening

- [ ] **Enforce Authenticator App or Security Key:** In the Security settings, enable an Authenticator app (TOTP) or a physical Security Key (FIDO2). *Note: X restricts SMS-based 2FA to Premium subscribers, which makes TOTP/Security Keys the primary (and safer) option for most users.*
