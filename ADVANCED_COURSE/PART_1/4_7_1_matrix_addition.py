def mtrx_fill(rows):
    mtrx = []
    for _ in range(rows):
        row = [int(el) for el in input().split()]
        mtrx.append(row)
    return mtrx


def mtrx_add(left_mtrx, right_mtrx):
    rows = len(left_mtrx)
    cols = len(left_mtrx[0])
    result_mtrx = []
    for i in range(rows):
        row = [(left_mtrx[i][j] + right_mtrx[i][j]) for j in range(cols)]
        result_mtrx.append(row)
    return result_mtrx


def main():
    rows, columns = [int(el) for el in input().split()]
    left_mtrx = mtrx_fill(rows)
    input()
    right_mtrx = mtrx_fill(rows)
    matrix_sum = mtrx_add(left_mtrx, right_mtrx)
    for i in range(rows):
        for j in range(columns):
            print(str(matrix_sum[i][j]).ljust(3), end=' ')
        print()


main()
