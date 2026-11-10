"""Check local HTML link targets and fragments. Run from any directory."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.headings = 0
        self.language = False
        self.viewport = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        for key in ("href", "src"):
            if key in attrs:
                self.links.append(attrs[key])
        self.headings += tag == "h1"
        self.language |= tag == "html" and bool(attrs.get("lang"))
        self.viewport |= tag == "meta" and attrs.get("name") == "viewport"


root = Path(__file__).resolve().parents[1]
pages = {}
for path in root.rglob("*.html"):
    page = Page()
    page.feed(path.read_text())
    assert len(page.ids) == len(set(page.ids)), f"Duplicate IDs: {path}"
    assert page.headings == 1, f"Expected one main heading: {path}"
    assert page.language and page.viewport, f"Missing language/viewport: {path}"
    pages[path] = page

references = 0
for path, page in pages.items():
    for link in page.links:
        url = urlsplit(link)
        if url.scheme or url.netloc:
            continue
        target = (path.parent / unquote(url.path)).resolve() if url.path else path
        if target.is_dir():
            target /= "index.html"
        assert target.exists(), f"Missing target: {path} -> {link}"
        if url.fragment:
            assert target in pages and unquote(url.fragment) in pages[target].ids, (
                f"Missing fragment: {path} -> {link}"
            )
        references += 1
assert (root / "resume.pdf").read_bytes().startswith(b"%PDF-"), "Invalid PDF signature"
print(f"PASS: {len(pages)} HTML pages; {references} local targets/fragments; unique IDs;")
print("one H1 per page; language/viewport metadata; résumé PDF signature.")
print("Limit: does not test external links, visual layout, PDF readability, or keyboard behavior.")
