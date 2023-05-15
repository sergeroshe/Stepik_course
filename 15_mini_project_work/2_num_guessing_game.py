import random

GUESS_LEFT_BORDER = 1
GREETING = 'Добро пожаловать в числовую угадайку'
RANDOM_LEFT_BORDER = 1
RANDOM_RIGHT_BORDER = 100
VALID_LEFT_BORDER = 1
VALID_RIGHT_BORDER = 100
ERROR_MESSAGE = f'А может быть все-таки введем целое число от ' \
                f'{VALID_LEFT_BORDER} до {VALID_RIGHT_BORDER}? \n'
PROMPT_MESSAGE = f'Введите число от ' \
                 f'{VALID_LEFT_BORDER} до {VALID_RIGHT_BORDER}: \n'
TOO_SMALL_MESSAGE = 'Ваше число меньше загаданного, попробуйте еще разок'
TOO_BIG_MESSAGE = 'Ваше число больше загаданного, попробуйте еще разок'
WIN_MESSAGE = 'Вы угадали, поздравляем!'
FAREWALL_MESSAGE = 'Спасибо, что играли в числовую угадайку. Еще увидимся...'


def min_guaranteed_guess_count(left_border, right_border):
    middle = (left_border + right_border) // 2
    division_count = 0

    while middle != left_border:
        middle = (left_border + right_border) // 2
        division_count += 1
        right_border = middle

    return division_count


def is_valid(input_string):
    result = input_string.isdigit() and VALID_LEFT_BORDER <= int(input_string) <= VALID_RIGHT_BORDER
    return result


def is_guessed():
    answer = ''
    is_guess_wrong = True
    rand_num = random.randint(RANDOM_LEFT_BORDER, RANDOM_RIGHT_BORDER)
    while is_guess_wrong:
        guess = input(PROMPT_MESSAGE)
        if not is_valid(guess):
            print(ERROR_MESSAGE)
        else:
            guess_num = int(guess)
            if guess_num == rand_num:
                is_guess_wrong = False
                answer = WIN_MESSAGE
            elif guess_num < rand_num:
                answer = TOO_SMALL_MESSAGE
            else:
                answer = TOO_BIG_MESSAGE
    return answer


def main():
    print(GREETING)

    # while True:
    #     guess = input(PROMPT_MESSAGE)
    #     if not is_valid(guess):
    #         print(ERROR_MESSAGE)
    #     else:
    #         guess_num = int(guess)
    #         break

    guess_right_border = int(input())

    guaranteed_min_tries = min_guaranteed_guess_count(GUESS_LEFT_BORDER, guess_right_border)

    print(guaranteed_min_tries)


main()