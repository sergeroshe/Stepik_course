from random import choice

GREETING = 'Давайте играть в угадайку слов!'
ENTER_GUESS_PROMPT_P_1 = 'Введите букву или всё слово, состоящее из '
ENTER_GUESS_PROMPT_P_2 = ' букв'
WIN_MESSAGE = 'Поздравляем, вы угадали слово! Вы победили!'
WRONG_GUESS_MESSAGE = 'Ответ неверный'
LOSING_MESSAGE = 'Вы проиграли.'
TYPE_ERROR_MESSAGE = 'Введенные данные должны содержать только текст!\n'
LEN_ERROR_MESSAGE = 'Введенное слово должно состоять из '
REPEAT_ERROR = 'Вы уже вводили эту букву, попробуйте другую'
COLON_SEP = ':'
EXCLAMATION_SIGN = '!'
WORD_COMPLETION_FILLING_CHAR = '_'
MAX_TRIES_COUNT = 6
STAGES = [  # финальное состояние: голова, торс, обе руки, обе ноги
    '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
    # голова, торс, обе руки, одна нога
    '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
    # голова, торс, обе руки
    '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
    # голова, торс и одна рука
    '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
    # голова и торс
    '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
    # голова
    '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
    # начальное состояние
    '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
]

WORD_LIST = ['арбуз', 'банан', 'вагон', 'гиббон', 'дом', 'еж', 'железо',
             'зебра', 'игла', 'корабль', 'лес', 'мама', 'нос', 'окно',
             'пианино', 'река', 'солнце', 'трамвай', 'улица', 'фонарь',
             'хлеб', 'цветок', 'шар', 'щенок', 'электроника', 'юбка',
             'яблоко', 'аэропорт', 'бумага', 'вышка', 'голубь', 'дверь',
             'ежедневник', 'жара', 'замок', 'изделие', 'корень', 'лавка',
             'магазин', 'нож', 'опера', 'песок', 'ручка', 'самолет', 'таблица',
             'утка', 'флаг', 'холодильник', 'церковь', 'шапка', 'щука',
             'электричество', 'ящик', 'авиалиния', 'булавка', 'выставка',
             'горка', 'двигатель', 'ежик', 'желание', 'зачёт', 'изучение',
             'колбаса', 'лампа', 'марка', 'ночь', 'обувь', 'парад', 'рыба',
             'сахар', 'творог', 'улитка', 'фильм', 'художник', 'цыпленок',
             'шоколад', 'щит', 'энергия', 'яблоня', 'автомобиль', 'бюджет',
             'выход', 'город', 'дверца', 'ежемесячник', 'завод',
             'измерение', 'колесник', 'ландыш', 'математика', 'нота', 'область',
             'палец', 'ряд', 'самолечение', 'тайна', 'университет', 'факультет',
             'ход', 'цепочка', 'штаны', 'щётка', 'экспресс', 'ягода', 'айсберг', 'бар',
             'вязание', 'голова', 'дворник', 'жатва', 'заказ', 'избушка',
             'компьютер', 'лестница', 'медицина', 'новый', 'огород', 'память', 'расчёт',
             'самоубийство', 'таракан', 'унитаз', 'фазан', 'царапина', 'шарик',
             'щупальце', 'экономика', 'язык', 'алфавит', 'баня', 'вектор', 'голос', 'двойник',
             'ежеминутка', 'желток', 'закат', 'извинение', 'комар', 'лен', 'мелочь', 'ножка', 'определение',
             'паркет', 'рассвет', 'сантехника', 'такси', 'увольнение', 'фальш', 'хрен', 'цветение', 'шкаф',
             'щиток', 'эмиграция', 'ядро']
FATAL_GAME_STAGE = STAGES[0]


def get_hangman_picture(tries):
    stage = STAGES[tries]
    return stage


def get_word():
    random_word = 'лесенка'  # choice(WORD_LIST)

    return random_word


def get_valid_string_input(guessed_word, prompt, len_error_message, type_error_message):
    valid_string_input = False
    input_string = input(prompt)
    while not valid_string_input:
        if input_string.isalpha():
            if len(input_string) == 1 or len(input_string) == len(guessed_word):
                valid_string_input = True
            else:
                print(len_error_message)
                input_string = input(prompt)
        else:
            print(type_error_message)
            input_string = input(prompt)

    valid_string_input = input_string
    return valid_string_input


def get_guessed_letter_indexes(word, guess_letter):
    guessed_letter_idx_list = []
    [guessed_letter_idx_list.append(i) for i in range(len(word)) if guess_letter == word[i]]
    return guessed_letter_idx_list


def hangman_game(guessed_word):
    print(GREETING)

    guessed_letters = []  # список уже названных букв
    guessed_words = []

    word_completion = WORD_COMPLETION_FILLING_CHAR * len(guessed_word)
    word_completion_list = list(word_completion)
    word_char_list = list(guessed_word)

    guessed = False
    game_lost = False

    tries_remained = MAX_TRIES_COUNT
    while not guessed and not game_lost:

        game_current_stage = get_hangman_picture(tries_remained)
        print(game_current_stage)
        print(*word_completion_list)
        enter_guess_prompt = f'{ENTER_GUESS_PROMPT_P_1}{len(guessed_word)}{ENTER_GUESS_PROMPT_P_2}{COLON_SEP}\n'
        len_error_message = f'{LEN_ERROR_MESSAGE}{len(guessed_word)}{ENTER_GUESS_PROMPT_P_2}{EXCLAMATION_SIGN}'
        input_string = get_valid_string_input(guessed_word, enter_guess_prompt, len_error_message, TYPE_ERROR_MESSAGE)

        successful_guess_processing = input_string in guessed_word and input_string != guessed_word
        while successful_guess_processing:
            guessed_letter = input_string
            guessed_letter_idx_list = get_guessed_letter_indexes(guessed_word, input_string)
            guessed_letters.append(guessed_letter)
            if guessed_letter in word_completion_list:
                print(REPEAT_ERROR)
                break

            for idx in guessed_letter_idx_list:
                for j in range(len(word_completion_list)):
                    if idx == j:
                        word_completion_list[j] = input_string
            print(*word_completion_list)
            word_completion = ''.join(word_completion_list)
            if word_completion == guessed_word or input_string == guessed_word:
                break
            else:
                input_string = get_valid_string_input(guessed_word, enter_guess_prompt, len_error_message,
                                                      TYPE_ERROR_MESSAGE)

                successful_guess_processing = input_string in guessed_word and input_string != guessed_word

        guessed = input_string == guessed_word or word_completion == guessed_word

        tries_remained -= 1
        print(WRONG_GUESS_MESSAGE)
        if tries_remained == 0:
            break

    if guessed:
        print(*word_char_list)
        print(WIN_MESSAGE)

    else:
        print(FATAL_GAME_STAGE)
        print(LOSING_MESSAGE)
        print(*word_char_list)


def main():
    guessed_word = get_word()
    hangman_game(guessed_word)


main()
