UPPER_QUARTER_AMOUNT_MSG = 'Верхняя четверть: '
RIGHT_QUARTER_AMOUNT_MSG = 'Правая четверть: '
LOWER_QUARTER_AMOUNT_MSG = 'Нижняя четверть: '
LEFT_QUARTER_AMOUNT_MSG = 'Левая четверть: '

size = int(input())

matrix = []
row = []
for _ in range(size):
    row = input().split()
    int_row = [int(item) for item in row]
    matrix.append(int_row)
#
# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [3, 4, 5, 6],
#           [1, 2, 3, 4]]

upper_quarter_amount = 0
right_quarter_amount = 0
lower_quarter_amount = 0
left_quarter_amount = 0

for i in range(size):
    for j in range(size):
        # upper quarter
        if i < j and i + j + 1 < size:
            upper_quarter_amount += matrix[i][j]
        elif i < j and i + j + 1 > size:
            right_quarter_amount += matrix[i][j]
        # lower quarter
        elif i > j and i + j + 1 > size:
            lower_quarter_amount += matrix[i][j]
        # left quarter
        elif i > j and i + j + 1 < size:
            left_quarter_amount += matrix[i][j]

print(f'{UPPER_QUARTER_AMOUNT_MSG}{upper_quarter_amount}')
print(f'{RIGHT_QUARTER_AMOUNT_MSG}{right_quarter_amount}')
print(f'{LOWER_QUARTER_AMOUNT_MSG}{lower_quarter_amount}')
print(f'{LEFT_QUARTER_AMOUNT_MSG}{left_quarter_amount}')

# Выше главной диагонали: i < j,
# Главная диагональ: i = j
# Ниже главной диагонали: i > j
# Выше побочной диагонали: i + j + 1 < n
# Побочная диагональ: i + j + 1 = n
# Ниже побочной диагонали: i + j + 1 > n
