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
            row_el = 0
            for j in range(left_mtrx_col_amount):
                left_mtrx_row_el = left_mtrx[k][j]
                right_mtrx_col_el = right_mtrx[j][i]
                row_el += left_mtrx_row_el * right_mtrx_col_el
            row.append(row_el)
        mtrx_mult_.append(row)
    return mtrx_mult_


def mtrx_power(mtrx, matrix_power):
    powered_matrix = mtrx
    for _ in range(matrix_power - 1):
        powered_matrix = mtrx_mult(powered_matrix, mtrx)

    return powered_matrix


def mtrx_print(mtrx, col_width):
    for row in mtrx:
        for el in row:
            print(str(el).ljust(col_width), end=' ')
        print()


def main():
    matrix_size = int(input())
    matrix = mtrx_fill(matrix_size)
    matrix_power = int(input())

    result_mtrx = mtrx_power(matrix, matrix_power)

    mtrx_print(result_mtrx, MTRX_COL_WIDTH)


main()

# matrix = [[1, 2, 1],
#           [3, 3, 3],
#           [1, 2, 1]]

# matrix = [[1, 2, 1],
#           [3, 3, 3],
#           [1, 2, 1]]

# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
