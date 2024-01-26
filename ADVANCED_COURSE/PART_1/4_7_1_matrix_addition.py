rows, columns = [int(el) for el in input().split()]
matrix_1 = []
for _ in range(rows):
    row = [int(el) for el in input().split()]
    matrix_1.append(row)
empty_line = input()
matrix_2 = []
for _ in range(rows):
    row = [int(el) for el in input().split()]
    matrix_2.append(row)

matrix_sum = []
for i in range(rows):
    row = [(matrix_1[i][j] + matrix_2[i][j]) for j in range(columns)]
    matrix_sum.append(row)

for i in range(rows):
    for j in range(columns):
        print(str(matrix_sum[i][j]).ljust(3), end=' ')
    print()
