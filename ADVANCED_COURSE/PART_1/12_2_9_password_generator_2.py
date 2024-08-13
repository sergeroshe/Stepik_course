from string import ascii_uppercase as u, \
    ascii_lowercase as l, digits as d
from random import shuffle, choice

IGNORE_CHARS = 'lI1Oo0'
MINIMUM_PASSWORD_LENGTH = 3
CHAR_TYPE_AMOUNT = 3


def generate_password(pswd_length):
    pswd_list = []
    for _ in range(pswd_length // CHAR_TYPE_AMOUNT):
        pswd_list.append(choice(u))
        pswd_list.append(choice(l))
        pswd_list.append(choice(d))
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
    password_amount = 3
    password_length = get_correct_length()
    # password_length = 15

    password_list = [generate_password(password_length) for _ in range(password_amount)]
    print(*password_list, sep='\n')


main()
