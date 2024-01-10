BLANK_CELL_FILLING_CHAR = '.'
COLOURED_CELL_FILLING_CHAR = '*'

row_amount, column_amount = [int(el) for el in input().split()]

matrix = []

for i in range(row_amount):
    row = []
    for j in range(column_amount):
        if i % 2 == 0:
            if j % 2 == 0:
                row.append(BLANK_CELL_FILLING_CHAR)
            else:
                row.append(COLOURED_CELL_FILLING_CHAR)
        else:
            if j % 2 > 0:
                row.append(BLANK_CELL_FILLING_CHAR)
            else:
                row.append(COLOURED_CELL_FILLING_CHAR)

    matrix.append(row)

for row in matrix:
    print(*row)