row_amount = int(input())
col_amount = int(input())


matrix = []
row_list = []

for i in range(row_amount):
    for j in range(col_amount):
        row_list.append(input())

    matrix.append(' '.join(row_list))
    row_list = []


print(*matrix, sep='\n')


# def print_matrix(matrix, n, width=1):
#     for r in range(n):
#         for c in range(n):
#             print(str(matrix[r][c]).ljust(width), end=' ')
#         print()