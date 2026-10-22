# Threat Models for Civilians

Enterprise security professionals use threat modeling to anticipate how adversaries will attack a network. When helping a family member or friend recover from a personal account compromise, applying a simplified threat model helps prioritize which accounts to lock down first.

## The Three Tiers of Personal Digital Risk

### Tier 1: Identity Anchors (The Keys to the Kingdom)
**Examples:** Primary Email (Gmail, Outlook), Password Manager, Apple ID, Phone Number (SIM).
**The Threat:** If an attacker compromises a Tier 1 asset, they control the recovery mechanism for every other account you own. They can initiate password resets for your bank, intercept 2FA codes, and lock you out of your devices.
**Incident Response Priority:** **CRITICAL**. These must be secured and isolated before any other recovery actions are taken. 

### Tier 2: Financial & Reputational
**Examples:** Banking Apps, PayPal, Crypto Exchanges, Primary Social Media (Meta, X, LinkedIn).
**The Threat:** Direct financial theft or reputational damage (scamming friends and family by impersonating you). 
**Incident Response Priority:** **HIGH**. Once Tier 1 is secured, immediately freeze transactions and kill sessions in Tier 2 platforms. Do not attempt to secure Tier 2 if Tier 1 is still compromised (the attacker will just reset the password again).

### Tier 3: Commodities & Entertainment
**Examples:** Netflix, Spotify, Gaming Accounts (Steam, Epic), Retail (without stored payment).
**The Threat:** Nuisance. The attacker sells the account credentials for $2 on a forum so someone else can watch movies for free.
**Incident Response Priority:** **LOW**. Recover these only after the bleeding has stopped in Tiers 1 and 2.

## Common Adversary Archetypes Targeting Civilians

1. **The Credential Stuffer (Automated Bots)**
   * **Goal:** Test passwords leaked from a data breach against hundreds of other sites.
   * **Tactic:** Low effort. If you don't have 2FA and reuse passwords, they get in.
   * **Defense:** Unique passwords and basic 2FA.

2. **The Infostealer (Malware)**
   * **Goal:** Extract session cookies from a web browser to bypass 2FA entirely.
   * **Tactic:** Tricks the user into downloading a cracked game, PDF, or software patch. The malware quietly zips up the browser's credential vault and sends it to a Telegram channel.
   * **Defense:** Wipe the infected machine. Password resets are useless until the host is clean.

3. **The Scammer / Social Engineer**
   * **Goal:** Trick the user into handing over a 2FA code or initiating a wire transfer.
   * **Tactic:** "I accidentally sent you a code, can you text it back to me?" or "Your account has been suspended, click here to verify."
   * **Defense:** Education, FIDO2 Hardware Keys (which cannot be phished).
