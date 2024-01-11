COLOURS = ['.', '*']
row_amount, column_amount = [int(el) for el in input().split()]

matrix = []

for i in range(row_amount):
    row = []
    for j in range(column_amount):
        row.append(COLOURS[(j + i) % 2])

    matrix.append(row)

for row in matrix:
    print(*row)

