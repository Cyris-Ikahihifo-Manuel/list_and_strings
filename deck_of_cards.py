# importing random module to shuffle the cards and choice

import random

# card function

def shuffle_cards():
    suits = ['♥', '♦', '♣', '♠']
    cards_value = []

    # this will add 13 values within the cards_value list

    for i in range(13):
        card_value.append(i + 1)

    deck = []

    for suit in suits:
        for cards in card:
            if cards == 1:
                cards = 'A'
            elif cards == 11:
                cards = 'J'
            elif cards == 12:
                cards = 'Q'
            elif cards == 13:
                cards = 'K'
            deck.append(str(cards) + random.choice(suit))
    return deck

# player1, player2 are equal to each other since they're blank lists by default and will be used later on in the code

player1 = player2 = []

player1 = shuffle_cards()
player2 = shuffle_cards()
