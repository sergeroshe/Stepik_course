# row_amount, column_amount = [int(el) for el in input().split()]
#
row_amount = 5
column_amount = 3
matrix = []
k = 1
l = 0

for i in range(row_amount):
    row = []
    for j in range(column_amount):
        if i % 2 == 0:
            row.append(k)
            l = k
        else:
            row.append(l + column_amount - j)
        k += 1

    matrix.append(row)

# 1   2   3
# 6   5   4
# 7   8   9
# 12  11  10
# 13  14  15

for i in range(row_amount):
    for j in range(column_amount):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
