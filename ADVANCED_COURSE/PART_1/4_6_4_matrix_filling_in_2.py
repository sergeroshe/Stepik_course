row_amount, column_amount = [int(el) for el in input().split()]
element_amount = column_amount * row_amount
matrix = []

for i in range(row_amount):
    row = []
    for j in range(i + 1, i + element_amount, row_amount):
        row.append(j)

    matrix.append(row)

for i in range(row_amount):
    for j in range(column_amount):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()


# 1  4  7  10 13 16 19
# 2  5  8  11 14 17 20
# 3  6  9  12 15 18 21
