def get_middle_point(x_1, y_1, x_2, y_2):
    x_middle = (x_1 + x_2) / 2
    y_middle = (y_1 + y_2) / 2

    return x_middle, y_middle


def main():
    x_1, y_1 = int(input()), int(input())
    x_2, y_2 = int(input()), int(input())
    x, y = get_middle_point(x_1, y_1, x_2, y_2)

    print(x, y)


main()