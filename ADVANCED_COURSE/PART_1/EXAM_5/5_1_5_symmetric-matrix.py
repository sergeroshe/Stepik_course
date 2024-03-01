POSITIVE_ANSWER = 'YES'
NEGATIVE_ANSWER = 'NO'


def mtrx_fill(rows):
    mtrx = []
    for _ in range(rows):
        row = [int(el) for el in input().split()]
        mtrx.append(row)
    return mtrx


def is_mtrx_symmetric(mtrx):
    is_symmetric = True
    row_amount = len(mtrx)
    i = 0
    while is_symmetric and i < row_amount // 2:
        j = 0
        col_amount = len(mtrx[i])
        while is_symmetric and j < col_amount - i:
            left_upper_el = mtrx[i][j]
            right_lower_el = mtrx[-(j + 1)][-(i + 1)]
            is_symmetric = left_upper_el == right_lower_el
            j += 1
        i += 1

    return is_symmetric


def main():
    answer = POSITIVE_ANSWER
    # mtrx_size = 3
    # mtrx_size = int(input())
    # mtrx = mtrx_fill(mtrx_size)
    mtrx = [[0, 1, 2],
            [1, 2, 7],
            [2, 3, 4]]

    if not is_mtrx_symmetric(mtrx):
        answer = NEGATIVE_ANSWER

    print(answer)


main()

