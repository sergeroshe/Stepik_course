matrix_size = int(input())
matrix = []

for _ in range(matrix_size):
    matrix.append(input().split())

for i in range(matrix_size // 2):
    for j in range(matrix_size):
        matrix[i][j], matrix[-(i + 1)][j] = matrix[-(i + 1)][j], matrix[i][j]

for row in matrix:
    print(*row)