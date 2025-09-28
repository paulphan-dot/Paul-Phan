
def main():
    """Menu-driven program to work with a score."""
    score = get_valid_score()
    choice = get_menu_choice()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_status(score))
        elif choice == "S":
            print("*" * int(score))
        else:
            print("Invalid choice")
        choice = get_menu_choice()
    print("Farewell!")


def get_menu_choice():
    """Display menu and get the user's menu choice."""
    MENU_STRING = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"
    print(MENU_STRING)
    choice = input(">>> ").upper()
    return choice


def get_valid_score():
    """Get a valid score (0-100 inclusive)."""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def determine_status(score):
    """Determine the status of a given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
