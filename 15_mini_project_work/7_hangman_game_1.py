from random import choice

GREETING = 'Давайте играть в угадайку слов!'
ENTER_GUESS_PROMPT_P_1 = 'Введите букву или всё слово, состоящее из '
ENTER_GUESS_PROMPT_P_2 = ' букв'
WIN_MESSAGE = 'Поздравляем, вы угадали слово! Вы победили!'
WRONG_GUESS_MESSAGE = 'Ответ неверный'
GAME_LOST_MESSAGE = 'Вы проиграли.'
TYPE_ERROR_MESSAGE = 'Введенные данные должны содержать только текст!\n'
LEN_ERROR_MESSAGE = 'Введенное слово должно состоять из '
REPEAT_ERROR = 'Вы уже вводили эту букву, попробуйте другую'
COLON_SEP = ':'
EXCLAMATION_SIGN = '!'
FILLING_CHAR = '_'
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


def get_hangman_stage(tries):
    stage = STAGES[tries]
    return stage


def get_word():
    random_word = choice(WORD_LIST)

    return random_word


def get_constrained_alphabet_input(prompt, valid_len_list, len_error_message, type_error_message):
    valid_string_input = False

    input_string = input(prompt)

    while not valid_string_input:
        if input_string.isalpha():
            if len(valid_len_list) == 0:
                valid_string_input = True
            else:
                if len(input_string) in valid_len_list:
                    valid_string_input = True
                else:
                    print(len_error_message)
                    input_string = input(prompt)
        else:
            print(type_error_message)
            input_string = input(prompt)

    upper_input_string = input_string.upper()
    return upper_input_string


def find_all(source, symbol):
    symbol_idx_list = []
    start_idx = 0
    symbol_idx = source.find(symbol, start_idx)

    while symbol_idx != -1:
        symbol_idx_list.append(symbol_idx)
        start_idx = symbol_idx + 1
        symbol_idx = source.find(symbol, start_idx)

    return symbol_idx_list


def open_guessed_letters(guessed_letter_idx_list, source_word_completion_list, input_letter):
    for idx in guessed_letter_idx_list:
        for j in range(len(source_word_completion_list)):
            if idx == j:
                source_word_completion_list[j] = input_letter

    result_word_completion_list = source_word_completion_list
    return result_word_completion_list


def game_stage_display(tries_remained):
    game_current_stage = get_hangman_stage(tries_remained)
    if tries_remained < MAX_TRIES_COUNT:
        print(WRONG_GUESS_MESSAGE)
    print(game_current_stage)

    return game_current_stage


def get_prompt(guessed_word):
    enter_guess_prompt = f'{ENTER_GUESS_PROMPT_P_1}{len(guessed_word)}{ENTER_GUESS_PROMPT_P_2}{COLON_SEP}\n'
    len_error_message = f'{LEN_ERROR_MESSAGE}{len(guessed_word)}{ENTER_GUESS_PROMPT_P_2}{EXCLAMATION_SIGN}'

    return enter_guess_prompt, len_error_message


def guess_processing(input_string, valid_len_list, guessed_word, guessed_letters,
                     word_completion_list, word_char_list, enter_guess_prompt, len_error_message):
    input_letter = input_string
    guessed = False
    guessed_letter_idx_list = find_all(guessed_word, input_letter)

    if input_letter in guessed_letters:
        print(REPEAT_ERROR)

        guessed_letters.append(input_letter)

    word_completion_list = open_guessed_letters(guessed_letter_idx_list, word_completion_list, input_string)

    if word_completion_list == word_char_list:
        guessed = True
    else:
        print(*word_completion_list)
        # get_constrained_alphabet_input(prompt, valid_len_list, len_error_message, type_error_message)
        input_string = get_constrained_alphabet_input(enter_guess_prompt, valid_len_list,
                                                      len_error_message, TYPE_ERROR_MESSAGE)

    return guessed, input_string, word_completion_list


def game_run(tries_remained, guessed_word, guessed_letters, word_char_list, word_completion_list):
    guessed = guessed_word == word_char_list
    game_lost = False
    valid_input_len_list = []

    while not guessed and not game_lost:

        game_stage_display(tries_remained)

        print(*word_completion_list)

        enter_guess_prompt, len_error_message = get_prompt(guessed_word)
        input_string = get_constrained_alphabet_input(enter_guess_prompt, valid_input_len_list,
                                                      len_error_message, TYPE_ERROR_MESSAGE)
        successful_guess_processing = (input_string in guessed_word and input_string != guessed_word
                                       and word_completion_list != word_char_list)

        while successful_guess_processing:
            guessed, input_string, word_completion_list = guess_processing(input_string, valid_input_len_list,
                                                                           guessed_word, guessed_letters,
                                                                           word_completion_list, word_char_list,
                                                                           enter_guess_prompt, len_error_message)

            successful_guess_processing = (input_string in guessed_word and input_string != guessed_word and
                                           word_completion_list != word_char_list)

        guessed = input_string == guessed_word or word_completion_list == word_char_list

        tries_remained -= 1
        game_lost = not tries_remained

    print(*word_char_list)
    if guessed:
        print(WIN_MESSAGE)
    else:
        print(FATAL_GAME_STAGE)
        print(GAME_LOST_MESSAGE)


def hangman_game(guessed_word):
    print(GREETING)
    print(guessed_word)

    guessed_letters = []  # список уже названных букв
    guessed_words = []

    word_completion = FILLING_CHAR * len(guessed_word)
    word_completion_list = list(word_completion)

    word_char_list = list(guessed_word)
    tries_remained = MAX_TRIES_COUNT

    game_run(tries_remained, guessed_word, guessed_letters, word_char_list, word_completion_list)


def main():
    guessed_word = get_word().upper()
    hangman_game(guessed_word)


main()
