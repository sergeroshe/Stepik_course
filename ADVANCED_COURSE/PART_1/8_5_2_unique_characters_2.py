word_amount = int(input())
word_list = [input() for _ in range(word_amount)]
# word_list = ['авТорИтет', 'небо', 'машинА', 'Мёд']

set_word_list = []
for word in word_list:
    set_word_list.extend(set(word.lower()))

print(len(set(set_word_list)))
