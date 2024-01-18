# row_amount, column_amount = [int(el) for el in input().split()]
#
row_amount = 5
column_amount = 3
matrix = []
val_list = [i for i in range(1, column_amount + 1)]

val_list_idx = 0
for i in range(row_amount):
    val_list_idx = i % column_amount
    row = val_list[val_list_idx:] + val_list[:val_list_idx]
    matrix.append(row)

for i in range(row_amount):
    for j in range(column_amount):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
