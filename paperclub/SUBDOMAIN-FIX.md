# Fix: events.agentralabs.co returns 404

## Problem
`events.agentralabs.co/paperclub/` returns 404. The event page's OG meta tags and canonical URL point there, so social shares will hit a dead page.

## Root Cause
`events.agentralabs.co` is not configured as a domain alias in your Vercel project. Only `agentralabs.co` and `www.agentralabs.co` are serving the deployment.

## Fix (2 minutes)

### Step 1: Add Domain in Vercel Dashboard
1. Go to https://vercel.com/dashboard
2. Select your `agentralabs.co` project
3. Go to **Settings → Domains**
4. Click **Add Domain**
5. Enter: `events.agentralabs.co`
6. Vercel will detect it's an alias of the existing project

### Step 2: Add DNS CNAME Record
In your DNS provider (GoDaddy, Cloudflare, Namecheap, etc.):

| Type | Host | Value | TTL |
|------|------|-------|-----|
| CNAME | `events` | `cname.vercel-dns.com` | Auto |

If using Cloudflare:
- **Proxy status**: OFF (DNS only) — Vercel needs to see the CNAME directly
- Or if you want Cloudflare proxy ON, add `events.agentralabs.co` in Cloudflare as a CNAME to `cname.vercel-dns.com` with proxy OFF for the initial verification, then you can turn it ON after Vercel confirms.

### Step 3: Wait for Propagation
- Vercel will show "Validating..." then "Valid Configuration"
- DNS propagation: 5–60 minutes depending on provider
- SSL certificate is auto-provisioned by Vercel

### Step 4: Verify
```bash
curl -I https://events.agentralabs.co/paperclub/
# Should return 200, not 404
```

## Alternative: Use agentralabs.co/paperclub/ Only
If you don't want to set up the subdomain, update the OG meta tags in `paperclub/index.html` to use `https://agentralabs.co/paperclub/` instead. But the subdomain looks cleaner and is already referenced everywhere.

## Post-Fix Checklist
- [ ] `events.agentralabs.co/paperclub/` loads correctly
- [ ] Social share preview works (test with https://cards-dev.twitter.com/validator or LinkedIn Post Inspector)
- [ ] OG image loads at `https://events.agentralabs.co/paperclub/og-image.png`
