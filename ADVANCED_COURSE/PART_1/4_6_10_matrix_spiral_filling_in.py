MTRX_COL_WIDTH = 5


def left_right_filling(mtrx, num, left, right, top):
    for i in range(left, right + 1):
        mtrx[top][i] = num
        num += 1
    top += 1
    return num, top


def top_bottom_filling(mtrx, num, top, bottom, right):
    for i in range(top, bottom + 1):
        mtrx[i][right] = num
        num += 1
    right -= 1
    return num, right


def right_left_filling(mtrx, num, right, left, bottom):
    for i in range(right, left - 1, -1):
        mtrx[bottom][i] = num
        num += 1
    bottom -= 1
    return num, bottom


def bottom_top_filling(mtrx, num, bottom, top, left):
    for i in range(bottom, top - 1, -1):
        mtrx[i][left] = num
        num += 1
    left += 1
    return num, left


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
        num, top = left_right_filling(matrix, num, left, right, top)
        num, right = top_bottom_filling(matrix, num, top, bottom, right)
        if top <= bottom:
            num, bottom = right_left_filling(matrix, num, right, left, bottom)
        if left <= right:
            num, left = bottom_top_filling(matrix, num, bottom, top, left)

    mtrx_print(matrix, MTRX_COL_WIDTH)


main()
