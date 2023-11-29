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
def is_sequence_valid(sequence):
    checked_num_list = []
    len_sequence = len(matrix)
    max_element = matrix[0][0]
    min_element = matrix[0][0]
    first_column_amount = 0
    main_diagonal_sum = 0
    secondary_diagonal_sum = 0
    i = 0

    num_valid = True
    while i < len_sequence and num_valid:
        j = 0
        while j < len_sequence and num_valid:
            num = matrix[i][j]
            if i == 0:
                first_column_amount += matrix[j][i]
            if num not in checked_num_list:
                checked_num_list.append(num)
                if num > max_element:
                    max_element = num
                if num < min_element:
                    min_element = num
            else:
                num_valid = False
            if i == j:
                main_diagonal_sum += int(matrix[i][j])
            if i + j + 1 == matrix_size:
                secondary_diagonal_sum += int(matrix[i][j])

            j += 1
        i += 1

    is_sequence_valid_ = max_element == len(checked_num_list) and min_element == MATRIX_MIN_ELEMENT

    return is_sequence_valid_, first_column_amount, main_diagonal_sum, secondary_diagonal_sum


result = N_ANSWER

# # check of matrix content requirements corresponding
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
# SEQUENCE = [1, 8, 7, 3, 5, 6, 2, 4]
#
# SEQ_MIN_ELEMENT = 1
#
# checked_num_list = []
# cur_num = SEQUENCE[0]
# len_sequence = len(SEQUENCE)
# i = 0
# max_element = SEQUENCE[0]
# min_element = SEQUENCE[0]
#
# num_valid = True
# while i < len_sequence and num_valid:
#     num = SEQUENCE[i]
#     if num not in checked_num_list:
#         checked_num_list.append(num)
#         if num > max_element:
#             max_element = num
#         if num < min_element:
#             min_element = num
#     else:
#         num_valid = False
#     i += 1
#
# all_numbers_present = max_element == len_sequence and min_element == SEQ_MIN_ELEMENT
# print(all_numbers_present, len_sequence, max_element, min_element)