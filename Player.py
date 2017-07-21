class Player:

    def __init__(self, money=1000):
        self.money = money
        self.cards = []

    def add_money(self, amount):
        self.money += amount

    def sub_money(self, amount):
        self.money -= amount