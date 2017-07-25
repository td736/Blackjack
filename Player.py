class Player:

    def __init__(self, name, money=1000):
        self.money = money
        self.cards = []
        self.card_value = 0
        self.name = name
        self.money_bet = 0

    def bet(self, amount):
        amount = int(amount)
        while amount > self.money:
            amount = int(input("You only have ${}. \nBet amount: ".format(self.money)))
        self.money -= amount
        self.money_bet = amount

    def reset_hand(self):
        self.cards = []
        self.card_value = 0
        self.money_bet = 0

    def display_cards(self):
        print ('{} at {}'.format(self.cards, self.card_value))
