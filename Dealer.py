from Deck import Deck


class Dealer:

    def __init__(self, money='Null'):
        self.cards = []
        self.card_value = 0
        self.deck = Deck()
        self.players = []
        self.winners = []
        self.money = money

    def update_players(self, player_list):
        self.players = []
        for player in player_list:
            self.players.append(player)

    def deal_hand(self):
        for player in self.players:
            for card in range(2):
                card = self.deck.draw_card()
                player.cards.append(card[0])
                player.card_value += card[1]

    def hit(self, player):
        card = self.deck.draw_card()
        player.cards.append(card[0])
        player.card_value += card[1]

    def self_deal(self):
        self.hit(self)

    def play_own_hand(self):
        if self.find_lowest() < 17:
            while self.card_value < 17:
                self.self_deal()
        else:
            while self.card_value < self.find_lowest():
                self.self_deal()

    def find_lowest(self):
        lowest = min([player.card_value for player in self.players])

        if lowest > 21:
            return 0
        else:
            return lowest

    def pay_winners(self):
        """ This will be deducted from the dealers bank roll in the future. """
        for player in self.winners:
            player.money += player.money_bet * 2

    def receive_money(self):
        pass

    def reset_table(self):
        for player in self.players:
            player.reset_hand()

        self.deck.reset_deck()
        self.cards, self.winners = [], []
        self.card_value = 0


    def display_cards(self):
        print('{} at {}'.format(self.cards, self.card_value))
