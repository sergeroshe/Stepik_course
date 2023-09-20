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


def b_o_h_number_sys_calc(num):
    bin_converted_num = bin(num)
    oct_converted_num = oct(num)
    hex_converted_num = hex(num)

    return bin_converted_num, oct_converted_num, hex_converted_num


def main():

    num = get_num_input(ENTER_NUM_PROMPT, TYPE_ERROR_MESSAGE)
    bin_converted_num, oct_converted_num, hex_converted_num = b_o_h_number_sys_calc(num)

    print(bin_converted_num[2:], oct_converted_num[2:], hex_converted_num[2:].upper(), sep='\n')


main()
