class Player:

    def __init__(self, money=1000):
        self.money = money
        self.cards = []
        self.total = 0

    def add_money(self, amount):
        self.money += amount

    def sub_money(self, amount):
        self.money -= amount