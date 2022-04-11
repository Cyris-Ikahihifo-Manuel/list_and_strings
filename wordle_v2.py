# this list is before the main program because of the amount of words there were

words = ["""nabbed
naff
naivete
nanoamperes
nanocode
nanoelectronics
nanoscience
nanotube
Napier
Napoleon
napped
nappies
narcotics
Narnia
narration
narratives
Nassau
nastiness
nasturtiums
nationalist
natty
naturalness
naturist
naturists
naughtily
navels
naysayers
nebulous
neccessitated
necrophiliac
nectar
neglecting
negligibly
negotiability
negotiable
negotiated
negro
negroes
neigbourhood
neighbors
NEMS
neophytes
nerving
Nescafe
nestings
Netscape
Netware
neurologic
neurologically
neurologist
neurologists
neuropsychology
neurosciences
neurosurgery
neutralistic
neutralistically
neutrally
neutrals
Nevin
newscaster
Niagara
Nicaragua
Nicaraguan
Nichola
Nicholas
Nichole
nick
Nickelodeon
Nicki
Nicklaus
nicknaming
Nicolai
Nicolaides
Nicorette
nicotine
nieces
Nigel
Niger
Nigeria
Nigerian
niggard
niggardly
niggards
nigger
niggle
niggled
niggles
nigglies
nigh
nightdress
nightlies
nightmarish
Nijinsky
Nikita
Nikki
Nikolai
Nikolay
Nikon
Nile
Niles
Nilsson
Nimitz
Nina
Nintendo
Nisa
Nissan
nitrates
nitric
nitride
nitrogen
Niven
nixing
Nixon
nobbe
nobbers
nobbled
nobby
noblemen
nobleminded
noblemindedly
noisemaking
noisome
noisomely
Nolan
nomadicity
nominals
nominator
nonadjacent
nonambiguity
nonatomically
nonbibliographic
nonces
nonchalantly
noncollated
noncompliant
nonconsecutive
nonconvergence
noncorrelated
nondeclarative
nondestructive
nondisruptive
nonelected
nonexecutable
nonfunctional
nongraphical
nonhierarchical
nonhinted
nonignorable
nonincreasing
nonintegral
nonintegrated
noninteractive
noninteroperable
nonjoined
nonlinearity
nonliteral
nonmodularity
nonnative
nonnatural
nonnegated
nonoperational
nonoptimizing
nonpartisan
nonprogressive
nonpublished
nonrenewable
nonsensically
nonsequentially
nonsteroidal
nontechnical
nonterminated
nontheless
nonthreatening
nontransactional
nontranslucencies
nontranslucency
nooks
Noriega
normatively
nosedived
Nostromo
notables
notaries
notepad
nothings
novelists
Novell
Noyce
nozzles
NT
nuance
nuked
numb
numbing
numeration
numerators
numerologist
nuptial
nuptially
nurk
Nurnberg
nuzzled
Nycom"""]

# importing the random module so that every word is different from the previous one

import random

# guesses is equal to word, which is equal to guess which equals 0 because they're all undefined at the moment

guesses = word = guess = 0
letters = []

# response function that reiterates itself until the user has input something within the parameter 'boundaries' and
# the user for input displaying the message parameter. If the user doesnt input a value that isn't equal to the parameter
# boundaries than the program should display the parameter error_message


def response(message, boundaries, error_messages):
    while True:
        print()
        answer = input(message).upper().strip()
        if answer == boundaries:
            return answer
        else:
            text(error_messages)


# text function to make things easier to read when the program is running


def text(message):
    print()
    print(message)


# this should reiterate itself until the variable word has randomised itself into a string with 6 characters

while len(word) != 6:
    word = random.choice(words)

# main word guessing game (if the user enters too much or too little it shouldn't count as a guess, entering ? should
# display what the user's done)

while guess != word:

