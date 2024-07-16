PHONE_KEYS_DICT = {1: '.,?!:',
                   2: 'ABC',
                   3: 'DEF',
                   4: 'GHI',
                   5: 'JKL',
                   6: 'MNO',
                   7: 'PQRS',
                   8: 'TUV',
                   9: 'WXYZ',
                   0: ' '
                   }
phone_keys_dict_list_len = len(PHONE_KEYS_DICT)

input_string = input().upper()
# input_string = 'Hello, World!'.upper()

output_string = ''

for char in input_string:
    char_found = False
    i = 0
    while not char_found and i < phone_keys_dict_list_len:
        k = i
        v = PHONE_KEYS_DICT[k]
        if char in v:
            char_idx = v.index(char) + 1
            output_string += str(k) * char_idx
            char_found = True
        i += 1

print(output_string)
