import requests

USERNAME = "saichintamani"

url = f"https://api.github.com/users/{USERNAME}/repos"

response = requests.get(url)

if response.status_code != 200:
    print("Failed to fetch repositories")
    exit()

repos = response.json()

print("\n=== GITHUB REPOSITORIES ===\n")

for repo in repos:
    print(f"Name: {repo['name']}")
    print(f"Language: {repo['language']}")
    print(f"Stars: {repo['stargazers_count']}")
    print(f"Forks: {repo['forks_count']}")
    print(f"Updated: {repo['updated_at']}")
    print(f"Description: {repo['description']}")
    print("-" * 50)