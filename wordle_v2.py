# guesses is equal to word, which is equal to guess which equals 0 because they're all undefined at the moment

guesses = guess = 0
letters = hints = []

# response function that reiterates itself until the user has input something within the parameter 'boundaries' and
# the user for input displaying the message parameter. If the user doesnt input a value that isn't equal to the parameter
# boundaries than the program should display the parameter error_message


def response(message, error_messages):
    while True:
        print()
        answer = input(message).upper().strip()
        if len(answer) != 0:
            return answer
        else:
            text(error_messages)

# text function to make things easier to read when the program is running


def text(message):
    print()
    print(message)


# main word guessing game (if the user enters nothing it shouldn't count as a guess, entering ? should
# display what the user's done)

text("Welcome to word guesser")
word = response("Enter the word that someone has to guess", "Error, enter any word")

while guess != word or guesses == 5:
    guess = response("Guess what the word is", "Error, you must guess by answering")
    if guess == "?":
        text("List of hints")
        for hint in hints:
            text(hint)
    else:
        text("That was incorrect")
        guesses += 1
        hints.append(guess)
        if guesses == 1:
            text("The first letter of the word is {}".format(word[0]))
            hints.append("The first letter of the word is {}".format(word[0]))
        elif guesses == 3:
            text("The last letter of the word is {}".format(word[len(word) - 1]))
            hints.append("The last letter of the word is {}".format(word[len(word) - 1]))

if guess != word:
    text("Incorrect, you lose!")
else:
    text("Correct, you win!")
