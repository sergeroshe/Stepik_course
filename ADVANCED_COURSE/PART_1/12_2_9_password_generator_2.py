from string import ascii_uppercase as u, \
    ascii_lowercase as l, digits as d
from random import shuffle, choice

IGNORE_CHARS = 'lI1Oo0'
MINIMUM_PASSWORD_LENGTH = 3
CHAR_TYPE_AMOUNT = 3


def generate_password(pswd_length):
    pswd_list = []
    shift_list_len = 3
    pswd_list_full = False
    i = 0
    while not pswd_list_full:
        shift_list = [choice(u), choice(l), choice(d)]

        char = shift_list[i]
        if char not in IGNORE_CHARS:
            pswd_list.append(shift_list[i])
            i += 1
        if len(pswd_list) == pswd_length:
            pswd_list_full = True

        if i > shift_list_len - 1:
            i = 0
        print(shift_list)
        print(char)

    shuffle(pswd_list)
    pswd_string = ''.join(pswd_list)

    return pswd_string


def get_correct_length():
    correct_length_entered = False
    length = None
    while not correct_length_entered:
        length = int(input())
        if length > MINIMUM_PASSWORD_LENGTH - 1:
            correct_length_entered = True
    return length


def main():
    # password_amount = int(input())
    password_amount = 9
    # password_length = get_correct_length()
    password_length = 3

    password_list = [generate_password(password_length) for _ in range(password_amount)]
    print(*password_list, sep='\n')


main()
# zI2