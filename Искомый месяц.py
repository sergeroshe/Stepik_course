# объявление функции
lng_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']

lng_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']


def get_month(language, number):
    result_output = ''
    if lan == "ru":
        result_output = lng_ru[num - 1]
    else:
        result_output = lng_en[num - 1]
    return result_output


# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))