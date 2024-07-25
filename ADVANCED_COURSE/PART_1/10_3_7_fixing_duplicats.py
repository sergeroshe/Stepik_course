input_string_list = input().split()
# input_string_list = 'a a a a a'.split()

word_dict = {}
result_word_list = []

for word in input_string_list:
    word_dict[word] = word_dict.get(word, 0) + 1
    if word_dict[word] < 2:
        result_word_list.append(word)
    else:
        result_word_list.append(f'{word}_{word_dict[word] - 1}')

print(*result_word_list)