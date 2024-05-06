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
    move_x, move_y, shift = (seq_num, 0, [1, 0]) if seq_type == ROW_TYPE else (0, seq_num, [0, 1])

    while move_x < mtrx_size and move_y < mtrx_size and seq_valid:
        num = mtrx[move_y][move_x]
        if expected_min <= num <= mtrx_size:
            if num not in checked_num_list:
                checked_num_list.append(num)
            else:
                seq_valid = False
        else:
            seq_valid = False
        move_x += shift[1]
        move_y += shift[0]

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
    matrix_size = int(input())
    # matrix_size = 3
    mtrx = mtrx_fill(matrix_size)
    # mtrx = [[2, 3, 4, 1],   # 0, 1
    #         [3, 4, 1, 2],   # 1, 1
    #         [4, 1, 2, 3],   # 2, 1
    #         [1, 2, 3, 4]]
    # mtrx = [[1, 2, 3],
    #         [3, 2, 1],
    #         [2, 3, 4]]

    answer = Y_ANSWER

    if not is_latin_square(mtrx):
        answer = N_ANSWER

    print(answer)


main()
