from string import ascii_uppercase as u, \
    ascii_lowercase as l, digits as d
from random import shuffle, choice

IGNORE_CHARS = 'lI1Oo0'
MINIMUM_PASSWORD_LENGTH = 3
CHAR_TYPE_AMOUNT = 3


def generate_password(pswd_length):
    suitable_upper_letter_list = [char for char in u if char not in IGNORE_CHARS]
    suitable_lower_letter_list = [char for char in l if char not in IGNORE_CHARS]
    suitable_digit_list = [char for char in d if char not in IGNORE_CHARS]
    pswd_list = []
    char_type_list_len = CHAR_TYPE_AMOUNT

    i = 0
    pswd_list_full = False
    while not pswd_list_full:
        if i > char_type_list_len - 1:
            i = 0
        char_type_list = [choice(suitable_upper_letter_list),
                          choice(suitable_lower_letter_list),
                          choice(suitable_digit_list)]
        char = char_type_list[i]
        pswd_list.append(char)
        if len(pswd_list) == pswd_length:
            pswd_list_full = True
        i += 1

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
    password_amount = int(input())
    password_length = get_correct_length()

    password_list = [generate_password(password_length) for _ in range(password_amount)]
    print(*password_list, sep='\n')


main()