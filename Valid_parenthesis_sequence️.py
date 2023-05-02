def is_correct_bracket(text):
    opening_parenthesis = '('      # move to constant
    closing_parenthesis = ')'           # is_parenthesis_open
    count = 0

    value = False
    for char in text:
        if char == opening_parenthesis:
            count += 1
        elif char == closing_parenthesis:
            count -= 1
        if count < 0:
            break
    if count == 0:
        value = True

    return value


def main():
    txt = input()

    is_bracket_correct = is_correct_bracket(txt)

    print(is_bracket_correct)


main()
