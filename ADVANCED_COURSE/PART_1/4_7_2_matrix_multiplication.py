MTRX_COL_WIDTH = 5


def mtrx_fill(rows):
    mtrx = []
    for _ in range(rows):
        row = [int(el) for el in input().split()]
        mtrx.append(row)
    return mtrx


def mtrx_mult(left_mtrx, right_mtrx):
    mtrx_mult_ = []
    left_mtrx_row_amount = len(left_mtrx)
    left_mtrx_col_amount = len(left_mtrx[0])
    right_mtrx_col_amount = len(right_mtrx[0])
    for k in range(left_mtrx_row_amount):
        row = []
        for i in range(right_mtrx_col_amount):
            mult_amount = 0
            for j in range(left_mtrx_col_amount):
                left_row_el = left_mtrx[k][j]
                right_col_el = right_mtrx[j][i]
                mult_amount += left_row_el * right_col_el
            row.append(mult_amount)
        mtrx_mult_.append(row)
    return mtrx_mult_


def mtrx_print(mtrx, col_width):
    for row in mtrx:
        for el in row:
            print(str(el).ljust(col_width), end=' ')
        print()


def main():
    left_mtrx_row_amount, left_mtrx_col_amount = [int(el) for el in input().split()]
    left_mtrx = mtrx_fill(left_mtrx_row_amount)
    input()
    right_mtrx_row_amount, right_mtrx_col_amount = [int(el) for el in input().split()]
    right_mtrx = mtrx_fill(right_mtrx_row_amount)

    result_mtrx = mtrx_mult(left_mtrx, right_mtrx)

    mtrx_print(result_mtrx, MTRX_COL_WIDTH)


main()

# matrix_1_rows, matrix_1_cols = 3, 2
# matrix_1 = [[2, 5],
#             [6, 7],
#             [1, 8]]
#
# matrix_2_rows, matrix_2_cols = 2, 3
# matrix_2 = [[1, 2, 1],
#             [0, 1, 0]]
