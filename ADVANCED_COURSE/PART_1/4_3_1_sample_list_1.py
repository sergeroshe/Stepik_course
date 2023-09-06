row_number = int(input())
total_list = [[j for j in range(1, row_number + 1)] for i in range(row_number)]

print(*total_list, sep='\n')
