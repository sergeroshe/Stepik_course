def is_valid_triangle(side_list):
    result = True
    for _ in range(len(side_list)):
        side = side_list[0]
        other_sides_sum = sum(side_list[1:])
        if side >= other_sides_sum:
            result = False
            break
        del side_list[0]
        side_list.append(side)

    return result


def main():
    side_list = [int(input()), int(input()), int(input())]
    is_valid = is_valid_triangle(side_list)

    print(is_valid)


main()

# side_angles_list[i], side_angles_list[i - 2], side_angles_list[i - 1]\
#     = side_angles_list[i - 2], side_angles_list[i - 1], side_angles_list[i]
# shift element left