matrix_size = int(input())
# matrix_size = 5

matrix = []

for i in range(matrix_size):
    row = []
    for j in range(matrix_size):
        if i + j + 1 == matrix_size or i == j:
            row.append(1)

        else:
            row.append(0)
    matrix.append(row)


for row in matrix:
    print(*row, sep=' ')
