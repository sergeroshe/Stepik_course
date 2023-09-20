def get_factors(num):
    dividers_list = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            dividers_list.append(i)

    dividers_list.append(num)
    return dividers_list


def main():
    count = 0
    # считываем данные
    given_num = int(input())
    for factor in get_factors(given_num):
        count += 1
    print(count)


main()
