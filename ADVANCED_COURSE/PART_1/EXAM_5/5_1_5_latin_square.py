Y_ANSWER = 'YES'
N_ANSWER = 'NO'
MATRIX_MIN_ELEMENT = 1
ROW_TYPE = 0
COL_TYPE = 1


def mtrx_fill(rows):
    mtrx = []
    for _ in range(rows):
        row = [int(el) for el in input().split()]
        mtrx.append(row)
    return mtrx


def is_sequence_valid(mtrx, seq_num, seq_type, expected_min=1):
    checked_num_list = []
    seq_valid = True
    mtrx_size = len(mtrx)

    i = 0
    while i < mtrx_size and seq_valid:
        num = mtrx[seq_num][i] if seq_type == COL_TYPE else mtrx[i][seq_num]
        if expected_min <= num <= mtrx_size:
            if num not in checked_num_list:
                checked_num_list.append(num)
            else:
                seq_valid = False
        else:
            seq_valid = False
        i += 1

    return seq_valid


def is_latin_square(mtrx):
    row_valid = True
    col_valid = True
    i = 0
    mtrx_size = len(mtrx)

    while i < mtrx_size and row_valid and col_valid:
        row_valid = is_sequence_valid(mtrx, i, ROW_TYPE)
        col_valid = is_sequence_valid(mtrx, i, COL_TYPE)
        i += 1
    mtrx_valid = row_valid and col_valid
    return mtrx_valid


def main():
    # matrix_size = int(input())
    matrix_size = 4
    # mtrx = mtrx_fill(matrix_size)
    mtrx = [[2, 3, 4, 1],
            [3, 4, 1, 2],
            [4, 1, 2, 3],
            [1, 2, 3, 4]]
    # 2 3 4 1
    # 3 4 1 2
    # 4 1 2 3
    # 1 2 3 4

    answer = Y_ANSWER

    if not is_latin_square(mtrx):
        answer = N_ANSWER

    print(answer)


main()
