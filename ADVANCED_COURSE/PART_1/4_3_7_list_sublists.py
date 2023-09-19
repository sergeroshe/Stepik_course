# source_string_list = input().split()
source_string_list = 'a b c'.split()
len_source_string = len(source_string_list)

sub_list = []
# total_list = [source_string_list[i: i + 1] for i in range(0, len(source_string_list), 1)]
total_list = [[]]
for i in range(len_source_string):
    sub_list_size = i + 1
    for cur_char_idx in range(len_source_string):
        sub_list = source_string_list[cur_char_idx: cur_char_idx + sub_list_size]
        if len(sub_list) == sub_list_size:
            total_list.append(sub_list)
        else:
            break

print(total_list)

# for i in range(len_source_string):
#     for j in range(len_source_string):
#         sub_list = source_string[j: j + i + 1]
#         if len(sub_list) == i + 1:
#             total_list.append(sub_list)
#         else:
#             break


