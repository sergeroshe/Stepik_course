matrix_size = int(input())
matrix = []

for _ in range(matrix_size):
    matrix.append(input().split())

for i in range(matrix_size):
    for j in range(i + 1, matrix_size):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    matrix[i].reverse()

for row in matrix:
    print(*row)

# matrix_size = 4
# matrix = ['1 2 3 4'.split(),
#           '5 6 7 8'.split(),
#           '9 10 11 12'.split(),
#           '13 14 15 16'.split()]
# result_matrix = []
# for i in range(matrix_size):
#     row = []
#     for j in range(matrix_size):
#         row.append(matrix[j][i])
#     result_matrix.append(row)


