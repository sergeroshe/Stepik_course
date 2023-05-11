import random

START_RANGE = 1
GREETING = 'Добро пожаловать в числовую угадайку'
RANDOM_LEFT_BORDER = 1
RANDOM_RIGHT_BORDER = 100


def min_guaranteed_guess_count(start_range, end_range):
    middle = (start_range + end_range) // 2
    division_count = 0

    while middle != start_range:
        middle = (start_range + end_range) // 2
        division_count += 1
        end_range = middle

    return division_count


def main():
    print(GREETING)
    end_range = int(input())
    rand_num = random.randint(RANDOM_LEFT_BORDER, RANDOM_RIGHT_BORDER)

    guaranteed_min_tries = min_guaranteed_guess_count(START_RANGE, end_range)

    print(guaranteed_min_tries)


main()