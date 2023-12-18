Y_ANSWER = 'YES'
N_ANSWER = 'NO'
MATRIX_MIN_ELEMENT = 1
matrix_size = int(input())
# matrix_size = 3
# convert string list to int list
matrix = []
#
for _ in range(matrix_size):
    row = input().split()
    int_row = [int(item) for item in row]
    matrix.append(int_row)
#
# matrix = [[1, 8, 6],
#           [5, 3, 7],
#           [9, 4, 2]]
# # matrix = [[5, 3, 7],
# #           [3, 5, 7],
# #           [9, 4, 2]]

first_row_sum = sum(matrix[0])


# check if all numbers are non-gap valid sequence with valid min and max, make a function
def is_sequence_valid(mtrx, expected_min):
    checked_num_list = []
    mtrx_size = len(mtrx)
    expected_max = expected_min + mtrx_size ** 2 - 1
    max_el = mtrx[0][0]
    min_el = mtrx[0][0]

    row_counter = 0

    is_valid = True
    while row_counter < mtrx_size and is_valid:
        column_counter = 0
        while column_counter < mtrx_size and is_valid:
            num = mtrx[row_counter][column_counter]
            if num < expected_min or num > expected_max:
                if num not in checked_num_list:
                    checked_num_list.append(num)
                    if num > max_el:
                        max_el = num
                    if num < min_el:
                        min_el = num
            else:
                is_valid = False
            column_counter += 1
        row_counter += 1

    is_sequence_valid_ = max_el == expected_max and min_el == expected_min

    return is_sequence_valid_


result = N_ANSWER

# # check of matrix content requirements correspondence
sequence_valid, first_column_sum, main_diagonal_sum, secondary_diagonal_sum = is_sequence_valid(matrix)
diagonals_equal = main_diagonal_sum == secondary_diagonal_sum

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
