ENTER_NUM_PROMPT = 'Enter a number in decimal number system:\n'
TYPE_ERROR_MESSAGE = 'The entered data must be numeric!'
NUMBER_SYSTEMS_BASE_LIST = [2, 8, 16]


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


def b_o_h_number_sys_calc(num):
    converted_num_string = ''
    for base in NUMBER_SYSTEMS_BASE_LIST:
        if base == 2:
            converted_num_string += str(bin(num))[2:] + '\n'
        elif base == 8:
            converted_num_string += str(oct(num))[2:] + '\n'
        else:
            converted_num_string += str(hex(num))[2:].upper() + '\n'

    return converted_num_string


def main():

    num = get_num_input(ENTER_NUM_PROMPT, TYPE_ERROR_MESSAGE)
    converted_nums = b_o_h_number_sys_calc(num)

    print(converted_nums)


main()
