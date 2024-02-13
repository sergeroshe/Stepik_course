def mtrx_left_upper_corner(mtrx, num):
    rows = len(mtrx)
    cols = len(mtrx[0])
    for i in range(cols - 1):
        hor_move_range = i + 1 if i + 1 <= rows else rows
        for j in range(hor_move_range):
            vert_move = j
            left_shift = i - j
            mtrx[vert_move][left_shift] = num
            num += 1
    result_mtrx = mtrx
    return result_mtrx, num


def mtrx_right_lower_corner(mtrx_left_side, num):
    rows = len(mtrx_left_side)
    cols = len(mtrx_left_side[0])
    for i in range(rows):
        shift = i + cols if rows - i >= cols else rows

        for j in range(i, shift):
            # simplify calc
            # rename y
            # simply range up to y
            vert_move = j
            right_border = - 1
            left_shift = j - i
            mtrx_left_side[vert_move][right_border - left_shift] = num
            num += 1
    result_mtrx = mtrx_left_side
    return result_mtrx


def mtrx_print(mtrx):
    for row in mtrx:
        for el in row:
            print(str(el).ljust(3), end=' ')
        print()


def main():
    # rows, cols = [int(el) for el in input().split()]
    rows = 8
    cols = 3

    matrix_base = [[0] * cols for _ in range(rows)]

    num = 1
    matrix_left_side, num = mtrx_left_upper_corner(matrix_base, num)
    matrix_right_side = mtrx_right_lower_corner(matrix_left_side, num)

    mtrx_print(matrix_right_side)


main()

# 1  2  (# 1: i = 0, j = 0;)  # 2:  i = 0, j = 1
# 3  4  # 3: i = 1, j = 0;  # 4:  i = 1, j = 1
# 5  6  # 5: i = 2, j = 0;  # 6:  i = 2, j = 1
# 7  8  # 7: i = 3, j = 0;  # 8:  i = 3, j = 1
# 9  10 # 9: i = 4, j = 0;  # 10: i = 4, j = 1


# 3 4
# 1  2  4  7
# 3  5  8  10
# 6  9  11 12

# 3 4
# 1   2   4
# 3   5   7
# 6   8   10
# 9   11  12

# 1  2  4  7  10
# 3  5  8  11 13
# 6  9  12 14 15

# i = 0, 1
# i = 1, 2
# i = 2, 3
# i = 3, 3
# i = 4, 3

# 1[0, 0] 0, 1

# 2[0, 1]
# 3[1, 0]

# 4[0, 2]
# 5[1, 1] i = 1
# 6[2, 0] i = 2

# 7[0, 3]
# 8[1, 2]
# 9[2, 1]

# 10[1, 3]
# 11[2, 2]

# 12[2, 3]


# 3 4
# 1  2  4  7
# 3  5  8  10
# 6  9  11 12
