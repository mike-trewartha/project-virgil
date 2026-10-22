---
id: "IRP-TEL-001"
title: "SIM Swap / Phone Porting Compromise"
platform: "Telecommunications (General)"
version: "1.0.0"
last_verified: "2026-10-22"
severity_level: "Critical"
target_audience: "Operator & Tech-Savvy Helper"

indicators:
  - "Mobile device suddenly shows 'No Service', 'SOS Only', or 'SIM not provisioned'."
  - "Unexpected carrier emails thanking you for activating a new device or porting your number."
  - "A flood of SMS 2FA codes arriving just prior to losing cellular service."
  - "Simultaneous lockouts from bank accounts, crypto exchanges, and primary email."

prerequisites:
  clean_environment_required: false
  prerequisite_warning: "A SIM swap is a race condition. The attacker currently receives all calls and SMS 2FA codes intended for the victim. Action must be taken within minutes."
---

# [IRP-TEL-001] SIM Swap / Phone Porting Compromise

> **Blast Radius Warning:** A hijacked phone number bypasses SMS-based Two-Factor Authentication (2FA). Attackers use this to execute immediate password resets against high-value targets (cryptocurrency exchanges, banking, primary email).

---

## Phase 1: Emergency Containment (The Golden Hour)

Objective: Freeze financial assets and lock down Identity Anchors before the attacker intercepts the reset codes.

### 1. Carrier Intervention (Immediate)
* **Call the Carrier:** Use a different phone to call the victim's mobile carrier fraud department immediately.
* **The Directive:** Instruct the carrier that a fraudulent SIM swap/port-out is in progress. Demand they **suspend the line** or revert the port immediately.
* **Establish a PIN:** If reverting the SIM, force the carrier to add a high-security port-out PIN or voice password to the account to prevent the attacker from simply doing it again in an hour.

### 2. Identity Anchor Lockdown
While one person is on the phone with the carrier, the victim/helper must secure the root email addresses.
* Navigate to the primary email (Gmail/Outlook) and primary password manager from a trusted, logged-in device.
* **Remove SMS 2FA:** Go to the security settings and delete the compromised phone number as a recovery option.
* **Kill Sessions:** Execute the session termination steps detailed in the `identity-anchors` playbooks.

### 3. Financial Freeze
Attackers typically target crypto (Coinbase, Binance) and banking platforms within the first 10 minutes.
* Call the fraud departments of the victim's primary banks.
* Log into cryptocurrency exchanges and invoke the "Freeze Account" or "Lock Account" emergency link (often found at the bottom of login alert emails).

---

## Phase 2: Eradication & Persistence Hunting

If the attacker held the phone number for any length of time, you must assume they successfully reset passwords.

### 1. Identify Compromised Downstream Services
* Review the victim's primary email inbox, **Trash**, and **Archive** folders. Look for password reset confirmations, security alerts, or "New Login" emails.
* Any service that sent a reset token during the "No Service" window must be considered compromised.

### 2. Messenger Takeover Triage
* **WhatsApp/Signal/Telegram:** Attackers will register the victim's number on their own device to hijack messaging histories or scam contacts.
* Once the carrier restores the SIM to the victim's physical phone, immediately re-register WhatsApp, Signal, and Telegram. This automatically kicks the attacker's session off.
* Enable the respective app-specific PINs (e.g., WhatsApp Two-Step Verification) so a future SIM swap cannot hijack the chat profile.

---

## Phase 3: Post-Incident Hardening

- [ ] **Migrate 2FA:** Strip the phone number from *all* critical accounts. Move 2FA exclusively to Authenticator Apps (TOTP) or Hardware Security Keys (YubiKey). 
- [ ] **Carrier Port Freeze:** Keep the high-security verbal PIN or "Port Freeze" active on the telecommunications account permanently.
- [ ] **De-link Number from Identity:** Remove the phone number from the public profile of social media accounts (X, Meta) to prevent automated OSINT scraping from identifying the target.
