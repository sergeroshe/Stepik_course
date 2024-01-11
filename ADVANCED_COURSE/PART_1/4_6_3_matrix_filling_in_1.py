row_amount = int(input())
column_amount = int(input())

# row_amount = 3
# column_amount = 4
matrix = []
k = 0

for i in range(row_amount):
    row = []
    for j in range(k, k + column_amount):
        row.append(j + 1)
        k = j + 1
    matrix.append(row)


for i in range(row_amount):
    for j in range(column_amount):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
