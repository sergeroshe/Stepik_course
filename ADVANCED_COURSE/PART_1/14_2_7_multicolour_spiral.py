import turtle

INIT_SIDE = 5
LIMIT_SIDE = 300
SHIFT = 5
PENCOLOR_LIST = ['red', 'blue', 'yellow', 'green', 'violet', 'orange']


def spiral(init_side, limit_side, shift, color_list):
    pensize = turtle.pensize(5)
    pencolor = turtle.pencolor()
    side = init_side
    size_reached = side > limit_side
    heading = turtle.heading()
    turned_up = heading == 90
    spiral_complete = size_reached and turned_up
    i = 0
    while not spiral_complete:
        if i > len(color_list):
            i = 0
        turtle.forward(side)
        increase = i * 3
        turtle.pencolor(color_list[i])
        pensize = turtle.pensize(increase)
        side += shift
        heading = turtle.heading()
        size_reached = side > limit_side
        turned_up = heading == 90
        spiral_complete = size_reached and turned_up
        turtle.left(45)
        i += 1


def main():
    window = turtle.Screen()
    turtle.Screen().bgcolor('green')
    turtle.showturtle()
    turtle.shape('triangle')
    spiral(INIT_SIDE, LIMIT_SIDE, SHIFT, PENCOLOR_LIST)
    turtle.done()
    window.mainloop()


main()
