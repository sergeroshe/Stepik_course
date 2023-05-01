SEP_CHAR = '_'


def convert_to_python_case(text):
    word_list = []
    start_word_idx = 0

    for i in range(1, len(text)):
        string_letter = text[i]
        if string_letter.isupper():
            end_word_idx = i
            word_list.append(text[start_word_idx:end_word_idx].lower())
            start_word_idx = end_word_idx

    word_list.append(text[start_word_idx:].lower())
    converted_string = SEP_CHAR.join(word_list)

    return converted_string


def main():
    txt = 'ThisIsCamelCased'

    converted_to_python_string = convert_to_python_case(txt)

    print(converted_to_python_string)


main()
