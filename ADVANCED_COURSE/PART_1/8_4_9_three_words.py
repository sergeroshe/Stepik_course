Y_ANSWER = 'YES'
N_ANSWER = 'NO'

answer = Y_ANSWER

word_set_list = [set(word) for word in input().split()]

# word_list = [set(word) for word in 'автор товар отвар'.split()]
word_set_list_len = len(word_set_list)

char_set_equal = True

i = 0
while char_set_equal and i <= word_set_list_len - 1:
    char_set_equal = word_set_list[i] == word_set_list[i - 1]
    i += 1

if not char_set_equal:
    answer = N_ANSWER

print(answer)
