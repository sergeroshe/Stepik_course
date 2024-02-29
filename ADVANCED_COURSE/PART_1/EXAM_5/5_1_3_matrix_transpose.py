MTRX_COL_WIDTH = 2


def mtrx_fill(rows):
    mtrx = []
    for _ in range(rows):
        row = [int(el) for el in input().split()]
        mtrx.append(row)
    return mtrx


def mtrx_row_col_interchange(mtrx):
    row_amount = len(mtrx)
    col_amount = len(mtrx[0])
    for i in range(row_amount):
        for j in range(i + 1, col_amount):
            mtrx[i][j], mtrx[j][i] = mtrx[j][i], mtrx[i][j]


def mtrx_print(mtrx, col_width):
    for row in mtrx:
        for el in row:
            print(str(el).ljust(col_width), end=' ')
        print()


def main():
    matrix_size = int(input())
    matrix = mtrx_fill(matrix_size)
    # matrix = [[1, 2, 3],
    #           [4, 5, 6],
    #           [7, 8, 9]]

    mtrx_row_col_interchange(matrix)

    mtrx_print(matrix, MTRX_COL_WIDTH)


main()
