input_string_list = input().split()
skipped_el_amount = int(input())

input_string_list_len = len(input_string_list)
result_list = []
for start_idx in range(skipped_el_amount):
    sublist = input_string_list[start_idx::skipped_el_amount]
    result_list.append(sublist)

print(result_list)

