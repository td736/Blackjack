from Dealer import Dealer
from Player import Player


class Table:

    def __init__(self):
        self.dealer = Dealer()
        self.player_list = []

    def add_player(self):
        name = input("Name: ")
        buy_in = input("Buy-in: ")
        self.player_list.append(Player(name, int(buy_in)))

    def remove_player(self, name):
        for player in self.player_list:
            if player.name == name:
                self.player_list.remove(player)

    def start_hand(self):
        self.dealer.reset_table()
        for player in self.dealer.players:
            player.bet(int(input("{}'s bet: ".format(player.name))))
            self.dealer.deal_hand()

    def hit_loop(self):
        for player in self.dealer.players:
            print("{}'s turn.".format(player.name))
            player.display_cards()

            while input("Hit or stand(s): ") != "s":
                self.dealer.hit(player)

                if player.card_value > 21:
                    print("{} bust with:".format(player.name))
                    player.display_cards()
                    break

                elif player.card_value == 21:
                    print("{} has 21 with: ".format(player.name))
                    player.display_cards()
                    break

                player.display_cards()

    def dealers_turn(self):
        self.dealer.play_own_hand()

        if self.dealer.card_value > 21:
            print("Dealer busts with {}.".format(self.dealer.display_cards()))
            for player in self.dealer.players:
                if player.card_value <= 21:
                    self.dealer.winners.append(player)

        elif self.dealer.card_value <= 21:
            for player in self.dealer.players:
                if player.card_value == self.dealer.card_value:
                    print("{} tied with dealer. ${} returned.".format(player.name, player.money_bet))
                    player.money += player.money_bet

                elif 21 >= player.card_value > self.dealer.card_value:
                    print("{} beats the dealer. Won ${}.".format(player.name, player.money_bet*2))
                    self.dealer.winners.append(player)

                elif player.card_value < self.dealer.card_value <= 21:
                    print("{} lost ${}.".format(player.name, player.money_bet))

        print("Dealers cards are:")
        self.dealer.display_cards()
        self.dealer.pay_winners()

