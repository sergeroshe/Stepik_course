# rows, cols = [int(el) for el in input().split()]

rows = 3
cols = 4

diagonal_num = 0
num = 0

matrix = [[0] * cols for _ in range(rows)]

for diagonal_num in range(rows + cols - 1):
    for i in range(rows):
        for j in range(cols):
            if i + j == diagonal_num:
                num += 1
                matrix[i][j] = num

for i in range(rows):
    for j in range(cols):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()

# 3 4
# 1  2  4  7
# 3  5  8  10
# 6  9  11 12
