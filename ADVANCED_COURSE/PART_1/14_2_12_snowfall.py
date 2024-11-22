import turtle as t
import random as r

X_COORDINATES_RANGE = range(-200, 200)
Y_COORDINATES_RANGE = range(-200, 200)


def get_coordinates(x_range, y_range, snowflake_radius):
    x_coordinates_range_list = list(x_range)
    y_coordinates_range_list = list(y_range)
    x_coord = r.choice(x_coordinates_range_list)
    y_coord = r.choice(y_coordinates_range_list)
    taken_x_space = set(list(range(x_coord - snowflake_radius, x_coord + snowflake_radius)))
    taken_y_space = set(list(range(y_coord - snowflake_radius, y_coord + snowflake_radius)))
    free_x_coordinates_range = x_range - taken_x_space
    free_y_coordinates_range = y_range - taken_y_space
    return x_coord, y_coord, free_x_coordinates_range, free_y_coordinates_range


def snowflake(x_pos, y_pos, radius, feather_amount, color):
    feather_length = radius // 4
    t.speed(3)
    t.color(color)
    angle = 360 // feather_amount
    center = x_pos, y_pos
    t.penup()
    # t.goto(center)

    for i in range(feather_amount):
        t.goto(center)
        t.setheading(angle * i)
        snowflake_feather(feather_length, 3, angle, i)


def snowflake_feather(feather_length, ray_amount, angle, feather_number):
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
            t.setheading(angle * feather_number)
            t.pendown()
        # step 3
    t.forward(feather_length)


def snowfall():
    x_coordinates_range = (X_COORDINATES_RANGE)
    y_coordinates_range = (Y_COORDINATES_RANGE)
    while x_coordinates_range and y_coordinates_range:
        snowflake_radius = r.choice(range(10, 100))
        x_coordinates = get_coordinates(x_coordinates_range, y_coordinates_range, snowflake_radius)[0]
        y_coordinates = get_coordinates(x_coordinates_range, y_coordinates_range, snowflake_radius)[1]
        x_coordinates_range = get_coordinates(x_coordinates, y_coordinates, snowflake_radius)[2]
        y_coordinates_range = get_coordinates(x_coordinates, y_coordinates, snowflake_radius)[3]
        # coordinates = tuple(x_coordinates, y_coordinates)
        # make a square around used coordinates to use only wmpty space
        snowflake(x_coordinates, y_coordinates, snowflake_radius, 8, 'blue')


def main():
    window = t.Screen()
    t.showturtle()
    t.speed(0)
    t.pensize(1)
    snowfall()
    # t.hideturtle()
    window.mainloop()


main()
