MTRX_COL_WIDTH = 5


def mtrx_fill(mtrx_size, filling_char):
    mtrx = [list(filling_char * mtrx_size) for _ in range(mtrx_size)]
    return mtrx


# extract shift for x and y to arguments
def mtrx_line_fill(x, y, x_shift, y_shift, mtrx, filling_char):
    mtrx_size = len(mtrx)
    shift_list = [x_shift, y_shift]
    x_move = x
    y_move = y
    while 0 <= y_move <= mtrx_size - 1 \
            and 0 <= x_move <= mtrx_size - 1:
        mtrx[y_move][x_move] = filling_char
        x_move += shift_list[0]
        y_move += shift_list[1]


def mtrx_print(mtrx, col_width):
    for row in mtrx:
        for el in row:
            print(str(el).ljust(col_width), end='')
        print()


def main():
    # matrix_size = int(input())
    matrix_size = 7
    matrix = mtrx_fill(matrix_size, '*')

    for i in range(matrix_size):
        mtrx_line_fill(0, i, 1, 1, matrix, i)
        mtrx_line_fill(i, 0, 1, 1, matrix, i)

    mtrx_print(matrix, MTRX_COL_WIDTH)


main()
