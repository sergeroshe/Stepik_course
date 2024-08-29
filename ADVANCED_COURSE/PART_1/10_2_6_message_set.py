PHONE_KEYS_DICT = {1: '.,?!:',
                   2: 'ABC',
                   3: 'DEF',
                   4: 'GHI',
                   5: 'JKL',
                   6: 'MNO',
                   7: 'PQRS',
                   8: 'TUV',
                   9: 'WXYZ',
                   0: ' '}
CHAR_KEY_PUSH_NUMBER = {char: str(number) * (value.index(char) + 1) for number, value in PHONE_KEYS_DICT.items()
                        for char in value}

input_string = input().upper()

result_string = ''
for char in input_string:
    result_string += CHAR_KEY_PUSH_NUMBER.get(char, '')

print(result_string)


