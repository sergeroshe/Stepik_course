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


def b_o_h_number_sys_calc_v2(num):
    converted_num_string = str(bin(num))[2:] + '\n' + str(oct(num))[2:] + '\n' + str(hex(num))[2:].upper()

    return converted_num_string


def main():

    num = get_num_input(ENTER_NUM_PROMPT, TYPE_ERROR_MESSAGE)
    converted_nums = b_o_h_number_sys_calc_v2(num)

    print(converted_nums)


main()
