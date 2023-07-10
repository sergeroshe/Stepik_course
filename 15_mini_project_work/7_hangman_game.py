from random import choice, randrange

GREETING = 'Давайте играть в угадайку слов!'
ENTER_GUESS_PROMPT = 'Введите букву или всё слово, состоящее из {word_len} букв:\n'
ENTER_PRE_GUESSED_LETTER_POSITION_PROMPT = 'Введите номер буквы, которую необходимо открыть.\n' \
                                           'Если вы хотите самостоятельно угадать ВСЕ буквы слова, нажмите ENTER:\n'
RE_ENTER_PRE_GUESSED_LETTER_POSITION_PROMPT = 'Хотите открыть еще одну букву? ' \
                                              'Если да - введите число - номер позиции открываемой буквы в слове:\n'
WORD_DESCRIPTION_MESSAGE = 'Загаданное слово состоит из {word_len} букв и относится к категории "{category_name}"'
WIN_MESSAGE = 'Поздравляем, вы угадали слово! Вы победили!'
WRONG_GUESS_MESSAGE = 'Ответ неверный'
GAME_LOST_MESSAGE = 'Вы проиграли.'
TYPE_ERROR_MESSAGE = 'Введенные данные должны содержать только текст!\n'
LEN_ERROR_MESSAGE = 'Введенное слово должно состоять из {word_len} букв!'
REPEAT_ERROR = 'Вы уже вводили эту букву, попробуйте другую'
RANGE_ERROR_MESSAGE = 'Число должно быть от 1 до {last_letter_position} включительно!'
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
PREGUESSED_LETTER_IDX_LIST = [0, 2, -1]
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


def open_guessed_letters(guessed_letter_idx_list, word_char_completion_list, guessed_letter):
    for idx in guessed_letter_idx_list:
        word_char_completion_list[idx] = guessed_letter

    return word_char_completion_list


def game_stage_display(tries_remained):
    game_current_stage = get_hangman_stage(tries_remained)
    print(game_current_stage)


def get_dialog_messages(hidden_word, category_name):
    hidden_word_len = len(hidden_word)
    enter_guess_prompt = ENTER_GUESS_PROMPT.format(word_len=hidden_word_len, category_name=category_name)
    len_error_message = LEN_ERROR_MESSAGE.format(word_len=hidden_word_len)

    return enter_guess_prompt, len_error_message


def print_current_game_status(tries_remained, word_completion_list):
    game_stage_display(tries_remained)
    print(*word_completion_list)


def print_game_result(word_char_list, game_won):
    print(*word_char_list)
    if game_won:
        print(WIN_MESSAGE)
    else:
        print(FATAL_GAME_STAGE)
        print(GAME_LOST_MESSAGE)


def get_constrained_num_input(num, enter_letter_position_prompt, range_error_message,
                              left_border, right_border):
    is_num_valid = False
    while not is_num_valid:
        if left_border <= num <= right_border:
            is_num_valid = True
        else:
            print(range_error_message)
            num = int(input(enter_letter_position_prompt))

    return num


def get_distinct_num_input(num, num_list,
                           max_num, repeat_error):
    num_distinct = False
    while not num_distinct:
        print(repeat_error)
        num = get_num_input(ENTER_PRE_GUESSED_LETTER_POSITION_PROMPT.format(word_len=max_num), NON_NUMERIC_ERROR_MESSAGE)
        get_constrained_num_input(num,
                                  ENTER_PRE_GUESSED_LETTER_POSITION_PROMPT
                                  .format(word_len=max_num),
                                  RANGE_ERROR_MESSAGE.format
                                  (last_letter_position=max_num),
                                  1, max_num)
        num_distinct = num not in num_list
    return num


def get_num_input(prompt, error_message):
    is_string_num = False
    input_string = input(prompt)
    while not is_string_num:
        if input_string and input_string[0] == '-' and input_string[1:].isdigit() or input_string.isdigit():
            is_string_num = True
        else:
            print(error_message)
            input_string = input(prompt)

    num = int(input_string)
    return num


def get_pre_guessed_letters_idx_list(hidden_word):
    last_letter_position = len(hidden_word)
    pre_guessed_letters_list = []
    pre_guessed_letters_list_full = False
    while not pre_guessed_letters_list_full:
        if not pre_guessed_letters_list:
            pre_guessed_letter_idx = input(ENTER_PRE_GUESSED_LETTER_POSITION_PROMPT.
                                           format(word_len=last_letter_position))
        else:
            pre_guessed_letter_idx = input(RE_ENTER_PRE_GUESSED_LETTER_POSITION_PROMPT)
        if not pre_guessed_letter_idx.isdigit():
            pre_guessed_letters_list_full = True
        else:

            pre_guessed_letter_idx = get_constrained_num_input(int(pre_guessed_letter_idx),
                                                               ENTER_PRE_GUESSED_LETTER_POSITION_PROMPT
                                                               .format(word_len=last_letter_position),
                                                               RANGE_ERROR_MESSAGE.format
                                                               (last_letter_position=last_letter_position),
                                                               1, last_letter_position)
            pre_guessed_letter_position = pre_guessed_letter_idx - 1
            if pre_guessed_letter_position not in pre_guessed_letters_list:
                distinct_pre_guessed_letter_position = pre_guessed_letter_position
            else:
                distinct_pre_guessed_letter_position = get_distinct_num_input(
                    pre_guessed_letter_position,
                    pre_guessed_letters_list, last_letter_position, REPEAT_ERROR)
            pre_guessed_letters_list.append(distinct_pre_guessed_letter_position)
            pre_guessed_letters_list_full = len(pre_guessed_letters_list) == len(hidden_word)

    return pre_guessed_letters_list


def game_run(tries_remained, hidden_word, category_name):
    print(GREETING)
    hidden_word_len = len(hidden_word)
    print(WORD_DESCRIPTION_MESSAGE.format(word_len=hidden_word_len, category_name=category_name))
    word_char_list = list(hidden_word)
    game_won = False
    valid_input_len_list = [1, hidden_word_len]
    enter_guess_prompt, len_error_message = get_dialog_messages(hidden_word, category_name)
    guessed_letters = []
    pre_guessed_letters_list = get_pre_guessed_letters_idx_list(hidden_word)
    word_char_completion_list = get_word_char_completion_list(hidden_word, pre_guessed_letters_list)
    while not game_won and tries_remained:
        print_current_game_status(tries_remained, word_char_completion_list)

        input_string = get_constrained_alphabet_input(enter_guess_prompt, valid_input_len_list,
                                                      len_error_message, TYPE_ERROR_MESSAGE).upper()
        if input_string == hidden_word:
            game_won = True
        elif len(input_string) == 1:
            input_letter = input_string
            if input_letter not in guessed_letters:
                guessed_letters.append(input_letter)
                if input_letter in hidden_word:
                    guessed_letter_idx_list = find_all(hidden_word, input_letter)
                    word_char_completion_list = open_guessed_letters(guessed_letter_idx_list,
                                                                     word_char_completion_list, input_letter)
                    game_won = word_char_completion_list == word_char_list
                else:
                    print(WRONG_GUESS_MESSAGE)
                    tries_remained -= 1
            else:
                print(REPEAT_ERROR)
                tries_remained -= 1
        else:
            print(WRONG_GUESS_MESSAGE)
            tries_remained -= 1

    print_game_result(word_char_list, game_won)


def get_word_char_completion_list(hidden_word, preguessed_char_idx_list):
    word_completion = FILLING_CHAR * len(hidden_word)
    word_char_completion_list = list(word_completion)
    for i in range(len(preguessed_char_idx_list)):
        word_char_completion_list[preguessed_char_idx_list[i]] = hidden_word[preguessed_char_idx_list[i]]

    return word_char_completion_list


def main():
    game_is_going_on = True
    while game_is_going_on:
        hidden_word, category_name = get_hidden_word_with_category()
        game_run(MAX_TRIES_COUNT, hidden_word, category_name)
        new_game_wish = input(NEW_GAME_PROPOSAL_MESSAGE).lower()
        game_is_going_on = new_game_wish == YES_RESPONSE

    print(FAREWELL_MESSAGE)


main()
