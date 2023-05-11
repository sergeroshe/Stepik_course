import random
GREETING = 'Добро пожаловать в числовую угадайку! \n'
GUESS_LEFT_BORDER = 1
GUESS_RIGHT_BORDER_PROMPT_MESSAGE = 'Введите верхний диапазон чисел: \n'
VALID_LEFT_BORDER = 1
VALID_RIGHT_BORDER = 100


def num_guessing_game(start_range, end_range):
    middle = (start_range + end_range) // 2
    division_count = 0

    while middle != start_range:
        middle = (start_range + end_range) // 2
        division_count += 1
        end_range = middle

    return division_count


def is_valid(input_string):
    guess_right_border = int(input(GUESS_RIGHT_BORDER_PROMPT_MESSAGE))
    result = input_string.isdigit() and VALID_LEFT_BORDER < int(input_string) < VALID_RIGHT_BORDER
    return result


def main():
    print(GREETING)
    end_range = int(input())

    try_count = num_guessing_game(GUESS_LEFT_BORDER, end_range)

    print(try_count)


main()
