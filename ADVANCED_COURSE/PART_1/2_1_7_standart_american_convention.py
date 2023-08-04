SEP_CHAR = ','
num_reversed = str(int(input()))[::-1]

num_reversed_separated = [num_reversed[i: i + 3] for i in range(0, len(num_reversed), 3)]
num_reversed = SEP_CHAR.join(num_reversed_separated)
num = num_reversed[::-1]

print(num)


# my_list = ['000', '000', '000']
# my_string = SEP_CHAR.join(my_list)
# print(my_string)
