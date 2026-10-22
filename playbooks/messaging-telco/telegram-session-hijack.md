---
id: "IRP-TEL-004"
title: "Telegram Session Hijack & Takeover"
platform: "Telegram"
version: "1.0.0"
last_verified: "2026-10-22"
severity_level: "Critical"
target_audience: "Operator & Tech-Savvy Helper"

endpoints:
  web_login: "https://web.telegram.org/"
  active_sessions: "In-App: Settings > Devices"

indicators:
  - "You see a service message from 'Telegram' notifying you of a login from a new IP/Device."
  - "Messages appear as 'Read' before you open them."
  - "You are suddenly added to crypto, investment, or spam channels."
  - "A 'Two-Step Verification' password is required to log in, but you never set one."

prerequisites:
  clean_environment_required: false
  prerequisite_warning: "Unlike WhatsApp and Signal, Telegram is a cloud-based messenger. An attacker who logs in can instantly download and read your entire historical chat history, excluding 'Secret Chats'."
---

# [IRP-TEL-004] Telegram Session Hijack & Takeover

> **Blast Radius Warning:** Because Telegram stores standard chats in the cloud, session hijacking leads to immediate, total data exfiltration of past conversations, media, and files. Attackers often run parallel hidden sessions on Telegram Desktop to silently monitor victims.

---

## Phase 1: Emergency Containment (Kill Parallel Sessions)

Objective: Telegram allows multiple devices to be logged in simultaneously. You must manually hunt down and terminate the attacker's session.

### 1. Active Devices Purge
* Open Telegram on your smartphone.
* Navigate to **Settings > Devices** (or **Privacy and Security > Active Sessions**).
* You will see the device you are currently holding, followed by a list of other active sessions.
* Tap **Terminate All Other Sessions**.
* *Crucial Timing Rule:* If you just logged into a new device to recover your account, Telegram's security model prevents you from terminating older sessions for **24 hours**. If this happens, you must secure the account via Two-Step Verification (Phase 4) and wait out the timer.

---

## Phase 1B: Recovery & Lockout Bypass

If the attacker logged you out completely and set a rogue password:
1. Attempt to log in using your phone number and SMS code.
2. When prompted for the cloud password, tap **Forgot Password?**
3. If the attacker changed the recovery email, tap **Reset Account**. This will instantly delete the entire cloud history of the account and let you start fresh, preventing the attacker from continuing to impersonate you. (Note: This is a destructive, point-of-no-return action).

---

## Phase 2: Eradication & Persistence Hunting

### 1. Check Connected Bots & Apps
Attackers often grant malicious bots access to the account to automate spam.
* Navigate to **Settings > Privacy and Security > Bots and websites** (or **Logged in with Telegram**).
* Revoke access to any bot or website you do not recognize.

### 2. Group & Channel Audit
* Return to your main chat list.
* Leave any newly joined cryptocurrency or investment groups. 
* Check your archived chats (swipe down on the chat list to reveal) to ensure the attacker didn't hide their staging groups.

---

## Phase 3: Blast Radius Assessment

1. **Assume Total Exfiltration:** If the attacker had a session active, assume all photos, attachments, and messages in standard (non-Secret) chats were downloaded. 
2. **Warn Contacts:** Telegram attackers frequently scrape your contact list and message them links to phishing portals or investment scams. Post a warning on your other social platforms.

---

## Phase 4: Hardening & Post-Incident Closure

- [ ] **Enforce Two-Step Verification:** Navigate to **Settings > Privacy and Security > Two-Step Verification**. Set a strong password. This acts as a secondary barrier that an attacker must pass even if they intercept your SMS code.
- [ ] **Set a Recovery Email:** While setting the Two-Step Verification password, provide a secure, uncompromised recovery email (like a Gmail account secured by a hardware key).
- [ ] **Hide Phone Number:** Go to **Settings > Privacy and Security > Phone Number**. Set "Who can see my phone number" to **Nobody**, and "Who can find me by my number" to **My Contacts** to prevent OSINT scraping and targeted SIM swap profiling.
