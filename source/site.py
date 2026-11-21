"""Fill index.template.html from fogbank.json (palette hexes come straight from the theme) -> ../index.html."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://joshsaintjacque.github.io/t3code-theme-fogbank/"
REPO = "https://github.com/joshsaintjacque/t3code-theme-fogbank"
c = json.load(open(os.path.join(HERE, "..", "fogbank.json")))["colors"]
rows = [("Canvas", "canvas"), ("Sidebar", "sidebar"), ("Chrome and header", "chrome"), ("Message bubble", "messageSurface"),
        ("Code background", "codeBackground"), ("Text", "text"), ("Muted text", "textMuted"), ("Border", "border"),
        ("Accent, send, links", "accent"), ("Focus ring", "focus"), ("Lamp (search match)", "searchMatchActiveBackground"),
        ("Update", "update"), ("Error", "error"), ("Warning", "warning")]
body = "\n".join(
    f'<tr class="pr" tabindex="0" data-hex="{c[k]}"><td><span class="sw2" style="background:{c[k]}"></span>{n}</td><td class="hex">{c[k]}<span>copied</span></td></tr>'
    for n, k in rows)
dl = sys.argv[1] if len(sys.argv) > 1 else "about 70s"
t = open(os.path.join(HERE, "index.template.html")).read()
t = t.replace("__PALETTE__", body).replace("__SITE__", SITE).replace("__REPO__", REPO).replace("__DEMO_LEN__", dl)
open(os.path.join(HERE, "..", "index.html"), "w").write(t)
print("index.html", len(t))
