# importing random module since i cant think of 5 numerical scores

import random

# the lists that'll be used later on

names = ['cyris', 'a', 'b', 'c', 'd']
scores = []

for i in range(5):
    scores.append(random.randint(-100, 100))

# text function to make things easier to read when the program is running


def text(message):
    print()
    print(message)


# just sorting out the scores list in ascending order so that i can have the highest value
scores.sort()

# printing the 3rd item in the lists. i put 2 within the brackets since the index in items start from 0.
text(names[2])
text(scores[2])

# printing the lists in general to further prove that an indexes start from 0
text(names)
text(scores)

# using both the names and scores list in a print statement
text("Leaderboard")
for score in scores:
    print()
