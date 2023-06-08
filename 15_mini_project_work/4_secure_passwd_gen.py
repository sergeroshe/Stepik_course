from random import choice

DIGITS = '0123456789'
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
PUNCTUATION_CHARS = '!#$%&*+-=?@^_.'
AMBIGUOUS_CHARS = 'il1Lo0O'
PASSWD_COUNT_PROMPT = 'Количество паролей для генерации: \n'
CUR_PASSWD_LEN_PROMPT = 'Введите длину пароля:\n '
TYPE_ERROR_MESSAGE = 'Введенные данные должны быть числовыми!'
NO_RESPONSE = '1'
INCLUDE_NUMBERS_PROMPT = 'Включать ли цифры 0123456789?\n'
INCLUDE_UPPER_LETTERS_PROMPT = 'Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?\n'
INCLUDE_LOWER_LETTERS_PROMPT = 'Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?\n'
INCLUDE_PUNCT_PROMPT = 'Включать ли символы !#$%&*+-=?@^_?\n'
EXCLUDE_AMBIGUOUS_CHARS_PROMPT = 'Исключать ли неоднозначные символы il1Lo0O?\n'
CURRENT_PASSWORD_OUTPUT = 'Password # '
COLON_SEP = ':\n'


def get_num_input(prompt, error_message):
    is_string_num = False
    input_string = input(prompt)
    while not is_string_num:
        if len(input_string) != 0 and input_string[0] == '-' and\
               input_string[1:].isdigit() or input_string.isdigit():
            is_string_num = True
        else:
            print(error_message)
            input_string = input(prompt)

    is_string_num = int(input_string)
    return is_string_num


def secure_password_configurator():
    chars = ''

    passwd_count = get_num_input(PASSWD_COUNT_PROMPT, TYPE_ERROR_MESSAGE)
    cur_passwd_len = get_num_input(CUR_PASSWD_LEN_PROMPT, TYPE_ERROR_MESSAGE)

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

    return passwd_count, cur_passwd_len, chars


def generate_password(length, chars):
    password = ''
    for i in range(length):
        password += choice(chars)

    return password


def main():
    passwd_count, chars, length = secure_password_configurator()
    for i in range(passwd_count):
        password = generate_password(chars, length)
        current_passwd = CURRENT_PASSWORD_OUTPUT + str(i + 1) + COLON_SEP + password
        print(current_passwd)


main()

