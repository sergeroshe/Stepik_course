matrix_size = int(input())

matrix = []

for i in range(matrix_size):
    row = []
    for j in range(matrix_size):
        if i + j + 1 == matrix_size:
            row.append(1)
        elif i + j + 1 > matrix_size:
            row.append(2)
        else:
            row.append(0)
    matrix.append(row)

for row in matrix:
    print(*row, sep=' ')
