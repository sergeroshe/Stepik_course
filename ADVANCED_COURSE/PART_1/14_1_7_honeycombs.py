import turtle

SHIFT_ANGLE = 45
SIDE = 50


def hexagon(side):
    for _ in range(6):
        turtle.forward(side)
        turtle.left(60)


def honeycombs(side, num):
    for _ in range(num):
        hexagon(side)
        turtle.right(120)
        turtle.forward(side)
        turtle.left(60)


def main():
    window = turtle.Screen()
    turtle.showturtle()
    honeycombs(SIDE, 6)
    turtle.hideturtle()
    window.mainloop()


main()
