from dashboard import display_dashboard
from profile import display_profile


def welcome():
    print("=" * 50)
    print("          STUDENT LEARNING PORTAL")
    print("=" * 50)


def main():
    welcome()

    print("\n1. View Profile")
    print("2. View Dashboard")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        display_profile()
    elif choice == "2":
        display_dashboard()
    elif choice == "3":
        print("Thank you for using the Student Learning Portal.")
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()