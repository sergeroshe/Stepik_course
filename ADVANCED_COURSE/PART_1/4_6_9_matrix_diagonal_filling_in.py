rows, cols = [int(el) for el in input().split()]
# rows = 3
# cols = 5

num = 1

matrix = [[0] * cols for _ in range(rows)]

for i in range(cols - 1):
    x = i + 1 if i + 1 <= rows else rows
    for j in range(x):
        matrix[j][i - j] = num
        num += 1

for i in range(rows):
    if rows - 1 - i >= cols - 1:
        y = cols

    else:
        y = rows - i
    k = 0
    for j in range(i, i + y):
        matrix[j][cols - 1 - k] = num
        k += 1
        num += 1

for i in range(rows):
    for j in range(cols):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()


# 1  2  (# 1: i = 0, j = 0;)  # 2:  i = 0, j = 1
# 3  4  # 3: i = 1, j = 0;  # 4:  i = 1, j = 1
# 5  6  # 5: i = 2, j = 0;  # 6:  i = 2, j = 1
# 7  8  # 7: i = 3, j = 0;  # 8:  i = 3, j = 1
# 9  10 # 9: i = 4, j = 0;  # 10: i = 4, j = 1


# 3 4
# 1  2  4  7
# 3  5  8  10
# 6  9  11 12

# 3 4
# 1   2   4
# 3   5   7
# 6   8   10
# 9   11  12

# add one more loop for the movement within the last column


# 1  2  4  7  10
# 3  5  8  11 13
# 6  9  12 14 15

# i = 0, 1
# i = 1, 2
# i = 2, 3
# i = 3, 3
# i = 4, 3

# 1[0, 0] 0, 1

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
