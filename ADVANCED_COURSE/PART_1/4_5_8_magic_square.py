Y_ANSWER = 'YES'
N_ANSWER = 'NO'
MATRIX_MIN_ELEMENT = 1


# check if all numbers are non-gap valid sequence with valid min and max, make a function
def is_sequence_valid(mtrx, expected_min):
    checked_num_list = []
    mtrx_size = len(mtrx)
    expected_max = expected_min + mtrx_size ** 2 - 1

    row_ = 0

    is_valid = True
    while row_ < mtrx_size and is_valid:
        column = 0
        while column < mtrx_size and is_valid:
            num = mtrx[row_][column]
            if expected_min <= num <= expected_max:
                if num not in checked_num_list:
                    checked_num_list.append(num)
                else:
                    is_valid = False
            else:
                is_valid = False
            column += 1
        row_ += 1

    return is_valid


def matrix_diagonal_sums(mtrx):
    len_mtrx = len(mtrx)
    main_diagonal_sum = 0
    secondary_diagonal_sum = 0
    for i in range(len_mtrx):
        main_diagonal_sum += mtrx[i][i]
        secondary_diagonal_sum += mtrx[-(i + 1)][i]
    return main_diagonal_sum, secondary_diagonal_sum


def get_mtrx_column_sum(mtrx, col_idx):
    column_sum = 0
    for row in mtrx:
        column_sum += row[col_idx]
    return column_sum


def is_matrix_equal(sequence, target_sum):
    is_equal = True
    i = 0
    len_seq = len(sequence) - 1
    while is_equal and i <= len_seq:
        cur_column_sum = get_mtrx_column_sum(sequence, i)
        row_sum = sum(sequence[i])
        is_equal = cur_column_sum == target_sum and cur_column_sum == row_sum

        i += 1
    return is_equal


def main():
    matrix_size = int(input())
    matrix = []

    for _ in range(matrix_size):
        row = input().split()
        int_row = [int(item) for item in row]
        matrix.append(int_row)
    result = N_ANSWER
    if is_sequence_valid(matrix, MATRIX_MIN_ELEMENT):
        main_diag_sum, sec_diag_sum = matrix_diagonal_sums(matrix)
        matrix_diagonal_sums_equal = main_diag_sum == sec_diag_sum
        if matrix_diagonal_sums_equal:
            matrix_all_sum_equal = is_matrix_equal(matrix, main_diag_sum)

            if matrix_all_sum_equal:
                result = Y_ANSWER

    print(result)


main()
# If x == 1
#    Var = true
# Var = x == 1
# matrix with duplicate
# # matrix = [[5, 3, 7],
# #           [3, 5, 7],
# #           [9, 4, 2]]
# correct matrix
# # matrix = [[8, 1, 6],
# #           [3, 5, 7],
# #           [4, 9, 2]]
# # greater max matrix
# # matrix = [[5, 3, 7],
# #           [3, 5, 7],
# #           [10, 4, 2]]
#  less min matrix
# matrix = [[8, 0, 6],
#           [5, 3, 7],
#           [9, 4, 2]]
# correct matrix
