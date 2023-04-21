# объявление функции
def get_factors(num):
    div_amount = 0
    for i in range(1, num + 1):
        if num % i == 0:
            div_amount += 1

    return div_amount


def main():
    # считываем данные
    given_num = int(input())
    print(get_factors(given_num))


# вызываем функцию
main()
