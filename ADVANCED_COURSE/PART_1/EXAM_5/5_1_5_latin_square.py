Y_ANSWER = 'YES'
N_ANSWER = 'NO'
MATRIX_MIN_ELEMENT = 1


def mtrx_fill(rows):
    mtrx = []
    for _ in range(rows):
        row = [int(el) for el in input().split()]
        mtrx.append(row)
    return mtrx


def is_sequence_valid(seq, expected_min):
    checked_num_list = []
    mtrx_size = len(seq)
    expected_max = mtrx_size

    i = 0

    is_valid = True
    while i < mtrx_size and is_valid:
        num = seq[i]
        if expected_min <= num <= expected_max:
            if num not in checked_num_list:
                checked_num_list.append(num)
            else:
                is_valid = False
        else:
            is_valid = False
        i += 1

    return is_valid


def is_latin_square(mtrx):
    row_valid = True
    col_valid = True
    i = 0
    mtrx_size = len(mtrx)
    while i < mtrx_size and row_valid and col_valid:
        row_valid = is_sequence_valid(mtrx[i], 1)
        len_row = len(mtrx[i])
        j = 0
        while j < len_row and col_valid:
            cur_col_el = mtrx[j][i]
            if j > 0:
                prev_col_el = mtrx[j - 1][i]
                col_valid = 1 <= cur_col_el <= mtrx_size and cur_col_el != prev_col_el
            j += 1

        i += 1
    mtrx_valid = row_valid and col_valid
    return mtrx_valid
    # remove extra iteration, ged rid of column list


def main():
    matrix_size = int(input())
    mtrx = mtrx_fill(matrix_size)
    matrix_size = 4
    #
    # mtrx = [[2, 3, 4, 1],
    #         [3, 4, 1, 2],
    #         [4, 1, 2, 3],
    #         [1, 2, 3, 4]]

    answer = Y_ANSWER

    if not is_latin_square(mtrx):
        answer = N_ANSWER

    print(answer)


main()
