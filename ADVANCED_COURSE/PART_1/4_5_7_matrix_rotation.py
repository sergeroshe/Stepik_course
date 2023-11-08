# matrix_size = int(input())
# matrix = []
#
# for _ in range(matrix_size):
#     matrix.append(input().split())
matrix_size = 4
matrix = ['1 2 3 4'.split(),
          '5 6 7 8'.split(),
          '8 6 4 2'.split(),
          '3 4 5 6'.split()]
# result = 3 8 5 1
        #  4 6 6 2
        #  5 4 7 3
        #  6 2 8 4

# 0 0 = 0 -1, 0 1 = 1 -1, 0 -2 = -2 -1, 0 -1 = -1 -1,
# 1 0 = 0 -2,
# i = 0: i = 0, j = 0: j = -1
# i + j = 3:
# i = matrix_size - (i + j) -> 3-3=0;
# j = i + matrix_size -> 0 + 3 = 3
# for i in range(matrix_size):
#     row = matrix[i]
#     column = []
#     for j in range(matrix_size):
#         column.append(matrix[j][i])
#     matrix[i] = column
rotated = zip(*reversed(matrix))
for row in rotated:
    print(*row)

# for i in range(matrix_size // 2):
#     for j in range(matrix_size):
#         matrix[i][j], matrix[-(i + 1)][j] = matrix[-(i + 1)][j], matrix[i][j]
#
# for row in matrix:
#     print(*row)
# print()
#
# matrix_size = 4
# matrix = ['1 2 3 4'.split(),
#           '5 6 7 8'.split(),
#           '8 6 4 2'.split(),
#           '3 4 5 6'.split()]
# result_matrix = []
# for i in range(matrix_size):
#     row = []
#     for j in range(matrix_size):
#         row.append(matrix[j][i])
#     result_matrix.append(row)

#
#
# matrix = ['1 2 3'.split(),
#           '4 5 6'.split(),
#           '7 8 9'.split()]

# result = 7 4 1 [0][0] = [0][2], [0][1] = [1][2], [0][2] = [2][2],
#          8 5 2 [1][2] = [2][1]
#          9 6 3
