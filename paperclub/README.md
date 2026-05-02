# Agentra Paper Club — Operations Dashboard
## https://events.agentralabs.co/paperclub

---

## Quick Status

| Item | Status |
|------|--------|
| **Date** | June 28, 2026 ✅ |
| **Page** | Live with RSVP form ✅ |
| **Venue** | TBD — The Corner Room / Bohemian / Gateway (see EVENT-PLAN.md) |
| **Sponsors** | 0 confirmed — sponsor-deck.html ready |
| **Presenters** | 0 confirmed — outreach-crm.csv has 20 targets |
| **Attendees** | 0 confirmed — applications open via Formspree |
| **Social posts** | 5 drafted — social-launch-kit.md ready |
| **Budget** | ₹55K/session baseline — see EVENT-PLAN.md |

---

## Files (what does what)

| File | Purpose |
|------|---------|
| `index.html` | Event page — live at events.agentralabs.co/paperclub |
| `EVENT-PLAN.md` | Master operational plan: budget, timeline, venue, risk |
| `sponsor-deck.html` | Sponsor pitch deck — open in browser, print to PDF |
| `social-launch-kit.md` | 5 ready-to-post social media posts (X, LinkedIn) |
| `outreach-templates.md` | Personalized DM/email templates for 20 targets |
| `outreach-crm.csv` | Contact tracker — status, response, follow-up dates |
| `response-playbook.md` | How to reply to every type of response |
| `impact-analysis.md` | Direct/indirect/long-term impact thesis |
| `applicants.csv` | Application review tracker with scoring rubric |
| `social_bot.py` | Automation script for X posts/DMs (needs xurl auth) |
| `social-commands.md` | Copy-paste xurl commands ready to execute |

---

## What You Need to Do Right Now

### 1. Activate Social Media (5 min)

```bash
# Run these manually (requires browser OAuth flow)
xurl auth oauth2 --app my-app YOUR_USERNAME
xurl auth default my-app
xurl whoami

# Then post announcement immediately:
xurl post "We're starting the India edition of YC Paper Club.

Every 3 weeks, 30 researchers and builders meet in Kolkata.
Five new papers. Ten minutes each. Then we argue.
Dinner is off the record. The talks go online.

Session 1: June 28. 30 seats. Curated, not first-come.

Request a spot → events.agentralabs.co/paperclub"
```

See `social-commands.md` for all ready-to-execute commands.

### 2. Send First 5 Cold Outreaches (15 min)

Open `outreach-crm.csv`. Sort by `tier=1` and `status=not_contacted`.

Personalized templates are in `outreach-templates.md`. Copy, customize 30%, send.

First 5 targets:
1. Kundan Kumar (Stability AI) — X DM
2. Rishabh Jain (FAIR/Meta) — X DM  
3. Sreeram Kannan (EigenLayer) — X DM
4. Sarvam AI team — email
5. ISI Kolkata faculty — email

Update `outreach-crm.csv` with `status=contacted` and `first_contact_date`.

### 3. Call Venues This Week (30 min)

| Venue | Phone | Ask For |
|-------|-------|---------|
| The Corner Room | Search + call | Private dining room, June 28, 5–10 PM, 35 people, outside catering OK? |
| Bohemian | Search + call | Same questions. Their experimental food fits the research vibe. |
| Gateway Hotel | Search + call | Backup option. Professional AV. |

See EVENT-PLAN.md Section 3 for full venue specs.

### 4. Review Applications Daily (5 min)

Formspree sends emails. Copy applicant info into `applicants.csv` and score using the rubric in EVENT-PLAN.md Section 5.

Target: 80+ applications by June 14.

---

## Weekly Rhythm

| Day | Task | Time |
|-----|------|------|
| Monday | Review weekend responses, update CRM, send follow-up 1s | 20 min |
| Tuesday | Post social content, send 5 new cold outreaches | 20 min |
| Wednesday | Sponsor outreach (if pipeline low), check venue | 20 min |
| Thursday | Cohort update email to warm leads, review applicants | 15 min |
| Friday | Send follow-up 2s, plan next week's content | 15 min |
| Saturday | Post thread/content, review metrics | 15 min |
| Sunday | Rest | 0 min |

Total: ~105 min/week = ~1.75 hours/week of active work.

---

## If You Want Me (Hermes) to Handle More

I can execute once you give me access:

| Task | What You Need to Give Me |
|------|--------------------------|
| Post to X automatically | `xurl auth` completed + run `xurl auth status` |
| Send emails via your account | SMTP credentials or Gmail API access |
| Call venues for you | I don't have phone access — you call, I script the conversation |
| Automate application review | Access to your Formspree account or email forwarding |
| Build a proper backend | Deploy a Next.js app with DB — I can build this |

---

## Success Metrics (Review Weekly)

| Metric | Week 1 Target | Week 4 Target |
|--------|---------------|---------------|
| Cold outreaches sent | 15 | 40 |
| Response rate | 30% | 35% |
| Presenter confirmations | 3 | 5 |
| Attendee confirmations | 10 | 25 |
| Sponsor conversations | 2 | 5 |
| Social post impressions | 5,000 | 20,000 |
| Website applications | 50 | 120 |

---

## Direct vs. Indirect Impact

### Direct (measurable in 4 months)
- 25 YouTube videos × 1,000 views = 25,000 researcher-minutes
- 150 attendee-relationships built
- 2–3 potential Agentra hires
- Content library as permanent asset

### Indirect (6–18 months)
- Kolkata becomes a node on the "India AI" map
- 2–4 startup ideas born from dinner conversations
- Copycat Paper Clubs in Bangalore, Delhi
- Agentra Labs becomes known as a convener, not just a startup

### Long-term (18+ months)
- 100+ videos = searchable research library
- 200+ trusted network members
- Policy/narrative influence through regular researcher consensus
- Potential 5-city Paper Club network by 2027

See `impact-analysis.md` for full breakdown.

---

*Dashboard maintained by Hermes. Last updated: May 2026.*
