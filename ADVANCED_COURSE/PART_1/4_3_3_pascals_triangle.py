# triangle = []
# # row = []
# # triangle_size = int(input())
# size = 5


# for i in range(triangle_size + 1):
#     row = [1] * (i + 1)
#     for j in range(1, i):
#         row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
#     triangle.append(row)
#
# print(triangle[-1])

def get_pascals_triangle_row(size):
    row = [1]
    for i in range(size):
        row.append(row[i] * (size - i) // (i + 1))
    return row


def main():
    row_number = int(input())
    pascals_triangle_row = get_pascals_triangle_row(row_number)
    print(pascals_triangle_row)


main()