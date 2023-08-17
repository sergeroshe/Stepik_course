CARD_LIST = ['камень', 'ножницы', 'бумага']
GAME_RESULT_LIST = ['ничья', 'Руслан', 'Тимур']
player_1_card = input()
player_2_card = input()
case = CARD_LIST.index(player_1_card) - CARD_LIST.index(player_2_card)
result = GAME_RESULT_LIST[case]

print(result)
