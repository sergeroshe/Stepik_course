ENTER_NUM_PROMPT = 'Enter a number in decimal number system:\n'
NUMBER_SYSTEM_CHARS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                       'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                       'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                       'U', 'V', 'W', 'X', 'Y', 'Z', 'ﺍ', 'ﺏ', 'ﺕ', 'ﺙ']
TYPE_ERROR_MESSAGE = 'The entered data must be numeric!'
BASE_LEFT_BORDER = 1
BASE_RIGHT_BORDER = len(NUMBER_SYSTEM_CHARS) + 1
ENTER_BASE_PROMPT = f'Enter a number between {BASE_LEFT_BORDER} and {BASE_RIGHT_BORDER}' \
                        f' inclusive for base of a new number system:\n'
BASE_ERROR_MESSAGE = f'The number must be between {BASE_LEFT_BORDER} and {BASE_RIGHT_BORDER} inclusive!'


def get_num_input(prompt, error_message):
    is_string_num = False
    input_string = input(prompt)
    while not is_string_num:
        if input_string and input_string[0] == '-' and input_string[1:].isdigit() or input_string.isdigit():
            is_string_num = True
        else:
            print(error_message)
            input_string = input(prompt)

    num = int(input_string)
    return num


#  returns num input within range [left_border, right_border]
def get_constrained_num_input(enter_base_prompt, type_error_message, base_error_message, left_border, right_border):
    is_num_valid = False
    num = get_num_input(enter_base_prompt, type_error_message)
    while not is_num_valid:
        if left_border <= num <= right_border:
            is_num_valid = True
        else:
            print(base_error_message)
            num = get_num_input(enter_base_prompt, type_error_message)

    return num


def number_sys_calc(num, base):
    quotient = num // base
    remainder = num % base
    converted_digits = NUMBER_SYSTEM_CHARS[remainder]

    while quotient >= base:
        num = quotient
        quotient = num // base
        remainder = num % base

        converted_digits += NUMBER_SYSTEM_CHARS[remainder]

    leading_converted_digit = NUMBER_SYSTEM_CHARS[quotient] if quotient else ''

    reversed_converted_digits = converted_digits[::-1]
    converted_num = leading_converted_digit + reversed_converted_digits

    return converted_num


def main():

    num = get_num_input(ENTER_NUM_PROMPT, TYPE_ERROR_MESSAGE)
    base = get_constrained_num_input(ENTER_BASE_PROMPT, TYPE_ERROR_MESSAGE, BASE_ERROR_MESSAGE,
                                     BASE_LEFT_BORDER, BASE_RIGHT_BORDER)

    converted_number_system_num = number_sys_calc(num, base)

    print(converted_number_system_num)


main()
