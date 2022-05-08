# import random module for the random names

import random

# letters list to come up with names since i cant think of any names

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']

# bunch of list names

first_names = []
surnames = []
year_level = []

# this first for loop should repeat it between 100 to 200 times, the second and third for loop should randomise the
# student's name and the random.randint should randomise the student's year level

for student in range(random.randint(50, 100)):
    first_names.append("")
    surnames.append("")
    for i in range(random.randint(3, 20)):
        first_names[student] = first_names[student] + random.choice(letter)
    for i in range(random.randint(3, 20)):
        surnames[student] = surnames[student] + random.choice(letter)
    year_level.append(random.randint(9, 13))

print(first_names)
print(surnames)
print(year_level)
