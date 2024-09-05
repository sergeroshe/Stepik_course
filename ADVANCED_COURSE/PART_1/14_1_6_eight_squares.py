import turtle

SHIFT_ANGLE = 45
SIDE = 200


def square(side):
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)


#
# intenting to use a square func as an argument of below func, not working yet
def turn_figure(shift):
    angle = 0
    for _ in range(8):
        square(SIDE)
        angle += shift
        turtle.setheading(angle)


def main():
    window = turtle.Screen()
    turtle.showturtle()
    turn_figure(SHIFT_ANGLE)
    turtle.hideturtle()
    window.mainloop()


main()
