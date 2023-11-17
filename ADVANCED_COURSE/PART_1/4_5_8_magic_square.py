Y_ANSWER = 'YES'
N_ANSWER = 'NO'
# matrix_size = int(input())
# matrix = [input().split() for i in range(matrix_size)]
matrix = ['6 1 8'.split(),
          '3 5 7'.split(),
          '2 9 4'.split()]

matrix_size = len(matrix)

valid_num_list = list(range(1, matrix_size ** 2 + 1))
result = N_ANSWER

int_matrix = ([[int(matrix[i][j]) for j in range(matrix_size)] for i in range(matrix_size)])
sorted_matrix = sorted([int(matrix[i][j]) for j in range(matrix_size) for i in range(matrix_size)])
# check if all numbers are present
all_numbers_present = valid_num_list == sorted_matrix

if all_numbers_present:
    row_sum = 0
    main_diagonal_sum = 0
    secondary_diagonal_sum = 0

    rows_equal = True
    columns_equal = True
    row_column_sum_equal = True
    row_diagonal_sum_equal = True

    i = 0
    while row_column_sum_equal and \
            row_column_sum_equal and \
            rows_equal and columns_equal \
            and i < matrix_size:
        # row sum calculation
        row_sum = sum(int_matrix[i])

        j = 0
        cur_column = []
        cur_column_sum = 0
        while row_column_sum_equal and \
                row_column_sum_equal and \
                rows_equal and columns_equal \
                and j < matrix_size:
            cur_column.append(int_matrix[j][i])
            if i == j:
                main_diagonal_sum += int(matrix[i][j])
            if i + j + 1 == matrix_size:
                secondary_diagonal_sum += int(matrix[i][j])
            j += 1
        # current column sum calculation
        cur_column_sum = sum(cur_column)
        # all checks after first iteration
        if 0 < i < matrix_size:
            if sum(int_matrix[i]) != sum(int_matrix[i - 1]):
                rows_equal = False
            if cur_column_sum != sum(cur_column):
                columns_equal = False
            if cur_column_sum != row_sum:
                row_column_sum_equal = False

        i += 1
    # final checks
    if row_column_sum_equal \
            and columns_equal \
            and main_diagonal_sum == secondary_diagonal_sum \
            and row_sum == secondary_diagonal_sum:
        result = Y_ANSWER

print(result)
