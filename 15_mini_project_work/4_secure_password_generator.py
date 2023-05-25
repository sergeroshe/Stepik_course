from random import choice

DIGITS = '0123456789'
CAP_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
PUNCTUATION = '!#$%&*+-=?@^_.'
AMBIGUOUS_CHARS = 'il1Lo0O'

PASSWD_NUM_PROMPT = 'Количество паролей для генерации: \n'
CUR_PASSWD_ADJ_PROMPT = 'Настройте содержимое пароля №'
INCLUDE_NUM_PROMPT = 'Включать ли цифры 0123456789?'
INCLUDE_CAP_LETTERS_PROMPT = 'Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?'
INCLUDE_LOW_LETTERS_PROMPT = 'Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?'
INCLUDE_PUNCT_PROMPT = 'Включать ли символы !#$%&*+-=?@^_?'
EXCLUDE_AMBIG_CHARS_PROMPT = 'Исключать ли неоднозначные символы il1Lo0O?'
CUR_PASSWD_LEN_PROMPT = 'Введите длину пароля '
CUR_PASSWD_OUTPUT = 'Пароль №'
ERROR_INSUFFICIENT_CHARACTERS = 'Вы не выбрали достаточное количество символов для пароля!' \
                                '\nЧтобы сгенерировать пароль, запустите программу еще раз.'
COLUMN_SEP = ':'

Y_RESPONSE = '1'


def secure_password_generator():
    # chars = ''

    passwd_num = int(input(PASSWD_NUM_PROMPT))  # Количество паролей для генерации;

    for k in range(passwd_num):
        password = ''
        char_list = []
        is_char_list_full = False
        while not is_char_list_full:
            print(CUR_PASSWD_ADJ_PROMPT + str(k + 1) + COLUMN_SEP)
            answer = input(INCLUDE_NUM_PROMPT)
            if answer == Y_RESPONSE:
                char_list.extend(DIGITS)

            answer = input(INCLUDE_CAP_LETTERS_PROMPT)
            if answer == Y_RESPONSE:
                char_list.extend(CAP_LETTERS)

            answer = input(INCLUDE_LOW_LETTERS_PROMPT)
            if answer == Y_RESPONSE:
                char_list.extend(LOWER_LETTERS)

            answer = input(INCLUDE_PUNCT_PROMPT)
            if answer == Y_RESPONSE:
                char_list.extend(PUNCTUATION)

            answer = input(EXCLUDE_AMBIG_CHARS_PROMPT)
            if answer == Y_RESPONSE:

                amb_char_idx_list = []
                for i in range(len(char_list)):
                    if char_list[i] in AMBIGUOUS_CHARS:
                        amb_char_idx_list.append(i)

                amb_char_idx_count = 0
                for idx in amb_char_idx_list:
                    del char_list[idx - amb_char_idx_count]
                    amb_char_idx_count += 1
            is_char_list_full = True

        cur_passwd_len = int(input(CUR_PASSWD_LEN_PROMPT + str(k + 1) + COLUMN_SEP + '\n'))
        if len(char_list) > 0:
            for k in range(cur_passwd_len):
                password += choice(char_list)
            print(CUR_PASSWD_OUTPUT + str(k + 1) + COLUMN_SEP + '\n' + password)
        else:
            print(ERROR_INSUFFICIENT_CHARACTERS)


secure_password_generator()


def main():
    pass


main()
