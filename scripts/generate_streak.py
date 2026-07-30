#!/usr/bin/env python3
from github_api import fetch_contribution_days
from svg import create_streak_svg
from datetime import datetime

all_days = fetch_contribution_days()

# Calculate current streak
current_streak = 0
for day in reversed(all_days):
    if day["contributionCount"] > 0:
        current_streak += 1
    else:
        break

# Calculate longest streak
longest_streak = 0
temp_streak = 0
for day in all_days:
    if day["contributionCount"] > 0:
        temp_streak += 1
        longest_streak = max(longest_streak, temp_streak)
    else:
        temp_streak = 0

# Format dates for current streak
if current_streak > 0:
    streak_end = datetime.strptime(all_days[-1]["date"], "%Y-%m-%d")
    streak_start = datetime.strptime(all_days[-current_streak]["date"], "%Y-%m-%d")
    current_range = f"{streak_start.strftime('%b %d').lower()} – {streak_end.strftime('%b %d').lower()}"
else:
    current_range = "no current streak"

# Find longest streak date range
longest_range = "no longest streak"
if longest_streak > 0:
    temp_streak = 0
    best_start = 0
    for i, day in enumerate(all_days):
        if day["contributionCount"] > 0:
            temp_streak += 1
            if temp_streak == longest_streak:
                best_start = i - longest_streak + 1
                break
        else:
            temp_streak = 0
    
    start_date = datetime.strptime(all_days[best_start]["date"], "%Y-%m-%d")
    end_date = datetime.strptime(all_days[best_start + longest_streak - 1]["date"], "%Y-%m-%d")
    longest_range = f"{start_date.strftime('%b %d').lower()} – {end_date.strftime('%b %d').lower()}"

svg = create_streak_svg(current_streak, current_range, longest_streak, longest_range)

with open("assets/streak.svg", "w", encoding="utf-8") as file:
    file.write(svg)

print("Streak SVG generated!")