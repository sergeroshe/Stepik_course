def is_valid_triangle(side_1, side_2, side_3):
    while side_1 < (side_2 + side_3) and side_2 < (side_1 + side_3)\
            and side_3 < (side_1 + side_2):
        return True
    else:
        return False
#

def main():
    a, b, c = [int(input()), int(input()), int(input())]
    print(is_valid_triangle(a, b, c))


main()
