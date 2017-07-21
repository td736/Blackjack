# from Deck import Deck

class Dealer:

    def __init__(self):
        self.cards = []

    def player_bust(self, player):

        total = 0
        for card in player.cards:
            total += card.value()
        if total > 21:
            return True
        else:
            player.total = total
