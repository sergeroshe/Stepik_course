input_string_list = input().split()
skipped_el_amount = int(input())
# input_string_list = 'a b c d e f g h i j k l m n'.split()
# skipped_el_amount = 2

input_string_list_len = len(input_string_list)
result_list = []
for start_idx in range(skipped_el_amount):
    sublist = []
    for i in range(start_idx, input_string_list_len, skipped_el_amount):
        sublist.append(input_string_list[i])
    result_list.append(sublist)

print(result_list)

