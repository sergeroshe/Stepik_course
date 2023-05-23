from random import choice

DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_.'
AMBIGUOUS_CHARS = 'il1Lo0O'

Y_RESPONSE = '1'

def secure_password_generator():
    chars = ''

    passwd_num = int(input('Количество паролей для генерации: \n'))  # Количество паролей для генерации;

    for i in range(passwd_num):
        password = ''
        char_list = []
        is_char_list_full = False
        while not is_char_list_full:
            print('Please choose your password ' + str(i + 1) + ' content:\n')
            answer = input('Включать ли цифры 0123456789?')
            if answer == Y_RESPONSE:
                char_list.extend(DIGITS)

            answer = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?')
            if answer == Y_RESPONSE:
                char_list.extend(UPPERCASE_LETTERS)

            answer = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?')
            if answer == Y_RESPONSE:
                char_list.extend(LOWERCASE_LETTERS)

            answer = input('Включать ли символы !#$%&*+-=?@^_?')
            if answer == Y_RESPONSE:
                char_list.extend(PUNCTUATION)

            answer = input('Исключать ли неоднозначные символы il1Lo0O?')
            if answer == N_RESPONSE:
                char_list.extend(AMBIGUOUS_CHARS)
            is_char_list_full = True

        cur_passwd_len = int(input('Введите длину пароля ' + str(i + 1) + ':\n'))
        if len(char_list) > 0:
            for j in range(cur_passwd_len):
                password += choice(char_list)
            print('password_' + str(i + 1) + ':\n' + password)
        else:
            print('Вы не выбрали достаточное количество символов для пароля!\n'
                  'Чтобы сгенерировать пароль, запустите программу еще раз.')


secure_password_generator()


def main():
    pass


main()
