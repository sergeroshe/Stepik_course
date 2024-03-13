MTRX_COL_WIDTH = 5


def mtrx_fill(mtrx_size, filling_char):
    mtrx = [list(filling_char * mtrx_size) for _ in range(mtrx_size)]
    return mtrx


def mtrx_print(mtrx, col_width):
    for row in mtrx:
        for el in row:
            print(str(el).ljust(col_width), end='')
        print()


def main():
    # matrix_size = int(input())
    matrix_size = 6
    matrix = mtrx_fill(matrix_size, '0')
    mtrx_print(matrix, MTRX_COL_WIDTH)


main()
