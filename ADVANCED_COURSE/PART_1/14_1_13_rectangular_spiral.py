import turtle

INIT_SIDE = 5
LIMIT_SIDE = 33
SHIFT = 5


def spiral(init_side, limit_side, shift):
    side = init_side
    size_reached = side > limit_side
    heading = turtle.heading()
    turned_up = heading == 90
    spiral_complete = size_reached and turned_up
    while not spiral_complete:
        turtle.left(90)
        turtle.forward(side)
        side += shift
        heading = turtle.heading()
        size_reached = side > limit_side
        turned_up = heading == 90
        spiral_complete = size_reached and turned_up


def main():
    window = turtle.Screen()
    turtle.showturtle()
    spiral(INIT_SIDE, LIMIT_SIDE, SHIFT)
    turtle.hideturtle()
    window.mainloop()


main()
