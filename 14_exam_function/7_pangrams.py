ALFABET = 'abcdefghijklmnopqrstuvwxyz'
LEN_ALFABET = len(ALFABET)


def is_pangram(text):
    processed_chars = []
    match_count = 0
    lower_text = text.lower()

    for c in lower_text:
        if c not in processed_chars:
            if c in ALFABET:
                processed_chars.append(c)
                match_count += 1
        if match_count == LEN_ALFABET:
            break

    result_output = match_count >= LEN_ALFABET

    return result_output


def main():
    input_text = 'jsdfhsadfhkljsad'

    is_input_text_pangram = is_pangram(input_text)

    print(is_input_text_pangram)


main()
