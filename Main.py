from Table import Table


def main():
    table = Table()

    while input("Add player or start(s): ") != 's':
        table.add_player()
        table.dealer.update_players(table.player_list)

    while True:
        table.start_hand()
        table.hit_loop()
        table.dealers_turn()

        for player in table.player_list:
            if player.money <= 0:
                table.remove_player(player.name)

        while input("Add players or next round(s): ") != 's':
            table.add_player()

        if len(table.player_list) == 0:
            break

        else:
            table.dealer.update_players(table.player_list)



if __name__ == '__main__':
    main()
