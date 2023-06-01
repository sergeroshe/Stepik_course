from random import randint

YES_RESPONSE = '1'
GUESS_LEFT_BORDER = 1
GREETING = 'Добро пожаловать в числовую угадайку!'
TOO_SMALL_MESSAGE = 'Ваше число МЕНЬШЕ загаданного, попробуйте еще разок'
TOO_BIG_MESSAGE = 'Ваше число БОЛЬШЕ загаданного, попробуйте еще разок'
WIN_MESSAGE = 'ВЫ УГАДАЛИ, ПОЗДРАВЛЯЕМ!'
NUM_IN_RANGE_PROMPT = 'Введите число от '
BORDER_PROMT = 'Введите числовую границу:\n'

LEFT_BORDER_PROMPT_MESSAGE = 'Введите нижнюю границу числового диапазона: \n'
RIGHT_BORDER_PROMPT = 'Введите верхнюю границу числового диапазона: \n'
FAREWELL_MESSAGE = 'Спасибо, что играли в числовую угадайку. Еще увидимся...'
GUESS_NUMBER_MESSAGE = 'Число сделанных вами попыток:'
# GAME_NUMBER_MESSAGE = 'Общее число сделанных вами попыток:'
ERROR_OUT_OF_GUESS_MESSAGE = 'А может быть все-таки введем целое число от '
BORDER_ERROR_MESSAGE = 'Это число должно быть больше чем '
TYPE_ERROR_MESSAGE = 'Введенные данные должны быть числовыми!'
NEW_GAME_PROPOSAL_MESSAGE = 'Хотите сыграть еще? \nНажмите: "1", затем: ENTER, ' \
                            'если ДА\nНажмите любую клавишу, затем: ENTER, если НЕТ\n'
STOP_GAME_RESPONSE = '**'
GIVE_UP_PROPOSAL = f'Если вы хотите досрочно закончить игру и узнать загаданное число, нажмите {STOP_GAME_RESPONSE}'
HIDDEN_NUM_REVELATION = 'Загаданное число:\n'
COLON_SEP = ':'
UP_TO_SEP = ' до '
MINUS_CHAR = '-'
MIN_GUARANTEED_GUESS_MESSAGE = 'Минимальное гарантированное число попыток угадывания в этом диапазоне:'
EXCLAMATION_SIGN = '!'


def min_guaranteed_guess_count(left_border, right_border):
    middle = (left_border + right_border) // 2 + 1
    division_count = 0

    while middle != left_border:
        middle = (left_border + right_border) // 2
        division_count += 1
        right_border = middle

    return division_count


def is_valid(input_string, guess_left_border, guess_right_border):
    result = input_string.lstrip('-').isdigit() and guess_left_border <= int(input_string) <= guess_right_border
    return result


#  returns integer input, asks untill get valid input
def get_num_input(prompt):
    is_string_num = False
    input_string = input(prompt)
    while not is_string_num:
        if input_string[0] == MINUS_CHAR and input_string[1:].isdigit() or input_string.isdigit():
            is_string_num = True
        else:
            print(TYPE_ERROR_MESSAGE)
            input_string = input(prompt)

    is_string_num = int(input_string)
    return is_string_num


def guessing_game_run():
    is_guess_wrong = True
    guess_count = 0

    guess_left_border = get_num_input(LEFT_BORDER_PROMPT_MESSAGE)
    guess_right_border = get_num_input(RIGHT_BORDER_PROMPT)

    is_right_border_correct = guess_right_border > guess_left_border
    while not is_right_border_correct:
        print(f'{BORDER_ERROR_MESSAGE}{guess_left_border}{EXCLAMATION_SIGN}\n')
        guess_right_border = int(input(RIGHT_BORDER_PROMPT))
        if guess_right_border > guess_left_border:
            is_right_border_correct = True
    guaranteed_min_tries = min_guaranteed_guess_count(guess_left_border, guess_right_border)
    print(MIN_GUARANTEED_GUESS_MESSAGE, guaranteed_min_tries, sep='\n')
    hidden_num = randint(guess_left_border, guess_right_border)
    error_message = f'{ERROR_OUT_OF_GUESS_MESSAGE}{guess_left_border}{UP_TO_SEP}{guess_right_border}? \n'
    guess_prompt = f'{NUM_IN_RANGE_PROMPT}{guess_left_border}{UP_TO_SEP}{guess_right_border}{COLON_SEP} \n'

    while is_guess_wrong:
        guess = input(f'{GIVE_UP_PROPOSAL}\n{guess_prompt}')
        if guess == STOP_GAME_RESPONSE:
            print(f'{HIDDEN_NUM_REVELATION}{hidden_num}')
            is_guess_wrong = False
        elif not is_valid(guess, guess_left_border, guess_right_border):
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

