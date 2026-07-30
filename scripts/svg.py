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
    """Create the streak stats SVG card."""
    
    font_pro = "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="620" height="96" viewBox="0 0 620 96" fill="none">
<rect x="1" y="1" width="618" height="94" rx="10" fill="#ffffff" stroke="#d0d7de"/>

<line x1="310" y1="16" x2="310" y2="80" stroke="#d8dee4" stroke-width="1"/>

<text x="34" y="44" font-size="34" font-family="{font_pro}" font-weight="700" fill="#3f4750">{current_streak}</text>
<text x="34" y="64" font-size="12" font-family="{font_pro}" fill="#a5abb3">Current streak</text>
<text x="34" y="80" font-size="11" font-family="{font_pro}" fill="#a5abb3">{current_range}</text>

<text x="344" y="44" font-size="34" font-family="{font_pro}" font-weight="700" fill="#3f4750">{longest_streak}</text>
<text x="344" y="64" font-size="12" font-family="{font_pro}" fill="#a5abb3">Longest streak</text>
<text x="344" y="80" font-size="11" font-family="{font_pro}" fill="#a5abb3">{longest_range}</text>

</svg>'''