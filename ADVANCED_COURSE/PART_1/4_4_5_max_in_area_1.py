size = int(input())
# size = 3

matrix = []
row = []
for _ in range(size):
    row = input().split()
    int_row = [int(item) for item in row]
    matrix.append(int_row)
#
# print(matrix)

# Программа должна вывести одно число —
# максимальный элемент в заштрихованной области квадратной матрицы.
# если элемент находится выше главной диагонали, то i < j, если ниже - i > j

# matrix = [[-50, -10, -20],
#           [-19, -78, -70],
#           [-11, -12, -19]]
max_item = matrix[0][0]

for i in range(len(matrix)):
    for j in range(0, i + 1):
        item = matrix[i][j]
        if item > max_item:
            max_item = item

print(max_item)

