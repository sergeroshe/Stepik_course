matrix_size = int(input())
matrix = []

for _ in range(matrix_size):
    matrix.append(input().split())

for i in range(matrix_size // 2):
    for j in range(i, matrix_size):
        if i == j or i + j + 1 == matrix_size:
            matrix[i][j], matrix[-(i + 1)][j] = matrix[-(i + 1)][j], matrix[i][j]

for row in matrix:
    print(*row)


# matrix = ['1 2 3 4'.split(),
#           '5 6 7 8'.split(),
#           '8 6 4 2'.split(),
#           '3 4 5 6'.split()]
