# Launching plotarmor.gg

The site is built and checked locally. Nothing is published yet. The steps below happen in this
order, and each needs Selly's yes in the website session's chat.

## A. Put the site on GitHub (the website session does this after your yes)
1. Create a **public** repo `sellybros711/plot-armor-site` and push `main`.
   (Free GitHub Pages needs a public repo. Everything in it is meant to be public anyway.)
2. Repo → **Settings** → **Pages** → Source: **Deploy from a branch** → Branch **main**,
   folder **/docs** → **Save**. The custom domain `plotarmor.gg` is already set by the file
   `docs/CNAME`.

## B. Your clicks: point plotarmor.gg at GitHub and turn on HTTPS
1. **Verify the domain with GitHub first** (stops anyone else from using it on GitHub):
   github.com → your photo (top right) → **Settings** → **Pages** (left menu) → **Add a domain** →
   type `plotarmor.gg` → **Add domain**. GitHub shows a TXT record named like
   `_github-pages-challenge-sellybros711`. Keep this tab open.
2. In another tab, sign in where you bought plotarmor.gg and open its **DNS** settings
   (often called "Manage DNS", "DNS records" or "Advanced DNS").
3. Add the **TXT** record from step 1: Type `TXT`, Host/Name exactly as GitHub shows it
   (without `.plotarmor.gg` if your registrar adds that itself), Value exactly as shown. Save.
4. Back on GitHub, click **Verify**. If it says "not found yet", wait 10 minutes and try again
   (it can take up to a day).
5. In the DNS settings, delete any **parking**, **forwarding** or existing **A**/**CNAME** records
   for `@` (the bare domain) and `www`.
6. Add four **A** records, each with Host `@`:
   `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
7. (Optional, for newer networks) four **AAAA** records, each with Host `@`:
   `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153`
8. Add one **CNAME** record: Host `www`, Value `sellybros711.github.io`
9. GitHub → the plot-armor-site repo → **Settings** → **Pages**. Under "Custom domain" it should
   show `plotarmor.gg` and "DNS check successful" (allow up to an hour).
10. Tick **Enforce HTTPS** as soon as it can be clicked (GitHub makes the certificate itself;
    this can take up to 24 hours).
11. Open https://plotarmor.gg and https://www.plotarmor.gg on your phone. Both should show the
    site with a padlock.

If a menu name differs, GitHub's own help page is "Managing a custom domain for your GitHub
Pages site". Tell the website session which registrar you use and it will fill in exact names.

## C. After the site is live
- Run `python3 tools/check_links.py --online`, and open `https://plotarmor.gg/anything` to see the 404 page.
- **Privacy URLs to paste into each Chrome Web Store listing** (Privacy tab → Privacy policy URL):
  - Plot Armor: Spoiler Blocker for Movies & TV: `https://plotarmor.gg/movies-tv/privacy/`
  - Plot Armor: Filter Out What You Don't Want: `https://plotarmor.gg/filter/privacy/`
  - Plot Armor: Sports Spoiler Blocker: `https://plotarmor.gg/sports/privacy/`
- Movies & TV is already in the store: developer dashboard → the item → **Privacy** tab →
  replace the privacy policy URL → **Save draft** → **Submit for review**. The old GitHub
  address keeps working, so nothing breaks in between.
- Optional: the store listing's "Homepage URL" can be the product page, e.g.
  `https://plotarmor.gg/movies-tv/`.

## When something changes
- A product goes into the store: replace its `<span class="soon">…</span>` on the front page and
  its product page with `<a class="btn" href="STORE LINK">Add to Chrome</a>`.
- A privacy policy changes in a product's folder: copy the new words into that product's
  `docs/<product>/privacy/index.html` and update the date.
