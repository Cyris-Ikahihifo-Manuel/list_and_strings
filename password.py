# text function to make things easier to read when the program is running


def text(message):
    print()
    print(message)


# this program should reiterate itself until the user has input a password that has at least 8 characters and has at
# least one number

not_met = True

while not_met:
    print()
    password = input("Enter a password (password must have at least 8 characters and 1 number)").strip()
    if len(password) >= 8:
        for character in password:
            if character.isdigit():
                not_met = False
        if not_met:
            text("This password doesn't have a number")
    else:
        if len(password) < 8:
            text("This password is too short")
