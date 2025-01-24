import turtle as t
import random as r
import math

COORD_LIST_X = list(range(-200, 200))
COORD_LIST_Y = list(range(-200, 200))
COLOR_LIST = ['blue', 'red', 'green', 'grey', 'black', 'brown', 'pink']
MIN_SNOWFLAKE_RADIUS = 10
MAX_SNOWFLAKE_RADIUS = 50
SNOWLAKE_FEATHER_RAY_ANGLE = 45
TRY_AMOUNT_LIMIT = 2
SNOWLAKE_FEATHER_AMOUNT = 8


def generate_circle_params():
    x_pos = -600 + r.random() * 1200
    y_pos = -300 + r.random() * 600
    cur_radius = r.choice(range(MIN_SNOWFLAKE_RADIUS, MAX_SNOWFLAKE_RADIUS))
    print(f'x = {x_pos}, y = {y_pos}')

    return x_pos, y_pos, cur_radius


# order of args
# rename params to x_1, x_2 based
def check_circles_overlay(x_pos, y_pos, prev_x_pos, prev_y_pos, prev_radius, radius):
    overlay_found = False
    distance = math.sqrt((x_pos - prev_x_pos) ** 2 + (y_pos - prev_y_pos) ** 2)
    # rename params to x_1, x_2 based
    print(f'distance = {distance}')
    overlay_found = prev_radius + radius >= distance

    return overlay_found


def get_snowflake_params(prev_circle_list, try_amount_limit):
    color = None
    x_pos, y_pos, radius, try_limit_exceeded = get_circle(prev_circle_list, try_amount_limit)
    ray_length = radius // 4
    snowlake_feather_amount = r.choice(list(range(2, 15)))
    angle = 360 // snowlake_feather_amount
    random_turn = r.choice(range(0, 360, angle // 3))

    if not try_limit_exceeded:
        color = r.choice(COLOR_LIST)

    return (x_pos, y_pos, radius, color, ray_length,
            snowlake_feather_amount, random_turn, try_limit_exceeded)


def get_circle(prev_circle_list, try_amount_limit):
    free_space_found = False
    try_amount = 0
    prev_circle_list_len = len(prev_circle_list)
    try_limit_exceeded = False
    while not free_space_found and not try_limit_exceeded:
        overlay_found = False
        x_pos, y_pos, radius = generate_circle_params()
        i = 0
        # extract logic to func!
        while not overlay_found and i < prev_circle_list_len:
            prev_circle_params = prev_circle_list[i]
            prev_x_pos = prev_circle_params[0]
            prev_y_pos = prev_circle_params[1]
            prev_radius = prev_circle_params[2]
            print(f'prev radius = {prev_radius}, current radius = {radius}')
            overlay_found = check_circles_overlay(x_pos, y_pos, prev_x_pos, prev_y_pos, prev_radius, radius)
            if overlay_found:
                try_amount += 1
                print(f'overlay found!')
            i += 1

        if not overlay_found:
            print(f'Free space found!')
            free_space_found = True
        elif try_amount > try_amount_limit:
            try_limit_exceeded = True
            print(f'try_amount = {try_amount}')

    return x_pos, y_pos, radius, try_limit_exceeded


def draw_snowflake(x_pos, y_pos, radius, feather_amount, color, random_turn):
    # make a param
    ray_length = radius // 4
    t.color(color)
    center = x_pos, y_pos
    t.penup()
    angle = 360 // feather_amount
    # make an arg of get snflk params
    for feather in range(feather_amount):
        t.goto(center)
        direction = angle * feather + random_turn
        t.setheading(direction)
        draw_snowflake_feather(ray_length, 3, 45, direction)


# check func separately
def draw_snowflake_feather(ray_length, ray_pair_amount, ray_angle, direction):
    # rename args
    for i in range(ray_pair_amount):
        t.pendown()
        # step 1
        t.forward(ray_length)
        for i in range(1, ray_pair_amount):
            rod_pos = t.pos()[0], t.pos()[1]
            if i % 2:
                t.left(ray_angle)
            else:
                t.right(ray_angle)
            t.pendown()
            # step 2
            t.forward(ray_length)
            t.penup()
            t.goto(rod_pos)
            t.setheading(direction)
            t.pendown()
        # step 3
    t.forward(ray_length)


# rename vars
def start_snowfall():
    prev_circle_list = []
    # rand color, size, ray amont
    try_limit_exceeded = False
    while not try_limit_exceeded:
        (x_pos, y_pos, radius, color, ray_length,
         snowlake_feather_amount, random_turn, try_limit_exceeded) = get_snowflake_params(prev_circle_list,
                                                                                          TRY_AMOUNT_LIMIT)
        if not try_limit_exceeded:
            draw_snowflake(x_pos, y_pos, radius, snowlake_feather_amount,
                           color, random_turn)
            circle = (x_pos, y_pos, radius)
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
