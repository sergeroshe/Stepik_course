import random

GUESS_LEFT_BORDER = 1
GREETING = 'Добро пожаловать в числовую угадайку! \n'
RANDOM_LEFT_BORDER = 1
RANDOM_RIGHT_BORDER = 100
ERROR_MESSAGE = 'А может быть все-таки введем целое число от 1 до'
GUESS_RIGHT_BORDER_PROMPT_MESSAGE = 'Введите верхний диапазон чисел: \n'


def min_guaranteed_guess_count(left_border, right_border):
    middle = (left_border + right_border) // 2
    division_count = 0

    while middle != left_border:
        middle = (left_border + right_border) // 2
        division_count += 1
        right_border = middle

    return division_count


def is_valid(input_string):
    guess_right_border = int(input(GUESS_RIGHT_BORDER_PROMPT_MESSAGE))
    result = input_string.isdigit() and 1 < int(input_string) < RANDOM_RIGHT_BORDER
    return result


def main():
    print(GREETING)
    result = is_valid(input_value)
    while result:
        input_value = input()
        if not is_valid(input_value):
            print(ERROR_MESSAGE + str(guess_right_border))
        else:
            input_num = int(input_value)
    is_valid(input())

    rand_num = random.randint(RANDOM_LEFT_BORDER, RANDOM_RIGHT_BORDER)

    guaranteed_min_tries = min_guaranteed_guess_count(GUESS_LEFT_BORDER, guess_right_border)

    # print(guaranteed_min_tries)

    # return result


main()
