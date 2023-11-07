matrix_size = int(input())
# matrix_size = 3
matrix = []

for _ in range(matrix_size):
    matrix.append(input().split())


for i in range(matrix_size // 2):
    for j in range(matrix_size):
        matrix[i][j], matrix[-(i + 1)][j] = matrix[-(i + 1)][j], matrix[i][j]

result_matrix = []
for i in range(matrix_size):
    row = []
    for j in range(matrix_size):
        row.append(matrix[j][i])
    result_matrix.append(row)

for row in result_matrix:
    print(*row)

#
#
# matrix = ['1 2 3'.split(),
#           '4 5 6'.split(),
#           '7 8 9'.split()]

# result = 7 4 1 [0][0] = [0][2], [0][1] = [1][2], [0][2] = [2][2],
#          8 5 2 [1][2] = [2][1]
#          9 6 3