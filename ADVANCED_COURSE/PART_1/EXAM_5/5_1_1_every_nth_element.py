input_string_list = input().split()
skipped_el_amount = int(input())
# input_string_list = 'a b c d e f g h i j k l m n'.split()
# skipped_el_amount = 2

input_string_list_len = len(input_string_list)
result_list = []
for i in range(skipped_el_amount):
    sublist = []
    for j in range(i, input_string_list_len, skipped_el_amount):
        if input_string_list[j] not in result_list:
            sublist.append(input_string_list[j])
    result_list.append(sublist)

print(result_list)

