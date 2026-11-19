"""Check every link and image on the site.

    python3 tools/check_links.py            # inside links and images only
    python3 tools/check_links.py --online   # also opens every outside link once

Inside links must point to a file in docs/ (a folder link means its index.html).
Prints each problem and exits with 1 if there are any.
"""
import os
import re
import sys
import urllib.request
from html.parser import HTMLParser

DOCS = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'docs')


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.found = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            self.ids.add(a['id'])
        for key in ('href', 'src'):
            if a.get(key) and not (tag == 'link' and a.get('rel') == 'canonical'):
                self.found.append(a[key])
        if tag == 'meta' and a.get('property') == 'og:image':
            self.found.append(a['content'].replace('https://plotarmor.gg', ''))


def local_target(path):
    path = path.split('#')[0].split('?')[0]
    full = os.path.normpath(os.path.join(DOCS, path.lstrip('/')))
    if os.path.isdir(full):
        full = os.path.join(full, 'index.html')
    return full


def main():
    online = '--online' in sys.argv
    problems, outside, pages = [], {}, {}
    for root, _, files in os.walk(DOCS):
        for name in files:
            if name.endswith('.html'):
                p = os.path.join(root, name)
                parser = Links()
                parser.feed(open(p, encoding='utf-8').read())
                pages[os.path.relpath(p, DOCS)] = parser
    ids = {os.path.normpath(os.path.join(DOCS, k)): v.ids for k, v in pages.items()}
    for page, parser in sorted(pages.items()):
        for link in parser.found:
            if link.startswith(('http://', 'https://')):
                outside.setdefault(link, page)
            elif link.startswith('mailto:'):
                continue
            elif link.startswith('#'):
                if link[1:] not in parser.ids:
                    problems.append(f'{page}: missing #{link[1:]}')
            elif not link.startswith('/'):
                problems.append(f'{page}: use links that start with / ({link})')
            else:
                target = local_target(link)
                if not os.path.exists(target):
                    problems.append(f'{page}: broken link {link}')
                elif '#' in link and link.split('#')[1] not in ids.get(target, set()):
                    problems.append(f'{page}: missing anchor {link}')
    if online:
        for url, page in sorted(outside.items()):
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (link check)'})
            try:
                code = urllib.request.urlopen(req, timeout=15).status
            except Exception as e:  # noqa: BLE001
                code = getattr(e, 'code', str(e))
            ok = code == 200
            print(f'{"ok " if ok else "BAD"} {code} {url}')
            if not ok:
                problems.append(f'{page}: outside link failed ({code}) {url}')
    print(f'{len(pages)} pages, {len(outside)} outside links checked' if online else f'{len(pages)} pages checked')
    for p in problems:
        print('PROBLEM', p)
    sys.exit(1 if problems else 0)


if __name__ == '__main__':
    main()
