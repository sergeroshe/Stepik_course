def get_pascals_triangle_row(row_number) -> list:
    prev_row = []
    cur_row = []

    for i in range(row_number + 1):
        cur_row = [1] * (i + 1)
        for j in range(1, i):
            cur_row[j] = prev_row[j - 1] + prev_row[j]
        prev_row = cur_row

    return cur_row


def main():
    triangle = []
    triangle_size = int(input())

    for i in range(triangle_size):
        row = get_pascals_triangle_row(i)
        triangle.append(row)

    for row in triangle:
        print(*row)


main()
