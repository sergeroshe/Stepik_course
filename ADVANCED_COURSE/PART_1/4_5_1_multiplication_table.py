# string_amount = int(input())
# column_amount = int(input())
string_amount = 4
column_amount = 6
mult = []
#
# for i in range(string_amount):
#     row = []
#     for j in range(column_amount):
#         row.append(i * j)
#     mult.append(row)

for i in range(string_amount):
    mult.append([(i * j) for j in range(column_amount)])

for i in range(string_amount):
    for j in range(column_amount):
        print(str(mult[i][j]).ljust(3), end=' ')
    print()
