# plotarmor.gg

The website for the Plot Armor family of Chrome extensions. Plain HTML and one CSS file, with no
build step, no frameworks, no cookies, no analytics and no outside fonts or scripts.

- `docs/`: the whole site, exactly as served (GitHub Pages serves this folder).
  Each page is `docs/<page>/index.html`; shared styles are in `docs/style.css`.
- `tools/check_links.py`: checks every link and image. `--online` also opens outside links.
- `PLAN.md`: the approved plan. `LAUNCH.md`: publishing steps and the privacy URLs for the store.

See it locally:

    python3 -m http.server 8411 --directory docs     # then open http://localhost:8411

The header and footer are repeated on every page; change them on all pages at once
(the link checker catches broken links). Product names are exact: never add ™ or ®.
