def get_pascale_triangle_row(row_list):
    row_list = [1] + row_list
    for i in range(1, len(row_list) - 1):
        row_list[i] += row_list[i + 1]
    return row_list


def main():
    triangle_size = int(input())
    row = []
    for _ in range(triangle_size):
        row = get_pascale_triangle_row(row)
        print(*row)


main()
