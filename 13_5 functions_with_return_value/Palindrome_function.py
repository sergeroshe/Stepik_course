def is_palindrome(sentence):
    value = True
    len_s = len(sentence) - 1
    half_len = len(sentence) // 2
    left_side_idx = 0
    right_side_idx = 0
    valid_char_count = 0
    ignore_char_count = 0 ##

    while valid_char_count // 2 <= half_len - ignore_char_count // 2:
        left_side_element = sentence[left_side_idx]
        right_side_element = sentence[len_s - right_side_idx]
        if left_side_element not in IGNORE_CHAR_LIST and right_side_element not in IGNORE_CHAR_LIST:
            left_side_idx += 1
            right_side_idx += 1
            valid_char_count += 1
            if right_side_element != left_side_element:
                value = False
                break
        elif left_side_element in IGNORE_CHAR_LIST:
            left_side_idx += 1
            ignore_char_count += 1
        elif right_side_element in IGNORE_CHAR_LIST:
            right_side_idx += 1
            ignore_char_count += 1

    return value


IGNORE_CHAR_LIST = ' ,/.!?-'


def main():
    line = input().lower()

    is_line_palindrome = is_palindrome(line)

    print(is_line_palindrome)


main()