def calculate_internship_readiness():

    github_score = 85
    project_score = 90
    portfolio_score = 80
    consistency_score = 75
    dsa_score = 60

    readiness = (
        github_score +
        project_score +
        portfolio_score +
        consistency_score +
        dsa_score
    ) / 5

    print("\n=== INTERNSHIP READINESS ENGINE ===\n")

    print(f"Readiness Score: {readiness:.0f}%\n")

    print("Strong Areas:")
    print("✅ Projects")
    print("✅ GitHub Activity")
    print("✅ Portfolio Development")

    print("\nWeak Areas:")
    print("⚠ DSA Practice")
    print("⚠ Competitive Programming")

    print("\nRecommended Actions:")
    print("1. Solve 3 LeetCode problems")
    print("2. Maintain GitHub streak")
    print("3. Build CIOS daily")
    print("4. Publish one project update")


if __name__ == "__main__":
    calculate_internship_readiness()