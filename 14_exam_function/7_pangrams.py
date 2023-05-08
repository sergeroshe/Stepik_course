ALFABET = 'abcdefghijklmnopqrstuvwxyz'
LEN_ALFABET = len(ALFABET)
skip_list = []


def is_pangram(text):
    match_count = 0
    result_output = True
    lower_text = text.lower()

    for c in lower_text:
        if c not in skip_list:
            for d in ALFABET:
                if c == d:
                    skip_list.append(c)
                    match_count += 1
                    break
        if len(skip_list) == LEN_ALFABET or match_count == LEN_ALFABET:
            break

    if match_count < LEN_ALFABET:
        result_output = False

    return result_output


def main():
    input_text = 'Jackdaws love my big sphinx of quartz'

    is_input_text_pangram = is_pangram(input_text)

    print(is_input_text_pangram)


main()
