MIN_ALPHABET_CHAR_IDX = ord('a')
MAX_ALPHABET_CHAR_IDX = ord('z')
ALPHABET_RANGE = MAX_ALPHABET_CHAR_IDX - MIN_ALPHABET_CHAR_IDX + 1
ENTER_MESSAGE_PROMPT = 'Enter text in English to encrypt:\n'
PUNCTUATION_CHARS = ',.!"!\'@#$%^&*()_+-'
# PUNCTUATION_CHARS = '!'

WORD_SEP = ' '


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
        if letter not in PUNCTUATION_CHARS:
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


def get_word_len(word):
    result_word = word
    if not word[0].isalnum() or not word[-1].isalnum():
        for char in PUNCTUATION_CHARS:
            if char in word:
                result_word = word.strip(char)

    result_word_len = len(result_word)

    # result_word_len = len(result_word)

    return result_word_len


def caesar_encrypt_by_word_len(source_string):
    source_word_list = source_string.split()

    encrypted_msg = ''
    for word in source_word_list:
        word_len = get_word_len(word)
        encrypted_word = caesar_encrypt(word, word_len)
        encrypted_msg += encrypted_word + WORD_SEP

    return encrypted_msg


def main():
    source_string = input(ENTER_MESSAGE_PROMPT)

    encrypted_string = caesar_encrypt_by_word_len(source_string)

    print(encrypted_string)


main()