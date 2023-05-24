import random

GUESS_LEFT_BORDER = 1
GREETING = 'Добро пожаловать в числовую угадайку!'
TOO_SMALL_MESSAGE = 'Ваше число меньше загаданного, попробуйте еще разок'
TOO_BIG_MESSAGE = 'Ваше число больше загаданного, попробуйте еще разок'
WIN_MESSAGE = 'Вы угадали, поздравляем!'
PROMPT_MESSAGE = 'Введите число от '
RIGHT_BORDER_PROMPT_MESSAGE = 'Введите верхнюю границу числового диапазона: \n'
FAREWELL_MESSAGE = 'Спасибо, что играли в числовую угадайку. Еще увидимся...'
GUESS_NUMBER_MESSAGE = 'Число сделанных вами попыток:'
ERROR_OUT_OF_GUESS_MESSAGE = 'А может быть все-таки введем целое число от '
COLON_SEP = ':'
UP_TO_SEP = ' до '


def min_guaranteed_guess_count(left_border, right_border):
    middle = (left_border + right_border) // 2
    division_count = 0

    while middle != left_border:
        middle = (left_border + right_border) // 2
        division_count += 1
        right_border = middle

    return division_count


def is_valid(input_string, guess_right_border):
    result = input_string.isdigit() and guess_right_border <= int(input_string) <= guess_right_border
    return result


def main():
    print(GREETING)

    is_guess_wrong = True
    guess_count = 1

    while is_guess_wrong:
        guess_right_border = int(input(RIGHT_BORDER_PROMPT_MESSAGE))
        hidden_num = random.randint(GUESS_LEFT_BORDER, guess_right_border)
        guess = input(PROMPT_MESSAGE + str(guess_right_border) + COLON_SEP + '\n')
        error_message = f'{ERROR_OUT_OF_GUESS_MESSAGE}{GUESS_LEFT_BORDER}{UP_TO_SEP}{guess_right_border}? \n'
        if not is_valid(guess, guess_right_border):
            print(error_message)
        else:
            guess_num = int(guess)
            if guess_num < hidden_num:
                print(TOO_SMALL_MESSAGE)
            elif guess_num > hidden_num:
                print(TOO_BIG_MESSAGE)
            else:
                print(WIN_MESSAGE)
                print(GUESS_NUMBER_MESSAGE, guess_count, sep='\n')
                print(FAREWELL_MESSAGE)

                is_guess_wrong = False
        guess_count += 1

    # guaranteed_min_tries = min_guaranteed_guess_count(GUESS_LEFT_BORDER, guess_right_border)
    # print(guaranteed_min_tries)


main()
