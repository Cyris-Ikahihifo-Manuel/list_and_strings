# importing random module in order to randomise names (just because i cant think of names)

import random

# letters list (letters list for the random module because i cant think of names)

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"]

# first_names, surnames, year_level and usernames lists to store the student's first name, their surname and when they started in
# which year. the reason i made it why they are all empty lists (and should be equal to each other) instead of equalling
# each other (instead of first_names = surnames = year_level = []) is because this does not work out on how i expect
# the program to run

first_names = []
surnames = []
year_level = []

# text function to make things easier to read when the program is running


def text(message):
    print()
    print(message)


# the question function should reiterate itself until the user has input something other than an empty string


def question(message):
    while True:
        print()
        answer = input(message)
        if len(answer) != 0:
            return answer
        else:
            text("Error, enter something")


# this is to generate random names (their names arent going to be pretty) and the year_level.append is that way (with
# 2018 inside the brackets) because this is for the year 9 cohort (as said in the documents)

student_count = random.randint(10, 50)

for i in range(student_count):
    first_names.append("")
    for _ in range(random.randint(3, 8)):
        first_names[i] = first_names[i] + random.choice(letters)
    surnames.append("")
    for _ in range(random.randint(5, 8)):
        surnames[i] = surnames[i] + random.choice(letters)
    year_level.append("2018")


# this for loop should generate student usernames as i expected if done correctly

usernames = []

for i in range(student_count):
    usernames.append(year_level[i][2:4] + surnames[i].title() + first_names[i][0].upper())

# this part of the program is to test whether i have done it correctly

not_finished = True

print(usernames)
print(first_names)
print(surnames)
print(year_level)
