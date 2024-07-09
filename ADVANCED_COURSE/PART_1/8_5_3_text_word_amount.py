word_set = {word.strip('.,;:-?!').lower() for word in input().split()}

string_word_amount = len(word_set)

print(string_word_amount)