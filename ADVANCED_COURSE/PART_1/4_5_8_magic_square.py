Y_ANSWER = 'YES'
N_ANSWER = 'NO'
MATRIX_MIN_ELEMENT = 1
# matrix_size = int(input())
matrix_size = 3
# convert string list to int list
# matrix = []

# for _ in range(matrix_size):
#     row = input().split()
#     int_row = [int(item) for item in row]
#     matrix.append(int_row)
#
matrix = [[8, 1, 6],
          [3, 5, 7],
          [4, 9, 2]]

main_diagonal_sum = 0
secondary_diagonal_sum = 0
first_row_sum = sum(matrix[0])

checked_num_list = []


# check if all numbers are non-gap valid sequence with valid min and max, make a function
def is_sequence_valid(sequence):
    len_sequence = len(sequence)
    first_column_sum = 0

    i = 0
    num_valid = True
    while i < len_sequence and num_valid:
        j = 0
        while j < len_sequence and num_valid:
            if i == 0:
                first_column_sum += sequence[j][i]
            if sequence[i][j] not in checked_num_list:
                checked_num_list.append(sequence[i][j])
            j += 1
        i += 1

    if checked_num_list:
        len_checked_num_list = len(checked_num_list)
        for k in range(len_checked_num_list):
            for l in range(k + 1, len_checked_num_list):
                # sorting the list
                if checked_num_list[k] > checked_num_list[l]:
                    checked_num_list[k], checked_num_list[l] = \
                        checked_num_list[l], checked_num_list[k]
                # min, max elements calc
    min_element = checked_num_list[0]
    max_element = checked_num_list[-1]

    is_sequence_valid = max_element == \
                        matrix_size ** 2 and min_element == MATRIX_MIN_ELEMENT

    return is_sequence_valid, first_column_sum


# for i in range(matrix_size):
#     for j in range(matrix_size):
#         if i == 0:
#             first_column_sum += matrix[j][i]
#         # diagonal sums calculation
#         if i == j:
#             main_diagonal_sum += int(matrix[i][j])
#         if i + j + 1 == matrix_size:
#             secondary_diagonal_sum += int(matrix[i][j])
#         if matrix[i][j] < min_element:
#             min_element = matrix[i][j]
#         if matrix[i][j] > max_element:
#             max_element = matrix[i][j]

result = N_ANSWER

# # check of matrix content requirements corresponding

diagonals_equal = main_diagonal_sum == secondary_diagonal_sum
sequence_valid, first_column_sum = is_sequence_valid(matrix)

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
    # final checks
    if rows_equal and columns_equal and row_sum_column_sum_equal:
        result = Y_ANSWER

print(result)
