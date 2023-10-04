size = int(input())

matrix = []
row = []
for _ in range(size):
    row = input().split()
    int_row = [int(item) for item in row]
    matrix.append(int_row)

# print(matrix)
#
# matrix = [[6, 0],
#           [7, 9]]

max_item = max([matrix[0][0]])

area_list = []

for i in range((len(matrix) + 1) // 2):
    for j in range(0, i + 1):
        area_list.append(matrix[i][j])
        area_list.append(matrix[-(i + 1)][j])
        area_list.append(matrix[-(i + 1)][-(j + 1)])
        area_list.append(matrix[i][-(j + 1)])
        current_max = max(area_list)
        if current_max > max_item:
            max_item = current_max

print(max_item)

# print(max(area_list))
# print(area_list)

