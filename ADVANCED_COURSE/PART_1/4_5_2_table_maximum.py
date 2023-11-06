row_amount = int(input())
column_amount = int(input())
# column_amount = 3
# row_amount = 3

matrix = []

for _ in range(row_amount):
    row = input()
    row = [int(x) for x in row.split()]
    matrix.append(row)

# matrix = ['5 3 4'.split(),
#           '2 3 0'.split(),
#           '4 1 5'.split()]

max_item = matrix[0][0]
result = [0, 0]

i = 0
while i <= row_amount - 1:
    j = 0
    while j <= column_amount - 1:
        if int(matrix[i][j]) > int(max_item):
            max_item = matrix[i][j]
            result = [i, j]
        j += 1

    i += 1

print(*result)
