import random
GREETING = 'Добро пожаловать в числовую угадайку!'
GUESS_LEFT_BORDER = 1
GUESS_RIGHT_BORDER_PROMPT_MESSAGE = 'Введите число от '
VALID_LEFT_BORDER = 1
VALID_RIGHT_BORDER = 100
ERROR_MESSAGE = "Ошибка ввода! Необходима ввести число от "


def num_guessing_game(left_border, right_border):
    middle = (left_border + right_border) // 2
    division_count = 0

    while middle != left_border:
        middle = (left_border + right_border) // 2
        division_count += 1
        right_border = middle

    return division_count


def is_valid(input_string):
    result = input_string.isdigit() and VALID_LEFT_BORDER < int(input_string) <= VALID_RIGHT_BORDER
    return result


def main():
    print(GREETING)
    right_border = int(input(GUESS_RIGHT_BORDER_PROMPT_MESSAGE + str(VALID_LEFT_BORDER)
                             + ' до ' + str(VALID_RIGHT_BORDER) + ': \n'))
    if not is_valid(str(right_border)):
        print(ERROR_MESSAGE + str(VALID_LEFT_BORDER) + ' до ' + str(VALID_RIGHT_BORDER))
    else:
        try_count = num_guessing_game(GUESS_LEFT_BORDER, right_border)

        print(try_count)


main()
