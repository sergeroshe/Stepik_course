row_amount = int(input())
col_amount = int(input())
# row_amount = 2
# col_amount = 3
matrix = []
row_list = []

for _ in range(row_amount):
    for _ in range(col_amount):
        row_list.append(input())

    matrix.append(row_list)
    row_list = []

for row in range(row_amount):
    for col in range(col_amount):
        print(matrix[row][col], end=' ')
    print()

print()

for col in range(col_amount):
    for row in range(row_amount):
        print(matrix[row][col], end=' ')
    print()
