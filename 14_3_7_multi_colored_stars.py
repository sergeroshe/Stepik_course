import turtle as t
import random as r
import math

COORD_LIST_X = list(range(-200, 200))
COORD_LIST_Y = list(range(-200, 200))
COLOR_LIST = ['blue', 'red', 'green', 'yellow', 'grey', 'black', 'brown', 'pink']
MIN_SNOWFLAKE_RADIUS = 10
MAX_SNOWFLAKE_RADIUS = 50
SNOWLAKE_FEATHER_RAY_ANGLE = 45
TRY_AMOUNT_LIMIT = 2
MIN_SNOWLAKE_FEATHER_AMOUNT = 2
MAX_SNOWLAKE_FEATHER_AMOUNT = 15
RAY_LENGTH_RADIUS_PROPORTION = 4
SNOWFLAKE_RANDOM_TURN_PRECISION = 3


def generate_circle_params():
    x_pos = -600 + r.random() * 1200
    y_pos = -300 + r.random() * 600
    cur_radius = r.choice(range(MIN_SNOWFLAKE_RADIUS, MAX_SNOWFLAKE_RADIUS))
    print(f'x = {x_pos}, y = {y_pos}')

    return x_pos, y_pos, cur_radius


def check_segments_overlay(x_1, y_1, x_2, y_2, radius_1, radius_2):
    distance = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
    print(f'distance = {distance}')
    overlay_found = radius_1 + radius_2 >= distance

    return overlay_found


def get_snowflake_params(prev_circle_list, color_list,
                         ray_length_radius_proportion, max_snowlake_feather_amount,
                         min_snowlake_feather_amount, snowflake_random_turn_precision,
                         try_amount_limit):
    (color, random_turn) = None, None
    x_pos, y_pos, size, try_limit_exceeded = get_circle(prev_circle_list, try_amount_limit)

    if not try_limit_exceeded:
        color = r.choice(color_list)
        ray_length = size // ray_length_radius_proportion
        snowlake_feather_amount = int(r.random() * max_snowlake_feather_amount + min_snowlake_feather_amount)
        angle = 360 // snowlake_feather_amount
        random_turn = r.choice(range(0, 360, angle // snowflake_random_turn_precision))

    return (x_pos, y_pos, size, color, random_turn, try_limit_exceeded)


def check_circles_overlay(x_pos, y_pos, size, prev_circle_list):
    try_amount = 0
    prev_circle_list_len = len(prev_circle_list)
    overlay_found = False
    i = 0
    while not overlay_found and i < prev_circle_list_len:
        prev_circle_params = prev_circle_list[i]
        prev_x_pos = prev_circle_params[0]
        prev_y_pos = prev_circle_params[1]
        prev_radius = prev_circle_params[2]
        print(f'prev size = {prev_radius}, current size = {size}')
        overlay_found = check_segments_overlay(prev_x_pos, prev_y_pos, x_pos, y_pos, prev_radius, size)
        if overlay_found:
            try_amount += 1
            print(f'overlay found!')
        i += 1
    return overlay_found


def get_circle(prev_circle_list, try_amount_limit):
    try_amount = 0
    try_limit_exceeded = False
    while not try_limit_exceeded:
        x_pos, y_pos, size = generate_circle_params()
        overlay_found = check_circles_overlay(x_pos, y_pos, size, prev_circle_list)
        if not overlay_found:
            print(f'Free space found!')
        elif try_amount > try_amount_limit:
            try_limit_exceeded = True
            print(f'try_amount = {try_amount}')

        return x_pos, y_pos, size, try_limit_exceeded
        

def draw_star(x_pos, y_pos, ray_length, random_turn):
    t.goto(x_pos, y_pos)
    t.left(random_turn)
    for _ in range(5):
        t.forward(ray_length)
        t.right(144)


def start_snowfall():
    prev_circle_list = []
    # rand color, size, ray amont
    try_limit_exceeded = False
    while not try_limit_exceeded:
        x_pos, y_pos, size, color, random_turn, try_limit_exceeded = (
            get_snowflake_params(prev_circle_list, COLOR_LIST,
                                 RAY_LENGTH_RADIUS_PROPORTION,
                                 MAX_SNOWLAKE_FEATHER_AMOUNT,
                                 MIN_SNOWLAKE_FEATHER_AMOUNT,
                                 SNOWFLAKE_RANDOM_TURN_PRECISION,
                                 TRY_AMOUNT_LIMIT))
        if not try_limit_exceeded:
            t.penup()
            t.fillcolor(color)
            t.begin_fill()
            draw_star(x_pos, y_pos, size, random_turn)
            t.end_fill()
            circle = (x_pos, y_pos, size)
            print(try_limit_exceeded)
            prev_circle_list.append(circle)
        else:
            print(f'Try limit exceeded!')


def main():
    # extract init to func
    window = t.Screen()
    t.showturtle()
    t.speed(3)
    t.pensize(1)

    start_snowfall()

    t.hideturtle()
    window.mainloop()


main()
