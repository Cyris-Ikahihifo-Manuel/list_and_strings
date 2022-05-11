# importing random module in order to randomise names (just because i cant think of names)

import random

# letters list (letters list for the random module because i cant think of names)

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"]

# first_names, surnames and year_level lists to store the student's first name, their surname and when they started in
# which year. the reason i made it why they are all empty lists (and should be equal to each other) instead of equalling
# each other (instead of first_names = surnames = year_level = []) is because this does not work out on how i expect
# the program to run

first_names = []
surnames = []
year_level = []

# this is to generate random names (their names arent going to be pretty)

student_count = random.randint(10, 50)

for i in range(student_count):
    first_names.append("")
    for _ in range(random.randint(3, 8)):
        first_names[i] = first_names[i] + random.choice(letters)
    surnames.append("")
    for _ in range(random.randint(5, 8)):
        surnames[i] = surnames[i] + random.choice(letters)
    year_level.append(random.randint(2018, 2022))

# the question function should reiterate itself until the user has input something other than an empty string


def question(message):
    while True:
        print()
        answer = input(message)
        if len(answer) != 0:
            return answer
        else:
            text("Error, enter something")


# text function to make things easier to read when the program is running


def text(message):
    print()
    print(message)


# main program running

not_finished = True

while not_finished:
    response = question("Y/N Are you finished with learner year checker?").lower()
    if response == "y":
        not_finished = False
    elif response == "n":
        response = question("Enter a student's username")
    else:
        text("Error, enter either Y/N")
