IGNORE_CHAR_LIST = ' ,/.!?-'


def is_palindrome(sentence):
    value = True                                   # move to constant
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
                value = False
                break
        elif left_side in IGNORE_CHAR_LIST:
            left_side_count += 1
        elif right_side in IGNORE_CHAR_LIST:
            right_side_count += 1

        i += 1
    return value


def is_prime(num):
    num = int(num)
    answer = True
    if num > 1:
        for i in range(2, (num // 2) + 1):
            if num % i == 0:
                answer = False
                break
    else:
        answer = False
    return answer


def is_valid_password(password):  # reuse old functions
    pattern = 'a:b:c'.split(':')
    palindrome_char = 'a'
    prime_num_char = 'b'
    even_num_char = 'c'
    value = True
    for i in range(len(password)):
        password_num = password[i]
        password_len = len(password)
        if password_len == len(pattern):
            if pattern[i] == palindrome_char and not is_palindrome(password_num):
                value = False
                break
            elif pattern[i] == prime_num_char and not is_prime(password_num):
                value = False
                break
            elif pattern[i] == even_num_char:
                if int(password_num) % 2 != 0:
                    value = False
                    break
        else:
            value = False
            break
    return value


def main():

    user_password = input().split(':')

    is_password_valid = is_valid_password(user_password)

    print(is_password_valid)


main()
