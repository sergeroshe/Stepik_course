def mtrx_fill(rows):
    mtrx = []
    for _ in range(rows):
        row = [int(el) for el in input().split()]
        mtrx.append(row)
    return mtrx


def mtrx_mult(left_mtrx, right_mtrx):
    mtrx_mult_ = []
    left_mtrx_rows = len(left_mtrx)
    left_mtrx_cols = len(left_mtrx[0])
    right_mtrx_cols = len(right_mtrx[0])
    for k in range(left_mtrx_rows):
        row = []
        for i in range(right_mtrx_cols):
            mult_amount = 0
            for j in range(left_mtrx_cols):
                matrix_1_row_el = left_mtrx[k][j]
                matrix_2_col_el = right_mtrx[j][i]
                mult_amount += matrix_1_row_el * matrix_2_col_el
            row.append(mult_amount)
        mtrx_mult_.append(row)
    return mtrx_mult_


def main():
    left_mtrx_rows, left_mtrx_cols = [int(el) for el in input().split()]

    left_mtrx = mtrx_fill(left_mtrx_rows)
    input()
    right_mtrx_rows, right_mtrx_cols = [int(el) for el in input().split()]
    right_mtrx = mtrx_fill(right_mtrx_rows)
    matrix_mult = mtrx_mult(left_mtrx, right_mtrx)

    for i in range(left_mtrx_rows):
        for j in range(right_mtrx_cols):
            print(str(matrix_mult[i][j]).ljust(3), end=' ')
        print()


main()

# matrix_1_rows, matrix_1_cols = 3, 2
# matrix_1 = [[2, 5],
#             [6, 7],
#             [1, 8]]
#
# matrix_2_rows, matrix_2_cols = 2, 3
# matrix_2 = [[1, 2, 1],
#             [0, 1, 0]]
