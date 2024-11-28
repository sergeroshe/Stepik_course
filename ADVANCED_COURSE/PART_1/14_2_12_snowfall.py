import turtle as t
import random as r

COORD_LIST = list(range(-200, 200))


def get_coordinates(coord_list):
    x_pos, y_pos = r.sample(coord_list, 2)
    return x_pos, y_pos, coord_list


def draw_snowflake(x_pos, y_pos, radius, feather_amount, color):
    feather_length = radius // 4
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
        draw_snowflake_feather(feather_length, 3, angle, direction)


# check func separately
def draw_snowflake_feather(feather_length, ray_amount, angle, direction):
    # rename args
    for j in range(ray_amount):
        t.pendown()
        # step 1
        t.forward(feather_length)
        for k in range(1, ray_amount):
            rod_pos = t.pos()[0], t.pos()[1]
            if k % 2:
                t.left(angle)
            else:
                t.right(angle)
            t.pendown()
            # step 2
            t.forward(feather_length)
            t.penup()
            t.goto(rod_pos)
            t.setheading(direction)
            t.pendown()
        # step 3
    t.forward(feather_length)


def cause_snowfall():
    snowflake_radius = r.choice(range(10, 50))
    coord_list = COORD_LIST
    while coord_list:
        # snowflake_radius = r.choice(range(10, 100))
        x_pos, y_pos, coord_list = get_coordinates(coord_list)
        # make a square around used coordinates to use only wmpty space
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
