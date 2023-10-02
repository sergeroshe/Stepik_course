size = int(input())
#
matrix = []
# size = 2
# matrix = [['1 2 3 4'], ['5 6 3 15']]
row = []
for _ in range(size):
    row = input().split()
    int_row = [int(item) for item in row]
    matrix.append(int_row)


for row in matrix:
    counter_list = []
    arithmetic_mean = sum(row) // len(row)
    counter = 0
    for col in row:
        if col > arithmetic_mean:
            counter += 1
    counter_list.append(counter)
    print(*counter_list, sep='\n')


# TODO: create list of data, and print val after
