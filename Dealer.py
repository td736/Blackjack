from Deck import Deck

class Dealer:

    def __init__(self):
        self.cards = []
        self.deck = Deck()

    def deal_to_player(self, player):

        if len(player.cards) == 0:
            player.cards.append(self.deck.draw_card())
            player.cards.append(self.deck.draw_card())
        else:
            player.cards.append(self.deck.draw_card())


    def player_bust(self, player):

        total = 0
        for card in player.cards:
            total += card.value()
        if total > 21:
            return True
        else:
            player.total = total
