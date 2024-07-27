WORD_AMOUNT = 2
POSITIVE_ANSWER = 'YES'
NEGATIVE_ANSWER = 'NO'

answer = POSITIVE_ANSWER

word_dcts = [{} for _ in range(WORD_AMOUNT)]

for dct in word_dcts:
    word = input()
    for letter in word:
        dct[letter] = dct.get(letter, 0) + 1

if word_dcts[0] != word_dcts[1]:
    answer = NEGATIVE_ANSWER

print(answer)