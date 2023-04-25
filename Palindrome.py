# объявление функции
def is_palindrome(sentence):
    value = True
    ignore_chars_list = ' ,.!?-'

    for char in ignore_chars_list:
        if char in ignore_chars_list:
            sentence = sentence.replace(char, '')

    half_len = len(sentence) // 2 + len(sentence) % 2
    len_s = len(sentence)

    for i in range(half_len):
        cat = sentence[len_s - 1 - i]
        dog = sentence[i]
        if cat != dog:
            value = False
            break
    return value


def main():
    line = input().lower()
    print(is_palindrome(line))

