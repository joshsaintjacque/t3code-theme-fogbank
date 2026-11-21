"""Build the Fogbank theme for T3 Code: fogbank.json + preview SVG."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
SLATE = "#8c89b3"   # distant headland
AMBER = "#f2b950"   # lamp


def data_uri(svg):
    out = svg.replace("%", "%25").replace("#", "%23").replace('"', "'").replace("<", "%3C")
    return 'url("data:image/svg+xml,' + out + '")'


# ---------------------------------------------------------------- lighthouse
def lighthouse_svg():
    return (
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 380'>"
        "<defs><radialGradient id='g'><stop offset='0' stop-color='#f6c862' stop-opacity='.55'/><stop offset='1' stop-color='#f6c862' stop-opacity='0'/></radialGradient>"
        "<linearGradient id='t' x1='0' x2='1'><stop offset='0' stop-color='#a19ec4'/><stop offset='1' stop-color='#8582ae'/></linearGradient></defs>"
        "<g opacity='.82'>"
        "<path d='M20 380C28 350 52 338 76 336L124 336C150 338 172 350 182 380Z' fill='#8d8ab2'/>"
        "<path d='M78 340L91 112H109L122 340Z' fill='url(#t)'/>"
        "<path d='M84.5 250L87 205H113L115.5 250Z' fill='#6f6c9a' opacity='.55'/>"
        "<path d='M89 160L90.5 126H109.5L111 160Z' fill='#6f6c9a' opacity='.55'/>"
        "<rect x='80' y='104' width='40' height='8' rx='1.5' fill='#7a779f'/>"
        "<path d='M82 104V94M90 104V94M98 104V94M106 104V94M114 104V94' stroke='#7a779f' stroke-width='1.6'/>"
        "<rect x='81' y='93' width='38' height='2.4' fill='#7a779f'/>"
        "<rect x='89' y='76' width='22' height='18' fill='#e7d9ab'/>"
        "<path d='M95 76V94M105 76V94' stroke='#8a87b0' stroke-width='1.6'/>"
        "<path d='M85 76Q100 52 115 76Z' fill='#6f6c9a'/><path d='M100 54V44' stroke='#6f6c9a' stroke-width='2'/>"
        "</g>"
        "<circle cx='100' cy='85' r='46' fill='url(#g)'/>"
        "</svg>")


def ridge_svg():
    return ("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1200 120' preserveAspectRatio='none'>"
            "<path d='M0 120V70C90 52 160 40 250 56S390 84 480 66 640 30 760 48 930 86 1030 62 1130 40 1200 50V120Z' fill='#bfbcdb' opacity='.5'/>"
            "<path d='M0 120V92C120 78 210 70 330 84S520 106 640 88 860 64 980 82 1120 96 1200 86V120Z' fill='#aaa7cc' opacity='.45'/></svg>")


def gulls_svg():
    return ("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 120 120'><g fill='none' stroke='#7c79a4' stroke-width='1.6' stroke-linecap='round' stroke-linejoin='round' opacity='.7'>"
            "<path d='M20 40q8-9 16 0q8-9 16 0'/><path d='M66 22q6-7 12 0q6-7 12 0'/><path d='M44 78q5-6 10 0q5-6 10 0'/></g></svg>")


def preview_svg():
    return lighthouse_svg()


# ---------------------------------------------------------------- colours
colors = {
    "canvas": "#e8e7f0", "chrome": "#dedcea", "toolbar": "#dedcea", "toolbarForeground": "#2a2940",
    "toolbarBorder": "#c8c5da", "toolbarControl": "#d3d0e3", "toolbarControlForeground": "#2a2940",
    "toolbarControlHover": "#c6c3da", "surface": "#f1f0f6", "surfaceRaised": "#f6f5fa",
    "surfaceOverlay": "#faf9fc", "text": "#2a2940", "textMuted": "#55536f", "border": "#c6c3d8",
    "input": "#bbb8d0", "focus": "#5a5fa3", "accent": "#474c8a", "accentForeground": "#f7f6fc",
    "secondary": "#d9d6e8", "secondaryForeground": "#34324d", "muted": "#dedcea",
    "mutedForeground": "#58566f", "placeholder": "#78768f", "secondaryLabel": "#58566f",
    "iconMuted": "#6a6884", "error": "#b0384a", "errorForeground": "#8b2236", "errorSurface": "#f4dde1",
    "warning": "#855008", "warningForeground": "#744505", "warningSurface": "#f4e7cf",
    "update": "#2b7686", "updateForeground": "#1c5663", "updateSurface": "#d7e9ed",
    "accentSurface": "#d9daee", "accentSurfaceForeground": "#33366b", "messageSurface": "#dad8ea",
    "messageForeground": "#2a2940", "messageAction": "#474c8a", "messageActionForeground": "#f7f6fc",
    "messageActionHover": "#383c76", "codeBackground": "#f4f3f9", "codeForeground": "#2e2d47",
    "searchMatchBackground": "#f0d9a0", "searchMatchForeground": "#3a2a05",
    "searchMatchActiveBackground": "#e3ac3e", "searchMatchActiveForeground": "#2a1c02",
    "sidebar": "#dddbea", "sidebarForeground": "#2a2940", "sidebarMutedForeground": "#55537a",
    "sidebarControlSurface": "#e9e8f2", "sidebarRowHover": "#d1cee3", "sidebarRowActive": "#c9c6dd",
    "sidebarRowSelected": "#c8c5e0", "sidebarBorder": "#c8c5da", "terminalBackground": "#f1f0f6",
    "terminalForeground": "#2a2940", "terminalCursor": "#474c8a", "terminalSelection": "#cfcde6",
    "terminalScrollbar": "#c1bed6", "terminalScrollbarHover": "#a9a6c4",
}

CW = "var(--chat-content-max-width,46rem)"
BUSY = ('body:has([data-timeline-row-kind="working"])',
        'body:has([data-thread-item] [aria-busy="true"][aria-current]:not([aria-current="false"]))')


def busy(sel):
    return ",".join(f"{b} {sel}" for b in BUSY)


AREA = '[data-workspace-area="conversation"]'
SERIF = '"Iowan Old Style","Palatino Linotype",Palatino,"Hoefler Text",Georgia,serif'
MONO = 'ui-monospace,"SF Mono",Menlo,monospace'

# lighthouse geometry (svg viewBox 200x380 -> aspect 1.9; lamp at y=85)
def geom(w):
    h = round(w * 1.9)
    lamp_bottom = 20 + round(h * (1 - 85 / 380))
    return h, lamp_bottom

W_WIDE, W_NARROW, W_MINI = 190, 96, 60
BEAM = 1600  # px square; the mask fades to nothing at the edge, so nothing is wasted

# Fog tile = one third of the conversation width. Every ellipse sits wholly inside its tile (so the repeat has no
# seams), and the drift moves exactly one tile, so the loop is seamless and divides the hero clip evenly.
# Two tile periods (1/3 and 1/2 of the conversation width) so the bands never repeat on one rhythm; they realign every
# full conversation width, i.e. 50% of the 200%-wide layer, which is the drift distance (7px/s at 192s).
MIST_A = (
    "radial-gradient(ellipse 50% 4.5% at 40% 16%,rgba(255,255,255,.9),transparent 78%),"
    "radial-gradient(ellipse 48% 5% at 62% 41%,rgba(158,154,206,.3),transparent 78%),"
    "radial-gradient(ellipse 44% 5.5% at 35% 63%,rgba(255,255,255,.85),transparent 78%),"
    "radial-gradient(ellipse 46% 4% at 60% 86%,rgba(172,168,214,.32),transparent 78%)"
)
MIST_B = (
    "radial-gradient(ellipse 56% 5% at 55% 8%,rgba(255,255,255,.7),transparent 78%),"
    "radial-gradient(ellipse 38% 5.5% at 30% 29%,rgba(255,255,255,.88),transparent 78%),"
    "radial-gradient(ellipse 40% 4.5% at 68% 52%,rgba(158,154,206,.26),transparent 78%),"
    "radial-gradient(ellipse 52% 6% at 42% 75%,rgba(255,255,255,.9),transparent 78%),"
    "radial-gradient(ellipse 52% 4% at 50% 95%,rgba(172,168,214,.3),transparent 78%)"
)
MIST = MIST_A + "," + MIST_B + ",linear-gradient(to top,rgba(255,255,255,.8),transparent 28%)"
MIST_SIZE = ",".join(["16.6667% 100%"] * 4 + ["25% 100%"] * 5 + ["100% 100%"])

BANK = "linear-gradient(to top,rgba(238,237,246,.94) 0,rgba(238,237,246,.78) 70px,rgba(238,237,246,.3) 150px,rgba(238,237,246,0) 210px)"


def lh_bg(w):
    return (f"{BANK} left bottom/100% 210px no-repeat,"
            f"var(--fb-l) left calc(75% + {w // 4}px + {CW}/4) bottom 20px/{w}px auto no-repeat,"
            f"var(--fb-g) left calc(25% - {w // 4}px - {CW}/4 + 12px) top 12%/{int(w*.7)}px auto no-repeat,"
            "var(--fb-r) left bottom/100% 120px no-repeat,"
            "linear-gradient(180deg,#eceaf4 0%,#e6e4ef 55%,#e0deec 100%)")


def beam(w):
    h, lb = geom(w)
    return f"{AREA}::after{{right:calc((100% - {CW})/4 - {BEAM // 2}px);bottom:{lb - BEAM // 2}px}}"


beam_cone = (
    "radial-gradient(circle closest-side,rgba(255,214,120,.65) 0,rgba(255,214,120,0) 46px),"
    "conic-gradient(from -8deg at 50% 50%,transparent 0deg,rgba(240,170,60,.42) 8deg,transparent 16deg,"
    "transparent 172deg,rgba(240,170,60,.05) 180deg,transparent 188deg,transparent 360deg)"
)
BEAM_MASK = "radial-gradient(circle closest-side,#000 5%,rgba(0,0,0,.7) 26%,transparent 68%)"
INK = "#474c8a"
RULE = "#c6c3d8"

css = (
    ":root{--fb-l:" + data_uri(lighthouse_svg()) + ";--fb-g:" + data_uri(gulls_svg()) + ";--fb-r:" + data_uri(ridge_svg()) + "}"
    # ---------- conversation: sky, headland lighthouse, dense ground fog (static, behind the tower foot)
    # position/isolation/overflow are forced here ON PURPOSE: the fog and beam are ::before/::after layers that need this
    # box as their containing block, isolation keeps their z-index:-1 above this box's own background, and clip stops
    # the oversize beam and the 200%-wide fog tile creating scroll.
    f"{AREA}{{position:relative;isolation:isolate;overflow:clip;background:{lh_bg(W_WIDE)}!important}}"
    # near fog: one constant speed (no duration swaps, so nothing teleports); busy only raises opacity
    f"{AREA}::before{{content:\"\";position:absolute;left:0;top:0;bottom:0;width:200%;z-index:-1;pointer-events:none;"
    f"background-image:{MIST};background-size:{MIST_SIZE};background-repeat:repeat-x,repeat-x,repeat-x,repeat-x,repeat-x,repeat-x,repeat-x,repeat-x,repeat-x,no-repeat;opacity:.78;transition:opacity 2.6s ease;"
    "animation:fb-drift 192s linear infinite}"
    "@keyframes fb-drift{to{transform:translate3d(-50%,0,0)}}"
    + busy(f"{AREA}::before") + "{opacity:1}"
    # lamp beam: paused and invisible at rest. Turn starts: a strong first sweep that settles to half strength.
    # Turn ends: one last bloom (the beam flares once and dissolves) -- the "done" beat.
    "@property --fb-b{syntax:'<number>';inherits:false;initial-value:0}"
    f"{AREA}::after{{content:\"\";position:absolute;width:{BEAM}px;height:{BEAM}px;z-index:-1;pointer-events:none;"
    f"background:{beam_cone};-webkit-mask-image:{BEAM_MASK};mask-image:{BEAM_MASK};"
    "--fb-b:0;opacity:calc(var(--fb-b)*.5 + var(--fb-b)*(1 - var(--fb-b))*2.8);transition:--fb-b 3.4s ease-out;animation:fb-sweep 16s linear infinite paused}"
    + beam(W_WIDE)
    + "@keyframes fb-sweep{to{transform:rotate(360deg)}}"
        "@keyframes fb-settle{0%{opacity:0}12%{opacity:1}100%{opacity:.5}}"
    + busy(f"{AREA}::after") + "{--fb-b:1;transition:none;animation:fb-sweep 16s linear infinite running,fb-settle 12s ease-out forwards}"
    # narrow windows: smaller lighthouse in the thinner gutter, retired when there is no gutter at all
    f"@media (max-width:1459px){{{AREA}{{background:{lh_bg(W_NARROW)}!important}}{beam(W_NARROW)}}}"
    "@media (max-width:1459px){@keyframes fb-settle{0%{opacity:0}12%{opacity:.8}100%{opacity:.5}}}"
    f"@media (max-width:1239px) and (min-width:1180px){{{AREA}{{background:{lh_bg(W_MINI)}!important}}{beam(W_MINI)}}}"
    # below ~1180px there is no gutter: the tower retires and a small lantern halo marks the working state instead
    f"@media (max-width:1179px){{{AREA}{{background:{BANK} left bottom/100% 210px no-repeat,var(--fb-r) left bottom/100% 120px no-repeat,linear-gradient(180deg,#eceaf4,#e0deec)!important}}"
    f"{AREA}::after{{width:200px;height:200px;right:-30px;bottom:80px;-webkit-mask-image:none;mask-image:none;"
    "background:radial-gradient(circle closest-side,rgba(255,214,120,.95) 0,rgba(255,214,120,.5) 40%,rgba(255,214,120,0) 100%);"
    "animation:fb-halo 4.5s ease-in-out infinite paused}"
    + busy(f"{AREA}::after") + "{animation:fb-halo 4.5s ease-in-out infinite running}"
    "@keyframes fb-halo{0%,100%{transform:scale(.85)}50%{transform:scale(1.05)}}}"
    # reading column scrim: a clear patch of air so text never sits on fog art
    f"{AREA} .messages-timeline-scroll{{background:linear-gradient(90deg,transparent calc(50% - {CW}/2 - 96px),"
    f"rgba(239,238,246,.93) calc(50% - {CW}/2 - 12px),rgba(239,238,246,.93) calc(50% + {CW}/2 + 12px),"
    f"transparent calc(50% + {CW}/2 + 96px))!important}}"
    # ---------- sidebar: chart lettering, mist at the foot, a lamp-bar sweeps while any turn runs
    # (sidebar-inner is already a column box; position:relative only gives the foot bar a containing block)
    f"[data-slot=\"sidebar-inner\"]{{position:relative;font-family:{SERIF};background:radial-gradient(ellipse 90% 14% at 30% 100%,rgba(255,255,255,.8),transparent 75%),"
    "radial-gradient(ellipse 70% 8% at 80% 93%,rgba(255,255,255,.5),transparent 75%),#dddbea!important}"
    "[data-slot=\"sidebar-inner\"]::after{content:\"\";position:absolute;left:0;bottom:0;width:42%;height:2px;pointer-events:none;"
    "background:linear-gradient(90deg,transparent,#e0a23a,transparent);opacity:0;transform:translateX(-110%);transition:opacity 1.6s}"
    + "@media (max-width:1239px){" + busy("[data-slot=\"sidebar-inner\"]::after") + "{opacity:.9;animation:fb-bar 6s ease-in-out infinite}}"
    "@keyframes fb-bar{0%{transform:translateX(-110%)}60%,100%{transform:translateX(280%)}}"
    # ---------- header: serif title, hairline; a lamp glint passes while a turn runs, one brighter pass when it ends.
    # (background-position is NOT !important so the animation can move it)
    f"[data-chat-header]{{font-family:{SERIF};letter-spacing:.01em;background-color:rgba(223,221,235,.9)!important;"
    "background-image:linear-gradient(90deg,transparent,rgba(232,166,52,.9),transparent)!important;background-repeat:no-repeat;"
    "background-size:30% 2px;background-position:-45% 100%;border-bottom:1px solid rgba(160,156,196,.35)!important}"
    + busy("[data-chat-header]") + "{animation:fb-glint 7s ease-in-out infinite}"
    "@keyframes fb-glint{0%{background-position:-45% 100%}65%,100%{background-position:145% 100%}}"
    # ---------- working row, work rows and busy threads. Longhands only, so selected/hover fills survive.
    "[data-timeline-row-kind=\"working\"]{background-image:linear-gradient(90deg,transparent,rgba(240,176,70,var(--a,.3)),transparent);"
    "background-size:40% 100%;background-position:-67% 0;background-repeat:no-repeat;"
    "border-radius:8px;animation:fb-wash var(--d,6s) ease-in-out infinite}"
    "[data-thread-item] [aria-busy=\"true\"]{--a:.14;--d:5s;background-image:linear-gradient(90deg,transparent,rgba(240,176,70,var(--a,.3)),transparent);"
    "background-size:40% 100%;background-position:-67% 0;background-repeat:no-repeat;animation:fb-wash var(--d) ease-in-out infinite}"
    "@keyframes fb-wash{to{background-position:167% 0}}"
    f"[data-timeline-row-kind=\"work\"]{{font-family:{SERIF};font-style:italic;border-left:2px solid rgba(150,146,190,.45);padding-left:10px;font-variant-numeric:tabular-nums}}"
    # ---------- sidebar rows
    "[data-thread-item]{border-radius:10px;transition:background-color .35s ease}"
    "[data-thread-item]:hover{background-image:linear-gradient(90deg,rgba(255,255,255,.6),rgba(255,255,255,0))}"
    "[data-thread-item] [aria-busy=\"true\"],[data-thread-item] [aria-current]:not([aria-current=\"false\"]){border-radius:10px}"
    f"[data-thread-item] [aria-current]:not([aria-current=\"false\"]){{box-shadow:inset 2px 0 {INK}}}"
    # project monogram: a small buoy
    f"[data-slot=\"project-monogram\"]{{border-radius:999px!important;box-shadow:inset 0 0 0 1.5px #6a6fb0!important;color:#33366b!important;font-family:{SERIF};font-style:italic;"
    "background:radial-gradient(circle at 50% 0,rgba(242,185,80,.6),transparent 62%),#f1f0f8!important}"
    # ---------- messages
    "[data-user-message-bubble]{background:#dad8ea!important;border:1px solid rgba(150,146,190,.35)!important;border-radius:16px 16px 5px 16px!important;box-shadow:0 1px 0 rgba(255,255,255,.7) inset}"
    "[data-slot=\"composer-host\"]{background:rgba(247,246,251,.97)!important;border:1px solid rgba(150,146,190,.5)!important;border-radius:16px!important;"
    "transition:border-color .4s ease,box-shadow .5s ease}"
    "[data-slot=\"composer-host\"]:focus-within{border-color:#6a6fb0!important;box-shadow:0 0 0 3px rgba(106,111,176,.16),0 -10px 26px -8px rgba(240,176,70,.32)}"
    "[data-slot=\"composer-host\"]{background-image:linear-gradient(to bottom,rgba(255,255,255,.95),rgba(255,255,255,0) 22px),linear-gradient(90deg,transparent,rgba(130,126,176,.4) 25%,rgba(130,126,176,.4) 75%,transparent) !important;"
    "background-size:100% 100%,100% 1px!important;background-position:0 0,0 calc(100% - 44px)!important;background-repeat:no-repeat!important}"
    "[data-user-message-bubble]{background-image:radial-gradient(circle at 96% 108%,rgba(255,243,209,.8),transparent 55%)!important}"
    "[data-slot=\"dialog-popup\"],[data-slot=\"popover-popup\"],[data-slot=\"menu-popup\"]{background-image:linear-gradient(to bottom,rgba(255,255,255,.9),transparent 56px)!important}"
    f".chat-markdown-codeblock{{background:#f4f3f9!important;border:1px solid rgba(150,146,190,.4)!important;border-left:3px solid #9a97c6!important;border-radius:10px!important;font-family:{MONO}}}"
    ".chat-markdown :not(pre)>code{color:#3a3e78;background:rgba(71,76,138,.09);padding:.06em .32em;border-radius:5px}"
    f".chat-markdown :is(h1,h2,h3,h4){{font-family:{SERIF};font-weight:600;letter-spacing:.005em;color:#25243b}}"
    ".chat-markdown :is(h1,h2){border-bottom:1px solid transparent;border-image:linear-gradient(90deg,rgba(130,126,176,.45),transparent 80%) 1;padding-bottom:.25em}"
    f".chat-markdown :is(h1,h2,h3) code{{font-family:{MONO}}}"
    ".chat-markdown a{color:#3d479a!important;text-decoration-color:rgba(61,71,154,.4);text-underline-offset:3px}"
    ".chat-markdown blockquote{border-left:2px solid #b3afd2!important;color:#55536f;font-style:italic}"
    ".chat-markdown hr{border:0!important;height:1px;background:linear-gradient(90deg,transparent,#a9a6c8 20%,#a9a6c8 80%,transparent)!important}"
    f".chat-markdown table{{border-collapse:separate;border-spacing:0;border:1px solid {RULE};border-radius:10px;overflow:hidden}}"
    f".chat-markdown th{{background:#e3e1ef;font-family:{SERIF};font-variant:small-caps;letter-spacing:.04em}}"
    f".chat-markdown :is(th,td){{border-bottom:1px solid {RULE}}}.chat-markdown tr:last-child td{{border-bottom:0}}"
    f".chat-markdown li::marker{{color:#7f7cb0}}.chat-markdown ol>li::marker{{font-family:{SERIF};font-weight:600}}"
    "svg.lucide{stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round}"
    "::selection{background:rgba(240,176,70,.38)}"
    # focus: one themed ring everywhere except the composer, which draws its own via :focus-within
    f":focus-visible{{outline:2px solid #5a5fa3!important;outline-offset:2px}}"
    "[data-slot=\"composer-host\"] :focus-visible,.composer-tiptap,.composer-tiptap:focus-visible{outline:none!important}"
    # ---------- popovers, menus, dialogs, tooltips
    "[data-slot=\"dialog-popup\"],[data-slot=\"popover-popup\"],[data-slot=\"menu-popup\"]{background:#faf9fc!important;border:1px solid #c6c3d8!important;border-radius:14px!important;box-shadow:0 14px 40px -12px rgba(60,58,100,.32)!important}"
    f"[data-slot=\"dialog-popup\"] :is(h1,h2,h3){{font-family:{SERIF}}}"
    "[data-slot=\"tooltip-popup\"]{background:#34324d!important;color:#f3f2f9!important;border-radius:8px!important;box-shadow:0 6px 18px -6px rgba(40,38,80,.4)!important}"
    # ---------- controls: buttons, inputs, selects, switches
    "[data-slot=\"button\"],[data-slot=\"input\"],[data-slot=\"select-trigger\"]{border-radius:10px!important}"
    "[data-slot=\"button\"]{transition:box-shadow .25s ease,transform .12s ease,background-color .25s ease}"
    f"[data-slot=\"button\"]:hover{{box-shadow:0 2px 8px -4px rgba(71,76,138,.35)}}"
    "[data-slot=\"button\"]:active{transform:translateY(1px) scale(.985);box-shadow:none}"
    "[data-slot=\"button\"]:focus-visible{outline:2px solid #5a5fa3!important;outline-offset:2px;box-shadow:0 0 0 5px rgba(240,176,70,.35)!important}"
    "[data-slot=\"input\"],[data-slot=\"select-trigger\"]{background-color:#f6f5fa!important;border-color:#bbb8d0!important;transition:border-color .3s,box-shadow .3s}"
    "[data-slot=\"input\"]:hover,[data-slot=\"select-trigger\"]:hover{border-color:#9d9ac2!important}"
    "[data-slot=\"input\"]:focus-visible,[data-slot=\"select-trigger\"]:focus-visible{border-color:#6a6fb0!important;box-shadow:0 0 0 3px rgba(106,111,176,.18)}"
    "[data-slot=\"switch\"]{transition:background-color .3s ease,box-shadow .3s ease}"
    "[data-slot=\"switch\"][aria-checked=\"true\"]{background-color:#474c8a!important;box-shadow:0 0 12px -2px rgba(240,176,70,.7)}"
    "[data-slot=\"switch\"][aria-checked=\"true\"]>*{background-color:#fff3d1!important}"
    "[data-slot=\"switch\"][aria-checked=\"false\"]{background-color:#c9c6dd!important}"
    # ---------- panels
    f"[data-thread-details-card]{{background-color:#f3f2f9!important;border:1px solid {RULE}!important;border-radius:14px!important;box-shadow:0 10px 30px -14px rgba(60,58,100,.3)}}"
    f"[data-thread-terminal-drawer]{{background-color:#f1f0f6!important;background-image:linear-gradient(to bottom,rgba(255,255,255,.75),transparent 48px);border-top:1px solid {RULE}!important;border-color:{RULE}!important}}"
    f"[data-settings-page-scroll]{{background-image:radial-gradient(ellipse 60% 18% at 88% 0,rgba(255,255,255,.85),transparent 72%),radial-gradient(ellipse 50% 14% at 6% 100%,rgba(158,154,206,.3),transparent 72%)}}"
    f"[data-settings-page-scroll] :is(h1,h2,h3){{font-family:{SERIF};font-weight:600}}"
    # ---------- scrollbars
    "::-webkit-scrollbar-track{background:transparent!important}"
    "[data-slot=\"scroll-area-scrollbar\"]{background:transparent!important}"
    "::-webkit-scrollbar-thumb,[data-slot=\"scroll-area-thumb\"]{background:rgba(100,96,148,.3)!important;border-radius:999px!important}"
    "::-webkit-scrollbar-thumb:hover,[data-slot=\"scroll-area-thumb\"]:hover{background:rgba(100,96,148,.5)!important}"
    # ---------- reduced motion: freeze to a calm still (beam hangs toward the left gutter while a turn runs)
    "@media (prefers-reduced-motion:reduce){"
    f"{AREA}::before,{AREA}::after,[data-slot=\"sidebar-inner\"]::after,[data-chat-header],[data-timeline-row-kind],[data-thread-item] [aria-busy],[data-slot=\"button\"],[data-slot=\"switch\"]{{animation:none!important;transition:none!important}}"
    f"{AREA}::after{{transform:rotate(-64deg)}}"
    + busy(f"{AREA}::after") + "{opacity:.5!important}"
    "[data-slot=\"sidebar-inner\"]::after{transform:translateX(30%)}"
    + busy("[data-chat-header]") + "{background-position:50% 100%!important}"
    "[data-timeline-row-kind=\"working\"],[data-thread-item] [aria-busy=\"true\"]{background-position:50% 0}"
    "[data-slot=\"composer-host\"]{transition:none!important}}"
)

theme = {"version": 1, "id": "fogbank", "name": "Fogbank", "appearance": "light", "accent": "#474c8a", "canvas": "#e8e7f0",
         "colors": colors, "css": css}
with open(os.path.join(HERE, "..", "fogbank.json"), "w") as fh:
    json.dump(theme, fh, ensure_ascii=False)
os.makedirs(os.path.join(HERE, "..", "assets"), exist_ok=True)
with open(os.path.join(HERE, "..", "assets", "lighthouse.svg"), "w") as fh:
    fh.write(preview_svg())
print("css chars:", len(css))
