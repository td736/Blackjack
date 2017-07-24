from Player import Player
from Dealer import Dealer


def main():
    player = Player()
    dealer = Dealer()

    dealer.players.append(player)

    while input('Play another hand or quit(q): ') != 'q':
        dealer.reset_table()
        dealer.players[0].bet(input("Bet amount: "))
        dealer.deal_hand()
        dealer.players[0].display_cards()

        while input("Hit or stand(s): ") != 's':
            dealer.hit(dealer.players[0])

            if dealer.players[0].card_value > 21:
                print('Player bust with:')
                dealer.players[0].display_cards()
                break

            elif dealer.players[0].card_value == 21:
                dealer.winners.append(dealer.players[0])
                print('Player wins with 21.')
                break
            dealer.players[0].display_cards()

        if not dealer.players[0].card_value >= 21:
            dealer.play_own_hand(dealer.players[0])

            if dealer.card_value > 21:
                print('Dealer bust with {} at {}'.format(dealer.cards, dealer.card_value))
                dealer.winners.append(dealer.players[0])
            else:
                print('House wins with {} at {}.'.format(dealer.cards, dealer.card_value))

        if len(dealer.winners) != 0:
            print('Player wins {}.'.format(dealer.players[0].money_bet * 2))
            dealer.pay_winners()





if __name__ == '__main__':
    main()