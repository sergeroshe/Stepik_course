ENTER_NUM_PROMPT = 'Enter a number in decimal number system:\n'
ENTER_BASE_PROMPT = 'Enter a base of new number system:\n'


def number_sys_calc(num, base):

    remainder_list = []
    quotient = num // base
    remainder = num % base
    remainder_list.append(remainder)

    while quotient >= base:
        num = quotient
        quotient = num // base
        remainder = num % base
        remainder_list.append(remainder)

    remainder_list.reverse()
    remainder_list_based_num_part = ''
    for remainder in remainder_list:
        remainder_list_based_num_part += str(remainder)

    num_str = str(quotient) + remainder_list_based_num_part

    return num_str


def main():
    num = int(input(ENTER_NUM_PROMPT))
    base = int(input(ENTER_BASE_PROMPT))

    new_number_system_num = number_sys_calc(num, base)

    print(new_number_system_num)


main()
