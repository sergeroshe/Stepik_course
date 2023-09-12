source_string = input().split()
# source_string = 'a b c'.split()
len_source_string = len(source_string)

total_list = [[]]
sub_list = []

for i in range(len_source_string):
    sublist_increases = True
    j = 0
    while sublist_increases:
        sub_list = source_string[j: j + i + 1]
        if len(sub_list) == i + 1:
            total_list.append(sub_list)
        sublist_increases = len(sub_list) == i + 1
        j += 1

print(total_list)

# for i in range(len_source_string):
#     for j in range(len_source_string):
#         sub_list = source_string[j: j + i + 1]
#         if len(sub_list) == i + 1:
#             total_list.append(sub_list)
#         else:
#             break
