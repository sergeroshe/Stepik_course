# rows, cols = [int(el) for el in input().split()]

rows = 5
cols = 7

matrix = [[0] * cols for _ in range(rows)]

num = 1
top = 0
bottom = rows - 1
left = 0
right = cols - 1

while top <= bottom and left <= right:
    for i in range(left, right + 1):
        matrix[top][i] = num
        num += 1
    top += 1

    for i in range(top, bottom + 1):
        matrix[i][right] = num
        num += 1
    right -= 1

    if top <= bottom:
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

    if left <= right:
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

for i in range(rows):
    for j in range(cols):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()

# 4 5

# 1  2  3  4  5
# 14 15 16 17 6
# 13 20 19 18 7
# 12 11 10 9  8
