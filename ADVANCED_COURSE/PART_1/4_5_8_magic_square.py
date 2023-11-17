matrix_size = int(input())
matrix = [input().split() for i in range(matrix_size)]
# matrix = ['6 1 8'.split(),
#           '3 5 7'.split(),
#           '2 9 4'.split()]

matrix_size = len(matrix)

valid_num_list = list(range(1, matrix_size ** 2 + 1))
result = "NO"

int_matrix = ([[int(matrix[i][j]) for j in range(matrix_size)] for i in range(matrix_size)])
sorted_matrix = sorted([int(matrix[i][j]) for j in range(matrix_size) for i in range(matrix_size)])

all_numbers_present = valid_num_list == sorted_matrix
if all_numbers_present:
    row_sum = 0
    column_sum = 0
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
        row_sum = sum(int_matrix[i])
        if i < matrix_size - 1 and sum(int_matrix[i]) != sum(int_matrix[i + 1]):
            rows_equal = False

        j = 0
        cur_column = []
        column_sum = 0
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

        if 0 > i < matrix_size - 1 and column_sum != sum(cur_column):
            columns_equal = False

        column_sum = sum(cur_column)

        if column_sum != row_sum:
            row_column_sum_equal = False

        i += 1

    if row_column_sum_equal \
            and columns_equal \
            and main_diagonal_sum == secondary_diagonal_sum \
            and row_sum == secondary_diagonal_sum:
        result = 'YES'
print(result)

