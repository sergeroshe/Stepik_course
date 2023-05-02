IGNORE_CHAR_LIST = ' ,/.!?-'
SEPARATOR = ':'
PALINDROME_NUM_CHAR = 'a'
PRIME_NUM_CHAR = 'b'
EVEN_NUM_CHAR = 'c'
PATTERN = 'a:b:c'


def is_palindrome(sentence):
    result = True                                   # move to constant
    len_s = len(sentence) - 1
    half_len = len(sentence) // 2
    left_side_count = 0
    right_side_count = 0
    i = 0

    while left_side_count <= half_len and right_side_count <= half_len:
        left_side = sentence[left_side_count]
        right_side = sentence[len_s - right_side_count]
        if left_side not in IGNORE_CHAR_LIST and right_side not in IGNORE_CHAR_LIST:
            left_side_count += 1
            right_side_count += 1
            if right_side != left_side:
                result = False
                break
        elif left_side in IGNORE_CHAR_LIST:
            left_side_count += 1
        elif right_side in IGNORE_CHAR_LIST:
            right_side_count += 1

        i += 1
    return result


def is_prime(num):
    result = True
    if num > 1:
        for i in range(2, (num // 2) + 1):
            if num % i == 0:
                result = False
                break
    else:
        result = False
    return result


def is_even(num):
    answer = num % 2 == 0

    return answer


def is_valid_password(password, pattern, separator):  # reuse old functions
    pattern_list = pattern.split(separator)
    password_list = password.split(separator)
    result = True

    if len(password_list) == len(pattern_list):
        for i in range(len(password_list)):
            password_part = password_list[i]
            password_num = int(password_part)

            if pattern_list[i] == PALINDROME_NUM_CHAR:
                if not is_palindrome(password_part):
                    result = False
                    break
            elif pattern_list[i] == PRIME_NUM_CHAR:
                if not is_prime(password_num):
                    result = False
                    break
            elif pattern_list[i] == EVEN_NUM_CHAR:
                if not is_even(password_num):
                    result = False
                    break

    else:
        result = False

    return result


def main():

    user_password = input()

    is_password_valid = is_valid_password(user_password, PATTERN, SEPARATOR)

    print(is_password_valid)


main()
