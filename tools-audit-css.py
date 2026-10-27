# every class the HTML uses should have at least one rule in the stylesheet
import re, sys, pathlib
sheet = pathlib.Path('/home/user/resume-is-here/styles.css').read_text()
fail = False
for f in sys.argv[1:]:
    html = pathlib.Path(f).read_text()
    style = sheet + '\n'.join(re.findall(r'<style>(.*?)</style>', html, re.S))
    used = set()
    for attr in re.findall(r'class="([^"]+)"', html):
        for c in attr.split():
            if c and not c.startswith('__'):
                used.add(c)
    # classes toggled only from JS still count as styled if a rule mentions them
    styled = set(re.findall(r'\.([A-Za-z][A-Za-z0-9_-]*)', style))
    missing = sorted(c for c in used - styled if not re.match(r'^(v[0-9]|m[0-9])', c))
    print(f'{pathlib.Path(f).name:12} used {len(used):3} | styled {len(used & styled):3} | NO RULE: {missing or "none"}')
    fail = fail or bool(missing)
sys.exit(1 if fail else 0)
