MTRX_COL_WIDTH = 5


#
def left_corner_bottom_filling(mtrx, num, start_hor_idx, stop_hor_idx, start_vert_idx, stop_vert_idx):
    # left to right movement
    range_list = [[start_hor_idx, stop_hor_idx],
                  [start_vert_idx, stop_vert_idx]]
    for i in range(range_list[0][0], range_list[0][1] + 1):
        mtrx[range_list[1][0]][i] = num
        num += 1
    # start_vert_idx += 1
    range_list[1][0] += 1
    # print(range_list[1][0])
    # top to bottom movement
    for i in range(range_list[1][0], range_list[1][1] + 1):
        mtrx[i][range_list[0][1]] = num
        num += 1
    # stop_hor_idx -= 1
    range_list[0][1] -= 1
    # print(range_list[0][1])

    return num, range_list[1][0], range_list[0][1]


# def left_corner_bottom_filling(mtrx, num, start_hor_idx, stop_hor_idx, start_vert_idx, stop_vert_idx):
#     # left to right movement
#     for i in range(start_hor_idx, stop_hor_idx + 1):
#         mtrx[start_vert_idx][i] = num
#         num += 1
#     start_vert_idx += 1
#     # top to bottom movement
#     for i in range(start_vert_idx, stop_vert_idx + 1):
#         mtrx[i][stop_hor_idx] = num
#         num += 1
#     stop_hor_idx -= 1
#     return num, start_vert_idx, stop_hor_idx


def right_corner_top_filling(mtrx, num, start_hor_idx, stop_hor_idx, start_vert_idx, stop_vert_idx):
    # right to left movement
    for i in range(start_hor_idx, stop_hor_idx - 1, -1):
        mtrx[start_vert_idx][i] = num
        num += 1
    start_vert_idx -= 1
    # bottom to top movement
    for i in range(start_vert_idx, stop_vert_idx - 1, -1):
        mtrx[i][stop_hor_idx] = num
        num += 1
    stop_hor_idx += 1
    return num, start_vert_idx, stop_hor_idx


def mtrx_print(mtrx, col_width):
    for row in mtrx:
        for el in row:
            print(str(el).ljust(col_width), end=' ')
        print()


def main():
    # rows = 5
    # cols = 7
    rows, cols = [int(el) for el in input().split()]

    matrix = [[0] * cols for _ in range(rows)]

    num = 1
    top = 0
    bottom = rows - 1
    left = 0
    right = cols - 1
    while top <= bottom and left <= right:
        num, top, right = left_corner_bottom_filling(matrix, num, left, right, top, bottom)

        if top <= bottom and left <= right:
            num, bottom, left = right_corner_top_filling(matrix, num, right, left, bottom, top)

    mtrx_print(matrix, MTRX_COL_WIDTH)


main()
