RUSSIAN_MONTHS_LIST = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
                       'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
ENGLISH_MONTHS_LIST = ['january', 'february', 'march', 'april', 'may', 'june',
                       'july', 'august', 'september', 'october', 'november', 'december']
RUSSIAN_LANG = 'ru'


def get_month(lang, num):
    if lang == RUSSIAN_LANG:
        result_output = RUSSIAN_MONTHS_LIST[num - 1]
    else:
        result_output = ENGLISH_MONTHS_LIST[num - 1]
    return result_output


def main():
    language = input()
    number = int(input())

    month_name = get_month(language, number)
    print(month_name)


main()
