row_amount = int(input())
col_amount = int(input())
# row_amount = 2
# col_amount = 3


matrix = []
row_list = []

for i in range(row_amount):
    for j in range(col_amount):
        row_list.append(input())

    matrix.append(row_list)
    row_list = []

for row in matrix:
    for col in row:
        print(col, end=' ')
    print()

