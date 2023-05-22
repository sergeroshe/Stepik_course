import random

DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_.'
Y_RESPONSE = 'Y'
N_RESPONSE = 'N'


def secure_password_generator():
    chars = ''


passwd_num = int(input())  # Количество паролей для генерации;
passwd_len = int(input())
# Длину одного пароля;
has_passwd_digits = True  # Включать ли цифры 0123456789?
has_passwd_cap_letters = True  # Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?
has_passwd_low_letters = True  # Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?
has_passwd_spec_chars = True  # Включать ли символы !#$%&*+-=?@^_?
are_ambiguous_chars_exluded = True  # Исключать ли неоднозначные символы il1Lo0O?


def main():
    pass


main()
