# Maciej Cieszyński
import random

class Deck:
    def __init__(self):
        self._cards = ['2♠', '3♠', '4♠', '5♠']
        # self._cards = ['2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♠', '2♣', '3♣', '4♣',
        #                '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣', 'A♣', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥',
        #                '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♥', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦',
        #                'J♦', 'Q♦', 'K♦', 'A♦']

    def __next__(self):
        if len(self._cards) != 0:
            random_card = random.choice(self._cards)
            self._cards.remove(random_card)
            return random_card
        raise StopIteration

    def __iter__(self):
        return self

if __name__ == '__main__':
    # tutaj można pisać dowolny kod, nie wpływa to na testy
    talia = Deck()
    for cards in talia:
        print(cards)
        input('NACIŚNIJ ENTER')
        # UWAGA! Nieskończona pętla!

    pass
