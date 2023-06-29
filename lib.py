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


def find_all(source, symbol):
    symbol_idx_list = []
    start_idx = 0
    symbol_idx = source.find(symbol, start_idx)

    while symbol_idx != -1:
        symbol_idx_list.append(symbol_idx)
        start_idx = symbol_idx + 1
        symbol_idx = source.find(symbol, start_idx)

    return symbol_idx_list


def get_constrained_alphabet_input(prompt, valid_len_list, len_error_message, type_error_message):
    valid_string_input = False

    input_string = input(prompt)

    while not valid_string_input:
        if input_string.isalpha():
            if not valid_len_list:
                valid_string_input = True
            else:
                if len(input_string) in valid_len_list:
                    valid_string_input = True
                else:
                    print(len_error_message)
                    input_string = input(prompt)
        else:
            print(type_error_message)
            input_string = input(prompt)

    return input_string


def get_alphabet_input(prompt, type_error_message):
    valid_string_input = False

    input_string = input(prompt)

    while not valid_string_input:
        if input_string.isalpha():
            valid_string_input = True
        else:
            print(type_error_message)
            input_string = input(prompt)

    return input_string

