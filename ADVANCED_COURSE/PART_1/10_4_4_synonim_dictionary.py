input_string_amount = int(input())

synonim = ''
input_string_dict = {}
for _ in range(input_string_amount):
    key, value = input().split()
    input_string_dict[key], input_string_dict[value] = value, key

translating_word = input()

synonim = input_string_dict[translating_word]


print(input_string_dict)
print(synonim)
