row_amount = int(input())
col_amount = int(input())
# row_amount = 2
# col_amount = 3
matrix = []

for i in range(row_amount):
    row_list = []
    for j in range(col_amount):
        row_list.append(input())

    matrix.append(row_list)

for row in range(row_amount):
    for col in range(col_amount):
        print(matrix[row][col], end=' ')
    print()

