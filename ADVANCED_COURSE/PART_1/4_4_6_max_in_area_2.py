size = int(input())

matrix = []
row = []
for _ in range(size):
    row = input().split()
    int_row = [int(item) for item in row]
    matrix.append(int_row)

max_item = max([matrix[0][0]])

for i in range((len(matrix) + 1) // 2):
    for j in range(0, i + 1):

        current_max = max(matrix[i][j], matrix[-(i + 1)][j],
                          matrix[-(i + 1)][-(j + 1)], matrix[i][-(j + 1)])
        if current_max > max_item:
            max_item = current_max

print(max_item)

# matrix = [[6, 0],
#           [7, 9]]

# print(area_list)

# Выше главной диагонали: i < j,
# Главная диагональ: i = j
# Ниже главной диагонали: i > j

# Выше побочной диагонали: i + j + 1 < n
# Побочная диагональ: i + j + 1 = n
# Ниже побочной диагонали: i + j + 1 > n

# i > j and i + j + 1 < n
# i < j and i + j + 1 > n
# matrix = [[6, 0, 4, 90],
#           [7, 9, 34, 98],
#           [6, 0, 74, 92],
#           [6, 0, 72, 92]]