# Ready-to-Execute Social Commands
## Copy-paste these after xurl is authenticated

---

## Step 1: Authenticate xurl (run manually once)

```bash
xurl auth oauth2 --app my-app YOUR_USERNAME
xurl auth default my-app
xurl whoami
```

---

## Step 2: Post announcement

```bash
xurl post "We're starting the India edition of YC Paper Club.

Every 3 weeks, 30 researchers and builders meet in Kolkata.
Five new papers. Ten minutes each. Then we argue.
Dinner is off the record. The talks go online.

Session 1: June 28. 30 seats. Curated, not first-come.

Request a spot → events.agentralabs.co/paperclub"
```

---

## Step 3: Post "why Kolkata" thread (tweet 1 of 5)

```bash
xurl post "Everyone asks 'why not Bangalore?'

Bangalore has the meetups. The panels. The sponsored booths.

Kolkata has ISI. Jadavpur. IIT KGP two hours away.
Researchers who've never sat across from a builder shipping to production.

That's the gap. That's why.

June 28 · events.agentralabs.co/paperclub"
```

---

## Step 4: Send DM to Kundan Kumar

```bash
xurl dm @kundankumar "Hey Kundan, we're running a YC Paper Club-style event in Kolkata on June 28. 30 researchers + builders, 5 papers, off-the-record dinner. Would love you to present on diffusion/open weights. Interested? → events.agentralabs.co/paperclub"
```

---

## Step 5: Automated batch (after you have 5+ targets)

```bash
cd /mnt/c/Users/ab916/agentralabs.co/paperclub
python3 social_bot.py post-announcement
python3 social_bot.py dm-batch
python3 social_bot.py check-mentions
```

---

## All Post Variants (ready to copy)

### Teaser
```bash
xurl post "Papers on the table for Session 1 vote:

→ Recursive Language Models (Prime Intellect)
→ s1: Simple Test-Time Scaling (Stanford)
→ Kimi K2 (Moonshot)
→ DeepSeek-V3.2 (DeepSeek-AI)
→ Anthropic's reasoning-faithfulness paper

Attendees pick the final 5. Apply to vote:
events.agentralabs.co/paperclub"
```

### First 10 confirmed
```bash
xurl post "First 10 seats confirmed.

Mix so far: builders, researchers, PhD students, one wildcard.
Cities: Kolkata, Bangalore, Kharagpur, Delhi.

Still 20 seats left. Application closes June 14.

events.agentralabs.co/paperclub"
```

### Final call
```bash
xurl post "3 seats left for June 28.

If you're on the fence: the dinner conversation is the point.
The talks are just the excuse to get the right people in one room.

Apply anyway. We'll keep you in the loop for Session 2.

events.agentralabs.co/paperclub"
```

---

*Run these one at a time. X rate limits are strict.*
