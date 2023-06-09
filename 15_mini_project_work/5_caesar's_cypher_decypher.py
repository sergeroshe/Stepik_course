#  Кириллица:
MIN_ALPHABET_CHAR_IDX = ord('A')
MAX_ALPHABET_CHAR_IDX = ord('z')
ALPHABET_RANGE = MAX_ALPHABET_CHAR_IDX - MIN_ALPHABET_CHAR_IDX + 1

ENTER_SHIFT_PROMPT = 'Enter shift:\n'
TYPE_ERROR_MESSAGE = 'The entered data must be numeric!'
ENTER_MESSAGE_PROMPT = 'Enter message in Latin to deciphre:\n'
IGNORE_CHAR_LIST = '!#$%&*+-=?@^_., '


def get_num_input(prompt, error_message):
    is_string_num = False
    input_string = input(prompt)
    is_input_non_empty = len(input_string) != 0
    while not is_string_num:
        if is_input_non_empty and input_string[0] == '-' and input_string[1:].isdigit() or input_string.isdigit():
            is_string_num = True
        else:
            print(error_message)
            input_string = input(prompt)

    is_string_num = int(input_string)
    return is_string_num


def caesar_cypher():

    shift = get_num_input(ENTER_SHIFT_PROMPT, TYPE_ERROR_MESSAGE)
    source_msg = input(ENTER_MESSAGE_PROMPT)

    if shift < 0:
        shift = ALPHABET_RANGE - shift
    shift %= ALPHABET_RANGE

    upper_letter_idx_list = []
    result_msg_char_list = []
    for i in range(len(source_msg)):
        letter = source_msg[i]

        if letter.isupper():
            upper_letter_idx_list.append(i)
        if letter not in IGNORE_CHAR_LIST:
            result_msg_letter_idx = ord(letter) - shift

            if result_msg_letter_idx < MIN_ALPHABET_CHAR_IDX:
                result_msg_letter_idx = (MAX_ALPHABET_CHAR_IDX + 1) \
                                        - (MIN_ALPHABET_CHAR_IDX - result_msg_letter_idx) % ALPHABET_RANGE
            elif result_msg_letter_idx > MAX_ALPHABET_CHAR_IDX:
                result_msg_letter_idx = MIN_ALPHABET_CHAR_IDX + \
                                        (result_msg_letter_idx - (MAX_ALPHABET_CHAR_IDX + 1)) % ALPHABET_RANGE
        else:
            result_msg_letter_idx = ord(letter)

        result_msg_char_list.append(chr(result_msg_letter_idx))
        #  if

    for c in upper_letter_idx_list:
        for k in range(len(result_msg_char_list)):
            if c == k:
                result_msg_char_list[k] = result_msg_char_list[k].upper()
            else:
                result_msg_char_list[k] = result_msg_char_list[k].lower()

    result_msg = ''.join(result_msg_char_list)

    return result_msg


def main():
    decrypted_msg = caesar_cypher()
    print(decrypted_msg)


main()
