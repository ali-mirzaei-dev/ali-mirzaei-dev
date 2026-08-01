from github_api import fetch_contribution_days

days = fetch_contribution_days()

print(f"Total days: {len(days)}")
print(f"First day: {days[0]['date']}")
print(f"Last day: {days[-1]['date']}")

print("\nLast 15 days:")
for d in days[-15:]:
    print(f"{d['date']}: {d['contributionCount']} contributions")

# Simulate streak calc
current_streak = 0
for day in reversed(days):
    if day["contributionCount"] > 0:
        current_streak += 1
    else:
        break

print(f"\nCurrent streak calculated: {current_streak}")