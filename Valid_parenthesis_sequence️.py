OPENING_PARENTHESIS = '('
CLOSING_PARENTHESIS = ')'


def is_correct_bracket(text):
    count = 0

    for char in text:
        if char == OPENING_PARENTHESIS:
            count += 1
        elif char == CLOSING_PARENTHESIS:
            count -= 1
        if count < 0:
            break
    value = count == 0

    return value


def main():
    txt = input()

    is_bracket_correct = is_correct_bracket(txt)

    print(is_bracket_correct)


main()
