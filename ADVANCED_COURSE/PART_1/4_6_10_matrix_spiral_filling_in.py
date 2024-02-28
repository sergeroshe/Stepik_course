MTRX_COL_WIDTH = 5


def left_right_top_bottom_filling(mtrx, num, left, right, top, bottom):
    for i in range(left, right + 1):
        mtrx[top][i] = num
        num += 1
    top += 1
    for i in range(top, bottom + 1):
        mtrx[i][right] = num
        num += 1
    right -= 1
    return num, top, right


def right_left_bottom_top_filling(mtrx, num, left, right, top, bottom):
    for i in range(right, left - 1, -1):
        mtrx[bottom][i] = num
        num += 1
    bottom -= 1

    for i in range(bottom, top - 1, -1):
        mtrx[i][left] = num
        num += 1
    left += 1
    return num, bottom, left


def mtrx_print(mtrx, col_width):
    for row in mtrx:
        for el in row:
            print(str(el).ljust(col_width), end=' ')
        print()


def main():
    rows = 5
    cols = 7
    # rows, cols = [int(el) for el in input().split()]

    matrix = [[0] * cols for _ in range(rows)]

    num = 1
    top = 0
    bottom = rows - 1
    left = 0
    right = cols - 1
    while top <= bottom and left <= right:
        num, top, right = left_right_top_bottom_filling(matrix, num, left, right, top, bottom)

        if top <= bottom and left <= right:
            num, bottom, left = right_left_bottom_top_filling(matrix, num, left, right, top, bottom)

    mtrx_print(matrix, MTRX_COL_WIDTH)


main()
