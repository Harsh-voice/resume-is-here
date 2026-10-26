# every class the HTML uses should have at least one rule in the stylesheet
import re, sys, pathlib
html = pathlib.Path(sys.argv[1]).read_text()
style = '\n'.join(re.findall(r'<style>(.*?)</style>', html, re.S))
used = set()
for attr in re.findall(r'class="([^"]+)"', html):
    for c in attr.split():
        if c and not c.startswith('__'):
            used.add(c)
# classes toggled only from JS still count as styled if a rule mentions them
styled = set(re.findall(r'\.([A-Za-z][A-Za-z0-9_-]*)', style))
missing = sorted(c for c in used - styled if not re.match(r'^(v[0-9]|m[0-9])', c))
print('classes used:', len(used), '| with rules:', len(used & styled))
print('NO RULE:', missing or 'none')
sys.exit(1 if missing else 0)
