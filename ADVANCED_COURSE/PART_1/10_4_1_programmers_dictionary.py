NOT_FOUND_MESSAGE = 'Не найдено'
dictionary_word_amount = int(input())

dictionary = {}

for _ in range(dictionary_word_amount):
    key, value = input().split(': ')
    dictionary[key.lower()] = value

translating_word_amount = int(input())

result_string_list = []

for _ in range(translating_word_amount):
    translating_word = input().lower()
    if translating_word in dictionary:
        result_string_list.append(dictionary.get(translating_word))
    else:
        result_string_list.append(NOT_FOUND_MESSAGE)

print(*result_string_list, sep='\n')
