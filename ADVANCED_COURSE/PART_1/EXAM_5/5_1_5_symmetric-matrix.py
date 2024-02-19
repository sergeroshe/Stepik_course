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
    i = 0
    while is_symmetric and i < len(mtrx):
        j = 0
        while is_symmetric and j < len(mtrx[i]):
            mtrx_left_upper = mtrx[i][j]
            mtrx_right_lower = mtrx[-(j + 1)][-(i + 1)]
            is_symmetric = mtrx_left_upper == mtrx_right_lower
            j += 1
        i += 1

    return is_symmetric


def main():
    answer = POSITIVE_ANSWER
    # mtrx_size = 3
    mtrx_size = int(input())
    mtrx = mtrx_fill(mtrx_size)
    # mtrx = [[0, 3, 10],
    #         [4, 9, 3],
    #         [7, 4, 0]]

    if not is_mtrx_symmetric(mtrx):
        answer = NEGATIVE_ANSWER

    print(answer)


main()

