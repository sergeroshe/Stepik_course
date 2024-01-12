row_amount, column_amount = [int(el) for el in input().split()]
# row_amount = 3
# column_amount = 4
matrix = []
k = 1

for _ in range(row_amount):
    row = []
    for _ in range(column_amount):
        row.append(k)
        k += 1

    matrix.append(row)

for i in range(row_amount):
    for j in range(column_amount):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
