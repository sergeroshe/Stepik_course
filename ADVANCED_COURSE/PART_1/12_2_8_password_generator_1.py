from string import ascii_letters as a, digits as d
from random import sample, choice

IGNORE_CHARS = 'lI1Oo0'


def generate_password(pswd_length):
    char_list = a + d
    suitable_char_list = [char for char in char_list if char not in IGNORE_CHARS]
    pswd = ''.join(sample(suitable_char_list, pswd_length))
    return pswd


def main():
    password_amount = int(input())
    password_length = int(input())

    password_list = [generate_password(password_length) for _ in range(password_amount)]
    print(*password_list, sep='\n')


main()
