def calculate_overall_progress(courses):
    total = sum(progress for _, progress in courses)
    return total // len(courses)


def display_dashboard():
    print("\n========== LEARNING DASHBOARD ==========")
    print("Keep learning and improving every day!")

    courses = [
        ("Python Programming", 90),
        ("Object-Oriented Programming", 80),
        ("Git and GitHub", 75)
    ]

    for course, progress in courses:
        print(f"- {course}: {progress}% complete")

    overall = calculate_overall_progress(courses)

    print("-" * 42)
    print(f"Overall Progress: {overall}%")
    print("=" * 42)