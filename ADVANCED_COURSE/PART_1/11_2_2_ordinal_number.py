input_string_list = input().split()
ocurrencies_list = []

ocurrencies_number_dict = {}
for word in input_string_list:
    ocurrencies_number_dict[word] = ocurrencies_number_dict.get(word, 0) + 1
    ocurrencies_list.append(ocurrencies_number_dict[word])

print(*ocurrencies_list)