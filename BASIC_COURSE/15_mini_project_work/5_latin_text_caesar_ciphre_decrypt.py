MIN_ALPHABET_CHAR_IDX = ord('a')
MAX_ALPHABET_CHAR_IDX = ord('z')
ALPHABET_RANGE = MAX_ALPHABET_CHAR_IDX - MIN_ALPHABET_CHAR_IDX + 1

ENTER_SHIFT_PROMPT = 'Enter shift:\n'
TYPE_ERROR_MESSAGE = 'The data entered must be numeric!'
ENTER_MESSAGE_PROMPT = 'Enter text in English to encrypt or decrypt:\n'
IGNORE_CHAR_LIST = '!#$%&*+-=?@^_.«»,:; '

CIPHER_ACTION_PROMPT = 'To encrypt text, press ENTER,' \
                        ' to decrypt - press "1" then ENTER\n'
DECRYPT_ACTION_CONFIRM = '1'


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


def caesar_encrypt(source_msg, shift):
    result_msg = caesar_cypher_helper(source_msg, shift)
    return result_msg


def caesar_decrypt(source_msg, shift):
    result_msg = caesar_cypher_helper(source_msg, -shift)
    return result_msg


def caesar_cypher_helper(source_msg, shift):

    # Shift within range [0, ALPHABET_RANGE)
    # Works for negative shifts as well
    normalized_shift = shift % ALPHABET_RANGE

    upper_letter_idx_list = []
    result_msg_char_list = []
    for i in range(len(source_msg)):
        letter = source_msg[i]

        if letter.isupper():
            letter = letter.lower()
            upper_letter_idx_list.append(i)
        if letter not in IGNORE_CHAR_LIST:
            result_msg_letter_idx = ord(letter) + normalized_shift

            if result_msg_letter_idx < MIN_ALPHABET_CHAR_IDX:
                result_msg_letter_idx = (MAX_ALPHABET_CHAR_IDX + 1) \
                                        - (MIN_ALPHABET_CHAR_IDX - result_msg_letter_idx) % ALPHABET_RANGE
            elif result_msg_letter_idx > MAX_ALPHABET_CHAR_IDX:
                result_msg_letter_idx = MIN_ALPHABET_CHAR_IDX + \
                                        (result_msg_letter_idx - (MAX_ALPHABET_CHAR_IDX + 1)) % ALPHABET_RANGE
        else:
            result_msg_letter_idx = ord(letter)

        result_msg_char_list.append(chr(result_msg_letter_idx))

    for idx in upper_letter_idx_list:
        result_msg_char_list[idx] = result_msg_char_list[idx].upper()

    result_msg = ''.join(result_msg_char_list)

    return result_msg


def main():
    mode_option = input(CIPHER_ACTION_PROMPT)
    source_msg = input(ENTER_MESSAGE_PROMPT)
    shift = get_num_input(ENTER_SHIFT_PROMPT, TYPE_ERROR_MESSAGE)

    is_encrypt_mode = mode_option != DECRYPT_ACTION_CONFIRM

    if is_encrypt_mode:
        result_msg = caesar_encrypt(source_msg, shift)
    else:
        result_msg = caesar_decrypt(source_msg, shift)

    print(result_msg)


main()
