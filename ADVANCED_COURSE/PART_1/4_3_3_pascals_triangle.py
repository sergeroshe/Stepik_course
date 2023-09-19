def get_pascals_triangle_row(size):
    prev_row = []
    cur_row = []

    for i in range(size + 1):
        cur_row = [1] * (i + 1)
        for j in range(1, i):
            cur_row[j] = prev_row[j - 1] + prev_row[j]
        prev_row = cur_row

    return cur_row


def main():
    row_number = int(input())
    pascals_triangle_row = get_pascals_triangle_row(row_number)
    print(pascals_triangle_row)


main()

# def get_pascals_triangle_row(size):
#     row = [1]
#     for i in range(size):
#         row.append(row[i] * (size - i) // (i + 1))
#     return row
