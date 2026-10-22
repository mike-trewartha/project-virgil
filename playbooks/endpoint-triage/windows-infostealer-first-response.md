---
id: "IRP-EP-WIN-001"
title: "Suspected Windows Infostealer First-Response & Isolation"
platform: "Windows"
version: "1.0.0"
last_verified: "2026-10-22"
severity_level: "Critical"
target_audience: "Operator & Tech-Savvy Helper"

indicators:
  - "User downloaded a cracked game, software patch, cheat engine, or suspicious PDF/setup.exe."
  - "Browser closed unexpectedly or refreshed all cookies suddenly."
  - "Simultaneous ATO alerts across multiple unrelated platforms (Google, Discord, Steam, Meta)."
  - "Windows Defender was deliberately toggled off or added exclusion paths prior to running an executable."

prerequisites:
  clean_environment_required: true
  prerequisite_warning: "DO NOT attempt to reset passwords from this machine. Assume keyloggers and session token scrapers are active in memory or persistent in AppData."
---

# [IRP-EP-WIN-001] Suspected Windows Infostealer First-Response

> **Operational Warning:** Infostealers (e.g., Lumma, Stealc, Vidar, RedLine) target SQLite browser vaults to extract session cookies, saved passwords, autofill data, and cryptocurrency wallet extensions. Resetting credentials on an infected machine hands the new secrets directly back to the adversary.

---

## Phase 0: Immediate Network Severance

Before running scans or attempting diagnosis:

1. **Physical Isolation:** Unplug the Ethernet cable immediately.
2. **Wireless Isolation:** Toggle **Airplane Mode** or disconnect from Wi-Fi via the Windows Action Center (`Win + A`).
3. **Do Not Shut Down Immediately (If Preserving Memory/Triage):** If you intend to run live analysis, keep the machine disconnected from the network. If the user is unassisted and panicking, tell them to **power the machine completely off**.

---

## Phase 1: Establish Out-of-Band Containment

All identity recovery operations **must** occur from an uninfected device (e.g., iOS/Android phone or a clean secondary PC).

1. **Prioritize Primary Identity Anchors:**
   * Refer immediately to `playbooks/identity-anchors/google-account-ato.md` or `playbooks/identity-anchors/microsoft-account-ato.md`.
   * Terminate all active sessions via the web consoles from the clean device.
2. **Revoke Stored Master Credentials:**
   * Any credentials saved inside browser password managers (Chrome/Edge/Firefox autofill) on the infected PC must be considered fully compromised.
   * Prioritize password resets: Email > Password Manager Master Key > Banking > Social Media.

---

## Phase 2: Live System Triage (Operator / Helper View)

If you are triaging the host before deciding whether to wipe:

### 1. Fast Persistence Sweep
Check common userland autostart locations where stealers stage loaders:
* **Startup Folder:** Press `Win + R`, type `shell:startup`, press Enter. Inspect for unknown `.bat`, `.vbs`, `.js`, or `.lnk` shortcuts.
* **Task Scheduler:** Run `taskschd.msc`. Expand **Task Scheduler Library** and look for recent tasks executing binaries out of `%APPDATA%`, `%LOCALAPPDATA%`, or `C:\ProgramData\`.
* **Registry Run Keys:** Check:
  `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`
  `HKLM\Software\Microsoft\Windows\CurrentVersion\Run`

### 2. Browser Vault Blast Radius Inspection
Check which browsers had stored credentials or active sessions:
* Inspect `%LOCALAPPDATA%\Google\Chrome\User Data\Default\Network\Cookies`
* Inspect `%LOCALAPPDATA%\Microsoft\Edge\User Data\Default\Network\Cookies`
* If these profiles were logged into cryptocurrency extensions (Metamask, Phantom), assume private keys and seed phrases residing in local storage are drained or exfiltrated. Move remaining funds from a clean device immediately.

---

## Phase 3: Eradication

For consumer systems hit with modern stealers, in-place cleaning using traditional AV is rarely reliable due to multi-stage payloads and secondary backdoors (e.g., hidden Cobalt Strike beacons, rogue AnyDesk/RustDesk installs).

* [ ] **Recommended Remediation:** **Full OS Reinstall (Nuke & Pave)**
  1. Back up **raw personal files only** (plain `.docx`, `.pdf`, family photos) to an external USB. Avoid backing up executables, zips, or browser profile directories.
  2. Create a clean Windows installation media using Microsoft Media Creation Tool created on a **clean, separate PC**.
  3. Boot from USB, wipe all system partitions, and reinstall Windows cleanly.
* [ ] **Sub-Optimal (If Reinstall is Refused):**
  1. Boot Windows into **Safe Mode with Networking**.
  2. Run an offline scanner: Windows Defender Offline Scan (`Start > Settings > Privacy & security > Windows Security > Virus & threat protection > Scan options > Microsoft Defender Antivirus (offline scan)`).
  3. Run a secondary opinion tool like Malwarebytes or HitmanPro.
  4. Audit installed remote access tools: `appwiz.cpl` (check for unauthorized AnyDesk, TeamViewer, UltraViewer).

---

## Phase 4: Post-Rebuild Hardening

- [ ] **Migrate Away from Browser Credential Storage:** Ensure the user transitions all passwords from the built-in browser manager (Chrome/Edge) to a dedicated zero-knowledge password manager protected by a passkey or hardware 2FA.
- [ ] **Turn on Cloud-Delivered Protection:** Verify Windows Defender settings:
  `Settings > Privacy & security > Windows Security > Virus & threat protection settings > Real-time protection, Cloud-delivered protection, and Automatic sample submission (all ON)`.
- [ ] **Disable Script Hosts (Optional Helper Hardening):** If the victim routinely downloads torrents or mods, disable Windows Script Host to prevent `.vbs`/`.js` droppers:
  * Registry: Set `HKCU\Software\Microsoft\Windows Script Host\Settings\Enabled` to `0`.
