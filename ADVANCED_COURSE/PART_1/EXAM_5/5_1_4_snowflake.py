MTRX_FILLING_CHAR = '.'
SNOWFLAKE_FILLING_CHAR = '*'


def mtrx_fill(mtrx_size, filling_char):
    mtrx = []
    for i in range(mtrx_size):
        row = []
        for j in range(mtrx_size):
            row.append(filling_char)
        mtrx.append(row)
    return mtrx


def mtrx_middle_hor_line(mtrx, filling_char):
    mtrx_size = len(mtrx)
    for i in range(mtrx_size):
        mtrx_mid = mtrx_size // 2
        mtrx[mtrx_mid][i] = filling_char


def mtrx_middle_vert_line(mtrx, filling_char):
    mtrx_size = len(mtrx)
    for i in range(mtrx_size):
        mtrx_mid = mtrx_size // 2
        mtrx[i][mtrx_mid] = filling_char


def mtrx_main_diag(mtrx, filling_char):
    mtrx_size = len(mtrx)
    for i in range(mtrx_size):
        mtrx[i][i] = filling_char


def mtrx_sec_diag(mtrx, filling_char):
    mtrx_size = len(mtrx)
    for i in range(mtrx_size):
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

    mtrx_middle_hor_line(mtrx, SNOWFLAKE_FILLING_CHAR)
    mtrx_middle_vert_line(mtrx, SNOWFLAKE_FILLING_CHAR)
    mtrx_main_diag(mtrx, SNOWFLAKE_FILLING_CHAR)
    mtrx_sec_diag(mtrx, SNOWFLAKE_FILLING_CHAR)

    mtrx_print(mtrx, 3)


main()
