from random import randint

YES_RESPONSE = '1'
GUESS_LEFT_BORDER = 1
GREETING = 'Добро пожаловать в числовую угадайку!'
TOO_SMALL_MESSAGE = 'Ваше число МЕНЬШЕ загаданного, попробуйте еще разок'
TOO_BIG_MESSAGE = 'Ваше число БОЛЬШЕ загаданного, попробуйте еще разок'
WIN_MESSAGE = 'ВЫ УГАДАЛИ, ПОЗДРАВЛЯЕМ!'
ENTER_NUM_PROMPT = 'Введите число от '
LEFT_BORDER_PROMPT_MESSAGE = 'Введите нижнюю границу числового диапазона: \n'
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
    middle = (left_border + right_border) // 2 + 1
    division_count = 0

    while middle != left_border:
        middle = (left_border + right_border) // 2
        division_count += 1
        right_border = middle

    return division_count


def is_valid(input_string, guess_left_border, guess_right_border):
    result = input_string.isdigit() and guess_left_border <= int(input_string) <= guess_right_border
    return result


def guessing_game_run():
    is_guess_wrong = True
    guess_count = 0
    guess_left_border = int(input(LEFT_BORDER_PROMPT_MESSAGE))
    guess_right_border = int(input(RIGHT_BORDER_PROMPT))
    guaranteed_min_tries = min_guaranteed_guess_count(guess_left_border, guess_right_border)
    print(MIN_GUARANTEED_GUESS_MESSAGE, guaranteed_min_tries, sep='\n')
    hidden_num = randint(GUESS_LEFT_BORDER, guess_right_border)
    error_message = f'{ERROR_OUT_OF_GUESS_MESSAGE}{guess_left_border}{UP_TO_SEP}{guess_right_border}? \n'
    guess_prompt = f'{ENTER_NUM_PROMPT}{guess_left_border}{UP_TO_SEP}{guess_right_border}{COLON_SEP} \n'

    while is_guess_wrong:
        guess = input(guess_prompt)

        if not is_valid(guess, guess_left_border, guess_right_border):
            print(error_message)
        else:
            guess_num = int(guess)
            guess_count += 1
            if guess_num < hidden_num:
                print(TOO_SMALL_MESSAGE, GUESS_NUMBER_MESSAGE, guess_count, sep='\n')
            elif guess_num > hidden_num:
                print(TOO_BIG_MESSAGE, GUESS_NUMBER_MESSAGE, guess_count, sep='\n')
            else:
                print(WIN_MESSAGE, GUESS_NUMBER_MESSAGE, guess_count, sep='\n')

                is_guess_wrong = False


def main():
    print(GREETING)
    game_is_going_on = True
    while game_is_going_on:
        guessing_game_run()
        new_game_wish = input(NEW_GAME_PROPOSAL_MESSAGE).lower()
        game_is_going_on = new_game_wish == YES_RESPONSE

    print(FAREWELL_MESSAGE)


main()