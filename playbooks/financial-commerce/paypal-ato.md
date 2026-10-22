---
id: "IRP-FIN-001"
title: "PayPal Account Takeover & Fraud"
platform: "PayPal"
version: "1.0.0"
last_verified: "2026-10-22"
severity_level: "High"
target_audience: "Operator & Tech-Savvy Helper"

endpoints:
  security_dashboard: "https://www.paypal.com/myaccount/security/"
  password_change: "https://www.paypal.com/myaccount/security/password/change"
  auto_payments: "https://www.paypal.com/myaccount/autopay/"
  wallet_manage: "https://www.paypal.com/myaccount/money/"
  resolution_center: "https://www.paypal.com/resolutioncenter/"

indicators:
  - "Email notifications for transactions or money transfers you did not authorize."
  - "Bank account alerts showing withdrawals originating from PayPal."
  - "Notification that new bank accounts or credit cards were linked to your PayPal."

prerequisites:
  clean_environment_required: true
  prerequisite_warning: "Before securing PayPal, verify the primary email account (Gmail/Outlook) attached to it is secure. If the email is compromised, attackers will immediately intercept PayPal password resets."
---

# [IRP-FIN-001] PayPal Account Takeover (ATO)

> **Blast Radius Warning:** Attackers use compromised PayPal accounts to drain linked checking accounts, max out linked credit cards, and establish fraudulent recurring subscriptions. 

---

## Phase 1: Emergency Containment (Halt Financial Flow)

Objective: Stop active transactions and lock the attacker out of the session.

1. **Force Credential Rotation & Session Kill**
   * Navigate to: `https://www.paypal.com/myaccount/security/password/change`
   * Changing the password will prompt PayPal to terminate all active mobile and web sessions. Use a unique 20+ character password.
2. **Secure Two-Factor Authentication**
   * Navigate to: `https://www.paypal.com/myaccount/security/`
   * Check **2-step verification**. If the attacker added a rogue phone number, remove it immediately.

---

## Phase 1B: Recovery & Lockout Bypass

If the adversary locked the victim out:
1. **Do not use email recovery** until you have verified the victim's email inbox is not compromised (check for forwarding rules/filters).
2. Use the **"Having trouble logging in?"** link on the login page and elect to recover via SMS to the victim's verified phone number.
3. If online recovery fails, call PayPal Fraud Support directly. You will need the last 4 digits of a linked bank account or credit card to verify identity over the phone.

---

## Phase 2: Eradication & Persistence Hunting

### 1. Audit Linked Financial Instruments
Attackers may link their own bank accounts to withdraw your PayPal balance.
* Navigate to: `https://www.paypal.com/myaccount/money/`
* Review all **Banks** and **Cards**. Click and **Remove** any unrecognized accounts immediately.

### 2. Purge Fraudulent Auto-Payments & Subscriptions
Attackers often set up recurring billing agreements or link the PayPal account to rogue merchant services.
* Navigate to: `https://www.paypal.com/myaccount/autopay/`
* Review the **Active** list. Cancel any unauthorized merchant agreements.

---

## Phase 3: Blast Radius Assessment & Downstream Remediation

1. **Report Unauthorized Transactions:**
   * Navigate to: `https://www.paypal.com/resolutioncenter/`
   * Select **Report a Problem** and flag every fraudulent transaction as "Unauthorized activity."
2. **External Bank Notification:**
   * If money was successfully pulled from a linked checking account, contact the bank's fraud department immediately. Instruct them to reverse the ACH pull from PayPal. (Note: This may cause the PayPal balance to go negative, which PayPal will need to resolve via the Resolution Center).
