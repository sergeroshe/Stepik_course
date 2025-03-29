# input_string_list = input().lower().split()
input_string_list = input().lower().split()
#
# input_string_list = 'London is the capital of Great Britain. ' \
#                     'More than six million people live in London. ' \
#                     'London lies on both banks of the river Thames. ' \
#                     'It is the largest city in Europe and one of the ' \
#                     'largest cities in the world. London is not only the' \
#                     ' capital of the country, it is also a very big port,' \
#                     ' one of the greatest commercial centres in the world,' \
#                     ' a university city, and the seat' \
#                     ' of the government of Great Britain!'.lower().split()

word_dict = {}

for word in input_string_list:
    word = word.strip(' .,!?:;-')
    word_dict[word.strip(' .,!?:;-')] = word_dict.get(word, 0) + 1

min_word_occuring_amount = min(word_dict.values())

rarest_word_list = []

for k, v in word_dict.items():
    if v == min_word_occuring_amount:
        rarest_word_list.append(k)

print(min(rarest_word_list))