MIN_ALPHABET_CHAR_IDX = ord('a')
MAX_ALPHABET_CHAR_IDX = ord('z')
ALPHABET_RANGE = MAX_ALPHABET_CHAR_IDX - MIN_ALPHABET_CHAR_IDX + 1
ENTER_MESSAGE_PROMPT = 'Enter text in English to encrypt or decrypt:\n'
IGNORE_CHAR_LIST = ',.!"!@#$%^&*((()))_+'


def ave_caesar():
    pass


def caesar_encrypt(source_msg, shift):
    result_msg = caesar_cypher_helper(source_msg, shift)
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


def word_len_list_configurator(source_string):
    raw_word_list = source_string.split()
    result_word_len_list = []
    for word in raw_word_list:
        result_word = ''
        if not word.isalnum():
            for char in IGNORE_CHAR_LIST:
                if char in word:
                    result_word = word.replace(char, '')
            result_word_len_list.append(len(result_word))
        else:
            result_word = word
            result_word_len_list.append(len(result_word))

    return result_word_len_list


def main():
    source_string = input()
    result_word_len_list = word_len_list_configurator(source_string)
    source_word_list = source_string.split()
    result_word_list = []
    for i in range(len(source_word_list)):
        word = source_word_list[i]
        result_word = caesar_encrypt(word, result_word_len_list[i])
        result_word_list.append(result_word)

    print(*result_word_list)


main()