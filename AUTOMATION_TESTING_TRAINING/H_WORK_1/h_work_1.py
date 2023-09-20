# Задание со звёздочкой.
# Дано:
# num_str = '123'
# Требуется написать код который переводит данную строку в int
# без использования функции int. Подсказка - можно пользоваться ord и chr.

def convert_str_to_int(input_string) -> int:
    len_string = len(input_string)
    num = 0
    for i in range(len(input_string)):
        dig = ord(input_string[i]) - 48
        num += dig * 10 ** ((len_string - 1) - i)

    return num


def convert_int_to_str(input_num) -> str:
    reverse_num_string = ''
    while input_num:
        reverse_num_string += chr((input_num % 10) + 48)
        input_num //= 10
    num_string = reverse_num_string[::-1]
    return num_string


def main():
    source_string = input()
    source_num = int(input())

    result_num = convert_str_to_int(source_string)
    result_string = convert_int_to_str(source_num)

    print(result_num, type(result_num), result_string, type(result_string), sep='\n')


main()
