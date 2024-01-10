BLANK_CELL_FILLING_CHAR = '.'
COLOURED_CELL_FILLING_CHAR = '*'

rows_amount_column_amount = input().split()
rows_amount = int(rows_amount_column_amount[0])
column_amount = int(rows_amount_column_amount[1])

matrix = []

for i in range(rows_amount):
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