import turtle as t
import random as r


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
    while True:
        current_coordinates_set = set()
        snowflake_radius = r.choice(range(10, 100))
        x_coordinates_range = (range(-snowflake_radius * 10, snowflake_radius * 10, snowflake_radius))
        y_coordinates_range = (range(-snowflake_radius * 10, snowflake_radius * 10, snowflake_radius))
        x_coordinates = r.choice(x_coordinates_range)
        y_coordinates = r.choice(y_coordinates_range)
        # coordinates = tuple(x_coordinates, y_coordinates)
        current_coordinates_set.add((x_coordinates, y_coordinates))
        # make a square around used coordinates to use only wmpty space
        current_coordinates = r.choice(list(current_coordinates_set))
        snowflake(current_coordinates[0], current_coordinates[0], snowflake_radius, 8, 'blue')
        print(current_coordinates_set)


def main():
    window = t.Screen()
    t.showturtle()
    t.speed(0)
    t.pensize(1)
    snowfall()
    # t.hideturtle()
    window.mainloop()


main()
