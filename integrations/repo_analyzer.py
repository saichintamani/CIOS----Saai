import requests
from datetime import datetime

USERNAME = "saichintamani"

url = f"https://api.github.com/users/{USERNAME}/repos"

repos = requests.get(url).json()

print("\n=== CIOS REPOSITORY ANALYSIS ===\n")

for repo in repos:

    score = 0

    if repo["description"]:
        score += 20

    if repo["language"]:
        score += 20

    if repo["stargazers_count"] > 0:
        score += 20

    if repo["forks_count"] >= 0:
        score += 10

    updated = repo["updated_at"][:10]

    score += 30

    print(f"\nRepository: {repo['name']}")
    print(f"Score: {score}/100")

    if score < 50:
        print("Recommendation: Improve immediately")

    elif score < 80:
        print("Recommendation: Moderate improvement")

    else:
        print("Recommendation: Strong repository")

    print("-" * 40)