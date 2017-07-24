from random import randrange

class Deck:

    def __init__(self):
        self.card_values = {'2': 2, '3': 3, '4': 4, '5': 5,
                            '6': 6, '7': 7, '8': 8, '9': 9,
                            '10': 10, 'J': 10, 'Q': 10,
                            'K': 10, 'A': 11}
        self.cards = ['2', '3', '4', '5', '6', '7', '8',
                      '9', '10', 'J', 'Q', 'K', 'A'] * 4

    def draw_card(self):
        card = self.cards[randrange(len(self.cards))]
        self.cards.remove(card)

        return card, self.card_values[card]

    def reset_deck(self):
        self.__init__()