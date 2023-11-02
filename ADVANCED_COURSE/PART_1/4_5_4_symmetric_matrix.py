POSITIVE_ANSWER = 'YES'
NEGATIVE_ANSWER = 'NO'

matrix_size = int(input())
matrix = [input().split() for _ in range(matrix_size)]

# matrix = ['0 1 2'.split(),
#           '1 2 7'.split(),
#           '2 3 4'.split()]
# matrix_size = len(matrix)

answer = POSITIVE_ANSWER
is_symmetric = True
i = 0
while is_symmetric and i < len(matrix):
    j = 0
    while is_symmetric and j < len(matrix[i]):
        is_symmetric = matrix[i][j] == matrix[j][i]
        j += 1
    i += 1

if not is_symmetric:
    answer = NEGATIVE_ANSWER
    symmetric = False

print(answer)
