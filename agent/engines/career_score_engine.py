def calculate_career_score():

    github_score = 80
    portfolio_score = 70
    project_score = 90

    score = (
        github_score +
        portfolio_score +
        project_score
    ) / 3

    print("\n=== CAREER SCORE ===\n")
    print(f"Career Score: {score:.0f}/100")


if __name__ == "__main__":
    calculate_career_score()