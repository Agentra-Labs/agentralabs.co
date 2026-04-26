# Agentra-Labs Landing Page

Modern, high-converting landing page inspired by PXL Corp's retro OS aesthetic.

## Features

- **Windows 95/98 inspired UI** — windows, title bars, status bars, folder icons
- **Glitch effect on primary heading** — cyberpunk vibe
- **Scanline & CRT overlay** — nostalgic terminal atmosphere
- **Typewriter animation** for manifesto text
- **Scroll-triggered number counters** for social proof
- **Fully responsive** — mobile-friendly
- **No dependencies** — vanilla HTML/CSS/JS, deploy anywhere

## Structure

```
agentra-landing/
├── index.html      # Main page
├── styles.css      # All styles (CSS variables, retro theming)
├── script.js       # Clock, typewriter, counters, interactions
└── README.md       # This file
```

## Customization

### Colors

Edit CSS variables in `styles.css`:

```css
:root {
  --accent: #58a6ff;      /* Primary accent (buttons, links) */
  --success: #3fb950;     /* Active/online status */
  --error: #f85149;       /* Error states */
  --bg: #0d1117;          /* Page background */
  --bg-window: #161b22;   /* Window background */
}
```

### Content

- Projects: edit `.project-card` blocks in `index.html`
- Stats: update `data-count` attributes for counters
- Links: replace GitHub/email URLs as needed

### Deploy

Just upload the folder to any static host:

- **Vercel / Netlify** — drag & drop
- **GitHub Pages** — push to `gh-pages` branch
- **S3 + CloudFront** — static hosting
- **Any web server** — point to `index.html`

## Credits

Inspired by [pxlcorp.xyz](https://www.pxlcorp.xyz) — check them out.

Built for Agentra-Labs. MIT License.
