RUS_MONTHS_LIST = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
ENG_MONTHS_LIST = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
RUS_LANG = 'ru'
ENG_LANG = 'eng'


def get_month(language, number):
    if language == RUS_LANG:
        result_output = RUS_MONTHS_LIST[number - 1]
    else:
        result_output = ENG_MONTHS_LIST[number - 1]
    return result_output


def main():
    lan = input()
    num = int(input())

    month_name = get_month(lan, num)
    print(month_name)


main()