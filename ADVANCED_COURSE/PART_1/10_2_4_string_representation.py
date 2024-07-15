NUMBER_DICT = {'0': 'zero',
               '1': 'one',
               '2': 'two',
               '3': 'three',
               '4': 'four',
               '5': 'five',
               '6': 'six',
               '7': 'seven',
               '8': 'eight',
               '9': 'nine'
               }

input_string_number = input()

string_number_list = [NUMBER_DICT[dig] for dig in input_string_number]

print(*string_number_list)