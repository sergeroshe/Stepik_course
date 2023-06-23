from random import choice
GREETING = 'Давайте играть в угадайку слов!'
ENTER_GUESS_PROMPT = 'Введите букву или всё слово целиком:\n'
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


def get_string_input(prompt, error_message):
    is_input_string = False
    input_string = input(prompt)
    while not is_input_string:
        if input_string.isalpha():
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
        guess_letter = get_string_input(ENTER_GUESS_PROMPT, TYPE_ERROR_MESSAGE)
        if guess_letter in word:
            guessed_letter_idx_list = get_guessed_letter_indexes(word, guess_letter)

            for j in range(len(guessed_letter_idx_list)):
                for k in range(len(word_completion_list)):
                    if guessed_letter_idx_list[j] == k:
                        word_completion_list[k] = guess_letter
        i -= 1


def main():
    word = get_word()
    play(word)


main()
