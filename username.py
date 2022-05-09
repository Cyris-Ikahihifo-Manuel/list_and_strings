# import random module for the random names

import random

# letters list to come up with names since i cant think of any names

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']

# bunch of lists that will keep track of a "student's" first name, surname and year level

first_names = surnames = year_level = []
not_finished = True

# this first for loop should repeat it between 100 to 200 times, the second and third for loop should randomise the
# student's name and the random.randint should randomise the student's year level


for student in range(2):
    first_names.append("")
    surnames.append("")
    for i in range(random.randint(3, 20)):
        first_names[student] = str(first_names[student]) + random.choice(letter)
    for i in range(random.randint(3, 20)):
        surnames[student] = surnames[student] + random.choice(letter)
    year_level.append(random.randint(9, 13))

print(len(first_names))
print(len(surnames))
print(len(year_level))
print(first_names)
print(surnames)
print(year_level)

# question_function that will reiterate itself until the user has input a valid value. If the user inputs an invalid
# value the function should display the error_message parameter


def question_func(question, error_message):
    while True:
        print()
        answer = input(question).lower().strip()
        if len(answer) == 0:
            text("Error, " + error_message)
        else:
            return answer


# text function, not for any other purpose than aesthetics


def text(message):
    print()
    print(message)


# main program running


while not_finished:
    response = question_func("Enter a student's username (enter ? for help)", "enter a student's username")
    if response == "?":
        response = question_func("Do you need to see their usernames?", "enter either y/n")
        if response == "y":
            text("List of students usernames")
            print()
            for student in first_names:
                print(str(year_level[first_names.index(student)]) + surnames[first_names.index(student)].title() + student[0].upper())
    else:
        text("That username doesnt exist")
