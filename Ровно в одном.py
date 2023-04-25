def is_one_away(word_1, word_2):
    value = True
    count = 0
    if len(word_1) == len(word_2):
        for i in range(len(word_1)):
            if word_1[i] != word_2[i]:
                count += 1
        if count != 1:
            value = False
    else:
        value = False
    return value


def main():
    word, another_word = input(), input()
    print(is_one_away(word, another_word))


main()
