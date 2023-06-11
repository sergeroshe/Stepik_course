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
    cur_passwd_len = get_num_input(CUR_PASSWD_LEN_PROMPT, TYPE_ERROR_MESSAGE)

    digits_included = input(f'{INCLUDE_DIGITS_PROMPT}{QUESTION_MARK}\n') != NO_RESPONSE
    upper_letters_included = input(f'{INCLUDE_UPPER_LETTERS_PROMPT}{QUESTION_MARK}\n') != NO_RESPONSE
    lower_letters_included = input(f'{INCLUDE_LOWER_LETTERS_PROMPT}{QUESTION_MARK}\n') != NO_RESPONSE
    punctuation_included = input(f'{INCLUDE_PUNCT_PROMPT}{QUESTION_MARK}\n') != NO_RESPONSE
    ambiguous_chars_excluded = input(f'{EXCLUDE_AMBIGUOUS_CHARS_PROMPT}{QUESTION_MARK}\n') != NO_RESPONSE

    # for _ in range(passwd_count):
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

    return passwd_count, chars, cur_passwd_len


def generate_password(chars, length):
    password = ''
    for i in range(length):
        password += choice(chars)

    return password


def main():
    passwd_count, chars, length = secure_password_configurator()
    passwd_list = []
    digits_included = DIGITS[-1] in chars
    if digits_included:
        dig_answer = POSITIVE_ACTION_CONFIRM
    else:
        dig_answer = NEGATIVE_ACTION_CONFIRM
    upper_letters_included = UPPER_LETTERS[-1] in chars
    if upper_letters_included:
        upper_letters_answer = POSITIVE_ACTION_CONFIRM
    else:
        upper_letters_answer = NEGATIVE_ACTION_CONFIRM
    lower_letters_included = LOWER_LETTERS[-1] in chars
    if lower_letters_included:
        lower_letters_answer = POSITIVE_ACTION_CONFIRM
    else:
        lower_letters_answer = NEGATIVE_ACTION_CONFIRM
    punctuation_included = PUNCTUATION_CHARS in chars
    if punctuation_included:
        punctuation_answer = POSITIVE_ACTION_CONFIRM
    else:
        punctuation_answer = NEGATIVE_ACTION_CONFIRM
    ambiguous_chars_excluded = AMBIGUOUS_CHARS not in chars
    if ambiguous_chars_excluded:
        ambiguous_chars_answer = POSITIVE_ACTION_CONFIRM
    else:
        ambiguous_chars_answer = NEGATIVE_ACTION_CONFIRM

    for i in range(passwd_count):
        password = generate_password(chars, length)
        current_passwd = f'{CURRENT_PASSWORD_OUTPUT + str(i + 1) + COLON_SEP}\n{password}'
        passwd_list.append(current_passwd)

    summary_config = f'{SUMMARY_CONFIG_MESSAGE}\n{PASSWD_COUNT_MESSAGE} {passwd_count}\n'\
                     f'{PASSWD_LEN_MESSAGE} {length}\n{INCLUDE_DIGITS_PROMPT + COLON_SEP + dig_answer}\n'\
                     f'{INCLUDE_UPPER_LETTERS_PROMPT + COLON_SEP + upper_letters_answer}\n'\
                     f'{INCLUDE_LOWER_LETTERS_PROMPT + COLON_SEP + lower_letters_answer}\n'\
                     f'{INCLUDE_PUNCT_PROMPT + COLON_SEP + punctuation_answer}\n'\
                     f'{EXCLUDE_AMBIGUOUS_CHARS_PROMPT + COLON_SEP + ambiguous_chars_answer}'

    print()
    print(summary_config)
    print()
    print('Ваши пароли:')
    print(*passwd_list, sep='\n')


main()

