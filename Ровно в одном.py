def has_diff(word_1, word_2, diff_count):
    value = True
    count = 0
    word_1_len = len(word_1)
    word_2_len = len(word_2)
    if word_1_len == word_2_len:
        for i in range(word_1_len):
            if word_1[i] != word_2[i]:
                count += 1
        value = count == diff_count
    else:
        value = False
    return value


####################################################


DIFF_COUNT = 1


def main():

    word, another_word = 'asdfa', 'asdfl'

    is_difference_num_valid = has_diff(word, another_word, DIFF_COUNT)

    print(is_difference_num_valid)


main()
