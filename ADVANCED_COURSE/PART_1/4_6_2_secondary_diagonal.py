# matrix_size = int(input())
matrix_size = 8

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


# for i in range(matrix_size):
#     matrix[-(i + 1)][i] = 1
#     for j in range(i + 1, matrix_size):
#         matrix[-(i + 1)][j] = 2

for row in matrix:
    print(*row, sep=' ')
