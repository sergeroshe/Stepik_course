import turtle as t
import random as r

COORD_LIST_X = list(range(-200, 200))
COORD_LIST_Y = list(range(-200, 200))
MIN_SNOWFLAKE_RADIUS = 10
MAX_SNOWFLAKE_RADIUS = 50


def get_coordinates(coord_list_x, coord_list_y, max_radius):
    x_pos = r.choice(coord_list_x)
    y_pos = r.choice(coord_list_y)
    del coord_list_x[coord_list_x.index(x_pos) - max_radius:coord_list_x.index(x_pos) + max_radius]
    del coord_list_y[coord_list_y.index(y_pos) - max_radius:coord_list_y.index(y_pos) + max_radius]
    return x_pos, y_pos, coord_list_x, coord_list_y


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


def cause_snowfall():
    # snowflake_radius = r.choice(range(MIN_SNOWFLAKE_RADIUS, MAX_SNOWFLAKE_RADIUS))
    x_coord_list = COORD_LIST_X
    y_coord_list = COORD_LIST_Y
    while len(x_coord_list and y_coord_list) > 2:
        snowflake_radius = r.choice(range(10, 100))
        x_pos, y_pos, x_coord_list, y_coord_list = get_coordinates(x_coord_list, y_coord_list, MAX_SNOWFLAKE_RADIUS)
        draw_snowflake(x_pos, y_pos, snowflake_radius, 8, 'blue')



def main():
    # extract init to func
    window = t.Screen()
    t.showturtle()
    t.speed(0)
    t.pensize(1)
    cause_snowfall()
    # t.hideturtle()
    window.mainloop()


main()
