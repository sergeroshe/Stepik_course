from random import choice, randrange

GREETING = 'Давайте играть в угадайку слов!'
ENTER_GUESS_PROMPT = 'Введите букву или всё слово, состоящее из {word_len} букв:\n'
ENTER_PRE_GUESSED_CHAR_POSITION_PROMPT = 'Введите номер буквы, которую необходимо открыть.\n' \
                                         'Если вы хотите самостоятельно угадать ВСЕ буквы слова, нажмите ENTER:\n'
ENTER_NUMBER_PROMPT = 'Введите число:\n'
WORD_DESCRIPTION_MESSAGE = 'Загаданное слово состоит из {word_len} букв и относится к категории "{category_name}"'
WIN_MESSAGE = 'Поздравляем, вы угадали слово! Вы победили!'
WRONG_GUESS_MESSAGE = 'Ответ неверный'
GAME_LOST_MESSAGE = 'Вы проиграли.'
TYPE_ERROR_MESSAGE = 'Введенные данные должны содержать только текст!\n'
HIDDEN_WORD_REVEALED_MESSAGE = 'Вы открыли все буквы слова.'
LEN_ERROR_MESSAGE = 'Введенное слово должно состоять из {word_len} букв!'
REPEAT_CHAR_ERROR = 'Вы уже вводили эту букву, попробуйте другую'
REPEAT_NUMBER_ERROR = 'Вы уже вводили эту цифру, попробуйте другую'
RANGE_ERROR_MESSAGE = 'Число должно быть от 1 до {last_char_position} включительно!'
NON_NUMERIC_ERROR_MESSAGE = 'Введенные данные должны быть числовыми!'
FILLING_CHAR = '_'
NEW_GAME_PROPOSAL_MESSAGE = 'Хотите сыграть еще? \nНажмите: "1", затем: ENTER, ' \
                            'если ДА\nНажмите любую клавишу, затем: ENTER, если НЕТ\n'
FAREWELL_MESSAGE = 'Спасибо, что играли в угадайку слов! Еще увидимся...'
YES_RESPONSE = '1'
STAGES = [  # финальное состояние: голова, торс, обе руки, обе ноги

    '''
                   --------
                   |      |
                   |      ☻
                   |     _|_
                   |    / | \\
                   |     / \\
                   -   _/   \\_
                ''',
    '''
                   --------
                   |      |
                   |      ☺
                   |     _|_
                   |    / | \\
                   |     / \\
                   -   _/   \\
                ''',
    '''
                   --------
                   |      |
                   |      ☺
                   |     _|_
                   |    / | \\
                   |     / \\
                   -    /   \\
                ''',
    # голова, торс, обе руки, одна нога
    '''
                   --------
                   |      |
                   |      ☺
                   |     _|_
                   |    / | \\
                   |     / 
                   -    /   
                ''',
    # голова, торс, обе руки
    '''
                   --------
                   |      |
                   |      ☺
                   |     _|_
                   |    / | \\
                   |     
                   -    
                ''',
    # голова, торс и одна рука
    '''
                   --------
                   |      |
                   |      ☺
                   |     _|_
                   |    / | 
                   |    
                   -    
                ''',
    # голова и торс
    '''
                   --------
                   |      |
                   |      ☺
                   |     _|_
                   |   
                   |    
                   -    
                ''',
    # голова
    '''
                   --------
                   |      |
                   |      ☺
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
FOODS = ['желток', 'арбуз', 'банан', 'хлеб', 'яблоко', 'колбаса',
         'сахар', 'творог', 'хрен', 'шоколад', 'каша', 'макароны', 'рис', 'лаваш']
ANIMALS_PLANTS = ['ягода', 'комар', 'фазан', 'таракан', 'ландыш', 'гиббон',
                  'щука', 'еж', 'зебра', 'щенок', 'голубь', 'утка', 'ежик',
                  'рыба', 'улитка', 'цыпленок', 'яблоня', 'цветок']
NATURE = ['лес', 'корень', 'река', 'песок', 'лен', 'айсберг', 'цветение', 'закат']
TRANSPORT = ['вагон', 'двигатель', 'корабль', 'трамвай', 'аэропорт',
             'самолет', 'авиалиния', 'автомобиль', 'экспресс', 'такси']
MUSICAL_INSTRUMENTS = ['пианино', 'гитара', 'скрипка', 'барабан', 'кларнет', 'саксофон', 'укулеле']

OTHER_WORDS = ['дом', 'железо',
               'игла', 'мама', 'нос', 'окно',
               'солнце', 'улица', 'фонарь',
               'шар', 'электроника', 'юбка',
               'бумага', 'вышка', 'дверь',
               'ежедневник', 'замок', 'изделие', 'лавка',
               'магазин', 'нож', 'опера', 'ручка', 'таблица',
               'флаг', 'холодильник', 'церковь', 'шапка',
               'электричество', 'ящик', 'булавка', 'выставка',
               'горка', 'желание', 'зачёт', 'изучение',
               'лампа', 'марка', 'ночь', 'обувь', 'парад',
               'фильм', 'художник', 'щит', 'энергия', 'бюджет',
               'выход', 'город', 'дверца', 'ежемесячник', 'завод',
               'измерение', 'колесник', 'математика', 'нота', 'область',
               'палец', 'ряд', 'самолечение', 'тайна', 'университет', 'факультет',
               'ход', 'цепочка', 'штаны', 'щётка', 'бар',
               'вязание', 'голова', 'дворник', 'жатва', 'заказ', 'избушка',
               'компьютер', 'лестница', 'медицина', 'огород', 'память', 'расчёт',
               'самоубийство', 'унитаз', 'царапина', 'шарик',
               'щупальце', 'экономика', 'язык', 'алфавит', 'баня', 'вектор', 'голос', 'двойник',
               'ежеминутка', 'извинение', 'мелочь', 'ножка', 'определение',
               'паркет', 'рассвет', 'сантехника', 'увольнение', 'фальш', 'шкаф',
               'щиток', 'эмиграция', 'ядро']
CATEGORIZED_WORD_LIST = [['Продукты', FOODS],
                         ['Животные и растения', ANIMALS_PLANTS],
                         ['Природа', NATURE],
                         ['Транспорт', TRANSPORT],
                         ['Музыкальные инструменты', MUSICAL_INSTRUMENTS],
                         ['Другие слова', OTHER_WORDS]]
PREGUESSED_CHAR_IDX_LIST = [0, 2, -1]
FATAL_GAME_STAGE = STAGES[0]
MAX_TRIES_COUNT = len(STAGES) - 1


def get_hangman_stage(tries):
    stage = STAGES[tries]
    return stage


def get_hidden_word_with_category():
    category_idx = randrange(0, len(CATEGORIZED_WORD_LIST) - 1)
    category_word_list = CATEGORIZED_WORD_LIST[category_idx][1]
    category_name = CATEGORIZED_WORD_LIST[category_idx][0]
    random_word = choice(category_word_list).upper()
    return random_word, category_name


def get_constrained_alphabet_input(prompt, valid_len_list, len_error_message, type_error_message):
    valid_string_input = False

    input_string = input(prompt)

    while not valid_string_input:
        if input_string.isalpha():
            if not valid_len_list:
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

    return input_string


def find_all(source, symbol):
    symbol_idx_list = []
    start_idx = 0
    symbol_idx = source.find(symbol, start_idx)

    while symbol_idx != -1:
        symbol_idx_list.append(symbol_idx)
        start_idx = symbol_idx + 1
        symbol_idx = source.find(symbol, start_idx)

    return symbol_idx_list


def open_guessed_chars(guessed_char_idx_list, word_char_completion_list, guessed_char):
    for idx in guessed_char_idx_list:
        word_char_completion_list[idx] = guessed_char

    return word_char_completion_list


def print_game_stage(tries_remained):
    game_current_stage = get_hangman_stage(tries_remained)
    print(game_current_stage)


def get_dialog_messages(hidden_word, category_name):
    hidden_word_len = len(hidden_word)
    enter_guess_prompt = ENTER_GUESS_PROMPT.format(word_len=hidden_word_len, category_name=category_name)
    len_error_message = LEN_ERROR_MESSAGE.format(word_len=hidden_word_len)

    return enter_guess_prompt, len_error_message


def print_game_start_info(tries_remained, word_completion_list):
    print_game_stage(tries_remained)
    print(*word_completion_list)


def print_game_result(word_char_list, game_won):
    print(*word_char_list)
    if game_won:
        print(WIN_MESSAGE)
    else:
        print(FATAL_GAME_STAGE)
        print(GAME_LOST_MESSAGE)


def get_num_input(prompt, error_message, none_accepted):
    is_input_valid = False
    input_string = input(prompt)
    num = None
    while not is_input_valid:
        if input_string and input_string[0] == '-' and input_string[1:].isdigit() or input_string.isdigit():
            num = int(input_string)
            is_input_valid = True
        elif not input_string and none_accepted:
            is_input_valid = True
        else:
            print(error_message)
            input_string = input(prompt)
    return num


def get_constrained_num_input(enter_base_prompt, type_error_message, base_error_message, left_border,
                              right_border, none_accepted):
    is_num_valid = False
    num = get_num_input(enter_base_prompt, type_error_message, none_accepted)
    while not is_num_valid:
        if num is not None and left_border <= num <= right_border:
            is_num_valid = True
        elif num is None and none_accepted:
            is_num_valid = True
        else:
            print(base_error_message)
            num = get_num_input(enter_base_prompt, type_error_message, none_accepted)

    return num


def get_pre_guessed_char_idx_list(hidden_word):
    hidden_word_len = len(hidden_word)
    pre_guessed_char_idx_list = []
    pre_guessed_char_idx_list_len = 0
    pre_guessed_input_complete = False

    while not pre_guessed_input_complete:
        pre_guessed_char_position = get_constrained_num_input(ENTER_PRE_GUESSED_CHAR_POSITION_PROMPT.
                                                              format(last_char_position=hidden_word_len),
                                                              TYPE_ERROR_MESSAGE,
                                                              RANGE_ERROR_MESSAGE.format
                                                              (last_char_position=hidden_word_len),
                                                              1, hidden_word_len, True)
        if pre_guessed_char_position is not None:
            pre_guessed_char_idx = pre_guessed_char_position - 1
            if pre_guessed_char_idx not in pre_guessed_char_idx_list:
                pre_guessed_char_idx_list.append(pre_guessed_char_idx)
                pre_guessed_char_idx_list_len += 1
                pre_guessed_input_complete = pre_guessed_char_idx_list_len == hidden_word_len
            else:
                print(REPEAT_NUMBER_ERROR)
        else:
            pre_guessed_input_complete = True

    return pre_guessed_char_idx_list


def is_hidden_word_revealed(pre_guessed_char_idx_list, hidden_word):
    hidden_word_revealed = len(pre_guessed_char_idx_list) == len(hidden_word)
    return hidden_word_revealed


def print_game_starting_status(hidden_word_len, category_name):
    print(GREETING)
    print(WORD_DESCRIPTION_MESSAGE.format(word_len=hidden_word_len, category_name=category_name))


def hangman_game(max_tries_count, hidden_word, category_name):
    hidden_word_len = len(hidden_word)
    print_game_starting_status(hidden_word_len, category_name)
    word_char_list = list(hidden_word)

    pre_guessed_char_idx_list = get_pre_guessed_char_idx_list(hidden_word)

    if not is_hidden_word_revealed(pre_guessed_char_idx_list, hidden_word):
        word_char_completion_list = get_word_char_completion_list(hidden_word, pre_guessed_char_idx_list)
        game_won = hangman_game_run(hidden_word, category_name, max_tries_count, word_char_completion_list)
        print_game_result(word_char_list, game_won)
    else:
        print_hidden_word_revelation(word_char_list)


def hangman_game_run(hidden_word, category_name, max_tries_count, word_char_completion_list):
    word_char_list = list(hidden_word)
    hidden_word_len = len(hidden_word)
    tries_remained = max_tries_count
    guessed_chars = []
    valid_input_len_list = [1, hidden_word_len]
    enter_guess_prompt, len_error_message = get_dialog_messages(hidden_word, category_name)
    game_won = False
    while not game_won and tries_remained:
        print_game_start_info(tries_remained, word_char_completion_list)
        input_string = get_constrained_alphabet_input(enter_guess_prompt, valid_input_len_list,
                                                      len_error_message, TYPE_ERROR_MESSAGE).upper()
        if input_string == hidden_word:
            game_won = True
        elif len(input_string) == 1:
            tries_remained = process_char(hidden_word, input_string, guessed_chars,
                                          word_char_completion_list, tries_remained)
            game_won = word_char_completion_list == word_char_list
        else:
            print(WRONG_GUESS_MESSAGE)
            tries_remained -= 1
    return game_won


def process_char(hidden_word, input_char, guessed_chars, word_char_completion_list, tries_remained):
    if input_char not in guessed_chars:
        guessed_chars.append(input_char)
        if input_char in hidden_word:
            guessed_char_idx_list = find_all(hidden_word, input_char)
            open_guessed_chars(guessed_char_idx_list, word_char_completion_list, input_char)
        else:
            print(WRONG_GUESS_MESSAGE)
            tries_remained -= 1
    else:
        print(REPEAT_CHAR_ERROR)
        tries_remained -= 1

    return tries_remained


def print_hidden_word_revelation(word_char_list):
    print(HIDDEN_WORD_REVEALED_MESSAGE)
    print(*word_char_list)


def get_word_char_completion_list(hidden_word, preguessed_char_idx_list):
    word_completion = FILLING_CHAR * len(hidden_word)
    word_char_completion_list = list(word_completion)
    if preguessed_char_idx_list:
        for idx in range(len(preguessed_char_idx_list)):
            word_char_completion_list[idx] = hidden_word[idx]

    return word_char_completion_list


def main():
    game_is_going_on = True
    while game_is_going_on:
        hidden_word, category_name = get_hidden_word_with_category()
        hangman_game(MAX_TRIES_COUNT, hidden_word, category_name)
        new_game_wish = input(NEW_GAME_PROPOSAL_MESSAGE).lower()
        game_is_going_on = new_game_wish == YES_RESPONSE

    print(FAREWELL_MESSAGE)


main()
