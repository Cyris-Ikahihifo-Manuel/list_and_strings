# importing random module for the randomly selected animal

import random

# this 2D list will have an item in its list randomly selected

animals = [["Salmon", "Pollock", "Cod"],
           ["Parrot", "Duck", "Wren"],
           ["Camel", "Lion", "Tiger"]]

# if this goes as i expected, 10 animals will be randomly selected, if the animal is in list 1 it should print that the
# animal is a fish. if it comes from list 2, it should say that the animal is a bird and if the animal is from list 3 it
# should say that the animal is a mammal.

for i in range(10):
    rand_num = random.randint(0, len(animals) - 1)

    animal = animals[rand_num][random.randint(0, len(animals[rand_num]) - 1)]

    if animal in animals[0]:
        print('{} is a fish'.format(animal))
    elif animal in animals[1]:
        print('{} is a bird'.format(animal))
    else:
        print('{} is a mammal'.format(animal))
