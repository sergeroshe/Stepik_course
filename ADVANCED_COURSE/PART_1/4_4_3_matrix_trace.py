# Элементы с равными индексами i == j находятся на главной диагонали.
# Такие элементы обозначаются matrix[i][i].
size = int(input())
# size = 3

# row_amount = 4
# col_amount = 4
matrix = []
# matrix = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

amount = 0
for string in range(size):
    matrix.append(input().split())

for row in range(size):
    amount += int(matrix[row][row])

print(amount)

