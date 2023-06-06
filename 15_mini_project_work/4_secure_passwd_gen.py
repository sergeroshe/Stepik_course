import random

DIGITS = '0123456789'
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
PUNCTUATION_CHARS = '!#$%&*+-=?@^_.'
PASSWD_NUM_PROMPT = 'Количество паролей для генерации: \n'
CUR_PASSWD_LEN_PROMPT = 'Введите длину пароля '
NO_RESPONSE = '1'
INCLUDE_NUM_PROMPT = 'Включать ли цифры 0123456789?\n'
INCLUDE_CAP_LETTERS_PROMPT = 'Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?\n'
INCLUDE_SMALL_LETTERS_PROMPT = 'Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?\n'
INCLUDE_PUNCT_PROMPT = 'Включать ли символы !#$%&*+-=?@^_?\n'
EXCLUDE_AMBIG_CHARS_PROMPT = 'Исключать ли неоднозначные символы il1Lo0O?\n'


def get_password_config():
    passwd_num = int(input(PASSWD_NUM_PROMPT))
    cur_passwd_len = int(input(CUR_PASSWD_LEN_PROMPT))
    answer = input(INCLUDE_NUM_PROMPT)
    is_num_included = answer != NO_RESPONSE
    answer = input(INCLUDE_CAP_LETTERS_PROMPT)
    is_cap_letter_included = answer != NO_RESPONSE
    answer = input(INCLUDE_SMALL_LETTERS_PROMPT)
    is_small_letter_included = answer != NO_RESPONSE
    answer = input(INCLUDE_PUNCT_PROMPT)
    is_punctuation_included = answer != NO_RESPONSE
    answer = input(EXCLUDE_AMBIG_CHARS_PROMPT)
    is_ambig_chars_excluded = answer != NO_RESPONSE

    return passwd_num, cur_passwd_len, is_num_included, is_cap_letter_included, is_small_letter_included, \
        is_punctuation_included, is_ambig_chars_excluded


def secure_password_generator():
    chars = ''
    get_password_config()


def main():
    secure_password_generator()


main()

