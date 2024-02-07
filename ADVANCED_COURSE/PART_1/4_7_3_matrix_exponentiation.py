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


def mtrx_power(mtrx, matrix_power):
    powered_matrix = mtrx
    for _ in range(matrix_power - 1):
        powered_matrix = mtrx_mult(powered_matrix, mtrx)

    return powered_matrix


def main():
    matrix_size = int(input())
    matrix = mtrx_fill(matrix_size)
    matrix_power = int(input())

    powered_matrix = mtrx_power(matrix, matrix_power)

    for i in range(matrix_size):
        for j in range(matrix_size):
            print(str(powered_matrix[i][j]).ljust(3), end=' ')
        print()


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
