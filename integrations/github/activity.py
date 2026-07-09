import requests

USERNAME = "saichintamani"


def get_github_activity():

    url = f"https://api.github.com/users/{USERNAME}/events/public"

    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to fetch activity")
        return

    events = response.json()

    print("\n=== GITHUB ACTIVITY ===\n")

    print(f"Recent Events Found: {len(events)}")

    if len(events) > 0:
        print("\nLatest Event:")

        latest = events[0]

        print(
            f"Type: {latest['type']}"
        )

        print(
            f"Repo: {latest['repo']['name']}"
        )

        print(
            f"Created: {latest['created_at']}"
        )


if __name__ == "__main__":
    get_github_activity()