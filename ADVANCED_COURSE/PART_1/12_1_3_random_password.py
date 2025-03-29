from random import randint

LETTER_RANGE_LIST = [[ord('a'), ord('z')], [ord('A'), ord('Z')]]
letter_range_list_len = len(LETTER_RANGE_LIST)
password_length = int(input())

password_list = ''
for _ in range(password_length):
    letter_case_val = LETTER_RANGE_LIST[randint(0, letter_range_list_len - 1)]
    password_list += chr(randint(letter_case_val[0], letter_case_val[1]))


print(*password_list, sep='')