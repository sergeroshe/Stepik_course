matrix_size = int(input())
matrix = []

for _ in range(matrix_size):
    matrix.append(input().split())

for i in range(matrix_size // 2):
    matrix[i][i] = matrix[-(i + 1)][i]
    matrix[-(i + 1)][-(i + 1)] = matrix[i][-(i + 1)]

#  for i in range(n):
#     matrix[i][i], matrix[matrix_size - i - 1][i] = matrix[matrix_size - i - 1][i], matrix[i][i]

for row in matrix:
    print(*row)

# matrix_size = 5
# matrix = ['2 2 3 1 3'.split(),
#           '4 6 6 7 5'.split(),
#           '7 8 9 7 8'.split(),
#           '4 5 6 4 5'.split(),
#           '1 2 3 1 2'.split()]
# main_diagonal_left = matrix[i][i]
# secondary_diagonal_left = matrix[-(i + 1)][i]
# main_diagonal_right = matrix[-(i + 1)][-(i + 1)]
# secondary_diagonal_right = matrix[i][-(i + 1)]

# initial bad solution
# for i in range(matrix_size // 2):
#     for j in range(i + 1, matrix_size):
#         if i + j + 1 == matrix_size:
#             matrix[i][j], matrix[-(i + 1)][j] = matrix[-(i + 1)][j], matrix[i][j]


# 2 2 3 1 3  0, -1; 1, -2; 2, -3 -> i, -(i + 1)
# 4 6 6 7 5
# 7 8 9 7 8
# 4 5 6 4 5
# 1 2 3 1 2 -1, 0;  -2, 1; -3, 2

# 1 2 3 1 2   0, 0 -> -1, 0;   1, 1 -> -2, 1   1, -2 -> -2, -2
# 4 5 6 4 5
# 7 8 9 7 8
# 4 6 6 7 5
# 2 2 3 1 3
