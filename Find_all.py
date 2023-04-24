def find_all(target, symbol):
    symbol_idx_list = []
    for i in range(len(target)):
        symbol_idx = target.find(symbol, i)
        if target[i] == symbol:
            symbol_idx_list.append(symbol_idx)

    return symbol_idx_list
# use find, var.:target_string


def main():
    target_string = input()  # maybe source-string?
    char = input()
    print(find_all(target_string, char))


main()








# Найти всех
# Напомним, что строковый метод find('a') возвращает местоположение первого вхождения символа a в строке.
# Проблема заключается в том, что данный метод не находит местоположение всех символов а.
# Напишите функцию с именем find_all(target, symbol), которая принимает два аргумента:
# строку target и символ symbol и возвращает список, содержащий все местоположения этого символа в строке.
# Примечание 1. Если указанный символ не встречается в строке, то следует вернуть пустой список.