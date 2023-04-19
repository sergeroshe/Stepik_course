num_list = [78, -32, 5]
list_len = len(num_list)

for i in range(list_len - 1):
    max_current_idx = num_list.index(max(num_list[:list_len - i]))
    num_list[max_current_idx], num_list[-i - 1] = num_list[-i - 1], num_list[max_current_idx]

print(num_list)