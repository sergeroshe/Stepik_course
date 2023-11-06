row_amount = int(input())
column_amount = int(input())
# row_amount = 8
# column_amount = 2
matrix = []

# Simple but ineffective solution:
# for i in range(row_amount):
#     mult.append([(i * j) for j in range(column_amount)])
# print(*mult, sep='\n')

# mult = []

for i in range(min(row_amount, column_amount)):
    row = []
    for j in range(i):
        row.append(matrix[j][i])
    for k in range(i, column_amount):
        row.append(i * k)
    matrix.append(row)

# Bellow we start filling in the matrix from the point where we stopped in the previous part.
# For example, if row_amount is 8 and column_amount is 3, we start with 3
# as 8 - (8 - 3) = 3, counting that 3 is the 4th element index.

if column_amount < row_amount:
    for l in range(row_amount - (row_amount - column_amount), row_amount):
        matrix.append([(m * l) for m in range(column_amount)])

for row in matrix:
    print(*row)

