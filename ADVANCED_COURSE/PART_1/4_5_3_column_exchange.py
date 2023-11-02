row_amount = int(input())
column_amount = int(input())

matrix = [input().split() for i in range(row_amount)]
column_x_idx, column_y_idx = map(int, input().split())

for _, row in enumerate(matrix):
    row[column_x_idx], row[column_y_idx] = row[column_y_idx], row[column_x_idx]


for row in matrix:
    print(*row)
