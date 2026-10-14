"""Generate info-card.svg: a neofetch-style animated card for a GitHub profile README.

Usage:  python scripts/make_info_card.py          -> animated info-card.svg
        set STATIC=1 to emit a frozen frame for previews.
Edit the CONFIG block below, then re-run.
"""
import os
from xml.sax.saxutils import escape

# ---------------- CONFIG: edit these ----------------
TITLE = "gouransh@github"
ROWS = [
    ("Now",        "B.Tech IT @ JMIT Radaur (2027)"),
    ("Prev",       "Generative AI Intern @ IBM"),
    ("Focus",      "AI/ML engineering, LLM apps, Software engeineering"),
    ("Stack",      "Python, LangChain, RAG"),
    ("Cloud",      "Azure OpenAI, Google Cloud"),
    ("Backend",    "FastAPI, MongoDB, MCP"),
    ("Highlights", "LLM voice assitant 'JARVIS' "),
    ("",           "Agentic AI caterer platform"),
]
# ----------------------------------------------------

STATIC = os.environ.get("STATIC") == "1"
W = 490
LINE_H = 24
TOP = 62
H = TOP + LINE_H * len(ROWS) + 24
FONT = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
BG, BAR, FG, KEY, DIM = "#0d1117", "#161b22", "#c9d1d9", "#58a6ff", "#8b949e"

parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
    "<style>"
    f"text{{font-family:{FONT};font-size:14px}}"
    ".line{opacity:0;animation:in .5s ease forwards}"
    "@keyframes in{from{opacity:0;transform:translateX(-8px)}to{opacity:1;transform:none}}"
    "</style>",
    f'<rect width="{W}" height="{H}" rx="10" fill="{BG}" stroke="#30363d"/>',
    f'<path d="M0 10a10 10 0 0 1 10-10h{W-20}a10 10 0 0 1 10 10v22H0z" fill="{BAR}"/>',
    '<circle cx="20" cy="16" r="5" fill="#ff5f56"/>',
    '<circle cx="38" cy="16" r="5" fill="#ffbd2e"/>',
    '<circle cx="56" cy="16" r="5" fill="#27c93f"/>',
    f'<text x="{W/2}" y="21" text-anchor="middle" fill="{DIM}" font-size="12">{escape(TITLE)}</text>',
]


def line(y, delay, inner):
    style = "" if STATIC else f' class="line" style="animation-delay:{delay:.2f}s"'
    if STATIC:
        style = ' style="opacity:1"'
    parts.append(f'<g{style}>{inner}</g>')


line(TOP - 8, 0.2, f'<text x="24" y="{TOP-8}" fill="{KEY}" font-weight="bold">{escape(TITLE)}</text>')
line(TOP + 4, 0.35, f'<text x="24" y="{TOP+4}" fill="{DIM}">{"-" * len(TITLE)}</text>')

for i, (k, v) in enumerate(ROWS):
    y = TOP + 28 + i * LINE_H - 8
    key = f'<text x="24" y="{y}" fill="{KEY}" font-weight="bold">{escape(k)}</text>' if k else ""
    val = f'<text x="130" y="{y}" fill="{FG}">{escape(v)}</text>'
    line(y, 0.5 + i * 0.18, key + val)

parts.append("</svg>")

with open("info-card.svg", "w", encoding="utf-8") as f:
    f.write("\n".join(parts))
print("wrote info-card.svg")