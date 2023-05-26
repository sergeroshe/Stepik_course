from random import randint

YES_RESPONSE = '1'
GUESS_LEFT_BORDER = 1
GREETING = 'Добро пожаловать в числовую угадайку!'
TOO_SMALL_MESSAGE = 'Ваше число МЕНЬШЕ загаданного, попробуйте еще разок'
TOO_BIG_MESSAGE = 'Ваше число БОЛЬШЕ загаданного, попробуйте еще разок'
WIN_MESSAGE = 'ВЫ УГАДАЛИ, ПОЗДРАВЛЯЕМ!'
ENTER_NUM_PROMPT = 'Введите число от '
RIGHT_BORDER_PROMPT = 'Введите верхнюю границу числового диапазона: \n'
FAREWELL_MESSAGE = 'Спасибо, что играли в числовую угадайку. Еще увидимся...'
GUESS_NUMBER_MESSAGE = 'Число сделанных вами попыток:'
# GAME_NUMBER_MESSAGE = 'Общее число сделанных вами попыток:'
ERROR_OUT_OF_GUESS_MESSAGE = 'А может быть все-таки введем целое число от '
NEW_GAME_PROPOSAL_MESSAGE = 'Хотите сыграть еще? \nНажмите: "1", затем: ENTER, ' \
                            'если ДА\nНажмите любую клавишу, затем: ENTER, если НЕТ\n'
COLON_SEP = ':'
UP_TO_SEP = ' до '
MIN_GUARANTEED_GUESS_MESSAGE = 'Минимальное гарантированное число попыток угадывания в этом диапазоне:'


def min_guaranteed_guess_count(left_border, right_border):
    middle = (left_border + right_border) // 2
    division_count = 0

    while middle != left_border:
        middle = (left_border + right_border) // 2
        division_count += 1
        right_border = middle

    return division_count


def is_valid(input_string, guess_right_border):
    result = input_string.isdigit() and GUESS_LEFT_BORDER <= int(input_string) <= guess_right_border
    return result


def main():
    print(GREETING)
    game_is_going_on = True
    while game_is_going_on:
        is_guess_wrong = True
        guess_count = 0
        guess_right_border = int(input(RIGHT_BORDER_PROMPT))
        guaranteed_min_tries = min_guaranteed_guess_count(GUESS_LEFT_BORDER, guess_right_border)
        print(MIN_GUARANTEED_GUESS_MESSAGE)
        print(guaranteed_min_tries)
        hidden_num = randint(GUESS_LEFT_BORDER, guess_right_border)
        error_message = f'{ERROR_OUT_OF_GUESS_MESSAGE}{GUESS_LEFT_BORDER}{UP_TO_SEP}{guess_right_border}? \n'
        guess_prompt = f'{ENTER_NUM_PROMPT}{GUESS_LEFT_BORDER}{UP_TO_SEP}{guess_right_border}{COLON_SEP} \n'

        while is_guess_wrong:
            guess = input(guess_prompt)

            if not is_valid(guess, guess_right_border):
                print(error_message)
            else:
                guess_num = int(guess)
                if guess_num < hidden_num:
                    print(TOO_SMALL_MESSAGE)
                    guess_count += 1
                    print(GUESS_NUMBER_MESSAGE, guess_count, sep='\n')
                elif guess_num > hidden_num:
                    print(TOO_BIG_MESSAGE)
                    guess_count += 1
                    print(GUESS_NUMBER_MESSAGE, guess_count, sep='\n')
                else:
                    print(WIN_MESSAGE)
                    guess_count += 1
                    print(GUESS_NUMBER_MESSAGE, guess_count, sep='\n')

                    is_guess_wrong = False
        new_game_wish = input(NEW_GAME_PROPOSAL_MESSAGE).lower()
        if new_game_wish != YES_RESPONSE:
            game_is_going_on = False
    print(FAREWELL_MESSAGE)


main()
