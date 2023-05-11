import random

GUESS_LEFT_BORDER = 1
GREETING = 'Добро пожаловать в числовую угадайку!'
RANDOM_LEFT_BORDER = 1
RANDOM_RIGHT_BORDER = 100
ERROR_MESSAGE = 'А может быть все-таки введем целое число от 1 до 100?'


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


def is_valid(input_string):
    result = input_string.isdigit() and 1 < int(input_string) < 100
    # return result

    while result:
        input_num = 0
        input_value = input()
        if not is_valid(input_value):
            print(ERROR_MESSAGE)
        else:
            input_num = int(input_value)

        print(input_num)


main()