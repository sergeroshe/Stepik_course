IGNORE_CHAR_LIST = ' .,-_:!@#$%^&?'


def is_palindrome(text):
    result = True
    left_side_idx = 0
    right_side_idx = len(text) - 1

    while left_side_idx != right_side_idx:
        left_side_element = text[left_side_idx]
        right_side_element = text[right_side_idx]
        is_left_side_letter = left_side_element not in IGNORE_CHAR_LIST
        is_right_side_letter = right_side_element not in IGNORE_CHAR_LIST

        if is_left_side_letter and is_right_side_letter:
            if left_side_element != right_side_element:
                result = False
                break
            else:
                left_side_idx += 1
                right_side_idx -= 1
        else:
            if not is_left_side_letter:
                left_side_idx += 1

            if not is_right_side_letter:
                right_side_idx -= 1

    return result


def main():
    line = input().lower()
    # line = 'Карман, жена, но Какашкин - вор! ' \
    #        'О, Ковалева... Вела во коровник. Ша! Как она нежна! рак...'.lower()

    is_line_palindrome = is_palindrome(line)

    print(is_line_palindrome)


main()
