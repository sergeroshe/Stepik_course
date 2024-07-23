text_string = 'orange strawberry barley gooseberry apple apricot barley' \
    ' currant orange melon pomegranate banana banana orange barley' \
    ' apricot plum grapefruit banana quince strawberry barley' \
    ' grapefruit banana grapes melon strawberry apricot currant' \
    ' currant gooseberry raspberry apricot currant orange' \
    ' lime quince grapefruit barley banana melon pomegranate' \
    ' barley banana orange barley apricot plum banana quince ' \
    'lime grapefruit strawberry gooseberry apple barley apricot' \
    ' currant orange melon pomegranate banana banana orange apricot ' \
    'barley plum banana grapefruit banana quince currant orange melon' \
    ' pomegranate barley plum banana quince barley lime grapefruit' \
    ' pomegranate barley'.split()

word_dict = {}
most_frequent_word = ''
max_word_occuring_amount = 0
word_occuring_amount = 0


for word in text_string:
    if word not in word_dict:
        word_dict[word] = text_string.count(word)
        word_occuring_amount = word_dict[word]
        if word_occuring_amount > max_word_occuring_amount or\
                (word_occuring_amount == max_word_occuring_amount
                 and word < most_frequent_word):
            max_word_occuring_amount = word_occuring_amount
            most_frequent_word = word

print(most_frequent_word)




