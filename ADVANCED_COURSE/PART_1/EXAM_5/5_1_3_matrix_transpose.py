def mtrx_fill(rows):
    mtrx = []
    for _ in range(rows):
        row = [int(el) for el in input().split()]
        mtrx.append(row)
    return mtrx


def mtrx_row_col_interchange(mtrx):
    rows = len(mtrx)
    cols = len(mtrx[0])
    result_mtrx = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(mtrx[j][i])
        result_mtrx.append(row)

    return result_mtrx


def mtrx_print(mtrx, col_width):
    for row in mtrx:
        for el in row:
            print(str(el).ljust(col_width), end=' ')
        print()


def main():
    mtrx_size = int(input())
    mtrx = mtrx_fill(mtrx_size)

    result_mtrx = mtrx_row_col_interchange(mtrx)

    mtrx_print(result_mtrx, 3)


main()
