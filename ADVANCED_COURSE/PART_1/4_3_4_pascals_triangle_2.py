def get_pascals_triangle_row(size):
    row = [1]
    for i in range(size):
        row.append(row[i] * (size - i) // (i + 1))
    return row


def main():
    pascals_triangle = []
    row_number = int(input())
    for i in range(row_number - 1, -1, -1):
        pascals_triangle.append(get_pascals_triangle_row(i))
    pascals_triangle.reverse()
    for row in pascals_triangle:
        print(*row)


main()

