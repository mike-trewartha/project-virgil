# Password Manager Recovery & Auditing

A password manager (e.g., 1Password, Bitwarden, Dashlane, LastPass) is the ultimate single point of failure. If the master vault is compromised, the attacker gains immediate access to every aspect of the victim's digital life.

This guide outlines how to triage and recover a vault during an incident.

## Incident Scenarios

### Scenario A: The Master Credential is Stolen
*The victim was phished for their Master Password, or reused it elsewhere.*
1. **Immediate Credential Rotation:** Log in from a clean device and change the Master Password immediately. 
2. **Rotate the Secret Key (If Applicable):** Platforms like 1Password use a Secret Key in addition to the Master Password. If the attacker obtained the emergency kit, you must regenerate the Secret Key.
3. **Session Revocation:** Navigate to the security settings of the vault and "Deauthorize all other devices" or "Log out everywhere."

### Scenario B: The Endpoint was Infected (Infostealer)
*The victim's PC was infected with malware while the vault was unlocked.*
1. **Assume Total Exfiltration:** Modern infostealers can scrape the decrypted contents of a password manager directly from browser memory or local cache if the vault is actively unlocked.
2. **Vault Freeze:** Do not change passwords on the infected machine. Power it down immediately. 
3. **The Great Rotation:** From a clean device, you must begin rotating the passwords for every critical account stored in the vault, starting with Identity Anchors (Email) and Financials.

## Auditing the Vault Post-Incident

If an attacker had access to the vault for even a few minutes, you must assume they exported its contents. 

1. **Check Export Logs:** Many enterprise or premium family tiers log when a vault is exported to a `.csv` or `.json` file. Check the activity logs.
2. **Check for Shared Folders:** Ensure the attacker did not create a "Shared Vault" or "Shared Folder" inviting their own account to maintain persistent access to the credentials.
3. **Check for Added Devices:** Review the list of authorized devices in the manager's settings and revoke anything unrecognizable.

## Hardening Recommendations for the Helper

When migrating a family member to a password manager:
* **Enforce Hardware 2FA:** Protect the vault with a YubiKey or FIDO2 token rather than an Authenticator app, rendering remote phishing of the vault impossible.
* **The Emergency Kit:** Print the recovery code/secret key and place it in a physical safe or bank safety deposit box. Do not store it digitally in their email or on their desktop.
* **Aggressive Auto-Lock:** Configure the vault to automatically lock after 5 minutes of inactivity or when the browser closes, minimizing the window for memory scraping malware.
