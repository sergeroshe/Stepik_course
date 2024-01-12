matrix_size = int(input())
# matrix_size = 5

matrix = []

for i in range(matrix_size):
    row = []
    for j in range(matrix_size):
        if i == j\
                or i + j + 1 == matrix_size\
                or i < j and i + j + 1 < matrix_size\
                or i > j and i + j + 1 > matrix_size:
            row.append(1)
        else:
            row.append(0)
    matrix.append(row)

for row in matrix:
    print(*row, sep=' ')
# если элемент находится выше главной диагонали, то i < j, если ниже - i > j.
# если элемент находится выше побочной диагонали, то i + j + 1 < n, если ниже - i + j + 1 > n.