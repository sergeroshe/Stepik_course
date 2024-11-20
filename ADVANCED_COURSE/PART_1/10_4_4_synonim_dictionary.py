input_string_amount = int(input())
# input_string_amount = 1

input_string_list = [(input().split()) for _ in range(input_string_amount)]
translating_word = input()
# translating_word = 'Pretty'

synonim = ''
input_string_dict = {}

synonim_not_found = True
i = 0

while synonim_not_found and i < len(input_string_list):
    key, value = input_string_list[i]
    if key == translating_word:
        synonim = value
        synonim_not_found = False
    elif value == translating_word:
        synonim = key
        synonim_not_found = False
    i += 1


print(synonim)