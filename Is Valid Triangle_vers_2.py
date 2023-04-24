def is_valid_triangle(side_1, side_2, side_3):
    sides_angles_list = [side_1, side_2, side_3]
    result = True
    for i in range(len(sides_angles_list)):
        side_angle = sides_angles_list[i]
        other_sides_sum = sides_angles_list[i - 1] + sides_angles_list[i - 2]

        sides_angles_list[i], sides_angles_list[i - 2], sides_angles_list[i - 1]\
            = sides_angles_list[i - 2], sides_angles_list[i - 1], sides_angles_list[i]
        # shift element left
        if side_angle >= other_sides_sum:
            result = False
            break
    return result

#
def main():
    a, b, c = [int(input()), int(input()), int(input())]
    print(is_valid_triangle(a, b, c))



main()