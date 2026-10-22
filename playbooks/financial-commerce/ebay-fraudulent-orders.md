---
id: "IRP-FIN-003"
title: "eBay Account Takeover & Fraud"
platform: "eBay"
version: "1.0.0"
last_verified: "2026-10-22"
severity_level: "High"
target_audience: "Operator & Tech-Savvy Helper"

endpoints:
  security_center: "https://accounts.ebay.com/acctsec/security-center"
  personal_info: "https://accountsettings.ebay.com/profile"
  wallet_manage: "https://ppcapp.ebay.com/myppc/wallet/list"
  purchase_history: "https://www.ebay.com/myb/PurchaseHistory"
  selling_overview: "https://www.ebay.com/sh/ovw"
  report_hacked: "https://www.ebay.com/help/account/protecting-account/get-help-hacked-account?id=4196"

indicators:
  - "Bids or offers placed on items you did not engage with."
  - "New listings created under your seller account for high-ticket items (e.g., electronics, vehicles)."
  - "Changes to your registered name, address, or phone number."
  - "Messages sent to other buyers or sellers from your account."

prerequisites:
  clean_environment_required: true
  prerequisite_warning: "eBay accounts are often compromised via email takeovers. Ensure the email account associated with the eBay profile is fully secured (passwords rotated, MFA enabled) before recovering the eBay account."
---

# [IRP-FIN-003] eBay Account Takeover (ATO)

> **Blast Radius Warning:** Attackers use compromised eBay accounts not just to buy items with your saved payment methods, but to set up fraudulent listings using your seller reputation, potentially exposing you to chargebacks and suspended accounts.

---

## Phase 1: Emergency Containment (Stop Active Adversary Access)

1. **Force Credential Rotation**
   * Navigate to: `https://accounts.ebay.com/acctsec/security-center`
   * Select **Password** and update it using a password manager.
2. **Review Connected Social Logins**
   * On the Security Center page, review **Third-party app access** and **Social sign in**. 
   * If the attacker linked their Google, Facebook, or Apple account to maintain persistent access, **Revoke** the connection immediately.
3. **Secure Two-Step Verification**
   * On the Security Center page, review your 2-step verification settings. Ensure the phone number listed is exclusively yours.

---

## Phase 1B: Recovery & Lockout Bypass

If the adversary locked the victim out:
1. Navigate directly to the hacked account reporting portal: `https://www.ebay.com/help/account/protecting-account/get-help-hacked-account?id=4196`
2. If online recovery is blocked, call the dedicated eBay security line (often listed as 1-866-961-9253 in the US, but verify regional numbers via the official help portal using Skype if necessary). 

---

## Phase 2: Eradication & Persistence Hunting

### 1. Audit Contact and Shipping Information
* Navigate to: `https://accountsettings.ebay.com/profile`
* Verify the **Email address**, **Phone number**, and all **Addresses** (Registration, Delivery, and Return addresses). 
* Attackers will change the delivery address to intercept goods, or the return address to divert seller returns.

### 2. Audit Financial Instruments
* Navigate to: `https://ppcapp.ebay.com/myppc/wallet/list`
* Review all saved payment options. Delete any unrecognized cards or bank accounts.
* If you are a seller, ensure the payout bank account has not been changed to route your funds to the attacker.

---

## Phase 3: Blast Radius Assessment & Downstream Remediation

1. **Check Buyer Activity:**
   * Navigate to: `https://www.ebay.com/myb/PurchaseHistory`
   * Review recent purchases and active bids. Contact the sellers immediately to explain the account was compromised and request order cancellations.
2. **Check Seller Activity:**
   * Navigate to: `https://www.ebay.com/sh/ovw` (Seller Hub).
   * Check for newly created listings. Attackers often list fake high-value items (like tractors, cameras, or cars). End these listings immediately to prevent defrauding other users.
3. **Financial Holds:**
   * Dispute any unauthorized charges that have hit your linked bank or credit card by contacting your financial institution directly.

---

## Phase 4: Hardening & Post-Incident Closure

- [ ] **Enforce Authenticator App:** Transition from SMS-based 2-step verification to an Authenticator App via the Security Center.
- [ ] **Monitor Messages:** Check your eBay messages for the next 48 hours to ensure no lingering conversations with defrauded buyers or sellers need addressing.
