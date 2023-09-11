num_list = [-48, -41, -32, 5, 78, 84, 90, 96, -71]
list_len = len(num_list)

for i in range(list_len - 1, -1, -1):
    max_num = num_list[i]
    max_num_idx = i
    for j in range(i - 1, -1, -1):
        if num_list[j] > max_num:
            max_num = num_list[j]
            max_num_idx = j
    num_list[i], num_list[max_num_idx] = num_list[max_num_idx], num_list[i]

print(num_list)
