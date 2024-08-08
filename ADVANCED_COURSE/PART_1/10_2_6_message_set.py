PHONE_KEYS_DICT = {'.,?!:': 1,
                   'ABC': 2,
                   'DEF': 3,
                   'GHI': 4,
                   'JKL': 5,
                   'MNO': 6,
                   'PQRS': 7,
                   'TUV': 8,
                   'WXYZ': 9,
                   ' ': 0}

# input_string = input().upper()
input_string = 'Hello, World!'.upper()
#
output_string = ''

for char in input_string:
    for key in PHONE_KEYS_DICT:
        if char in key:
            output_string += str(PHONE_KEYS_DICT[key]) * (key.index(char) + 1)
            break

print(output_string)
