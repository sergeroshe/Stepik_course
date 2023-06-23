from random import choice
GREETING = 'Давайте играть в угадайку слов!'
ENTER_GUESS_PROMPT_P_1 = 'Введите букву или всё слово, состоящее из '
ENTER_GUESS_PROMPT_P_2 = ' букв:\n'
TYPE_ERROR_MESSAGE = 'Введенные данные должны содержать только текст!\n'
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


def get_hangman_picture(tries):
    stage = STAGES[tries]
    return stage


def get_word():
    random_word = 'лесенка' # choice(WORD_LIST)

    return random_word


def get_string_input(guessed_word, prompt, error_message):
    is_input_string = False
    input_string = input(prompt)
    while not is_input_string:
        if input_string.isalpha() and len(input_string) == 1 or len(input_string) == len(guessed_word):
            is_input_string = True
        else:
            print(error_message)
            input_string = input(prompt)

    valid_string_input = input_string
    return valid_string_input


def get_guessed_letter_indexes(word, guess_letter):
    guessed_letter_idx_list = []
    [guessed_letter_idx_list.append(i) for i in range(len(word)) if guess_letter == word[i]]
    return guessed_letter_idx_list


def play(word):
    print(GREETING)
    guessed_letters = []  # список уже названных букв
    guessed_words = []
    word_completion = WORD_COMPLETION_FILLING_CHAR * len(word)
    word_completion_list = list(word_completion)
    guessed = False
    i = len(STAGES) - 1
    while not guessed:
        game_current_stage = get_hangman_picture(i)
        print(game_current_stage)
        print(*word_completion_list)
        enter_guess_prompt = f'{ENTER_GUESS_PROMPT_P_1}{len(word)}{ENTER_GUESS_PROMPT_P_2}'
        input_string = get_string_input(word, enter_guess_prompt, TYPE_ERROR_MESSAGE)
        if input_string in word:
            guessed_letter_idx_list = get_guessed_letter_indexes(word, input_string)
            for idx in guessed_letter_idx_list:
                for j in range(len(word_completion_list)):
                    if idx == j:
                        word_completion_list[j] = input_string

        i -= 1


def main():
    guessed_word = get_word()
    play(guessed_word)


main()
