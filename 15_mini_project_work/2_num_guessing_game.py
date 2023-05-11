import random

GUESS_LEFT_BORDER = 1
GREETING = 'Добро пожаловать в числовую угадайку'
RANDOM_LEFT_BORDER = 1
RANDOM_RIGHT_BORDER = 100


def min_guaranteed_guess_count(left_border, right_border):
    middle = (left_border + right_border) // 2
    division_count = 0

    while middle != left_border:
        middle = (left_border + right_border) // 2
        division_count += 1
        right_border = middle

    return division_count


def main():
    print(GREETING)
    guess_right_border = int(input())
    rand_num = random.randint(RANDOM_LEFT_BORDER, RANDOM_RIGHT_BORDER)

    guaranteed_min_tries = min_guaranteed_guess_count(GUESS_LEFT_BORDER, guess_right_border)

    print(guaranteed_min_tries)


main()