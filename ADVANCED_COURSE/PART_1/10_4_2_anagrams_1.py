WORD_AMOUNT = 2
POSITIVE_ANSWER = 'YES'
NEGATIVE_ANSWER = 'NO'

answer = POSITIVE_ANSWER

word_list = [input() for _ in range(WORD_AMOUNT)]

word_dict_list = []
word_list_len = len(word_list)

for word in word_list:
    cur_dict = {}
    for letter in word:
        cur_dict[letter] = cur_dict.get(letter, 0) + 1
    word_dict_list.append(cur_dict)

word_dict_list_len = len(word_dict_list)

i = 0
dicts_equal = True
while dicts_equal and i < word_dict_list_len:
    if word_dict_list[i] != word_dict_list[i - 1]:
        answer = NEGATIVE_ANSWER
    i += 1

print(answer)
