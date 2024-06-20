word_amount = int(input())
word_list = [input() for _ in range(word_amount)]

unique_char_amount_list = [len(set(word.lower())) for word in word_list]

print(unique_char_amount_list, sep='\n')
