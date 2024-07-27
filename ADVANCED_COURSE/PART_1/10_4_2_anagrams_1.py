WORD_AMOUNT = 2
POSITIVE_ANSWER = 'YES'
NEGATIVE_ANSWER = 'NO'

input_string_dict_list = []

word_1 = input()
# word_1 = 'cat'

word_1_dict = {}
for letter in word_1:
    word_1_dict[letter] = word_1_dict.get(letter, 0) + 1

word_2 = input()
# word_2 = 'rat'


word_2_dict = {}
for letter in word_2:
    word_2_dict[letter] = word_2_dict.get(letter, 0) + 1

answer = POSITIVE_ANSWER

if word_1_dict != word_2_dict:
    answer = NEGATIVE_ANSWER

print(answer)



