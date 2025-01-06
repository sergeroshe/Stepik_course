import turtle as t
import random as r
import math

COORD_LIST_X = list(range(-200, 200))
COORD_LIST_Y = list(range(-200, 200))
MIN_SNOWFLAKE_RADIUS = 10
MAX_SNOWFLAKE_RADIUS = 50


def get_random_params():
    x_pos = r.choice(COORD_LIST_X)
    y_pos = r.choice(COORD_LIST_Y)
    cur_radius = r.choice(range(MIN_SNOWFLAKE_RADIUS, MAX_SNOWFLAKE_RADIUS))
    return x_pos, y_pos, cur_radius


def get_circle(prev_circle_list):
    free_space_found = False
    value_list_len = len(prev_circle_list)
    while not free_space_found:
        overlay_found = False
        x_pos, y_pos, radius = get_random_params()
        i = 0
        while not overlay_found and i < value_list_len:
            value = prev_circle_list[i]
            prev_x_pos = value[0]
            prev_y_pos = value[1]
            prev_radius = value[2]
            distance = math.sqrt((x_pos - prev_x_pos) ** 2 + (y_pos - prev_y_pos) ** 2)
            print(f'distance = {distance}')
            print(f'prev, cur radius'
                  f' sum = {prev_radius + radius}')
            if prev_radius + radius >= distance:
                overlay_found = True
                print(f'overlay found!')
            else:
                i += 1
        if not overlay_found:
            print(f'Free space found!')
            # extract return out of loop
            return x_pos, y_pos, radius


def draw_snowflake(x_pos, y_pos, radius, feather_amount, color):
    ray_length = radius // 4
    t.speed(0)
    t.color(color)
    angle = 360 // feather_amount
    center = x_pos, y_pos
    t.penup()
    random_turn = r.choice(range(0, 360, angle // 2))
    for feather in range(feather_amount):
        t.goto(center)
        direction = angle * feather + random_turn
        t.setheading(direction)
        draw_snowflake_feather(ray_length, 3, angle, direction)


# check func separately
def draw_snowflake_feather(ray_length, ray_amount, angle, direction):
    # rename args
    for j in range(ray_amount):
        t.pendown()
        # step 1
        t.forward(ray_length)
        for k in range(1, ray_amount):
            rod_pos = t.pos()[0], t.pos()[1]
            if k % 2:
                t.left(angle)
            else:
                t.right(angle)
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
    while True:
        x_pos, y_pos, radius = get_circle(prev_circle_list)
        draw_snowflake(x_pos, y_pos, radius, 8, 'blue')
        circle = (x_pos, y_pos, radius)
        print(circle)
        prev_circle_list.append(circle)


def main():
    # extract init to func
    window = t.Screen()
    t.showturtle()
    t.speed(0)
    t.pensize(1)
    start_snowfall()
    # t.hideturtle()
    window.mainloop()


main()
