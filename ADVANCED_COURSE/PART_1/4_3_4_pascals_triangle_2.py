def get_pascals_triangle_row(size) -> list:
    prev_row = []
    cur_row = []

    for i in range(size + 1):
        cur_row = [1] * (i + 1)
        for j in range(1, i):
            cur_row[j] = prev_row[j - 1] + prev_row[j]
        prev_row = cur_row

    return cur_row


def main():
    # pascals_triangle = []
    # row_number = 5
    row_number = int(input())
    for i in range(row_number):
        row = get_pascals_triangle_row(i)
        ones, *values = row
        unpacked_row = ones, *values
        print(*unpacked_row)


main()
