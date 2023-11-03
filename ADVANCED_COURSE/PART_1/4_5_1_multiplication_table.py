row_amount = 5
column_amount = 15
mult = []

# for i in range(row_amount):
#     mult.append([(i * j) for j in range(column_amount)])
# print(*mult, sep='\n')
# #
# mult = []

for i in range(min(row_amount, column_amount)):
    row = []
    for j in range(i):
        row.append(mult[j][i])
    for k in range(i, column_amount):
        row.append(i * k)

    mult.append(row)
print()

for row in mult:
    print(*row)
# 0 0 0  0  0   0      #0
# 0 1 2  3  4   5      #1
# 0 2 4  6  8  10      #2
# 0 3 6  9  12 15      #3
# 0 4 8  12 16 20      #4
# 0 5 10 15 20 25      #5

# 0 0 0     #0
# 0 1 2     #1
# 0 2 4     #2
# 0 3 6     #3
# 0 4 8     #4
# 0 5 10    #5
# 0 6 12    #6
# 0 7 14    #7


# 0 0 0    #0
# 0 1 2    #1
# 0 0 4    #2

# [0, 0, 0]
# [0, 1, 2]
# [0, 0, 4]   mult[2][1] = mult[1][2]
# [0, 0, 0, 9, 12, 15, 18]  mult[3][1] = mult[1][3], mult[3][2] = mult[2][3]
# [0, 0, 0, 0, 16, 20, 24]  mult[4][1] = mult[1][4], mult[4][2] = mult[2][4], mult[4][3] = mult[3][4]
# [0, 0, 0, 0, 0, 25, 30]

