# row_amount, column_amount = [int(el) for el in input().split()]
#
row_amount = 5
column_amount = 3
matrix = []
k = 1
last_col_idx = 0

for i in range(row_amount):
    row = []
    last_col_idx = k - 1
    row_even = i % 2 == 0
    for j in range(column_amount):
        row.append(k if row_even else last_col_idx + column_amount - j)
        k += 1

    matrix.append(row)

for i in range(row_amount):
    for j in range(column_amount):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
