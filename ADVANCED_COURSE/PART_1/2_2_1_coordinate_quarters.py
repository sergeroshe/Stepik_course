QUARTER_MESSAGE = 'Первая четверть: {first_quarter_points_count} \n' \
                  ' Вторая четверть: {second_quarter_points_count} \n' \
                  'Третья четверть: {third_quarter_points_count} \n' \
                  'Четвертая четверть: {fourth_quarter_points_count}'


def get_coordinate_quarter(x, y):
    coordinate_quarter_num = 0
    if x and y:
        if x > 0 and y > 0:
            coordinate_quarter_num = 1
        elif x < 0 < y:
            coordinate_quarter_num = 2
        elif x < 0 and y < 0:
            coordinate_quarter_num = 3
        elif x > 0 > y:
            coordinate_quarter_num = 4

    return coordinate_quarter_num


def get_quarters_for_coordinates(quarter_message):
    point_amount = int(input())
    first_quarter_points_counter = 0
    second_quarter_points_counter = 0
    third_quarter_points_counter = 0
    fourth_quarter_points_counter = 0

    for i in range(point_amount):
        coordinates = input().split()
        x = int(coordinates[0])
        y = int(coordinates[1])

        coordinate_quarter = get_coordinate_quarter(x, y)
        if coordinate_quarter == 1:
            first_quarter_points_counter += 1
        elif coordinate_quarter == 2:
            second_quarter_points_counter += 1
        elif coordinate_quarter == 3:
            third_quarter_points_counter += 1
        elif coordinate_quarter == 4:
            fourth_quarter_points_counter += 1

    quarter_message = quarter_message.format(first_quarter_points_count=first_quarter_points_counter,
                                             second_quarter_points_count=second_quarter_points_counter,
                                             third_quarter_points_count=third_quarter_points_counter,
                                             fourth_quarter_points_count=fourth_quarter_points_counter)

    print(quarter_message)


def main():
    get_quarters_for_coordinates(QUARTER_MESSAGE)


main()
