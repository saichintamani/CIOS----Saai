import requests
from datetime import datetime, timezone

USERNAME = "saichintamani"


def check_github_status():

    url = f"https://api.github.com/users/{USERNAME}/events/public"

    response = requests.get(url)

    if response.status_code != 200:
        print("GitHub API Error")
        return

    events = response.json()

    latest = events[0]

    latest_time = datetime.fromisoformat(
        latest["created_at"].replace("Z", "+00:00")
    )

    now = datetime.now(timezone.utc)

    hours = (
        now - latest_time
    ).total_seconds() / 3600

    print("\n=== GITHUB STREAK ENGINE ===\n")

    print(f"Latest Activity: {latest['type']}")
    print(f"Repository: {latest['repo']['name']}")
    print(f"Hours Since Activity: {hours:.1f}")

    if hours < 24:
        print("Status: SAFE ✅")
    else:
        print("Status: AT RISK ⚠️")


if __name__ == "__main__":
    check_github_status()