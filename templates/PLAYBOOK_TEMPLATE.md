---
id: "IRP-XXX-001"
title: "[Platform Name] Account Takeover"
platform: "[Platform]"
version: "1.0.0"
last_verified: "YYYY-MM-DD"
severity_level: "[Critical | High | Medium]"
target_audience: "Operator & Tech-Savvy Helper"

# Provide direct configuration URLs here. Do not rely on UI click-paths.
endpoints:
  sessions: "https://..."
  password_change: "https://..."
  two_factor: "https://..."
  oauth_apps: "https://..."
  recovery: "https://..."

indicators:
  - "Indicator 1 (e.g., unexpected password reset email)."
  - "Indicator 2 (e.g., messages sent to contacts)."

prerequisites:
  clean_environment_required: true
  prerequisite_warning: "Provide any warnings about malware, infostealers, or platform-specific lockouts before recovery begins."
---

# [IRP-XXX-001] [Platform] Account Takeover (ATO)

> **Blast Radius Warning:** Briefly describe what an attacker gains by holding this account (e.g., financial access, downstream SSO, identity impersonation).

---

## Phase 0: Pre-Flight Safety Check

- [ ] **Establish Clean Device:** Verify the recovery is taking place on a clean device to prevent immediate credential theft.
- [ ] **Check Access Status:** Can the legitimate owner still sign in?

---

## Phase 1: Emergency Containment (Stop Active Adversary Access)

Objective: Kill existing attacker sessions and secure the perimeter credentials.

1. **Terminate Remote Sessions**
   * Navigate directly to: `[Insert Sessions URL]`
   * Select and log out all unrecognized sessions.
2. **Force Credential Rotation**
   * Navigate to: `[Insert Password URL]`
   * Generate a unique password using a password manager.
3. **Secure Two-Factor Authentication**
   * Navigate to: `[Insert 2FA URL]`
   * Remove any attacker-added phone numbers or authenticator apps.

---

## Phase 1B: Recovery & Lockout Bypass

If the adversary has locked the victim out:
1. Navigate directly to account recovery: `[Insert Recovery URL]`
2. **Execution Context:** Provide any platform-specific quirks (e.g., "Meta prefers familiar IP addresses," "Apple requires a trusted device").

---

## Phase 2: Eradication & Persistence Hunting

Objective: Remove backdoors that allow the adversary to retain access.

### 1. [Specific Persistence Vector 1]
* Navigate to: `[URL]`
* Describe what the attacker might hide here (e.g., mailbox rules, API keys).

### 2. [Specific Persistence Vector 2 (OAuth/Apps)]
* Navigate to: `[URL]`
* Describe how to revoke rogue applications.

---

## Phase 3: Blast Radius Assessment & Downstream Remediation

1. **[Downstream Risk 1]:** E.g., Audit linked credit cards.
2. **[Downstream Risk 2]:** E.g., Warn contacts about social engineering.

---

## Phase 4: Hardening & Post-Incident Closure

- [ ] **Enforce Strong MFA:** Transition from SMS 2FA to an Authenticator App or FIDO2 key.
- [ ] **Generate Backup Codes:** Store recovery codes physically offline.
