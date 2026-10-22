---
id: "IRP-FIN-002"
title: "Amazon Account Takeover & Fraud"
platform: "Amazon"
version: "1.0.0"
last_verified: "2026-10-22"
severity_level: "High"
target_audience: "Operator & Tech-Savvy Helper"

endpoints:
  login_and_security: "https://www.amazon.com/ap/cnep"
  wallet_manage: "https://www.amazon.com/cpe/yourpayments/wallet"
  address_book: "https://www.amazon.com/a/addresses"
  order_history: "https://www.amazon.com/your-orders"
  archived_orders: "https://www.amazon.com/gp/your-account/order-history?orderFilter=archived"
  message_center: "https://www.amazon.com/gp/message"

indicators:
  - "Unexpected order confirmation emails for digital gift cards or high-value electronics."
  - "Changes to your default shipping address or phone number."
  - "Password no longer works, or alerts regarding sign-ins from unrecognized devices."
  - "Items appearing in your 'Archived Orders' that you did not purchase."

prerequisites:
  clean_environment_required: true
  prerequisite_warning: "Attackers often archive fraudulent orders immediately to hide them from the default view. You must explicitly check the Archived Orders endpoint."
---

# [IRP-FIN-002] Amazon Account Takeover (ATO)

> **Blast Radius Warning:** Amazon holds active payment methods and physical addresses. Attackers exploit compromised accounts to order physical goods to drop addresses or quickly drain linked cards via digital gift card purchases.

---

## Phase 1: Emergency Containment (Stop Active Adversary Access)

Objective: Kill existing attacker sessions and halt fraudulent purchases.

1. **Force Credential Rotation & Session Kill**
   * Navigate to: `https://www.amazon.com/ap/cnep` (Login & Security).
   * Edit the **Password**. Changing the password forces a sign-out on all other devices. Use a password manager to generate a unique passphrase.
2. **Secure Two-Step Verification (2SV)**
   * On the same Login & Security page, select **Turn on** or **Manage** next to Two-Step Verification.
   * Review enrolled devices and phone numbers. Delete any unrecognized authenticators or phone numbers.

---

## Phase 1B: Recovery & Lockout Bypass

If the adversary locked the victim out:
1. Contact Amazon Customer Service via phone (the US dedicated account security number is 1-888-280-4331, but always verify via the official site) or use the "Forgot Password" flow if you still control the email.
2. **Execution Context:** Amazon support will often freeze the account entirely during a compromise investigation. This is the desired outcome to stop financial bleeding.

---

## Phase 2: Eradication & Persistence Hunting

Objective: Remove the attacker's footprint and staging data.

### 1. Audit Shipping Addresses
* Navigate to: `https://www.amazon.com/a/addresses`
* Attackers add drop addresses (often lockers or vacant homes). **Remove** any unrecognized addresses immediately.

### 2. Audit Payment Methods
* Navigate to: `https://www.amazon.com/cpe/yourpayments/wallet`
* Review stored credit cards and bank accounts. If the attacker added a stolen credit card to your account (a common money-laundering tactic), **Remove** it. Do not attempt to use it.

### 3. Unlink Connected Accounts & Devices
* Navigate to: `https://www.amazon.com/hz/mycd/myx#/home/devices/1` (Manage Your Content and Devices).
* Deregister any unrecognized Kindles, Fire TV sticks, or mobile apps.

---

## Phase 3: Blast Radius Assessment & Downstream Remediation

1. **Uncover Hidden Orders:**
   * Attackers mask their activity by archiving orders.
   * Navigate to: `https://www.amazon.com/gp/your-account/order-history?orderFilter=archived`
   * Review for fraudulent digital gift cards or physical items.
2. **Cancel & Report:**
   * For any pending fraudulent orders, attempt to cancel them immediately from the order page.
   * Contact your credit card issuer or bank to dispute charges that have already posted.

---

## Phase 4: Hardening & Post-Incident Closure

- [ ] **Implement Passkeys:** Under Login & Security, set up a Passkey (FIDO2 or device biometric) to replace passwords entirely.
- [ ] **Credit Card Preference:** For future safety, avoid linking debit cards directly to retail accounts. Credit cards offer significantly stronger fraud protection and chargeback capabilities.
