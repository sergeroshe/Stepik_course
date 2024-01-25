# rows, cols = [int(el) for el in input().split()]

rows = 6
cols = 8

num = 0

matrix = [[0] * cols for _ in range(rows)]
diagonal_count = rows + cols - 1

for i in range(diagonal_count):
    inner_loop_start_range = 0
    inner_loop_stop_range = (i + 1) % cols
    for j in range(inner_loop_start_range, inner_loop_stop_range):
        num += 1
        if j < rows and i < inner_loop_stop_range:
            matrix[j][i - j] = num
        # else:
        #     matrix[(j % rows) + j][(i % diagonal_count) - j] = num

for i in range(rows):
    for j in range(cols):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()

# 3 4
# 1  2  4  7
# 3  5  8  10
# 6  9  11 12

# 1[0, 0]

# 2[0, 1]
# 3[1, 0]

# 4[0, 2]
# 5[1, 1] i = 1
# 6[2, 0] i = 2

# 7[0, 3]
# 8[1, 2]
# 9[2, 1]

# 10[1, 3]
# 11[2, 2]

# 12[2, 3]


# 3 4
# 1  2  4  7
# 3  5  8  10
# 6  9  11 12
