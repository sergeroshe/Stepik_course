from random import choice

word_list = ['арбуз', 'банан', 'вагон', 'гиббон', 'дом', 'еж', 'железо',
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
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
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
    return stages[tries]


def get_word():
    random_word = choice(word_list)

    return random_word


def main():
    pass


main()
