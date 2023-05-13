def is_palindrome(sentence):
    value = True
    len_s = len(sentence) - 1
    left_side_idx = 0
    right_side_idx = len_s

    while left_side_idx != right_side_idx:
        left_side_element = sentence[left_side_idx]
        right_side_element = sentence[right_side_idx]
        if left_side_element in VALID_CHAR_LIST and right_side_element in VALID_CHAR_LIST:
            left_side_idx += 1
            right_side_idx -= 1
            if right_side_element != left_side_element:
                value = False
                break
        elif left_side_element not in VALID_CHAR_LIST:
            left_side_idx += 1
        elif right_side_element not in VALID_CHAR_LIST:
            right_side_idx -= 1
        else:
            left_side_idx += 1
            right_side_idx -= 1

    return value


VALID_CHAR_LIST = 'abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def main():
    line = input().lower()
    # line = 'Карман, жена, но Какашкин - вор! О, Ковалева... Вела во коровник. Ша! Как она нежна! рак...'.lower()

    is_line_palindrome = is_palindrome(line)

    print(is_line_palindrome)


main()