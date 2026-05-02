# Agentra Paper Club — Next 48 Hours Action Plan
## Concrete steps to go from planning → real momentum

---

## Hour 0–2: IMMEDIATE (You do this now)

### Step 1: Authenticate xurl (10 minutes)
```bash
xurl auth oauth2 --app my-app YOUR_X_USERNAME
xurl auth default my-app
xurl whoami
```
Once this works, tell me. I'll immediately post the announcement and start the DM campaign.

### Step 2: Verify 2–3 X handles manually (5 minutes)
Open these profiles and confirm they're the right people:
- https://x.com/sreeramkannan (Sreeram Kannan, EigenLayer) — should show "Founder @EigenCloud"
- https://x.com/tanmay2099 (Tanmay Gupta, AI2) — should show "Senior Research Scientist @allen_ai"
- https://x.com/AnimaAnandkumar (Anima Anandkumar, Caltech/NVIDIA) — should show "Bren Professor @caltech"

If any look wrong, tell me. I'll correct the CRM.

### Step 3: Send the first DM manually (10 minutes)
While I wait for xurl auth, you can manually send this DM to @sreeramkannan:

```
Hey Sreeram, we're running a YC Paper Club-style event in Kolkata on June 28. 30 researchers + builders, 5 papers, 10 min each, off-the-record dinner. Would love you to present on consensus/crypto-economics or just attend and argue. Interested? → agentralabs.co/paperclub
```

If he replies INTERESTED, forward me his response. I'll handle follow-up.

---

## Hour 2–12: SOCIAL MEDIA LAUNCH (I execute once xurl is ready)

Once you confirm xurl works, I will execute in this order:

1. **Post announcement tweet** — 1 tweet, announcement format
2. **Post "why Kolkata" thread** — 5-tweet thread
3. **Send 5 DMs** — to verified Tier 1 targets: @sreeramkannan, @tanmay2099, @AnimaAnandkumar, @kundan2510, @pratykumar
4. **Post paper teaser** — 1 tweet with the 6-paper shortlist

I will deliver results back to this chat with screenshots/confirmations.

---

## Hour 12–24: MANUAL OUTREACH (You do this)

### Step 4: Send 5 cold emails (30 minutes)
Copy-paste from `paperclub/assets/email-templates.html`. Send to:

1. **Rishabh Jain (FAIR/Meta)** — Find his correct email/LinkedIn. Search "Rishabh Jain Meta FAIR" on LinkedIn. Use template #2 (Researcher) or #3 (Builder).
2. **Nisheeth Vishnoi** — Find his EPFL email. Search "Nisheeth Vishnoi EPFL email". Send template #2.
3. **Sarvam AI team** — General team email or Pratyush Kumar's email. Use template variant for team.
4. **IIT KGP CS Faculty** — Email CS department head or a faculty member you know. Ask them to forward to relevant ML/AI researchers.
5. **ISI Kolkata Faculty** — Same approach. Email a contact or the department.

### Step 5: Call 2 venues (20 minutes)

Call **The Corner Room** (Park Street) and **Bohemian** (Ballygunge).

Script: *"Hi, I'm organizing a small private research dinner on June 28, Saturday, 5 PM to 9 PM. About 30–35 people. We'd need a private room or semi-private space. Do you have availability? Can we bring our own AV equipment? What's the minimum spend?"*

Take notes. Update me with what they say. I'll help you decide.

---

## Hour 24–48: MOMENTUM BUILDING (Both of us)

### Step 6: I monitor and report (automated)

The cron job `paperclub-social-check` (job ID: `4b73531b920b`) is running twice daily. It will:
- Check X mentions of @AgentraLabs
- Check for "Agentra Paper Club" search mentions
- Deliver a report to this chat at 10 AM and 6 PM UTC daily

If you want me to pause/resume/adjust it:
```bash
hermes cronjob pause 4b73531b920b
hermes cronjob resume 4b73531b920b
```

### Step 7: You share the page (10 minutes)

Post `agentralabs.co/paperclub` in 3 places:
1. Your personal X/Twitter with a short note
2. Any relevant WhatsApp/Telegram groups (YC SSS, IIT KGP alumni, etc.)
3. LinkedIn post about "starting something in Kolkata"

### Step 8: I build the admin dashboard (if you want it)

If managing CSVs is annoying, tell me. I'll build a lightweight Next.js admin panel with:
- Applicant review board (scoring + status)
- Outreach tracker (status + follow-up dates)
- Metrics dashboard (applications, confirmations, sponsor pipeline)
- SQLite backend, self-hosted

This takes me ~2 hours to build.

---

## Blocking Issues (Resolve Today)

| Issue | Why It Blocks | Fix |
|-------|---------------|-----|
| xurl not authenticated | Can't post to X or send DMs | Run the 3 commands in Step 1 |
| `events.agentralabs.co` 404 | OG tags point there, social shares break | Add Vercel alias (see SUBDOMAIN-FIX.md) OR update OG tags to use `agentralabs.co/paperclub` |
| Rishabh Jain contact unknown | Can't reach key presenter | Manual LinkedIn search (Step 4) |

---

## Success Criteria for Next 48 Hours

| Metric | Target |
|--------|--------|
| xurl authenticated | Yes/No (blocks everything else) |
| Announcement posted | 1 tweet live |
| DMs sent | 5+ to Tier 1 targets |
| Emails sent | 5+ cold outreaches |
| Venue calls made | 2+ |
| Social shares by you | 3+ |
| Applications received | 5+ via Formspree |

---

## If Something Goes Wrong

**xurl auth fails:** Paste me the exact error. Common fixes are in `social-commands.md`.

**No replies from targets:** Normal. 30% response rate is good. Follow-up in 7 days (I'll remind you via the cron job).

**Venue unavailable:** We have 5 backup options in EVENT-PLAN.md. No problem.

**Formspree not receiving applications:** Check your Formspree dashboard. If broken, tell me — I'll wire a backup.

---

*This plan was generated by Hermes. Update me on progress and I'll adjust.*
