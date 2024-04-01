MTRX_COL_WIDTH = 5


def mtrx_fill(mtrx_size, filling_char):
    mtrx = [list(filling_char * mtrx_size) for _ in range(mtrx_size)]
    return mtrx


def mtrx_diagonals_parallel_to_main(mtrx):
    mtrx_size = len(mtrx)
    for i in range(mtrx_size):
        for j in range(mtrx_size):
            mtrx[i][i] = 0
            mtrx[i][j] = j - i
            mtrx[i][j % (i + 1)] = i - (j % (i + 1))


def mtrx_print(mtrx, col_width):
    for row in mtrx:
        for el in row:
            print(str(el).ljust(col_width), end='')
        print()


def main():
    matrix_size = int(input())
    # matrix_size = 1
    matrix = mtrx_fill(matrix_size, '*')
    mtrx_diagonals_parallel_to_main(matrix)
    mtrx_print(matrix, MTRX_COL_WIDTH)


main()
