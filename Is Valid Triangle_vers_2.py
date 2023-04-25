def is_valid_triangle(side_1, side_2, side_3):
    side_angles_list = [side_1, side_2, side_3]
    result = True
    for i in range(len(side_angles_list)):
        side_angle = side_angles_list[i]
        other_sides_sum = side_angles_list[i - 1] + side_angles_list[i - 2]

        side_angles_list[i], side_angles_list[i - 2], side_angles_list[i - 1]\
            = side_angles_list[i - 2], side_angles_list[i - 1], side_angles_list[i]
        # shift element left
        if side_angle >= other_sides_sum:
            result = False
            break
    return result


def main():
    a, b, c = [int(input()), int(input()), int(input())]
    print(is_valid_triangle(a, b, c))



main()