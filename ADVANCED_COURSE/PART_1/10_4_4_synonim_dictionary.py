input_string_amount = int(input())
# input_string_amount = 1

input_string_list = [(input().split()) for _ in range(input_string_amount)]
translating_word = input()
# translating_word = 'Pretty'

synonim = ''
input_string_dict = {}
for key, value in input_string_list:
    if value == translating_word:
        synonim = key
    elif key == translating_word:
        synonim = value

print(synonim)
