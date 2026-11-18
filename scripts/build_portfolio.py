"""Generate two lightweight layouts from one shared portfolio content template."""
from pathlib import Path
from string import Template
import sys

root = Path(__file__).resolve().parents[1]
template = Template((root / 'portfolio/page.html.template').read_text())
layouts = [
    ('index.html', 'layout-evidence', ' aria-current="page"', ''),
    ('portfolio-story.html', 'layout-story', '', ' aria-current="page"'),
]
for name, layout, a, b in layouts:
    output = template.substitute(layout_class=layout, a_current=a, b_current=b)
    target = root / name
    if '--check' in sys.argv:
        assert target.read_text() == output, f'{name} differs from the shared template; regenerate it.'
    else:
        target.write_text(output)
print('PASS: both presentation pages match one shared content template.' if '--check' in sys.argv else 'Built evidence-grid and project-journal presentation options.')
