
def get_factors(num):
    dividers_list = []
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            dividers_list.append(i)

    dividers_list.append(num)
    return dividers_list


def number_of_factors(num):
    value = len(get_factors(num))
    return value


def main():
    # input
    number = int(input())
    # business logic
    factors_number = number_of_factors(number)
    # output
    print(factors_number)
    # send_sms(factors_number)


# вызываем функцию
main()
