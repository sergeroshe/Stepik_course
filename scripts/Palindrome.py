IGNORE_CHAR_LIST = ' .,-_:!@#$%^&?'


def is_palindrome(text):
    is_same_letter = True
    left_side_idx = 0
    right_side_idx = len(text) - 1

    while left_side_idx != right_side_idx and is_same_letter:
        left_side_char = text[left_side_idx]
        right_side_char = text[right_side_idx]
        is_left_side_letter = left_side_char not in IGNORE_CHAR_LIST
        is_right_side_letter = right_side_char not in IGNORE_CHAR_LIST

        if is_left_side_letter and is_right_side_letter:
            if left_side_char != right_side_char:
                is_same_letter = False
            else:
                left_side_idx += 1
                right_side_idx -= 1
        else:
            if not is_left_side_letter:
                left_side_idx += 1

            if not is_right_side_letter:
                right_side_idx -= 1

    return is_same_letter


def main():
    line = input().lower()

    is_line_palindrome = is_palindrome(line)

    print(is_line_palindrome)


main()