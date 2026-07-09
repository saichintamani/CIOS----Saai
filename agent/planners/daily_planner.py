def create_daily_plan():

    tasks = [

        {
            "platform": "GitHub",
            "task": "Improve CIOS Architecture",
            "priority": "HIGH"
        },

        {
            "platform": "Portfolio",
            "task": "Update AI Engineer Portfolio",
            "priority": "MEDIUM"
        },

        {
            "platform": "Learning",
            "task": "Study Docker Fundamentals",
            "priority": "HIGH"
        }
    ]

    print("\n=== CIOS DAILY PLAN ===\n")

    for i, task in enumerate(tasks, start=1):

        print(
            f"{i}. [{task['priority']}] "
            f"{task['platform']} -> "
            f"{task['task']}"
        )


if __name__ == "__main__":
    create_daily_plan()