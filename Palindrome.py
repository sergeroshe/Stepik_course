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


def main():

    line = input().lower()

    is_line_palindrome = is_palindrome(line)

    print(is_line_palindrome)


main()