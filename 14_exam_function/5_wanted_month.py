RUSSIAN_MONTHS_LIST = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
                       'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
ENGLISH_MONTHS_LIST = ['january', 'february', 'march', 'april', 'may', 'june',
                       'july', 'august', 'september', 'october', 'november', 'december']
RUSSIAN_LANG = 'ru'


def get_month(lang, num, russian_months_list, english_months_list, russian_lang):
    if lang == russian_lang:
        result_output = russian_months_list[num - 1]
    else:
        result_output = english_months_list[num - 1]
    return result_output


def main():
    language = input()
    number = int(input())

    month_name = get_month(language, number, RUSSIAN_MONTHS_LIST,
                           ENGLISH_MONTHS_LIST, RUSSIAN_LANG)
    print(month_name)
