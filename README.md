# Project Virgil

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Enterprise security teams have playbooks, centralized logging, and dedicated responders. The public has fragmented vendor FAQs, automated support loops, and panic. 

**Project Virgil** is an open-source catalogue of Incident Response (IR) playbooks designed specifically for consumer platforms (Google, Meta, Apple, etc.). Built with the operational rigor of enterprise Digital Forensics and Incident Response (DFIR), these guides are engineered to help individuals and their designated "family IT support" rapidly triage, contain, and recover from Account Takeovers (ATO).

## The Problem

When a personal account is compromised, changing the password is rarely enough. Modern adversaries establish persistence via hidden OAuth grants, mailbox forwarding rules, and connected SSO applications. Existing consumer guides fail to address this, and vendor documentation frequently breaks as UIs change.

## The Solution

Project Virgil playbooks bypass fragile UI click-paths. They rely on direct configuration endpoints and are structured strictly around the incident lifecycle:
1. **Pre-flight Checks:** Ensuring the local endpoint is clean before initiating recovery.
2. **Containment:** Killing active adversary sessions immediately.
3. **Eradication:** Hunting for persistence mechanisms (OAuth, forwarding rules, linked accounts).
4. **Recovery:** Re-establishing secure access and assessing the downstream blast radius.

## Core Playbooks

If you are actively dealing with a compromise, start here:

### Identity Anchors (High Blast Radius)
* [Google / Gmail Compromise](playbooks/identity-anchors/google-account-ato.md)
* [Apple ID Compromise](playbooks/identity-anchors/apple-id-ato.md) 
* [Microsoft Account Compromise](playbooks/identity-anchors/microsoft-account-ato.md)

### Social Media & Comms
* [Meta (Facebook/Instagram) Takeover](playbooks/social-media/meta-facebook-instagram-ato.md)
* [X / Twitter Takeover](playbooks/social-media/x-twitter-ato.md)

### Endpoint First-Response
* [Suspected Infostealer Infection (Windows)](playbooks/endpoint-triage/windows-infostealer-first-response.md)

## Who is this for?

* **The Victim:** High-contrast, clear steps to stop active bleeding.
* **The "Designated Helper":** The tech-savvy friend or family member tasked with fixing the compromise.
* **The Community:** Security professionals contributing updated tactics, broken endpoint links, and new platform recovery flows.

## Contributing

Consumer platforms change rapidly. This repository relies on community reporting to detect broken recovery links and new attacker persistence tactics. 

See our [Contributing Guidelines](CONTRIBUTING.md) to learn how to:
* Submit a PR to fix a broken platform deep-link.
* Propose a new playbook using our standardized YAML/Markdown schema.
* Report a newly observed ATO tactic.

## Disclaimer

*These playbooks are provided for educational and triage purposes only. Project Virgil is community-maintained and not affiliated with, nor endorsed by, any of the platforms documented herein. Use these guides at your own risk.*
