import random

DIGITS = '0123456789'
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
PUNCTUATION_CHARS = '!#$%&*+-=?@^_.'
AMBIGUOUS_CHARS = 'il1Lo0O'
PASSWD_NUM_PROMPT = 'Количество паролей для генерации: \n'
CUR_PASSWD_LEN_PROMPT = 'Введите длину пароля '
NO_RESPONSE = '1'
INCLUDE_NUM_PROMPT = 'Включать ли цифры 0123456789?\n'
INCLUDE_CAP_LETTERS_PROMPT = 'Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?\n'
INCLUDE_SMALL_LETTERS_PROMPT = 'Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?\n'
INCLUDE_PUNCT_PROMPT = 'Включать ли символы !#$%&*+-=?@^_?\n'
EXCLUDE_AMBIG_CHARS_PROMPT = 'Исключать ли неоднозначные символы il1Lo0O?\n'


def secure_password_generator():
    chars = ''

    passwd_num = int(input(PASSWD_NUM_PROMPT))
    cur_passwd_len = int(input(CUR_PASSWD_LEN_PROMPT))

    is_num_included = input(INCLUDE_NUM_PROMPT) != NO_RESPONSE
    is_cap_letter_included = input(INCLUDE_CAP_LETTERS_PROMPT) != NO_RESPONSE
    is_small_letter_included = input(INCLUDE_SMALL_LETTERS_PROMPT) != NO_RESPONSE
    is_punctuation_included = input(INCLUDE_PUNCT_PROMPT) != NO_RESPONSE
    is_ambig_chars_excluded = input(EXCLUDE_AMBIG_CHARS_PROMPT) != NO_RESPONSE

    for i in range(passwd_num):
        if is_num_included:
            chars += DIGITS
        if is_cap_letter_included:
            chars += UPPER_LETTERS
        if is_small_letter_included:
            chars += LOWER_LETTERS
        if is_punctuation_included:
            chars += PUNCTUATION_CHARS
        if is_ambig_chars_excluded:
            for c in chars:
                if c in AMBIGUOUS_CHARS:
                    chars = chars.replace(c, '')


def main():
    secure_password_generator()


main()

