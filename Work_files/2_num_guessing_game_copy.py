from random import randint

YES_RESPONSE = '1'
GREETING = 'Добро пожаловать в числовую угадайку'
GUESS_LEFT_BORDER = 1
LEFT_BORDER_PROMPT_MESSAGE = 'Введите нижнюю границу числового диапазона: \n'
RIGHT_BORDER_PROMPT_MESSAGE = 'Введите верхнюю границу числового диапазона: \n'
MIN_GUARANTEED_GUESS_MESSAGE = 'Минимальное гарантированное число попыток угадывания в этом диапазоне:'
PROMPT_MESSAGE = 'Введите число от '
ERROR_MESSAGE = 'А может быть все-таки введем целое число от'
BORDER_ERROR_MESSAGE = 'Это число должно быть больше чем'
TOO_SMALL_MESSAGE = 'Ваше число меньше загаданного, попробуйте еще разок'
TOO_BIG_MESSAGE = 'Ваше число больше загаданного, попробуйте еще разок'
WIN_MESSAGE = 'ВЫ УГАДАЛИ, ПОЗДРАВЛЯЕМ!\n'
NEW_GAME_PROPOSAL_MESSAGE = 'Хотите сыграть еще? \nНажмите: "1", затем: ENTER, если ДА\n' \
                            'Нажмите любую клавишу, затем: ENTER, если НЕТ\n'
FAREWELL_MESSAGE = 'Спасибо, что играли в числовую угадайку. Еще увидимся...'
TOTAL_GUESS_NUMBER_MESSAGE = 'Общее число сделанных вами попыток:'
GUESS_NUMBER_MESSAGE = 'Число сделанных вами попыток:'
SEP = ' до '


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


def main():
    print(GREETING)

    game_is_going_on = True
    while game_is_going_on:
        guess_left_border = int(input(LEFT_BORDER_PROMPT_MESSAGE))
        guess_right_border = int(input(RIGHT_BORDER_PROMPT_MESSAGE))
        is_right_border_correct = guess_right_border > guess_left_border
        while not is_right_border_correct:
            print(BORDER_ERROR_MESSAGE, str(guess_left_border), sep=' ', end='!\n')
            guess_right_border = int(input(RIGHT_BORDER_PROMPT_MESSAGE))
            if guess_right_border > guess_left_border:
                is_right_border_correct = True
        else:
            print(MIN_GUARANTEED_GUESS_MESSAGE)
            guaranteed_min_tries = min_guaranteed_guess_count(guess_left_border, guess_right_border)
            print(guaranteed_min_tries)
            hidden_num = randint(guess_left_border, guess_right_border)
            guess_count = 0

            is_guess_wrong = True
            while is_guess_wrong:
                guess = input(PROMPT_MESSAGE + str(guess_left_border) + SEP + str(guess_right_border) + ':\n')

                if not is_valid(guess, guess_left_border, guess_right_border):
                    print(ERROR_MESSAGE, guess_left_border, guess_right_border, sep=SEP, end='?\n')
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
                        is_guess_wrong = False
                        guess_count += 1
                        print(GUESS_NUMBER_MESSAGE, guess_count, sep='\n')
            new_game_wish = input(NEW_GAME_PROPOSAL_MESSAGE).lower()
            if new_game_wish != YES_RESPONSE:
                print(TOTAL_GUESS_NUMBER_MESSAGE, guess_count, sep='\n')
                game_is_going_on = False
    print(FAREWELL_MESSAGE)


main()