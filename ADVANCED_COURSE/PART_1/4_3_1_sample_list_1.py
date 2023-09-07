size = int(input())
total_list = [[j for j in range(1, size + 1)] for i in range(size)]

print(*total_list, sep='\n')
