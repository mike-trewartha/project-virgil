---
id: "IRP-SOC-002"
title: "LinkedIn Account Takeover"
platform: "LinkedIn"
version: "1.0.0"
last_verified: "2026-10-22"
severity_level: "High"
target_audience: "Operator & Tech-Savvy Helper"

endpoints:
  password_reset: "https://www.linkedin.com/uas/request-password-reset"
  active_sessions: "https://www.linkedin.com/mypreferences/d/categories/security"
  permitted_services: "https://www.linkedin.com/mypreferences/d/categories/data-privacy"
  hacked_support: "https://www.linkedin.com/help/linkedin/ask/ts-f-appeal"

indicators:
  - "Profile photo, headline, or current employment changed to a cryptocurrency or investment scam."
  - "Connections receiving messages offering 'job opportunities' or crypto investments."
  - "Notification that your primary email address was removed from the account."

prerequisites:
  clean_environment_required: true
  prerequisite_warning: "LinkedIn accounts are often tied to corporate email addresses. If the account is compromised, the attacker may attempt to pivot to the employer's network or impersonate the user to colleagues."
---

# [IRP-SOC-002] LinkedIn Account Takeover (ATO)

> **Blast Radius Warning:** A compromised LinkedIn profile leverages professional trust. Attackers use it to phish colleagues, recruit for fake jobs, or distribute malware to the victim's professional network. 

---

## Phase 1: Emergency Containment

1. **Force Credential Rotation**
   * Navigate to: `https://www.linkedin.com/uas/request-password-reset`
   * Change the password. 
2. **Kill Active Sessions**
   * Navigate to: `https://www.linkedin.com/mypreferences/d/categories/security` > **Where you're signed in**.
   * Click **End these sessions** for all unrecognized devices.

---

## Phase 1B: Recovery & Lockout Bypass

If the adversary locked the victim out by changing the email:
1. Navigate directly to the restriction appeals form: `https://www.linkedin.com/help/linkedin/ask/ts-f-appeal`. Alternatively, LinkedIn suggests navigating to their Help Center and selecting "Account hacked".
2. Contact LinkedIn support directly, attaching proof (like previous emails from LinkedIn) that the account belongs to you. Make sure you contact them using the personal email address that was connected to your account. LinkedIn may require you to verify your identity. You can also email their appeal team directly at `account-appeals@linkedin.com`.
3. *Note: LinkedIn support is notably slow. Expect a 3-4 day turnaround for identity verification. Do not engage with "hackers" on other platforms claiming they can recover the account for a fee.*

---

## Phase 2: Eradication & Persistence Hunting

### 1. Verify Email Addresses & Phone Numbers
* Navigate to **Settings & Privacy > Sign in & security > Email addresses**.
* Ensure only recognized email addresses are present. Remove any addresses added by the attacker. Check **Phone numbers** as well.

### 2. Audit Permitted Services (OAuth)
* Navigate to **Settings & Privacy > Data privacy > Permitted services**.
* Review third-party apps connected to the account. Click **Remove** for any suspicious applications.

---

## Phase 3: Blast Radius Assessment

1. **Review Messages:** Check the LinkedIn messaging inbox to see if the attacker sent phishing links or scam solicitations to connections.
2. **Review Posts & Profile:** Verify that the profile headline, experience, and recent activity (posts/comments) have not been altered to promote scams.

---

## Phase 4: Hardening

- [ ] **Enable Two-Step Verification:** Navigate to **Settings & Privacy > Sign in & security > Two-step verification**. Turn it on and prefer using an Authenticator app over SMS.
