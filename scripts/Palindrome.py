def is_palindrome(sentence):
    result = True
    left_side_idx = 0
    right_side_idx = len(sentence) - 1

    while left_side_idx != right_side_idx:
        left_side_element = sentence[left_side_idx]
        right_side_element = sentence[right_side_idx]
        if left_side_element in IGNORE_CHAR_LIST:
            is_left_side_letter = True
            left_side_idx += 1
        else:
            left_side_other_char = True
        if right_side_element in IGNORE_CHAR_LIST:
            is_right_side_letter = True
            right_side_idx -= 1
        else:
            right_side_other_char = True
        if left_side_element != right_side_element:
            result = False
            break

        # elif left_side_element not in VALID_CHAR_LIST:
        elif left_side_other_char and not right_side_other_char:
            right_side_idx -= 1
        else:
            left_side_idx += 1

    return result


IGNORE_CHAR_LIST = ' .,-_:!@#$%^&'


def main():
    line = input().lower()

    is_line_palindrome = is_palindrome(line)

    print(is_line_palindrome)


main()