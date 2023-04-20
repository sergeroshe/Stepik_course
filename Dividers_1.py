# объявление функции
def get_factors(num):

    dividers_list = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            dividers_list.append(i)

    return dividers_list + [num]


def main():
    # считываем данные
    given_num = int(input())
    print(get_factors(given_num))


# вызываем функцию
main()

#  Напишите функцию get_factors(num),
#  принимающую в качестве аргумента натуральное число
#  и возвращающую список всех делителей данного числа.