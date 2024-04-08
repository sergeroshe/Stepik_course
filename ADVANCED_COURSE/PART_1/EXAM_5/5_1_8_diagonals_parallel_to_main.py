MTRX_COL_WIDTH = 5


def mtrx_fill(mtrx_size, filling_char):
    mtrx = [list(filling_char * mtrx_size) for _ in range(mtrx_size)]
    return mtrx


def diagonal_move(y, x, mtrx, filling_char):
    mtrx_size = len(mtrx)
    shift = 1
    y_move = y
    x_move = x
    while 0 <= y_move <= mtrx_size - 1 \
            and 0 <= x_move <= mtrx_size - 1:
        mtrx[y_move][x_move] = filling_char
        y_move += shift
        x_move += shift


def mtrx_print(mtrx, col_width):
    for row in mtrx:
        for el in row:
            print(str(el).ljust(col_width), end='')
        print()


def main():
    matrix_size = int(input())
    # matrix_size = 7
    matrix = mtrx_fill(matrix_size, '*')

    for i in range(matrix_size):
        start = i
        diagonal_move(start, 0, matrix, start)
        diagonal_move(0, start, matrix, start)

    mtrx_print(matrix, MTRX_COL_WIDTH)


main()
