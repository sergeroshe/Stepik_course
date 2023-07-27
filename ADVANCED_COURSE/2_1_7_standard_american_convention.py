SEP_CHAR = ','
input_string = str(int(input()))
num_string_list = list(input_string)
if len(input_string) > 3:
    num_first_part = num_string_list[:len(num_string_list) % 3]

    num_last_part_reversed = num_string_list[len(num_string_list) % 3:][::-1]
    for i in range(len(num_last_part_reversed), 1, -1):
        if i % -3 == 0:
            num_last_part_reversed.insert(i, SEP_CHAR)

    num_last_part = num_last_part_reversed[::-1]
    if num_first_part:
        result_string = ''.join(num_first_part + num_last_part)
    else:
        result_string = ''.join(num_first_part + num_last_part[1:])
else:
    result_string = input_string

print(result_string)
