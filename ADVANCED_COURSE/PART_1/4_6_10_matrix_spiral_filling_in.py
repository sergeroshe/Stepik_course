MTRX_COL_WIDTH = 5
MOVE_FRONT = 1
MOVE_BACK = -1
STAY = 0


def mtrx_spiral_filling(mtrx):
    row_amount = len(mtrx)
    col_amount = len(mtrx[0])
    num = 1
    shift_list = [[0, 1, 1, -1],
                  [1, 0, -1, -1],
                  [0, -1, -1, 1],
                  [-1, 0, 1, 1]]
    y = 0
    x = 0
    while (0 <= x < col_amount and 0 <= y < row_amount) and mtrx[y][x] == 0:
        for shift in shift_list:
            while (0 <= x < col_amount and 0 <= y < row_amount) and mtrx[y][x] == 0:
                mtrx[y][x] = num
                y += shift[0]
                x += shift[1]
                num += 1
            y += shift[2]
            x += shift[3]


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

    mtrx_spiral_filling(matrix)
    mtrx_print(matrix, MTRX_COL_WIDTH)


main()
