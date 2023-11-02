row_amount = int(input())
column_amount = int(input())

result = ''
matrix = []
max_item_row = 0
max_item_column = 0
max_item = 0

for _ in range(row_amount):
    row = input()
    row = [int(x) for x in row.split()]
    matrix.append(row)

max_item = max(max(matrix, key=max))
max_found = False
i = 0
while not max_found and i <= row_amount - 1:
    j = 0
    while not max_found and j <= column_amount - 1:
        cur_item = matrix[i][j]
        if cur_item == max_item:
            result = f'{i} {j}'
            max_found = True
        j += 1

    i += 1

print(result)
# matrix = [[0, 3, 2, 4], [2, 3, 5, 5], [5, 1, 2, 3]]
# string_amount = 3
# column_amount = 4
# print(*matrix, sep='\n')
# print(max_item)
