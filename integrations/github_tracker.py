import requests

USERNAME = "saichintamani"


def get_profile():
    url = f"https://api.github.com/users/{USERNAME}"

    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to fetch profile")
        return

    data = response.json()

    print("\n=== GitHub Profile ===")
    print("Name:", data.get("name"))
    print("Followers:", data.get("followers"))
    print("Following:", data.get("following"))
    print("Public Repos:", data.get("public_repos"))
    print("Profile URL:", data.get("html_url"))


if __name__ == "__main__":
    get_profile()