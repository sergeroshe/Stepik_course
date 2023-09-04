#  Sample Input 1:
# 3
# Sample Output 1:
#
# [1, 2, 3]
# [1, 2, 3]
# [1, 2, 3]
# Sample Input 2:
total_list = []
row_number = 3
for i in range(row_number):
    cur_list = []
    for j in range(row_number):
        cur_list.append(j + 1)

    total_list.append(cur_list)

print(*total_list, sep='\n')
