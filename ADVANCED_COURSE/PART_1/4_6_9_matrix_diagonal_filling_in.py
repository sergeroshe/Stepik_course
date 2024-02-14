MTRX_COL_WIDTH = 5


def mtrx_left_upper_corner(mtrx, num):
    rows = len(mtrx)
    cols = len(mtrx[0])
    for i in range(cols - 1):
        hor_move_range = i + 1 if i + 1 <= rows else rows
        for j in range(hor_move_range):
            mtrx[j][i - j] = num
            num += 1
    return num


def mtrx_right_lower_corner(mtrx_left_side, num):
    rows = len(mtrx_left_side)
    cols = len(mtrx_left_side[0])
    for i in range(rows):
        shift = i + cols if rows - i >= cols else rows
        for j in range(i, shift):
            mtrx_left_side[j][-1 - (j - i)] = num
            num += 1


def mtrx_print(mtrx, col_width):
    for row in mtrx:
        for el in row:
            print(str(el).ljust(col_width), end=' ')
        print()


def main():
    rows, cols = [int(el) for el in input().split()]
    matrix_base = [[0] * cols for _ in range(rows)]

    num = 1
    mtrx_left_upper_corner(matrix_base, num)
    num = mtrx_left_upper_corner(matrix_base, num)
    mtrx_right_lower_corner(matrix_base, num)
    mtrx_print(matrix_base, MTRX_COL_WIDTH)


main()

