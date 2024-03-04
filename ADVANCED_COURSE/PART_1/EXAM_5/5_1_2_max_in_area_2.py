def mtrx_fill(rows):
    mtrx = []
    for _ in range(rows):
        row = [int(el) for el in input().split()]
        mtrx.append(row)
    return mtrx


def mtrx_right_lower_corner_max(mtrx):
    max_num = mtrx[0][-1]
    row_amount = len(mtrx)
    for i in range(1, row_amount):
        for j in range(-(i + 1), 0):
            num = mtrx[i][j]
            if num > max_num:
                max_num = num

    return max_num


def main():
    mtrx_size = int(input())
    # mtrx_size = 4
    mtrx = mtrx_fill(mtrx_size)
    # mtrx = [[1, 9, 5, 1, 4, 7],
    #         [6, 9, 8, 6, 7, 4],
    #         [1, 1, 6, 1, 1, 1],
    #         [1, 4, 5, 8, 7, 5],
    #         [6, 7, 8, 1, 1, 0],
    #         [6, 1, 8, 6, 7, 7]]

    max_num = mtrx_right_lower_corner_max(mtrx)

    print(max_num)


main()
