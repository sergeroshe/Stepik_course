MTRX_FILLING_CHAR = '.'
SNOWFLAKE_FILLING_CHAR = '*'
MTRX_COL_WIDTH = 5


def mtrx_fill(mtrx_size, filling_char):
    mtrx = []
    for i in range(mtrx_size):
        row = []
        for j in range(mtrx_size):
            row.append(filling_char)
        mtrx.append(row)
    return mtrx


def mtrx_cross(mtrx, filling_char):
    mtrx_size = len(mtrx)
    for i in range(mtrx_size):
        mtrx_mid = mtrx_size // 2
        mtrx[mtrx_mid][i] = filling_char
        mtrx[i][mtrx_mid] = filling_char


def mtrx_diags(mtrx, filling_char):
    mtrx_size = len(mtrx)
    for i in range(mtrx_size):
        mtrx[i][i] = filling_char
        mtrx[-(i + 1)][i] = filling_char


def mtrx_print(mtrx, col_width):
    for row in mtrx:
        for el in row:
            print(str(el).ljust(col_width), end='')
        print()


def main():
    mtrx_size = int(input())
    # mtrx_size = 5
    mtrx = mtrx_fill(mtrx_size, MTRX_FILLING_CHAR)

    mtrx_cross(mtrx, SNOWFLAKE_FILLING_CHAR)
    mtrx_diags(mtrx, SNOWFLAKE_FILLING_CHAR)

    mtrx_print(mtrx, MTRX_COL_WIDTH)


main()
