"""
CP1404 - Practical 03
Password Check
"""

MINIMUM_PASSWORD_LENGTH = 10


def main():
    """Check password and display in asterisks"""
    password = get_password()
    print_asterisks(password)


def get_password():
    """Ask for a password of minimum password length or longer"""
    password = input("Password: ")
    while len(password) < MINIMUM_PASSWORD_LENGTH:
        print("Invalid password")
        password = input("Password: ")
    return password


def print_asterisks(string):
    """Print asterisks of string length"""
    print("*" * len(string))


main()
