matrix_1_rows, matrix_1_cols = [int(el) for el in input().split()]
matrix_1 = []
for _ in range(matrix_1_rows):
    row = [int(el) for el in input().split()]
    matrix_1.append(row)
empty_line = input()

matrix_2_rows, matrix_2_cols = [int(el) for el in input().split()]
matrix_2 = []
for _ in range(matrix_2_rows):
    row = [int(el) for el in input().split()]
    matrix_2.append(row)

matrix_mult = []

for k in range(matrix_1_rows):
    row = []
    for i in range(matrix_2_cols):
        mult_amount = 0
        for j in range(matrix_1_cols):
            matrix_1_row_el = matrix_1[k][j]
            matrix_2_col_el = matrix_2[j][i]
            mult_amount += matrix_1_row_el * matrix_2_col_el
        row.append(mult_amount)
    matrix_mult.append(row)


for i in range(matrix_1_rows):
    for j in range(matrix_2_cols):
        print(str(matrix_mult[i][j]).ljust(3), end=' ')
    print()

# matrix_1_rows, matrix_1_cols = 3, 2
# matrix_1 = [[2, 5],
#             [6, 7],
#             [1, 8]]
#
# matrix_2_rows, matrix_2_cols = 2, 3
# matrix_2 = [[1, 2, 1],
#             [0, 1, 0]]

