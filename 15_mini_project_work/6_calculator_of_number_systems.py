ENTER_NUM_PROMPT = 'Enter a number in decimal number system:\n'
ENTER_BASE_PROMPT = 'Enter a base of new number system:\n'
HEX_SYSTEM_CHARS = ['A', 'B', 'C', 'D', 'E', 'F']


def number_sys_calc(num, base):

    # remainder_list = []
    quotient = num // base
    remainder = num % base
    if base == 16 and remainder > 9:
        remainder = HEX_SYSTEM_CHARS[remainder - 10]
    remainder_list_based_num_part = str(remainder)

    while quotient >= base:
        num = quotient
        quotient = num // base
        remainder = num % base
        if base == 16 and remainder > 9:
            remainder = HEX_SYSTEM_CHARS[remainder - 10]
        remainder_list_based_num_part += str(remainder)
    if base == 16 and 9 < quotient < 16:
        quotient = HEX_SYSTEM_CHARS[quotient - 10]
    num_last_part = remainder_list_based_num_part[::-1]
    num_str = str(quotient) + num_last_part

    return num_str


def main():
    num = int(input(ENTER_NUM_PROMPT))
    base = int(input(ENTER_BASE_PROMPT))

    new_number_system_num = number_sys_calc(num, base)

    print(new_number_system_num)


main()
