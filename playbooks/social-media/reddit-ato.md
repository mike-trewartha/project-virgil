---
id: "IRP-SOC-003"
title: "Reddit Account Takeover"
platform: "Reddit"
version: "1.0.0"
last_verified: "2026-10-22"
severity_level: "Medium"
target_audience: "Operator & Tech-Savvy Helper"

endpoints:
  account_activity: "https://www.reddit.com/account-activity"
  password_reset: "https://www.reddit.com/login/"
  authorized_apps: "https://www.reddit.com/prefs/apps/"
  support_request: "https://www.reddithelp.com/en/submit-request/account-issues"
  appeal_ban: "https://reddit.com/appeal"

indicators:
  - "Your account is posting spam, crypto links, or adult content without your knowledge."
  - "You are unexpectedly subscribed to subreddits you did not join."
  - "You receive notifications of account bans or suspensions from subreddits."

prerequisites:
  clean_environment_required: true
  prerequisite_warning: "If the user is on a PC, run a quick virus scan before attempting recovery. Also, ensure control of any Google/Apple/email accounts linked to the Reddit profile."
---

# [IRP-SOC-003] Reddit Account Takeover (ATO)

> **Blast Radius Warning:** Compromised Reddit accounts are primarily used in botnets to upvote spam, post malicious links, or distribute adult content. If the account is a moderator of a subreddit, the attacker may attempt to hijack or vandalize the community.

---

## Phase 1: Emergency Containment

1. **Kill Active Sessions**
   * Navigate to: `https://www.reddit.com/account-activity`
   * Log out of any sessions that are not yours.
2. **Force Credential Rotation**
   * Go to `https://www.reddit.com/login/` and use the password reset flow. If your email was changed by the attacker, check your inbox for an email from Reddit with a link to revert the change.
   * If you use the same passwords for multiple services, change those as well.

---

## Phase 1B: Recovery & Lockout Bypass

If the adversary locked the victim out:
1. Navigate to: `https://www.reddithelp.com/en/submit-request/account-issues`
2. Enter the account's email address.
3. Under "What do you need assistance with" select **Account Help**. 
4. Under "What type of account issues are occurring" select **Security Problems**, and then **I think my account has been hacked**. Submit the request, noting it may take a long time for a response.

---

## Phase 2: Eradication & Persistence Hunting

### 1. Authorized Applications
* Navigate to: `https://www.reddit.com/prefs/apps/`
* Attackers authorize scripts to automate posting. Click **revoke access** on any unrecognized applications.

### 2. Verify Linked Accounts
* Navigate to your **User Settings > Account**.
* Check the **Connected Accounts** section (Apple, Google). Disconnect any accounts that belong to the attacker.

---

## Phase 3: Blast Radius Assessment

1. **Review Subscriptions:** If the hacker joined unwanted subreddits, log into Old Reddit via browser (`https://old.reddit.com/`) to access a list of subscriptions you can easily manage.
2. **Review Comments and Posts:** Delete any spam or unauthorized content posted by the attacker.
3. **Appeals:** If the attacker's actions resulted in site-wide or shadow bans, appeal via `https://reddit.com/appeal`. You may also need to appeal to BotBouncer (`https://www.reddit.com/r/BotBouncer/new/`).

---

## Phase 4: Hardening

- [ ] **Enable Two-Factor Authentication:** Navigate to **User Settings > Safety & Privacy > Use two-factor authentication**. Set up an Authenticator app.
