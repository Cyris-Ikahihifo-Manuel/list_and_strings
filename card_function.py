# importing random module to shuffle the cards and choice

import random

# card function that will generate a 'pack' of cards


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


# if this goes as expected from me the

deck_of_cards = []
for v in range(5):
    deck_of_cards.append(v)
for decks in range(4):
    deck_of_cards[decks] = shuffle_cards()
    random.shuffle(deck_of_cards[decks])
    print(deck_of_cards[decks])
