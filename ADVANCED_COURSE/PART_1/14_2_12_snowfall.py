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


def get_circle_space():
    # impelement random, compare with choice
    x_pos = -600 + r.random() * 1200
    y_pos = -300 + r.random() * 600
    cur_radius = r.choice(range(MIN_SNOWFLAKE_RADIUS, MAX_SNOWFLAKE_RADIUS))
    print(f'x = {x_pos}, y = {y_pos}')

    return x_pos, y_pos, cur_radius


def get_snowflake_params(prev_circle_list, try_amount_limit):
    color = r.choice(COLOR_LIST)
    x_pos, y_pos, radius, try_limit_exceeded = get_circle(prev_circle_list, try_amount_limit)
    return x_pos, y_pos, radius, try_limit_exceeded, color


# rename vars to concistance
def get_circle(prev_circle_list, try_amount_limit):
    free_space_found = False
    try_amount = 0
    prev_circle_list_len = len(prev_circle_list)
    try_limit_exceeded = False
    while not free_space_found and not try_limit_exceeded:
        overlay_found = False
        x_pos, y_pos, radius = get_circle_space()
        i = 0
        while not overlay_found and i < prev_circle_list_len:
            params = prev_circle_list[i]
            prev_x_pos = params[0]
            prev_y_pos = params[1]
            prev_radius = params[2]
            distance = math.sqrt((x_pos - prev_x_pos) ** 2 + (y_pos - prev_y_pos) ** 2)
            print(f'prev radius = {prev_radius}, current radius = {radius}')
            print(f'distance = {distance}')
            if prev_radius + radius >= distance:
                try_amount += 1
                overlay_found = True
                print(f'overlay found!')
            i += 1

        if not overlay_found:
            print(f'Free space found!')
            free_space_found = True
        elif try_amount > try_amount_limit:
            try_limit_exceeded = True
            print(f'try_amount = {try_amount}')

    return x_pos, y_pos, radius, try_limit_exceeded


def draw_snowflake(x_pos, y_pos, radius, feather_amount, color):
    ray_length = radius // 4
    t.speed(0)
    t.color(color)
    angle = 360 // feather_amount
    center = x_pos, y_pos
    t.penup()
    # use random
    random_turn = r.choice(range(0, 360, angle // 2))
    for feather in range(feather_amount):
        t.goto(center)
        direction = angle * feather + random_turn
        t.setheading(direction)
        draw_snowflake_feather(ray_length, 3, 45, direction)


# check func separately
def draw_snowflake_feather(ray_length, ray_amount, ray_angle, direction):
    # rename args
    for j in range(ray_amount):
        t.pendown()
        # step 1
        t.forward(ray_length)
        for k in range(1, ray_amount):
            rod_pos = t.pos()[0], t.pos()[1]
            if k % 2:
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
        x_pos, y_pos, radius, try_limit_exceeded, color = get_snowflake_params(prev_circle_list, TRY_AMOUNT_LIMIT)
        if not try_limit_exceeded:
            # color = get_snowflake_params()
            draw_snowflake(x_pos, y_pos, radius, SNOWLAKE_FEATHER_AMOUNT, color)
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