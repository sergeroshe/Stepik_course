SENTENCE_AMOUNT = 2
POSITIVE_ANSWER = 'YES'
NEGATIVE_ANSWER = 'NO'
IGNORE_CHAR_LIST = '.,!?:;- '

answer = POSITIVE_ANSWER

sentence_list = [[word.strip(IGNORE_CHAR_LIST) for word in input().lower()]
                 for _ in range(SENTENCE_AMOUNT)]

word_dict_list = []
for word in sentence_list:
    cur_dict = {}
    for char in word:
        if char:
            cur_dict[char] = cur_dict.get(char, 0) + 1
    word_dict_list.append(cur_dict)

word_dict_list_len = len(word_dict_list)

i = 0
dicts_equal = True
while dicts_equal and i < word_dict_list_len:
    if word_dict_list[i] != word_dict_list[i - 1]:
        answer = NEGATIVE_ANSWER
    i += 1

print(answer)

# sentence_1_list = [word.strip(IGNORE_CHAR_LIST) for word in 'William Shakespeare'.lower()]
# sentence_2_list = [word.strip(IGNORE_CHAR_LIST) for word in 'I am a weakish: speller,'.lower()]
