ENTER_NUM_PROMPT = 'Enter a number in decimal number system:\n'
ENTER_BASE_PROMPT = 'Enter a base of new number system:\n'
NUMBER_SYSTEM_CHARS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
# HEX_SYSTEM_CHARS = ['A', 'B', 'C', 'D', 'E', 'F']


def number_sys_calc(num, base):
    quotient = num // base
    remainder = num % base
    # if base == 16 and remainder > 9:
    #     remainder = HEX_SYSTEM_CHARS[remainder - 10]
    last_num_part = str(NUMBER_SYSTEM_CHARS[remainder])

    while quotient >= base:
        num = quotient
        quotient = num // base
        remainder = num % base
        # if base == 16 and remainder > 9:
        #     remainder = NUMBER_SYSTEM_CHARS[remainder]
        last_num_part += str(remainder)
    # if base == 16:
    if 9 < quotient < 16:
        quotient = NUMBER_SYSTEM_CHARS[quotient]
    #     el
    if 0 == quotient:
        quotient = ''

    num_last_part = last_num_part[::-1]
    num_str = str(quotient) + num_last_part

    return num_str


def main():
    num = int(input(ENTER_NUM_PROMPT))
    # base = int(input(ENTER_BASE_PROMPT))

    binary_number_system_num = number_sys_calc(num, base=2)
    octal_number_system_num = number_sys_calc(num, base=8)
    hexadecimal_number_system_num = number_sys_calc(num, base=16)

    print(binary_number_system_num)
    print(octal_number_system_num)
    print(hexadecimal_number_system_num)


main()
