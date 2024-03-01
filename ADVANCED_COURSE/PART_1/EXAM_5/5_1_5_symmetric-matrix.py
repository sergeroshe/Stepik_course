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
    col_amount = len(mtrx[0])
    i = 0
    while is_symmetric and i < row_amount - 1:
        j = 0
        while is_symmetric and j < col_amount - i - 1:
            left_upper_el = mtrx[i][j]
            right_lower_el = mtrx[-(j + 1)][-(i + 1)]
            is_symmetric = left_upper_el == right_lower_el
            j += 1
        i += 1

    return is_symmetric


def main():
    answer = POSITIVE_ANSWER
    # mtrx_size = 3
    mtrx_size = int(input())
    mtrx = mtrx_fill(mtrx_size)
    # mtrx = [[1, 3, 4, 7, 5],  # 3: 0,1 -> 3: ;-2,-1 4: 0,2 -> -3, -1
    #         [3, 5, 8, 5, 7],  #
    #         [7, 4, 4, 8, 4],
    #         [6, 5, 4, 5, 3],
    #         [5, 1, 7, 3, 1]]

    # 1 3 4 7 5
    # 3 5 8 5 7
    # 7 4 4 8 4
    # 6 5 4 5 3
    # 5 1 7 3 1

    if not is_mtrx_symmetric(mtrx):
        answer = NEGATIVE_ANSWER

    print(answer)


main()
