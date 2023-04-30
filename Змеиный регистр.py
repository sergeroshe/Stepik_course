SEP_CHAR = '_'


def convert_to_python_case(text):
    word_list = []
    start_word = 0

    for i in range(len(text)):
        string_letter = text[i]
        if i > 0:
            if string_letter.isupper():
                end_word = i
                word_list.append(text[start_word:end_word].lower() + SEP_CHAR)
                start_word = end_word

    word_list.append(text[start_word:].lower())
    converted_string = ''.join(word_list)

    return converted_string


def main():
    txt = input()

    converted_to_python_string = convert_to_python_case(txt)

    print(converted_to_python_string)


main()
