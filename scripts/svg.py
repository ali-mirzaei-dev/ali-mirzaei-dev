def create_svg(contributions):

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

    start_x = 220
    graph_width = 430
    graph_height = 55
    baseline = 120

    step = graph_width / (len(weekly_totals) - 1)

    graph = ""

    for i, value in enumerate(weekly_totals):

        x = start_x + i * step
        y = baseline - value / highest * graph_height

        if i == 0:
            graph += f"M {x:.2f} {y:.2f} "
        else:
            graph += f"L {x:.2f} {y:.2f} "

    return f"""
<svg xmlns="http://www.w3.org/2000/svg"
width="760"
height="180"
viewBox="0 0 760 180">

<rect
x="1"
y="1"
width="758"
height="178"
rx="10"
fill="#ffffff"
stroke="#d0d7de"/>

<text
x="35"
y="62"
font-size="54"
font-family="Arial"
font-weight="700"
fill="#24292f">{total}</text>

<text
x="35"
y="88"
font-size="18"
font-family="Arial"
fill="#57606a">contributions in the last year</text>

<text
x="720"
y="45"
text-anchor="end"
font-size="34"
font-family="Arial"
font-weight="700"
fill="#24292f">{active_days}</text>

<text
x="720"
y="66"
text-anchor="end"
font-size="16"
font-family="Arial"
fill="#57606a">active days</text>

<text
x="720"
y="108"
text-anchor="end"
font-size="34"
font-family="Arial"
font-weight="700"
fill="#24292f">{best_week}</text>

<text
x="720"
y="129"
text-anchor="end"
font-size="16"
font-family="Arial"
fill="#57606a">best week</text>

<path
d="{graph}"
fill="none"
stroke="#6e7781"
stroke-width="3"
stroke-linecap="round"
stroke-linejoin="round"/>

</svg>
"""