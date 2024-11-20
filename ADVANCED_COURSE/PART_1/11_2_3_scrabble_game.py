WORD_COST_DICT = {1: ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'],
                  2: ['D', 'G'],
                  3: ['B', 'C', 'M', 'P'],
                  4: ['F', 'H', 'V', 'W', 'Y'],
                  5: ['K'],
                  8: ['J', 'X'],
                  10: ['Q', 'Z']}

input_word = input()
# input_word = 'DANSER'
word_cost = 0
for letter in input_word:
    for point, letter_list in WORD_COST_DICT.items():
        if letter in letter_list:
            word_cost += point
            break

print(word_cost)