NUM_WORD_LIST = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь',
                 'восемь', 'девять', 'десять', 'одиннадцать', 'двенадцать',
                 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать',
                 'семнадцать', 'восемнадцать', 'девятнадцать', 'двадцать',
                 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят',
                 'восемьдесят', 'девяносто', '']
SEPARATOR = '_'


def number_to_words(num):
    result_output = ''
    if num <= 20:
        result_output = NUM_WORD_LIST[num - 1]
    else:
        result_output = NUM_WORD_LIST[num // 10 + 17] + SEPARATOR + NUM_WORD_LIST[num % 10 - 1]

    return result_output


def main():
    n = int(input())

    number_in_words = number_to_words(n)

    print(number_in_words)


main()