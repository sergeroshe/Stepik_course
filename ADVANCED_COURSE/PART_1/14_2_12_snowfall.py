import turtle as t
import random as r


def snowflake(x_pos, y_pos, radius):
    feather_length = radius // 4
    t.speed(0)
    angle = 45
    center = x_pos, y_pos
    t.penup()
    # t.goto(center)

    for i in range(8):
        t.goto(center)
        t.setheading(angle * i)
        for j in range(3):
            t.pendown()
            # step 1
            t.forward(feather_length)
            for k in range(1, 3):
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
                t.setheading(angle * i)
                t.pendown()
            # step 3
        t.forward(feather_length)


def snowfall():
    while True:
        current_coordinates_set = set()
        snowflake_radius = r.choice(range(10, 100))
        coordinates_range = (range(-snowflake_radius * 10, snowflake_radius * 10, snowflake_radius))
        coordinates = tuple(r.sample(coordinates_range, 2))
        current_coordinates_set.add(coordinates)
        current_coordinates = r.choice(list(current_coordinates_set))
        snowflake(current_coordinates[0], current_coordinates[0], snowflake_radius)
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
