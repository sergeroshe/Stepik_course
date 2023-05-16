import random
YES_RESPONSE = 'д'
NO_RESPONSE = 'н'
GUESS_LEFT_BORDER = 1
GREETING = 'Добро пожаловать в числовую угадайку'
PROMPT_RIGHT_BORDER_MESSAGE = 'Введите верхнюю границу числового диапазона: \n'
NEW_GAME_PROPOSAL_MESSAGE = 'Хотите сыграть еще? \nНажмите "д", если ДА или нажмите любую клавишу, если НЕТ:\n'
TOO_SMALL_MESSAGE = 'Ваше число меньше загаданного, попробуйте еще разок'
TOO_BIG_MESSAGE = 'Ваше число больше загаданного, попробуйте еще разок'
WIN_MESSAGE = 'Вы угадали, поздравляем!'
FAREWELL_MESSAGE = 'Спасибо, что играли в числовую угадайку. Еще увидимся...'


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
        guess_right_border = int(input(PROMPT_RIGHT_BORDER_MESSAGE))
        # guaranteed_min_tries = min_guaranteed_guess_count(GUESS_LEFT_BORDER, guess_right_border)
        rand_num = random.randint(GUESS_LEFT_BORDER, guess_right_border)
        enter_num_message = f'Введите число от {GUESS_LEFT_BORDER} до {guess_right_border}: \n'
        error_message = f'А может быть все-таки введем целое число от ' \
                        f'{GUESS_LEFT_BORDER} до {guess_right_border}? \n'
        guess_count = 1

        is_guess_wrong = True
        while is_guess_wrong:
            guess = input(enter_num_message)
            if not is_valid(guess, guess_right_border):
                print(error_message)
            else:
                guess_num = int(guess)
                if guess_num < rand_num:
                    print(TOO_SMALL_MESSAGE)
                elif guess_num > rand_num:
                    print(TOO_BIG_MESSAGE)
                else:
                    print(f'{WIN_MESSAGE} \n')
                    is_guess_wrong = False
            guess_count += 1
        new_game_wish = input(NEW_GAME_PROPOSAL_MESSAGE).lower()
        if new_game_wish != YES_RESPONSE:
            print(f'{FAREWELL_MESSAGE}\nЧисло сделанных вами попыток:\n{guess_count}')
            game_is_going_on = False

    # while True:
    #     guess = input(PROMPT_MESSAGE)
    #     if not is_valid(guess):
    #         print(ERROR_MESSAGE)
    #     else:
    #         guess_num = int(guess)
    #         break

    # print(guaranteed_min_tries)


main()