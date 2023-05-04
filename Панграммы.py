LOWER_RANGE = 97
UPPER_RANGE = 123


def is_pangram(text):
    result_output = True

    for i in range(LOWER_RANGE, UPPER_RANGE):
        if chr(i) not in text:
            result_output = False
            break

    return result_output


def main():
    input_string = input().lower()
    print(is_pangram(input_string))


main()