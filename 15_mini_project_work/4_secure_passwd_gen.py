from random import choice

DIGITS = '0123456789'
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
PUNCTUATION_CHARS = '!#$%&*+-=?@^_.'
AMBIGUOUS_CHARS = 'il1Lo0O'

PASSWD_COUNT_PROMPT = 'Количество паролей для генерации: \n'
CUR_PASSWD_LEN_PROMPT = 'Введите длину пароля:\n'
INCLUDE_DIGITS_PROMPT = 'Включать ли цифры 0123456789'
INCLUDE_UPPER_LETTERS_PROMPT = 'Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ'
INCLUDE_LOWER_LETTERS_PROMPT = 'Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz'
INCLUDE_PUNCT_PROMPT = 'Включать ли символы !#$%&*+-=?@^_'
EXCLUDE_AMBIGUOUS_CHARS_PROMPT = 'Исключать ли неоднозначные символы il1Lo0O'

TYPE_ERROR_MESSAGE = 'Введенные данные должны быть числовыми!'
NO_RESPONSE = '1'
PASSWD_COUNT_MESSAGE = 'Количество паролей:'
PASSWD_LEN_MESSAGE = 'Длина пароля:'
YOUR_PASSWORDS_MESSAGE = 'Ваши пароли:'
POSITIVE_ACTION_CONFIRM = 'ДА'
NEGATIVE_ACTION_CONFIRM = 'НЕТ'

CURRENT_PASSWORD_OUTPUT = 'Password # '
SUMMARY_CONFIG_MESSAGE = 'Вы выбрали следующую конфигурацию паролей:'
COLON_SEP = ': '
QUESTION_MARK = '?'


def get_num_input(prompt, error_message):
    is_string_num = False
    input_string = input(prompt)
    while not is_string_num:
        if input_string and input_string[0] == '-' and input_string[1:].isdigit() or input_string.isdigit():
            is_string_num = True
        else:
            print(error_message)
            input_string = input(prompt)

    is_string_num = int(input_string)
    return is_string_num


def secure_password_configurator():
    chars = ''

    passwd_count = get_num_input(PASSWD_COUNT_PROMPT, TYPE_ERROR_MESSAGE)
    passwd_len = get_num_input(CUR_PASSWD_LEN_PROMPT, TYPE_ERROR_MESSAGE)

    digits_included = input(f'{INCLUDE_DIGITS_PROMPT}{QUESTION_MARK}\n') != NO_RESPONSE
    upper_letters_included = input(f'{INCLUDE_UPPER_LETTERS_PROMPT}{QUESTION_MARK}\n') != NO_RESPONSE
    lower_letters_included = input(f'{INCLUDE_LOWER_LETTERS_PROMPT}{QUESTION_MARK}\n') != NO_RESPONSE
    punctuation_included = input(f'{INCLUDE_PUNCT_PROMPT}{QUESTION_MARK}\n') != NO_RESPONSE
    ambiguous_chars_excluded = input(f'{EXCLUDE_AMBIGUOUS_CHARS_PROMPT}{QUESTION_MARK}\n') != NO_RESPONSE

    if digits_included:
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

    print_config(passwd_count, passwd_len, digits_included, upper_letters_included,
                 lower_letters_included, punctuation_included, ambiguous_chars_excluded)
    return passwd_count, chars, passwd_len


def print_config(passwd_count, passwd_len, digits_included, upper_letters_included,
                 lower_letters_included, punctuation_included, ambiguous_chars_excluded):

    dig_answer = POSITIVE_ACTION_CONFIRM if digits_included else NEGATIVE_ACTION_CONFIRM
    upper_letters_answer = POSITIVE_ACTION_CONFIRM if upper_letters_included else NEGATIVE_ACTION_CONFIRM
    lower_letters_answer = POSITIVE_ACTION_CONFIRM if lower_letters_included else NEGATIVE_ACTION_CONFIRM
    punctuation_answer = POSITIVE_ACTION_CONFIRM if punctuation_included else NEGATIVE_ACTION_CONFIRM
    ambiguous_chars_answer = POSITIVE_ACTION_CONFIRM if ambiguous_chars_excluded else NEGATIVE_ACTION_CONFIRM

    summary_config = f'{SUMMARY_CONFIG_MESSAGE}\n{PASSWD_COUNT_MESSAGE} {passwd_count}\n' \
                     f'{PASSWD_LEN_MESSAGE} {passwd_len}\n{INCLUDE_DIGITS_PROMPT + COLON_SEP + dig_answer}\n' \
                     f'{INCLUDE_UPPER_LETTERS_PROMPT + COLON_SEP + upper_letters_answer}\n' \
                     f'{INCLUDE_LOWER_LETTERS_PROMPT + COLON_SEP + lower_letters_answer}\n' \
                     f'{INCLUDE_PUNCT_PROMPT + COLON_SEP + punctuation_answer}\n' \
                     f'{EXCLUDE_AMBIGUOUS_CHARS_PROMPT + COLON_SEP + ambiguous_chars_answer}'

    print()
    print(summary_config)
    print()


def generate_password(chars, length):
    password = ''
    for i in range(length):
        password += choice(chars)

    return password


def print_passwords(passwd_list, passwd_num):
    print(YOUR_PASSWORDS_MESSAGE)
    for i in range(len(passwd_num)):
        passwd_num = f'{CURRENT_PASSWORD_OUTPUT + str(i + 1) + COLON_SEP}'
        print(passwd_num, passwd_list[i], sep='\n')
        print()

def generate_passwords(passwd_count, chars, length):
    passwd_list = []
    passwd_num_list = []
    for i in range(passwd_count):
        password = generate_password(chars, length)
        passwd_num_list.append(i + 1)
        passwd_list.append(password)
    return passwd_list, passwd_num_list


def main():
    passwd_count, chars, length = secure_password_configurator()
    passwd_list, passwd_num_list = generate_passwords(passwd_count, chars, length)
    print_passwords(passwd_list, passwd_num_list)


main()
