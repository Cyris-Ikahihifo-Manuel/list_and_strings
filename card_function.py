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
            if cards == 1:
                card = 'A'
            elif cards == 11:
                card = 'J'
            elif cards == 12:
                card = 'Q'
            elif cards == 13:
                card = 'K'
            else:
                card = str(cards)
            deck.append(str(card + suit))
    return deck


# the variables player1 and player2 call the shuffle_cards function but are on different lines of code because
# if they would equal the same (they store the same lists or randomisation of 'cards')

deck_of_cards = shuffle_cards()
random.shuffle(deck_of_cards)
print(deck_of_cards)
