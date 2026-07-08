import requests

USERNAME = "saichintamani"

HIGH_VALUE_PROJECTS = [
    "CIOS----Saai",
    "Lumina-",
    "portfolio",
    "MediReach-AI",
    "PrepMind-Ai"
]


def fetch_repositories():
    url = f"https://api.github.com/users/{USERNAME}/repos"
    response = requests.get(url)

    if response.status_code != 200:
        return []

    return response.json()


def calculate_priority(repo):

    score = 0

    if repo["name"] in HIGH_VALUE_PROJECTS:
        score += 50

    if repo["description"]:
        score += 20

    if repo["language"]:
        score += 10

    score += 20

    return score


def main():

    repos = fetch_repositories()

    ranked = []

    for repo in repos:

        score = calculate_priority(repo)

        ranked.append({
            "name": repo["name"],
            "score": score
        })

    ranked = sorted(
        ranked,
        key=lambda x: x["score"],
        reverse=True
    )

    print("\n=== CIOS CAREER ENGINE ===\n")

    print("Top Priority Projects:\n")

    for project in ranked[:5]:
        print(
            f"{project['name']} --> {project['score']}"
        )


if __name__ == "__main__":
    main()