from random import sample
CARD_SIZE = 5
NUMBER_RANGE = 75

card_list = list(sample(range(1, NUMBER_RANGE + 1), CARD_SIZE ** 2))

card = [[card_list[j] for j in range(i, i + CARD_SIZE)]
        for i in range(0, len(card_list), CARD_SIZE)]
card[CARD_SIZE // 2][CARD_SIZE // 2] = 0

for i in range(CARD_SIZE):
    for j in range(CARD_SIZE):
        print(str(card[i][j]).ljust(3), end=' ')
    print()
