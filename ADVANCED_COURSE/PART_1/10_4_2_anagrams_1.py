WORD_AMOUNT = 2
POSITIVE_ANSWER = 'YES'
NEGATIVE_ANSWER = 'NO'

answer = POSITIVE_ANSWER

word_dct_list = []

for _ in range(WORD_AMOUNT):
    word = input()
    dct = {}
    for letter in word:
        dct[letter] = dct.get(letter, 0) + 1
    word_dct_list.append(dct)

word_dct_list_len = len(word_dct_list)

i = 0
dicts_equal = True
while dicts_equal and i < word_dct_list_len:
    if word_dct_list[i] != word_dct_list[i - 1]:
        answer = NEGATIVE_ANSWER
    i += 1

print(answer)
