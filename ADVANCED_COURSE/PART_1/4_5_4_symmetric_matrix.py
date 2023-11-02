Y_MESSAGE = 'YES'
N_MESSAGE = 'NO'

matrix_size = int(input())
matrix = [input().split() for _ in range(matrix_size)]
#
# matrix = ['0 1 2'.split(),
#           '1 2 7'.split(),
#           '2 3 4'.split()]
# matrix_size = len(matrix)

# 0 1 2
# 1 2 7
# 2 3 4
answer = Y_MESSAGE
symmetric = True
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        symmetric = matrix[i][j] == matrix[j][i]
    if not symmetric:
        answer = N_MESSAGE
        symmetric = False
        break

print(answer)
