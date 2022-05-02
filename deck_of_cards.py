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
        for cards in cards_value:
            if cards_value == 1:
                cards_value = 'A'
            elif cards_value == 11:
                cards_value = 'J'
            elif cards == 12:
                cards_value = 'Q'
            elif cards == 13:
                cards_value = 'K'
            deck.append(str(cards_value) + random.choice(suit))
    return deck


# player1, player2 are equal to each other since they're blank lists by default and will be used later on in the code

player1 = player2 = []

player1 = shuffle_cards()
player2 = shuffle_cards()
