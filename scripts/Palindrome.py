IGNORE_CHAR_LIST = ' .,-_:!@#$%^&?'


def is_palindrome(sentence):
    result = True
    left_side_idx = 0
    right_side_idx = len(sentence) - 1

    while left_side_idx != right_side_idx:
        left_side_element = sentence[left_side_idx]
        right_side_element = sentence[right_side_idx]
        left_side_letter = left_side_element not in IGNORE_CHAR_LIST
        right_side_letter = right_side_element not in IGNORE_CHAR_LIST
        if left_side_letter and right_side_letter:
            left_side_idx += 1
            right_side_idx -= 1
            if left_side_element != right_side_element:
                result = False
                break
        elif not left_side_letter and not right_side_letter:
            left_side_idx += 1
            right_side_idx -= 1
        elif not left_side_letter and right_side_letter:
            left_side_idx += 1
        elif not right_side_letter and left_side_letter:
            right_side_idx -= 1

    return result


def main():
    line = input().lower()
    # line = ' Do me?.. Kill I victim? Must summit civil like mod.'.lower()

    is_line_palindrome = is_palindrome(line)

    print(is_line_palindrome)


main()
