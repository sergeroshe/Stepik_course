import random

DIGITS = '0123456789'
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
PUNCTUATION_CHARS = '!#$%&*+-=?@^_.'
AMBIGUOUS_CHARS = 'il1Lo0O'
PASSWD_COUNT_PROMPT = 'Количество паролей для генерации: \n'
CUR_PASSWD_LEN_PROMPT = 'Введите длину пароля '
NO_RESPONSE = '1'
INCLUDE_NUMBERS_PROMPT = 'Включать ли цифры 0123456789?\n'
INCLUDE_UPPER_LETTERS_PROMPT = 'Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?\n'
INCLUDE_LOWER_LETTERS_PROMPT = 'Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?\n'
INCLUDE_PUNCT_PROMPT = 'Включать ли символы !#$%&*+-=?@^_?\n'
EXCLUDE_AMBIGUOUS_CHARS_PROMPT = 'Исключать ли неоднозначные символы il1Lo0O?\n'


def secure_password_generator():
    chars = ''

    passwd_count = int(input(PASSWD_COUNT_PROMPT))
    cur_passwd_len = int(input(CUR_PASSWD_LEN_PROMPT))

    numbers_included = input(INCLUDE_NUMBERS_PROMPT) != NO_RESPONSE
    upper_letters_included = input(INCLUDE_UPPER_LETTERS_PROMPT) != NO_RESPONSE
    lower_letters_included = input(INCLUDE_LOWER_LETTERS_PROMPT) != NO_RESPONSE
    punctuation_included = input(INCLUDE_PUNCT_PROMPT) != NO_RESPONSE
    ambiguous_chars_excluded = input(EXCLUDE_AMBIGUOUS_CHARS_PROMPT) != NO_RESPONSE

    for _ in range(passwd_count):
        if numbers_included:
            chars += DIGITS
        if upper_letters_included:
            chars += UPPER_LETTERS
        if lower_letters_included:
            chars += LOWER_LETTERS
        if punctuation_included:
            chars += PUNCTUATION_CHARS
        if ambiguous_chars_excluded:
            for c in chars:
                if c in AMBIGUOUS_CHARS:
                    chars = chars.replace(c, '')


def main():
    secure_password_generator()


main()

