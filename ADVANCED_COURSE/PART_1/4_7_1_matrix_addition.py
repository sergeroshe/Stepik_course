MTRX_COL_WIDTH = 5


def mtrx_fill(row_amount):
    mtrx = []
    for _ in range(row_amount):
        row = [int(el) for el in input().split()]
        mtrx.append(row)
    return mtrx


def mtrx_add(left_mtrx, right_mtrx):
    row_amount = len(left_mtrx)
    col_amount = len(left_mtrx[0])
    result_mtrx = []
    for i in range(row_amount):
        row = [(left_mtrx[i][j] + right_mtrx[i][j]) for j in range(col_amount)]
        result_mtrx.append(row)
    return result_mtrx


def mtrx_print(mtrx, col_width):
    for row in mtrx:
        for el in row:
            print(str(el).ljust(col_width), end=' ')
        print()


def main():
    row_amount, col_amount = [int(el) for el in input().split()]
    left_mtrx = mtrx_fill(row_amount)
    input()
    right_mtrx = mtrx_fill(row_amount)

    result_mtrx = mtrx_add(left_mtrx, right_mtrx)

    mtrx_print(result_mtrx, MTRX_COL_WIDTH)


main()
