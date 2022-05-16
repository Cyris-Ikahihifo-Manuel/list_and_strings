# this 2D list has 3 empty lists which will be populated later according to the step by step plan (this will store and
# later display the 'account', 'username' and 'password')

passwords = [[], [], []]

# the question list

question = [['Enter an email account:', 'Enter a username:', 'Enter a password'], 'Enter an account to see their '
                                                                                  'password']

# text function to make things aesthetically pleasing


def text(message):
    print()
    print(message)


# if this goes according to the step by step plan it should display a menu of options (1-4), entering 1 should
# reiterate itself 3 times displaying the question list as input. It should reiterate itself until the user has
# entered a value (not as an empty string). It should also repeat itself 3 times going through the list in the 2D
# list questions. If the user entered 2 it shouldn't reiterate itself.

not_finished = True

while not_finished:
    text("""Lists of options
    1: make a new account
    2: display a password for an account
    3: display list of accounts
    4: you're done with program""")
    response = input()
    if response.isdigit():
        if 1 >= int(response) <= 4:
            if response == '1':
                for i in range(3):
                    while len(response) >= 1:
                        response = input(question[0][i]).strip()
                        passwords[i].append(response)
            elif response == '2':
                response = input(question[1])
                account_exists = False
                for account in passwords[0]:
                    if response == account:
                        account_exists = True
                if account_exists:
                    text("The password for account {] is {}".format(response, passwords[2][passwords[0].index(response)]))
                else:
                    text("Error, {} doesn't exist as an account".format(response))
            elif response == '3':
                text('List of accounts')
                print()
                for i in range(len(passwords[0])):
                    print('{} / {} / {}'.format(passwords[0][i], passwords[1][i], passwords[2][i]))
            else:
                text('Goodbye!')
                not_finished = False
        else:
            text('Error, enter a whole number between 1 and 4')
    else:
        text('Error, enter a whole number between 1 and 4')
