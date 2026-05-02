#!/usr/bin/env python3
"""
Agentra Paper Club — Social Media Automation
Requires: xurl authenticated (run `xurl auth oauth2 --app my-app` manually first)
Usage:
  python3 social_bot.py post-announcement    # Post announcement tweet
  python3 social_bot.py post-teaser          # Post paper teaser
  python3 social_bot.py dm-batch             # Send DMs from outreach-crm.csv
  python3 social_bot.py check-mentions       # Check mentions and suggest replies
  python3 social_bot.py weekly-update        # Post weekly cohort update
"""
import subprocess, json, csv, sys, time, random, os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CRM_PATH = os.path.join(BASE_DIR, "outreach-crm.csv")
LOG_PATH = os.path.join(BASE_DIR, "social-log.json")

POSTS = {
    "announcement": (
        "We're starting the India edition of YC Paper Club.\n\n"
        "Every 3 weeks, 30 researchers and builders meet in Kolkata.\n"
        "Five new papers. Ten minutes each. Then we argue.\n"
        "Dinner is off the record. The talks go online.\n\n"
        "Session 1: June 28. 30 seats. Curated, not first-come.\n\n"
        "Request a spot → events.agentralabs.co/paperclub"
    ),
    "teaser": (
        "Papers on the table for Session 1 vote:\n\n"
        "→ Recursive Language Models (Prime Intellect)\n"
        "→ s1: Simple Test-Time Scaling (Stanford)\n"
        "→ Kimi K2 (Moonshot)\n"
        "→ DeepSeek-V3.2 (DeepSeek-AI)\n"
        "→ Anthropic's reasoning-faithfulness paper\n\n"
        "Attendees pick the final 5. Apply to vote:\n"
        "events.agentralabs.co/paperclub"
    ),
    "why_kolkata": (
        "Everyone asks 'why not Bangalore?'\n\n"
        "Bangalore has the meetups. The panels. The sponsored booths.\n\n"
        "Kolkata has ISI. Jadavpur. IIT KGP two hours away.\n"
        "Researchers who've never sat across from a builder shipping to production.\n\n"
        "That's the gap. That's why.\n\n"
        "June 28 · events.agentralabs.co/paperclub"
    ),
    "first_10": (
        "First 10 seats confirmed.\n\n"
        "Mix so far: builders, researchers, PhD students, one wildcard.\n"
        "Cities: Kolkata, Bangalore, Kharagpur, Delhi.\n\n"
        "Still 20 seats left. Application closes June 14.\n\n"
        "events.agentralabs.co/paperclub"
    ),
    "final_call": (
        "3 seats left for June 28.\n\n"
        "If you're on the fence: the dinner conversation is the point.\n"
        "The talks are just the excuse to get the right people in one room.\n\n"
        "Apply anyway. We'll keep you in the loop for Session 2.\n\n"
        "events.agentralabs.co/paperclub"
    )
}

def xurl(cmd):
    """Run xurl command and return parsed JSON."""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"ERROR: {result.stderr}", file=sys.stderr)
        return None
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        print(f"RAW: {result.stdout}")
        return result.stdout

def log_action(action, details):
    entry = {"time": datetime.now().isoformat(), "action": action, "details": details}
    logs = []
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH) as f:
            logs = json.load(f)
    logs.append(entry)
    with open(LOG_PATH, "w") as f:
        json.dump(logs, f, indent=2)

def post(key):
    text = POSTS.get(key)
    if not text:
        print(f"Unknown post key: {key}")
        return
    print(f"Posting: {key}")
    # Escape newlines for shell
    shell_text = text.replace("\n", "\\n")
    result = xurl(f'xurl post "{shell_text}"')
    if result:
        print(json.dumps(result, indent=2))
        tweet_id = result.get("data", {}).get("id")
        log_action("post", {"key": key, "tweet_id": tweet_id, "text_preview": text[:80]})
        print(f"Posted! ID: {tweet_id}")

def dm_batch():
    """Send DMs to all 'not_contacted' Tier 1 and 2 targets."""
    if not os.path.exists(CRM_PATH):
        print(f"CRM not found: {CRM_PATH}")
        return

    with open(CRM_PATH) as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    for row in rows:
        if row["status"] != "not_contacted":
            continue
        if row["platform"] != "X":
            continue
        if int(row["tier"]) > 2:
            continue

        handle = row["handle"]
        template_key = row["message_template"]
        name = row["name"]

        # Load template content (simplified — in real use, expand from templates)
        msg = f"Hey {name.split()[0]}, we're running a YC Paper Club-style event in Kolkata on June 28. 30 researchers + builders, 5 papers, off-the-record dinner. Would love to have you present or attend. Interested? → events.agentralabs.co/paperclub"

        print(f"DM to {handle}: {msg[:60]}...")
        result = xurl(f'xurl dm {handle} "{msg}"')
        if result and "data" in result:
            print(f"  Sent to {handle}")
            log_action("dm", {"to": handle, "name": name, "template": template_key})
            # In real use, update CSV status to 'contacted'
        else:
            print(f"  FAILED for {handle}")
            log_action("dm_failed", {"to": handle, "name": name, "error": str(result)})

        time.sleep(random.uniform(30, 90))  # Rate limit safety

def check_mentions():
    """Check recent mentions and print suggested replies."""
    result = xurl("xurl mentions -n 20")
    if not result or "data" not in result:
        print("No mentions or error")
        return

    for mention in result.get("data", []):
        author = mention.get("author_id", "unknown")
        text = mention.get("text", "")
        tweet_id = mention.get("id")
        print(f"\n[@{author}]: {text}")

        # Simple heuristic for suggested reply
        if "apply" in text.lower() or "interested" in text.lower():
            print("  → SUGGESTED: Reply with application link + excitement")
        elif "sponsor" in text.lower():
            print("  → SUGGESTED: Reply with sponsor-deck.html link + offer call")
        elif "when" in text.lower() or "date" in text.lower():
            print("  → SUGGESTED: Reply with June 28 + time + link")
        else:
            print("  → SUGGESTED: Generic thank-you + link")

def weekly_update():
    text = (
        "This week in Paper Club:\n\n"
        "✓ 10 seats confirmed\n"
        "✓ 3 presenter slots filled\n"
        "✓ Paper shortlist drops June 7\n\n"
        "Applications still open. 20 seats left.\n\n"
        "events.agentralabs.co/paperclub"
    )
    post_text = text.replace("\n", "\\n")
    result = xurl(f'xurl post "{post_text}"')
    if result:
        print("Weekly update posted!")
        log_action("weekly_update", {"week": datetime.now().strftime("%Y-W%U")})

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "post-announcement":
        post("announcement")
    elif cmd == "post-teaser":
        post("teaser")
    elif cmd == "post-why-kolkata":
        post("why_kolkata")
    elif cmd == "post-first-10":
        post("first_10")
    elif cmd == "post-final-call":
        post("final_call")
    elif cmd == "dm-batch":
        dm_batch()
    elif cmd == "check-mentions":
        check_mentions()
    elif cmd == "weekly-update":
        weekly_update()
    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
