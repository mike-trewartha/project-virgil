# How to Help Family Members During a Cyber Incident

When you are the "tech-savvy" family member, you become the defacto Incident Commander when a relative clicks a bad link or has their Facebook hijacked. 

Enterprise IR emphasizes communication and scoping. When dealing with family, you must also manage panic, shame, and confusion.

## 1. Manage the Psychology (Stop the Panic)
Victims often feel intense shame or panic, which leads to erratic decision-making (like deleting evidence or paying scammers).
* **De-escalate:** Say, *"This happens to thousands of people a day. We can fix this, but I need you to stop clicking things and let me take over."*
* **No Blame:** Do not lecture them on *why* they shouldn't have clicked the link. Save the education for Phase 4 (Post-Incident). Focus entirely on containment.

## 2. Establish Secure Out-of-Band (OOB) Comms
If their primary phone or email is compromised, do not use it to communicate your recovery plan.
* If their email is hijacked, do not email them reset links.
* If their phone was SIM-swapped, rely on Wi-Fi-based calling (FaceTime Audio, WhatsApp) or a landline.

## 3. The Intake Interview (Scoping the Incident)
You need to establish the "Root Cause" and the "Blast Radius." Ask clear, non-technical questions:
* *"What exactly were you looking at right before this happened?"* (Determines if it was a phishing email, a fake Google ad, or a malicious download).
* *"Can you still get into your email?"* (Determines if the Identity Anchor is lost).
* *"Did you type your password, or did the screen just flash and close?"* (Differentiates between phishing and malware).

## 4. Take Operational Control
Remote troubleshooting via phone is agonizing and error-prone during an active ATO.
* **If in person:** Physically take their uncompromised smartphone (e.g., iPhone) and execute the Project Virgil playbooks yourself.
* **If remote:** Do not ask them to navigate complex security menus. If their machine is clean, use a trusted screen-sharing tool (like Chrome Remote Desktop, Zoom, or FaceTime screen share) and walk them through exactly where to click. 
* *Warning:* Never initiate a remote desktop session to a machine you suspect is actively infected with malware (Infostealers/RATs).

## 5. Post-Incident Hardening & Education
Once the accounts are secure and the adrenaline fades, implement preventative controls:
* **The "Wait 5 Minutes" Rule:** Teach them to never react instantly to an urgent email or SMS. Tell them to call you if a message demands immediate action.
* **Migrate from SMS to Apps/Keys:** Move their critical 2FA from SMS (which can be SIM-swapped) to an Authenticator app or a Passkey.
* **Set up Account Recovery:** Ensure *you* are listed as the trusted recovery contact for their Apple ID, Google Account, or Password Manager so you have authorized access during the next crisis.
