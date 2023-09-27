size = int(input())

matrix = []
row = []
for _ in range(size):
    row = input().split()
    int_row = [int(item) for item in row]
    matrix.append(int_row)

# matrix = [['1 2 3 4'], ['5 6 3 15']]
for row in matrix:
    arithmetic_mean = sum(row) // len(row)
    count = 0
    for col in row:
        if col > arithmetic_mean:
            count += 1
    print(count)