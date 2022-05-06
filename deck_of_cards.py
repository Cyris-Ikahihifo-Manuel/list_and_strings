# importing random module to shuffle the cards and choice

import random

# card function


def shuffle_cards():
    suits = ['♥', '♦', '♣', '♠']
    cards_value = []

    # this will add 13 values within the cards_value list

    for i in range(13):
        cards_value.append(i + 1)

    deck = []

    for suit in suits:
        for _ in cards_value:
            if cards_value == 1:
                cards_value = 'A'
            elif cards_value == 11:
                cards_value = 'J'
            elif cards_value == 12:
                cards_value = 'Q'
            elif cards_value == 13:
                cards_value = 'K'
            deck.append(str(random.choice(cards_value)) + random.choice(suit))
    return deck


# the variables player1 and player2 call the shuffle_cards function but are on different lines of code because
# if they would equal the same (they store the same lists or randomisation of 'cards')

deck_of_cards = shuffle_cards()
player1 = deck_of_cards[0:len(deck_of_cards) // 2]
player2 = deck_of_cards[len(deck_of_cards) // 2: len(deck_of_cards)]


print(player1)
print(len(player1))
print(player2)
print(len(player2))
