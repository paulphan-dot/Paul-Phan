MIN_LENGTH = 4


def main():
    """Get and print password using functions."""
    password = get_password()
    print_asterisks(password)


def get_password():
    """Get password to ensure it meets the min length requirement."""
    password = input("Enter password: ")
    while len(password) < MIN_LENGTH:
        print("Password too short")
        password = input("Enter password: ")
    return password


def print_asterisks(password):
    """Print as many asterisks as there are character"""
    print('*' * len(password))

main()
