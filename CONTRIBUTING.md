# Contributing to Project Virgil

Thank you for contributing. Consumer platforms change rapidly, and this repository relies on the infosec and tech community to keep recovery endpoints, tactics, and playbooks up-to-date.

## Core Principles for Contributions

1. **No UI Click-Paths:** Vendor UIs change constantly. Do not write instructions like *"Click the gear icon, then Security, then Advanced."* Instead, use direct URL endpoints (e.g., `https://myaccount.google.com/connections`).
2. **Phase Separation:** Maintain strict separation of IR phases (Pre-flight, Containment, Eradication, Recovery).
3. **Assume High Stress:** Write for a user who is panicked. Use clear, imperative language.

## Ways to Contribute

1. **Fixing a Broken Link/Changed URL:** Open a PR modifying the `endpoints:` section in the playbook's YAML frontmatter.
2. **Updating a Tactic:** If you observe a new way attackers maintain access, update the **Eradication** section.
3. **Creating a New Playbook:** Use `templates/PLAYBOOK_TEMPLATE.md`. Fill out the YAML frontmatter completely.

## Pull Request Checklist

- [ ] Changes adhere to the Markdown/YAML schema.
- [ ] New URLs are direct endpoints, not UI navigation paths.
- [ ] You updated the `last_verified` date in the frontmatter if you tested the steps.
