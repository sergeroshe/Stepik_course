Y_ANSWER = 'YES'
N_ANSWER = 'NO'
matrix_size = int(input())
matrix = [input().split() for i in range(matrix_size)]
# matrix = ['8 1 6'.split(),
#           '3 5 7'.split(),
#           '4 9 2'.split()]
#
# matrix_size = len(matrix)

valid_num_list = list(range(1, matrix_size ** 2 + 1))
result = N_ANSWER

int_matrix = ([[int(matrix[i][j]) for j in range(matrix_size)] for i in range(matrix_size)])
checked_num_list = []
for i in range(len(int_matrix)):
    for j in range(len(int_matrix)):
        if int_matrix[i][j] not in checked_num_list:
            checked_num_list.append(int_matrix[i][j])
# check of matrix content requirements corresponding
all_numbers_present = len(checked_num_list) == len(valid_num_list) and \
    min(checked_num_list) == min(valid_num_list) and \
    max(checked_num_list) == max(valid_num_list)

if all_numbers_present:
    main_diagonal_sum = 0
    secondary_diagonal_sum = 0
    prev_row_sum = 0
    cur_row_sum = 0
    prev_column_sum = 0

    rows_equal = True
    columns_equal = True
    row_sum_column_sum_equal = True
    row_diagonal_sum_equal = True

    i = 0
    while row_sum_column_sum_equal and \
            row_sum_column_sum_equal and \
            rows_equal and columns_equal \
            and i < matrix_size:
        prev_row_sum = sum(int_matrix[i - 1])
        cur_row_sum = sum(int_matrix[i])

        j = 0
        prev_column_sum = 0
        cur_column_sum = 0
        while row_sum_column_sum_equal and \
                row_sum_column_sum_equal and \
                rows_equal and columns_equal \
                and j < matrix_size:
            # diagonal sums calculation
            if i == j:
                main_diagonal_sum += int(matrix[i][j])
            if i + j + 1 == matrix_size:
                secondary_diagonal_sum += int(matrix[i][j])
            # column sums calculation
            prev_column_sum += int_matrix[j][i - 1]
            cur_column_sum += int_matrix[j][i]
            j += 1

        # all checks after each iteration
        if prev_row_sum != cur_row_sum:
            rows_equal = False
        if prev_column_sum != cur_column_sum:
            columns_equal = False
        if cur_column_sum != cur_row_sum:
            row_sum_column_sum_equal = False

        i += 1
    # final checks
    if rows_equal and columns_equal and main_diagonal_sum == secondary_diagonal_sum \
            and row_sum_column_sum_equal:
        result = Y_ANSWER

print(result)
