import turtle

SIDE = 200
SHIFT = 5


def square(side):
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)


def square_pattern(side, shift):
    while side > shift:
        side -= shift
        square(side)
        turtle.forward(shift)


def main():
    window = turtle.Screen()
    turtle.showturtle()
    square_pattern(SIDE, SHIFT)
    turtle.hideturtle()
    window.mainloop()


main()
