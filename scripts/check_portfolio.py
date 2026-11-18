"""Check the two portfolio options share actual content and professional links."""
from html.parser import HTMLParser
from pathlib import Path

class MainContent(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_main = False
        self.text = []
        self.links = []
        self.case_ids = set()
        self.layout_links = []
        self.in_layout_nav = False
        self.current_options = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'main':
            self.in_main = True
        if tag == 'nav' and attrs.get('aria-label') == 'Presentation options':
            self.in_layout_nav = True
        if tag == 'a' and self.in_layout_nav:
            self.layout_links.append(attrs.get('href'))
            self.current_options += attrs.get('aria-current') == 'page'
        if self.in_main and tag == 'a':
            self.links.append(attrs.get('href'))
        if tag == 'article' and attrs.get('id'):
            self.case_ids.add(attrs['id'])

    def handle_endtag(self, tag):
        if tag == 'main':
            self.in_main = False
        if tag == 'nav':
            self.in_layout_nav = False

    def handle_data(self, text):
        if self.in_main and text.strip():
            self.text.append(' '.join(text.split()))

root = Path(__file__).resolve().parents[1]
options = []
for filename in ['index.html', 'portfolio-story.html']:
    parser = MainContent()
    parser.feed((root / filename).read_text())
    assert parser.case_ids == {'coin-dash', 'museum', 'group-project'}
    assert parser.current_options == 1
    assert parser.layout_links == ['index.html#work', 'portfolio-story.html#work']
    for link in ['Mathai_Resume.pdf', 'https://github.com/JoshMathai',
                 'https://www.linkedin.com/in/joshua-mathai-5aa230370/',
                 'https://github.com/JoshMathai/The-Career-Engineered-Portfolio']:
        assert link in parser.links, f'Missing professional link: {filename}: {link}'
    options.append(parser)
assert options[0].text == options[1].text, 'Presentation options differ in main content'
assert options[0].links == options[1].links, 'Presentation options differ in main links'
assert (root / 'Mathai_Resume.pdf').read_bytes().startswith(b'%PDF-')
print('PASS: A and B have identical main text and links, including three case studies.')
print('PASS: both layout switches work as local links; one current option on each page.')
print('PASS: current résumé, owned GitHub/LinkedIn, and portfolio repository links present.')
print('Limit: structural checks do not establish browser behavior or real peer review.')
