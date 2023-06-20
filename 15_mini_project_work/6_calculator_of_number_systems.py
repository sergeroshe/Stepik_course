ENTER_NUM_PROMPT = 'Enter a number in decimal number system:\n'
ENTER_BASE_PROMPT = 'Enter a base of new number system:\n'
NUMBER_SYSTEM_CHARS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


def number_sys_calc(num, base):
    quotient = num // base
    remainder = num % base
    converted_digits = NUMBER_SYSTEM_CHARS[remainder]

    while quotient >= base:
        num = quotient
        quotient = num // base
        remainder = num % base

        converted_digits += NUMBER_SYSTEM_CHARS[remainder]

    leading_converted_digit = '' if quotient == 0 else NUMBER_SYSTEM_CHARS[quotient]

    reversed_converted_digits = converted_digits[::-1]
    converted_num = leading_converted_digit + reversed_converted_digits

    return converted_num


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
