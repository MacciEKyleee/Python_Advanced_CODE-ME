# Maciej Cieszyński
import random
from zaddom02_e1 import Deck


def draw_cards(deck, amount=1):
    card_list = []
    cards = 0

    while cards <= amount:
        cards = cards + 1
        return card_list.append(deck.__next__())


if __name__ == '__main__':
    deck = Deck()

    player1 = draw_cards(deck, 14)
    player2 = draw_cards(deck, 14)
    player3 = draw_cards(deck, 14)
    player4 = draw_cards(deck, 14)

    print(player1)
    print(player2)
    print(player3)
    print(player4)
