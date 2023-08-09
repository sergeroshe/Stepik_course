def get_coordinate_quarter(x, y):
    coordinate_quarter_num = 0
    x_coordinate = int(x)
    y_coordinate = int(y)
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


QUARTER_MESSAGE_LIST = ['Первая четверть: {first_quarter_points_count}',
                        'Вторая четверть: {second_quarter_points_count}',
                        'Третья четверть: {third_quarter_points_count}',
                        'Четвертая четверть: {forth_quarter_points_count}']
QUARTER_POINTS_COUNTER_LIST = [0, 0, 0, 0]
point_amount = int(input())

coordinates_list = []
result_string_list = []
for _ in range(point_amount):
    result_string_list = []
    coordinate_line_list = input().split()
    x = int(coordinate_line_list[0])
    y = int(coordinate_line_list[1])
    coordinate_quarter = get_coordinate_quarter(x, y)
    if coordinate_quarter:
        QUARTER_POINTS_COUNTER_LIST[coordinate_quarter - 1] += 1
    for current_quarter in QUARTER_MESSAGE_LIST:
        current_quarter = current_quarter.format(
            first_quarter_points_count=QUARTER_POINTS_COUNTER_LIST[0],
            second_quarter_points_count=QUARTER_POINTS_COUNTER_LIST[
                1],
            third_quarter_points_count=QUARTER_POINTS_COUNTER_LIST[2],
            forth_quarter_points_count=QUARTER_POINTS_COUNTER_LIST[3])
        result_string_list.append(current_quarter)
print(*result_string_list, sep='\n')
