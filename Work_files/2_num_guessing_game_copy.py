import random

YES_RESPONSE = 'д'
GREETING = 'Добро пожаловать в числовую угадайку'
GUESS_LEFT_BORDER = 1
LEFT_BORDER_PROMPT_MESSAGE = 'Введите нижнюю границу числового диапазона: \n'
RIGHT_BORDER_PROMPT_MESSAGE = 'Введите верхнюю границу числового диапазона: \n'
TOO_SMALL_MESSAGE = 'Ваше число меньше загаданного, попробуйте еще разок'
TOO_BIG_MESSAGE = 'Ваше число больше загаданного, попробуйте еще разок'
WIN_MESSAGE = 'Вы угадали, поздравляем!'
NEW_GAME_PROPOSAL_MESSAGE = 'Хотите сыграть еще? \nНажмите "д", если ДА или нажмите любую клавишу, если НЕТ:\n'
FAREWELL_MESSAGE = 'Спасибо, что играли в числовую угадайку. Еще увидимся...'
GUESS_NUMBER_MESSAGE = 'Число сделанных вами попыток:'


def min_guaranteed_guess_count(left_border, right_border):
    middle = (left_border + right_border) // 2
    division_count = 0

    while middle != left_border:
        middle = (left_border + right_border) // 2
        division_count += 1
        right_border = middle

    return division_count


def is_valid(input_string, guess_left_border, guess_right_border):
    result = input_string.isdigit() and guess_left_border <= int(input_string) <= guess_right_border
    return result


def main():
    print(GREETING)

    game_is_going_on = True
    while game_is_going_on:
        guess_left_border = int(input(LEFT_BORDER_PROMPT_MESSAGE))
        guess_right_border = int(input(RIGHT_BORDER_PROMPT_MESSAGE))
        hidden_num = random.randint(guess_left_border, guess_right_border)
        prompt_message = f'Введите число от ' \
                         f'{guess_left_border} до {guess_right_border}: \n'
        error_message = f'А может быть все-таки введем целое число от ' \
                        f'{guess_left_border} до {guess_right_border}? \n'
        guess_count = 1

        is_guess_wrong = True
        while is_guess_wrong:
            guess = input(prompt_message)

            if not is_valid(guess, guess_left_border, guess_right_border):
                print(error_message)
            else:
                guess_num = int(guess)
                if guess_num < hidden_num:
                    print(TOO_SMALL_MESSAGE)
                elif guess_num > hidden_num:
                    print(TOO_BIG_MESSAGE)
                else:
                    print(WIN_MESSAGE)
                    is_guess_wrong = False
            guess_count += 1
        new_game_wish = input(NEW_GAME_PROPOSAL_MESSAGE).lower()
        if new_game_wish != YES_RESPONSE:
            print(GUESS_NUMBER_MESSAGE, guess_count - 1, sep='\n')
            print(FAREWELL_MESSAGE)
            game_is_going_on = False

    # guaranteed_min_tries = min_guaranteed_guess_count(GUESS_LEFT_BORDER, guess_right_border)

    # print(guaranteed_min_tries)


main()
