---
id: "IRP-TEL-003"
title: "Signal Registration Lock & Hijacking"
platform: "Signal"
version: "1.0.0"
last_verified: "2026-10-22"
severity_level: "Medium"
target_audience: "Operator & Tech-Savvy Helper"

endpoints:
  linked_devices: "In-App: Settings > Linked Devices"

indicators:
  - "Signal prompts you to re-register your device."
  - "Contacts see 'Safety Number Changed' alerts for your chat."
  - "You receive Signal verification codes via SMS that you did not request."

prerequisites:
  clean_environment_required: false
  prerequisite_warning: "Signal is tied to your phone number. If you are a victim of a SIM swap, recover the phone number from the carrier first."
---

# [IRP-TEL-003] Signal Registration Lock & Hijacking

> **Blast Radius Warning:** Unlike WhatsApp, Signal does not sync past message history to newly registered devices. If an attacker hijacks your Signal account, they cannot read your old messages, but they can impersonate you in new messages and groups.

---

## Phase 1: Emergency Containment (Re-Registration)

Objective: Terminate the attacker's endpoint by reclaiming the Signal registration.

### 1. Re-Register the Device
* Open Signal. If prompted, enter your phone number to re-register.
* Wait for the SMS code and enter it. 
* Entering the code automatically deregisters the attacker's device. 

### 2. The Registration Lock Barrier
If you enter the SMS code and Signal prompts for a **Signal PIN** that the attacker changed:
* You are locked out, but the attacker's device is still deregistered. Neither of you has access.
* You must wait **7 days** for the Registration Lock to expire. After 7 days of inactivity, Signal will allow you to bypass the PIN and register a fresh profile. (Note: You will lose your profile metadata, but your local message history remains intact on your original device).

---

## Phase 2: Eradication & Persistence Hunting

### 1. Linked Devices Audit
If the attacker gained access and linked an iPad or desktop app, that linked session might survive the primary device rotation.
* Open Signal > Tap your **Profile Picture (Settings)** > **Linked Devices**.
* Swipe left (iOS) or tap (Android) on any unrecognized desktop or iPad session and select **Unlink**.

---

## Phase 3: Blast Radius & Downstream Remediation

1. **Safety Number Verification:** Your contacts will see an alert stating your Safety Number has changed. Inform them via another channel that this was due to a temporary account hijacking, but that the new Safety Number is now genuinely you.
2. **Group Re-Entry:** Because Signal is heavily encrypted, if you had to wipe your profile due to a lost PIN, you may need to ask group admins to re-add you to your existing Signal groups.

---

## Phase 4: Hardening & Post-Incident Closure

- [ ] **Enable Registration Lock:** Tap **Profile >  Account > Registration Lock** and toggle it **ON**. This requires your custom Signal PIN to register your number on a new phone, defeating SIM-swap attacks.
- [ ] **Memorize the PIN:** Signal will occasionally prompt you to enter the PIN to keep it fresh in your memory. Do not dismiss these prompts; if you forget the PIN and lose your device, you will be locked out of your own profile for 7 days.
