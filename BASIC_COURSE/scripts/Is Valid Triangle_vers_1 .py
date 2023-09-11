def is_valid_triangle(side_1, side_2, side_3):
    value = False
    if side_1 < (side_2 + side_3) and\
       side_2 < (side_1 + side_3) and\
       side_3 < (side_1 + side_2):
        value = True
    return value


def main():
    side_a, side_b, side_c = [int(input()), int(input()), int(input())]

    is_valid = is_valid_triangle(side_a, side_b, side_c)

    print(is_valid)


main()
