# matrix_size = int(input())
# matrix = [input().split() for i in range(matrix_size)]
matrix = ['8 1 6'.split(),
          '3 5 7'.split(),
          '4 9 2'.split()]
matrix_size = len(matrix)
valid_num_list = list(range(1, matrix_size ** 2 + 1))
result = "NO"

int_matrix = ([[int(matrix[i][j]) for j in range(matrix_size)] for i in range(matrix_size)])
sorted_matrix = sorted([int(matrix[i][j]) for j in range(matrix_size) for i in range(matrix_size)])
print(sorted_matrix)

all_numbers_present = valid_num_list == sorted_matrix
if all_numbers_present:
    row_sum = 0
    column_sum = 0
    main_diagonal_sum = 0
    secondary_diagonal_sum = 0

    for i in range(matrix_size):
        row_sum = sum(int_matrix[i])
        if i < matrix_size - 1 and sum(int_matrix[i]) != sum(int_matrix[i + 1]):
            result = 'NO'
            break
        cur_column = []
        for j in range(matrix_size):
            cur_column.append(int_matrix[j][i])  # TODO: find out how to calculate current column
            # and compare with neighbour one
            if i == j:
                main_diagonal_sum += int(matrix[i][j])
            if i + j + 1 == matrix_size:
                secondary_diagonal_sum += int(matrix[i][j])
        if 0 > i < matrix_size - 1 and column_sum != sum(cur_column):
            result = 'NO'
            # print(column_sum, sum(cur_column))
            break
        column_sum = sum(cur_column)
        if i < matrix_size - 1 and sum(int_matrix[i]) != sum(int_matrix[i + 1]):
            result = 'NO'
            break

    print(row_sum, column_sum, main_diagonal_sum, secondary_diagonal_sum)

    if row_sum == column_sum \
            and main_diagonal_sum == secondary_diagonal_sum \
            and row_sum == secondary_diagonal_sum:
        result = 'YES'
print(result)

# '8 1 6'.split(),
# '3 5 7'.split(),
# '4 9 2'.split()


#           '2 2 2 2 2 2 2 2 2 2'.split(),
#           '2 2 2 2 2 2 2 2 2 2'.split(),
#           '2 2 2 2 2 2 2 2 2 2'.split(),
#           '2 2 2 2 2 2 2 2 2 2'.split(),
#           '2 2 2 2 2 2 2 2 2 2'.split(),
#           '2 2 2 2 2 2 2 2 2 2'.split(),
#           '2 2 2 2 2 2 2 2 2 2'.split(),
#           '2 2 2 2 2 2 2 2 2 2'.split()]
