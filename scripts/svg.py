def create_contributions_svg(contributions):

    total = contributions["totalContributions"]
    weeks = contributions["weeks"]

    active_days = 0
    weekly_totals = []

    for week in weeks:

        week_total = 0

        for day in week["contributionDays"]:

            count = day["contributionCount"]

            week_total += count

            if count > 0:
                active_days += 1

        weekly_totals.append(week_total)

    best_week = max(weekly_totals)

    highest = max(weekly_totals)

    if highest == 0:
        highest = 1

    card_width = 760
    card_height = 180
    
    graph_padding_x = 30
    start_x = graph_padding_x
    end_x = card_width - graph_padding_x
    graph_width = end_x - start_x
    
    baseline = 175
    graph_height = 30

    step = graph_width / (len(weekly_totals) - 1)

    points = []
    for i, value in enumerate(weekly_totals):
        x = start_x + i * step
        y = baseline - value / highest * graph_height
        points.append((x, y))

    line_path = ""
    for i, (x, y) in enumerate(points):
        if i == 0:
            line_path += f"M {x:.2f} {y:.2f} "
        else:
            line_path += f"L {x:.2f} {y:.2f} "

    area_path = f"M {points[0][0]:.2f} {baseline:.2f} "
    for x, y in points:
        area_path += f"L {x:.2f} {y:.2f} "
    area_path += f"L {points[-1][0]:.2f} {baseline:.2f} Z"

    last_x, last_y = points[-1]

    font_pro = "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"

    return f"""<svg xmlns="http://www.w3.org/2000/svg"
width="{card_width}"
height="{card_height}"
viewBox="0 0 {card_width} {card_height}">

<rect
x="1"
y="1"
width="{card_width - 2}"
height="{card_height - 2}"
rx="10"
fill="#ffffff"
stroke="#d0d7de"/>

<text
x="35"
y="55"
font-size="54"
font-family="{font_pro}"
font-weight="700"
fill="#3f4750">{total}</text>

<text
x="35"
y="82"
font-size="18"
font-family="{font_pro}"
fill="#a5abb3">Contributions in the last year</text>

<text
x="720"
y="45"
text-anchor="end"
font-size="22"
font-family="{font_pro}"
font-weight="700"
fill="#3f4750">{active_days}</text>

<text
x="720"
y="66"
text-anchor="end"
font-size="16"
font-family="{font_pro}"
fill="#a5abb3">Active days</text>

<text
x="720"
y="105"
text-anchor="end"
font-size="22"
font-family="{font_pro}"
font-weight="700"
fill="#3f4750">{best_week}</text>

<text
x="720"
y="126"
text-anchor="end"
font-size="16"
font-family="{font_pro}"
fill="#a5abb3">Best week</text>

<path
d="{area_path}"
fill="#f0f2f5"
stroke="none"/>

<path
d="{line_path}"
fill="none"
stroke="#3f4750"
stroke-width="1.5"
stroke-linecap="round"
stroke-linejoin="round"/>

<circle
cx="{last_x:.2f}"
cy="{last_y:.2f}"
r="3"
fill="#3f4750"
stroke="#ffffff"
stroke-width="2"/>

</svg>
"""


def create_streak_svg(current_streak, current_range, longest_streak, longest_range):
    """Create the streak stats SVG card with subtle animations."""
    
    font_pro = "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="620" height="96" viewBox="0 0 620 96" fill="none">
<rect x="1" y="1" width="618" height="94" rx="10" fill="#ffffff" stroke="#d0d7de"/>

<!-- Vertical divider -->
<line x1="310" y1="16" x2="310" y2="80" stroke="#d8dee4" stroke-width="1"/>

<!-- Current Streak -->
<g opacity="0">
    <animate attributeName="opacity" from="0" to="1" begin="0.1s" dur="0.4s" fill="freeze"/>
    <text x="34" y="44" font-size="34" font-family="{font_pro}" font-weight="700" fill="#3f4750">{current_streak}</text>
    <text x="34" y="64" font-size="12" font-family="{font_pro}" fill="#a5abb3">Current streak</text>
    <text x="34" y="80" font-size="11" font-family="{font_pro}" fill="#a5abb3">{current_range}</text>
</g>

<!-- Longest Streak -->
<g opacity="0">
    <animate attributeName="opacity" from="0" to="1" begin="0.25s" dur="0.4s" fill="freeze"/>
    <text x="344" y="44" font-size="34" font-family="{font_pro}" font-weight="700" fill="#3f4750">{longest_streak}</text>
    <text x="344" y="64" font-size="12" font-family="{font_pro}" fill="#a5abb3">Longest streak</text>
    <text x="344" y="80" font-size="11" font-family="{font_pro}" fill="#a5abb3">{longest_range}</text>
</g>

</svg>'''

def create_languages_svg(sorted_langs, total_bytes, lang_repos):
    """Create the language stats SVG card with unified line color bars."""
    
    font_pro = "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    
    # Unified bar color — matches the graph line
    bar_color = "#3f4750"
    
    # Take top 5 languages
    top_langs = sorted_langs[:5]
    
    # Card dimensions
    card_width = 620
    card_height = 220
    
    # Bar settings
    bar_max_width = 180
    bar_height = 6
    
    # Build left column (By Bytes)
    left_bars = ""
    for i, (name, data) in enumerate(top_langs):
        y = 145 + i * 24
        pct = round(data["size"] / total_bytes * 100)
        bar_width = max(4, pct / 100 * bar_max_width)
        
        left_bars += f'''
<text x="34" y="{y}" font-size="12" font-family="{font_pro}" fill="#424a53">{name.lower()}</text>
<rect x="100" y="{y - 9}" width="{bar_width}" height="{bar_height}" rx="3" fill="{bar_color}"/>
<text x="290" y="{y}" text-anchor="end" font-size="12" font-family="{font_pro}" fill="#8c959f">{pct}%</text>'''
    
    # Build right column (By Repos)
    right_bars = ""
    max_repos = max(lang_repos.values()) if lang_repos else 1
    for i, (name, data) in enumerate(top_langs):
        y = 145 + i * 24
        count = lang_repos.get(name, 0)
        bar_width = max(4, count / max_repos * bar_max_width)
        
        right_bars += f'''
<text x="344" y="{y}" font-size="12" font-family="{font_pro}" fill="#424a53">{name.lower()}</text>
<rect x="410" y="{y - 9}" width="{bar_width}" height="{bar_height}" rx="3" fill="{bar_color}"/>
<text x="600" y="{y}" text-anchor="end" font-size="12" font-family="{font_pro}" fill="#8c959f">{count}</text>'''
    
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{card_width}" height="{card_height}" viewBox="0 0 {card_width} {card_height}" fill="none">
<rect x="1" y="1" width="{card_width - 2}" height="{card_height - 2}" rx="10" fill="#ffffff" stroke="#d0d7de"/>

<!-- Title -->
<text x="34" y="35" font-size="14" font-family="{font_pro}" font-weight="600" fill="#3f4750" letter-spacing="1">STATS</text>
<line x1="34" y1="42" x2="586" y2="42" stroke="#d8dee4" stroke-width="1"/>

<!-- Vertical divider -->
<line x1="310" y1="55" x2="310" y2="200" stroke="#d8dee4" stroke-width="1"/>

<!-- Left header -->
<text x="34" y="120" font-size="9" font-family="{font_pro}" fill="#8c959f" font-weight="600" letter-spacing="1">BY BYTES</text>

<!-- Left bars -->
{left_bars}

<!-- Right header -->
<text x="344" y="120" font-size="9" font-family="{font_pro}" fill="#8c959f" font-weight="600" letter-spacing="1">BY REPOS</text>

<!-- Right bars -->
{right_bars}

</svg>'''