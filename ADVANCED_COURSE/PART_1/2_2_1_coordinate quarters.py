def get_coordinate_quarter(x, y):
    coordinate_quarter_num = 0
    x_coordinate = x
    y_coordinate = y
    if x_coordinate and y_coordinate:
        if x_coordinate > 0 and y_coordinate > 0:
            coordinate_quarter_num = 1
        elif x_coordinate < 0 < y_coordinate:
            coordinate_quarter_num = 2
        elif x_coordinate < 0 and y_coordinate < 0:
            coordinate_quarter_num = 3
        elif x_coordinate > 0 > y_coordinate:
            coordinate_quarter_num = 4

    return coordinate_quarter_num


QUARTER_MESSAGE_LIST = ['Первая четверть: {current_quarter_points_count}',
                        'Вторая четверть: {current_quarter_points_count}',
                        'Третья четверть: {current_quarter_points_count}',
                        'Четвертая четверть: {current_quarter_points_count}']

point_amount = 2 # int(input())
quarter_points_counter_list = [0, 0, 0, 0]

for i in range(point_amount):
    coordinates = [-9, 3] # input().split()
    x = int(coordinates[0])
    y = int(coordinates[1])

    coordinate_quarter = get_coordinate_quarter(x, y)
    if coordinate_quarter:
        quarter_points_counter_list[coordinate_quarter - 1] += 1

    QUARTER_MESSAGE_LIST[0] = QUARTER_MESSAGE_LIST[0].format(current_quarter_points_count=
                                                             quarter_points_counter_list[0])
    QUARTER_MESSAGE_LIST[1] = QUARTER_MESSAGE_LIST[1].format(current_quarter_points_count=
                                                             quarter_points_counter_list[1])
    QUARTER_MESSAGE_LIST[2] = QUARTER_MESSAGE_LIST[2].format(current_quarter_points_count=
                                                             quarter_points_counter_list[2])
    QUARTER_MESSAGE_LIST[3] = QUARTER_MESSAGE_LIST[3].format(current_quarter_points_count=
                                                             quarter_points_counter_list[3])


print(*QUARTER_MESSAGE_LIST, sep='\n')
