string_amount = int(input())
column_amount = int(input())
result = ''
matrix = []
max_item_row_idx = 0
max_item_col_idx = 0
max_item = 0

for i in range(string_amount):
    row = input()
    row = [int(x) for x in row.split()]
    matrix.append(row)

result = ''
max_item = max(max(matrix, key=max))
flag = False
for i in range(string_amount):
    for j in range(column_amount):
        cur_item = matrix[i][j]
        if cur_item == max_item:
            result = f'{i} {j}'
            flag = True
            break
    if flag:
        break

print(matrix)
print(max_item)
print(result)
# matrix = [[0, 3, 2, 4], [2, 3, 5, 5], [5, 1, 2, 3]]
# string_amount = 3
# column_amount = 4