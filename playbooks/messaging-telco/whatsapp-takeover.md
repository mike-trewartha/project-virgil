---
id: "IRP-TEL-002"
title: "WhatsApp Account Takeover"
platform: "WhatsApp"
version: "1.0.0"
last_verified: "2026-10-22"
severity_level: "High"
target_audience: "Operator & Tech-Savvy Helper"

endpoints:
  whatsapp_web_logout: "In-App: Settings > Linked Devices"
  account_deletion: "https://faq.whatsapp.com/1119251868918239/?helpref=uf_share" # Emergency deactivation via email

indicators:
  - "The WhatsApp application suddenly logs you out with the message: 'Your phone number is no longer registered with WhatsApp on this phone.'"
  - "Contacts report receiving requests for money or crypto from your number."
  - "You receive unsolicited SMS verification codes for WhatsApp."

prerequisites:
  clean_environment_required: false
  prerequisite_warning: "If the attacker stole your WhatsApp account via a SIM swap, you MUST recover control of your phone number from your carrier before you can kick the attacker out of WhatsApp."
---

# [IRP-TEL-002] WhatsApp Account Takeover (ATO)

> **Blast Radius Warning:** WhatsApp takeovers are primarily used to scam the victim's address book. Because WhatsApp groups are inherently trusted, attackers will frequently impersonate the victim to solicit emergency funds from family members or post malicious crypto links into large group chats.

---

## Phase 1: Emergency Containment (The Take-Back Race)

Objective: Kick the attacker off the account by forcing a re-registration on your physical device. 

### 1. The Immediate Re-Verification
* Open WhatsApp on your smartphone.
* Enter your phone number and request the SMS verification code. 
* *Note: If the attacker guessed your code incorrectly too many times, WhatsApp may lock SMS verification for 12 hours. If this happens, request a **Phone Call** verification instead.*
* Once you enter the 6-digit code, the attacker’s session is immediately terminated. 

### 2. Lockout Bypass (Attacker Enabled a PIN)
If you enter the SMS code and WhatsApp asks for a Two-Step Verification PIN that you did not set:
* The attacker has enabled a rogue PIN to lock you out.
* You must wait **7 days** before WhatsApp allows you to sign in without the Two-Step Verification PIN.
* **Crucially:** Even though you are locked out for 7 days, the attacker’s session was still **disconnected** the moment you entered the SMS code. They can no longer message your contacts.

---

## Phase 2: Eradication & Persistence Hunting

If you maintained access or successfully took the account back, you must ensure the attacker didn't link secondary devices.

### 1. Linked Devices Audit
Attackers will often link WhatsApp Web or a companion device so they can maintain access even if you hold the primary phone.
* Open WhatsApp > **Settings** (or the three dots menu on Android) > **Linked Devices**.
* Review all active sessions. Tap any unrecognized device (e.g., "Windows", "Mac", "Web") and select **Log Out**.

---

## Phase 3: Blast Radius Assessment & Downstream Remediation

1. **Warn Your Network:** Use standard SMS, Facebook, or phone calls to notify close contacts and group admins that your WhatsApp was temporarily compromised and to ignore any financial requests.
2. **Review Group Admin Status:** If you were an admin of a WhatsApp group, the attacker may have added their own numbers as admins before you kicked them out. Review group participant lists and demote/remove unauthorized users.

---

## Phase 4: Hardening & Post-Incident Closure

- [ ] **Enforce Two-Step Verification:** Go to **Settings > Account > Two-Step Verification > Turn On**. Enter a 6-digit PIN and an email address. This prevents an attacker from registering your number even if they successfully execute a SIM swap.
- [ ] **Disable Voicemail Fallback:** Attackers often compromise WhatsApp by sending the verification code to voicemail in the middle of the night, then breaking into the victim's insecure carrier voicemail with a default PIN (e.g., 0000 or 1234). Call your carrier and set a complex voicemail PIN.
