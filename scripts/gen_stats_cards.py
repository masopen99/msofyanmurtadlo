import json

BG = "#0A101F"
TITLE = "#22D3EE"
TEXT = "#ffffff"
ICON = "#10B981"
BORDER = "#22D3EE"

with open("scripts/computed.json") as f:
    computed = json.load(f)

STATS = {
    "commits": 152,
    "issues": 8,
    "prs": 0,
    "repos": computed["total_repos"],
    "stars": computed["total_stars"],
}

def stats_card():
    rows = [
        ("Total Stars", STATS["stars"]),
        ("Total Commits", STATS["commits"]),
        ("Total PRs", STATS["prs"]),
        ("Total Issues", STATS["issues"]),
        ("Public Repos", STATS["repos"]),
    ]
    row_h = 30
    top = 55
    height = top + row_h * len(rows) + 20
    width = 450

    body = []
    for i, (label, val) in enumerate(rows):
        y = top + i * row_h
        body.append(f'''
        <g transform="translate(25, {y})">
          <circle cx="4" cy="-5" r="4" fill="{ICON}" />
          <text x="18" y="0" font-family="'Segoe UI', Ubuntu, Sans-Serif" font-size="14" fill="{TEXT}">{label}:</text>
          <text x="{width-50}" y="0" font-family="'Segoe UI', Ubuntu, Sans-Serif" font-size="14" font-weight="600" fill="{TITLE}" text-anchor="end">{val}</text>
        </g>''')

    svg = f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
  <rect x="0.5" y="0.5" rx="8" width="{width-1}" height="{height-1}" fill="{BG}" stroke="{BORDER}" stroke-opacity="0.35"/>
  <text x="25" y="30" font-family="'Segoe UI', Ubuntu, Sans-Serif" font-size="16" font-weight="700" fill="{TITLE}">Muhammad Sofyan Murtadlo's GitHub Stats</text>
  {"".join(body)}
</svg>'''
    return svg

def top_langs_card():
    langs = computed["top_langs"]
    width = 450
    bar_y = 55
    bar_h = 10
    row_h = 24
    top = bar_y + bar_h + 20
    height = top + row_h * len(langs) + 15

    # proportional bar
    bar_segments = []
    x = 25
    bar_w = width - 50
    for lang in langs:
        seg_w = bar_w * (lang["pct"] / 100)
        bar_segments.append(f'<rect x="{x:.1f}" y="{bar_y}" width="{seg_w:.1f}" height="{bar_h}" fill="{lang["color"]}" />')
        x += seg_w

    legend = []
    for i, lang in enumerate(langs):
        y = top + i * row_h
        legend.append(f'''
        <g transform="translate(25, {y})">
          <circle cx="5" cy="-5" r="5" fill="{lang["color"]}" />
          <text x="18" y="0" font-family="'Segoe UI', Ubuntu, Sans-Serif" font-size="13" fill="{TEXT}">{lang["name"]}</text>
          <text x="{width-50}" y="0" font-family="'Segoe UI', Ubuntu, Sans-Serif" font-size="13" fill="{TITLE}" text-anchor="end">{lang["pct"]}%</text>
        </g>''')

    svg = f'''<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
  <rect x="0.5" y="0.5" rx="8" width="{width-1}" height="{height-1}" fill="{BG}" stroke="{BORDER}" stroke-opacity="0.35"/>
  <text x="25" y="30" font-family="'Segoe UI', Ubuntu, Sans-Serif" font-size="16" font-weight="700" fill="{TITLE}">Most Used Languages</text>
  <rect x="25" y="{bar_y}" width="{bar_w}" height="{bar_h}" rx="5" fill="#1c2333" />
  <clipPath id="clip"><rect x="25" y="{bar_y}" width="{bar_w}" height="{bar_h}" rx="5" /></clipPath>
  <g clip-path="url(#clip)">{"".join(bar_segments)}</g>
  {"".join(legend)}
</svg>'''
    return svg

with open("assets/stats-card.svg", "w") as f:
    f.write(stats_card())

with open("assets/top-langs.svg", "w") as f:
    f.write(top_langs_card())

print("done")
