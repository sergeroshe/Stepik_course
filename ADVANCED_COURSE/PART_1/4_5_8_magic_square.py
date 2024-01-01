Y_ANSWER = 'YES'
N_ANSWER = 'NO'
MATRIX_MIN_ELEMENT = 1
# matrix_size = int(input())
matrix_size = 3
# convert string list to int list
# matrix = []
#
# for _ in range(matrix_size):
#     row = input().split()
#     int_row = [int(item) for item in row]
#     matrix.append(int_row)

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
matrix = [[8, 1, 6],  # i = 0, j = len_mtrx - 1
          [3, 5, 7],  # i = 1, j = len_mtrx - 2
          [4, 9, 2]]  # i = 2, j = len_mtrx - 3
first_row_sum = sum(matrix[0])


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


result = N_ANSWER


# calculate diagonal sums
def matrix_diagonal_sums(mtrx):
    len_mtrx = len(mtrx)
    main_diagonal_sum = 0
    secondary_diagonal_sum = 0
    for row in range(len_mtrx):
        for column in range(len_mtrx):
            if row == column:
                main_diagonal_sum += mtrx[row][column]
            if column == len_mtrx - row - 1:
                secondary_diagonal_sum += mtrx[row][column]
    return main_diagonal_sum, secondary_diagonal_sum


matrix_diagonal_sums(matrix)

if sequence_valid and diagonals_equal:
    rows_equal = True
    columns_equal = True
    row_sum_column_sum_equal = True
    row_diagonal_sum_equal = True

    i = 0
    while row_sum_column_sum_equal and \
            rows_equal and columns_equal \
            and i < matrix_size - 1:
        prev_row_sum = first_row_sum
        cur_row_sum = sum(matrix[i + 1])

        j = 0
        prev_column_sum = first_column_sum
        cur_column_sum = 0
        while row_sum_column_sum_equal and \
                rows_equal and columns_equal \
                and j < matrix_size:
            # column sums calculation
            cur_column_sum += matrix[j][i]

            j += 1

        # all checks after each iteration
        rows_equal = prev_row_sum == cur_row_sum
        columns_equal = prev_column_sum == cur_column_sum
        row_sum_column_sum_equal = cur_column_sum == cur_row_sum

        prev_row_sum = cur_row_sum
        prev_column_sum = cur_column_sum

        i += 1

    if rows_equal and columns_equal and row_sum_column_sum_equal:
        result = Y_ANSWER

print(result)
