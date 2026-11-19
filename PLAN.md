# plotarmor.gg: plan (2026-11-19, waiting for Selly's yes)

## What the site is

A small, plain website for the Plot Armor family of Chrome extensions. It's just files (HTML,
CSS and images) that a free host hands out. It has no server code, database, logins, payments,
cookies, trackers or outside fonts. Visiting the site loads files only from plotarmor.gg, so the
site keeps the same promise as the extensions.

## Pages

| Address | What's on it |
|---|---|
| `plotarmor.gg/` | **Front door.** One line on what Plot Armor is ("Protection for your X feed. Everything runs on your computer."), then one card per extension: shield icon, name, one-sentence summary, and either **Add to Chrome** or **Coming soon**. A short "Private by design" strip at the bottom. |
| `/movies-tv/` | Plot Armor: Spoiler Blocker for Movies & TV. What it covers, how it works (3 steps), screenshot, Add to Chrome, "Request a show" and "Report a problem" links, privacy link. |
| `/filter/` | The Filter extension (name: see question 1). Coming soon. |
| `/sports/` | Plot Armor: Sports Spoiler Blocker. Coming soon. |
| `/games/` | Plot Armor: Games (first game: GTA 6). Coming soon, short "being built" text. |
| `/movies-tv/privacy/` | Movies & TV privacy policy, moved here (same words). |
| `/sports/privacy/` | Sports privacy policy, copied from `plot-armor-sports/store/privacy.html`. |
| `/filter/privacy/` | Filter privacy policy, new (see "Privacy policies" below). |
| `/games/privacy/` | Added later, when Games is close to the store. |
| `/support/` | Help and contact: the two Google Forms, a contact email (question 3), a few FAQs ("Is my data sent anywhere?", "How do I remove it?", "It missed a spoiler"). |
| `404.html` | "This page doesn't exist" with links back to the front door and support. |

Every page shares the same header (logo + Products / Support) and footer (privacy links,
"Not affiliated with X", © Plot Armor).

### Links that already exist (copied from `spoiler-blocker/src/lib/links.ts`)
- Request a show: https://forms.gle/RirDDxQB4xXFK8PE6
- Report a problem (Movies & TV): https://forms.gle/nN2NF4e1QtX37FZN7
- Add to Chrome (Movies & TV): https://chromewebstore.google.com/detail/liidafcnfgmcemdeaaddafoenfbilbke

### "Coming soon" sign-up
There's no server, so a sign-up form has to live somewhere else. My pick: **one Google Form**,
"Tell me when it's out", with a checkbox per product and an email box. It's the same as the
existing forms, and the privacy wording already covers Google Forms. Until that form exists, the
cards just say **Coming soon** with no sign-up, so no link is ever broken. I can write a small
script you paste into Google Apps Script to make the form, the same way `create-request-form.gs`
was made. (Question 4.)

## Privacy policies

- **Stable addresses** to paste into the store: `https://plotarmor.gg/movies-tv/privacy/`,
  `/sports/privacy/` and `/filter/privacy/`.
- **Movies & TV:** same words, restyled to match the site, with the date updated. The old
  GitHub address (`sellybros711.github.io/spoiler-blocker-data/privacy.html`) keeps working. After
  launch you change the "Privacy policy URL" field in the store dashboard (click-by-click steps
  will be in `LAUNCH.md`). The site doesn't change anything in the store.
- **Sports:** copied as it is today.
- **Filter:** I'll draft it from the Filter's `CLAUDE.md`, then ask the Filter session to check
  every sentence. It **must say that account lookups go to X** (Filter asks X where accounts are
  based, using your own X sign-in). That's the one place a family extension sends a request to
  anyone besides a public-data download.
- Each policy page says at the top which product it covers, and when it was last updated.

## Being careful with words

- Names exactly as given, never ™ or ®.
- Each product page says only what that product does today. I'll take sentences from the store
  copy only after checking them against the product. For example, Filter's page talks about
  gambling, spam & scams and ads (what's built) and doesn't promise bots/crypto/politics as done.
  "More categories on the way" is fine.
- **Family privacy line, worded so it's true for all four:** "No account. No Plot Armor server.
  What you read on X stays on your computer." I won't write "nothing ever leaves your computer",
  because the extensions download data files and Filter looks up accounts on X.
- "Not affiliated with X, or with any show, league, team or game company" in the footer.

## Look

- **Brand:** the shared shield from `~/Projects/plot-armor-brand/icons/`. Movies & TV green
  (#19D97D), Filter red (#DB3434), Sports blue (#1E88E5). Each product page takes on its color.
  The family color is the existing Plot Armor violet (#6440F5, from the privacy page and the
  screenshot backgrounds). Games has no shield yet, so it uses a plain grey shield until the hub
  session makes one (I'll ask the hub).
- **Images:** icons copied into the site (not linked), plus `spoiler-blocker/store/promo-tile-440x280.png`
  and `store/screenshots/1-show-hub.png`. Sports, Filter and Games have no screenshots yet, so
  their pages use the big shield until screenshots exist.
- **Fast:** hand-written HTML and one small CSS file, no frameworks, system fonts. Images are
  resized to the size shown. Each page should be under about 200 KB.
- **Phone-first:** one column on phones, cards side by side on wider screens, no sideways scrolling.
- **Light and dark:** follows the computer's setting automatically.
- Basic sharing previews (title, description, image) so links look good when posted on X.

## Analytics

**None.** No visit counting, no cookies. The Chrome Web Store dashboard already shows installs.
If you want visit counts later, the only kind I'd suggest is a cookie-free counter
(GitHub Pages has none built in, so it would be something like GoatCounter). Even that sees
the page address, the referring site, screen size and country, and it would need its own line
in a site privacy note. Not part of this plan.

## Hosting: GitHub Pages (free)

You already use it for `spoiler-blocker-data` and `plot-armor-sports-data`, so there's no new
account. It gives free HTTPS for your own domain, and a push publishes the site. Cloudflare
Pages would also work, but it means a new account for no gain at this size.

What I'd do (each step only after your yes in this chat):
1. Create a **public** GitHub repo `sellybros711/plot-armor-site` and push `main`. (Free GitHub
   Pages needs a public repo. The site files are public anyway.)
2. Turn on Pages from `main` and set the custom domain `plotarmor.gg` (a `CNAME` file in the repo).

### Your clicks (DNS and HTTPS), in `LAUNCH.md`
1. **Verify the domain with GitHub first** (stops anyone else from claiming it): github.com →
   your photo → Settings → Pages → "Add a domain" → type `plotarmor.gg` → GitHub shows a TXT
   record. Keep that tab open.
2. Sign in to the company you bought plotarmor.gg from → find **DNS** / "Manage DNS" for plotarmor.gg.
3. Add the TXT record from step 1 (Type TXT, Host/Name as GitHub shows it, Value as shown). Save.
   Back on GitHub, click **Verify**. (It can take a few minutes, sometimes up to a day.)
4. Delete any "parking" or "forwarding" records the registrar added for `@` and `www`.
5. Add four **A** records, Host `@`: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`,
   `185.199.111.153`.
6. (Optional, for newer networks) four **AAAA** records, Host `@`: `2606:50c0:8000::153`,
   `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153`.
7. Add one **CNAME** record: Host `www`, Value `sellybros711.github.io`.
8. On GitHub: the plot-armor-site repo → Settings → Pages → Custom domain should show
   `plotarmor.gg` with a green "DNS check successful". (It can take up to an hour.)
9. Tick **Enforce HTTPS** when it becomes clickable (GitHub makes the certificate itself, up to 24 h).
10. Open https://plotarmor.gg and https://www.plotarmor.gg on your phone. Both should show the site.

I'll check the addresses and menu names against GitHub's current help page before writing
`LAUNCH.md`, and I'll fill in your registrar's exact menu names once you tell me which one it is.

## Done for launch (what "functioning" means)

- Every page opens; every link and button works (a small link-checker script runs over the
  whole site, inside links and outside ones).
- Privacy URLs are live on https://plotarmor.gg and listed in `LAUNCH.md`, ready to paste into
  each store listing.
- 404 page shows for a made-up address.
- Checked in the built-in browser at phone (375 px) and desktop sizes, in light and dark.
- HTTPS works for plotarmor.gg and www.plotarmor.gg.
- Committed to `main`. Pushing and DNS happen only after your yes.

## Not in this plan
Pro tier or payments, accounts, a blog, newsletters run by us, analytics, translations.

## Questions for Selly
1. **Filter's name.** The task says "Plot Armor: Filter Out Gambling", but the Filter project
   says you renamed it on 2026-11-17 to **"Plot Armor: Filter Out What You Don't Want"**. Which
   one goes on the site?
2. **Store status.** The task says only Movies & TV is in the store. The Sports listing notes say
   Movies & TV and Filter use the two slots. Is Filter submitted (even Unlisted)? If so, I'll show
   "Add to Chrome" for it once there's a link.
3. **Contact email.** The current privacy policy lists RunTheGames@outlook.com. OK to show it on
   the support page and in all policies, or do you want a new one (for example
   hello@plotarmor.gg, which needs email forwarding set up at your registrar)?
4. **Coming soon sign-up.** Google Form "Tell me when it's out" (I write the script, you run
   it), or just "Coming soon" with no sign-up for now?

## Built 2026-11-19 (Selly said yes; the four questions weren't answered, so these defaults were used)
1. Filter is shown as **"Plot Armor: Filter Out What You Don't Want"**, the name in the extension itself.
2. Filter, Sports and Games show "Coming soon" / "Being built" (no store links yet).
3. Contact email: RunTheGames@outlook.com, already public in the live privacy policies.
4. No sign-up form; cards just say "Coming soon".
Also: the Sports policy linked to `sellybros711.github.io/plot-armor-sports-data/`, which shows
a 404, so the moved copy shows that address as plain text. Words are otherwise unchanged.
The Filter policy is new and still needs checking by the Filter session.
