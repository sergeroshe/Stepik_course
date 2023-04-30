def is_correct_bracket(text):
    opening_parenthesis = '('
    closing_parenthesis = ')'
    count = 0

    is_parenthesis_open = False
    value = False
    for char in text:
        if char == opening_parenthesis:
            count += 1
            is_parenthesis_open = True
        elif char == closing_parenthesis:
            count -= 1
            if count == 0:
                is_parenthesis_open = False
        if count < 0:
            is_parenthesis_open = True
            break
    if not is_parenthesis_open:
        value = True

    return value


def main():

    txt = input()

    is_bracket_correct = is_correct_bracket(txt)

    print(is_bracket_correct)


main()
