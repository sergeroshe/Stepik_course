GAME_RESULT_LIST = ['ничья', 'Тимур', 'Руслан']


def get_game_result(player_1_card, player_2_card):
    result = 0
    if player_1_card != player_2_card:
        if player_1_card == 'Спок' and player_2_card == 'камень':
            result = 1
        elif player_1_card == 'бумага' and player_2_card == 'камень':
            result = 1
        elif player_1_card == 'ножницы' and player_2_card == 'ящерица':
            result = 1
        elif player_1_card == 'ящерица' and player_2_card == 'бумага':
            result = 1
        elif player_1_card == 'камень' and player_2_card == 'ножницы':
            result = 1
        elif player_1_card == 'ящерица' and player_2_card == 'Спок':
            result = 1
        elif player_1_card == 'камень' and player_2_card == 'ящерица':
            result = 1
        else:
            result = 2
    return result


def game_run(player_1_card, player_2_card, result_list):
    winner = result_list[get_game_result(player_1_card, player_2_card)]
    print(winner)


def main():
    player_1_card = input()
    player_2_card = input()
    game_run(player_1_card, player_2_card, GAME_RESULT_LIST)


main()
