ENTER_NUM_PROMPT = 'Enter a number in decimal number system:\n'
TYPE_ERROR_MESSAGE = 'The entered data must be numeric!'


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


def main():

    num = get_num_input(ENTER_NUM_PROMPT, TYPE_ERROR_MESSAGE)

    binary_number_system_num = str(bin(num))[2:]
    octal_number_system_num = str(oct(num))[2:]
    hexadecimal_number_system_num = str(hex(num))[2:].upper()

    print(binary_number_system_num)
    print(octal_number_system_num)
    print(hexadecimal_number_system_num)


main()
