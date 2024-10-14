import turtle

UMBRELLA_HEIGHT = 300
UMBRELLA_WIDTH = 400
RAY_AMOUNT = 4


def umbrella():
    umbrella_top = (0, UMBRELLA_HEIGHT)
    shift = UMBRELLA_WIDTH * 2 // (RAY_AMOUNT - 1)
    for i in range(RAY_AMOUNT):
        turtle.penup()
        turtle.goto(umbrella_top)
        turtle.pendown()
        turtle.goto(UMBRELLA_WIDTH - (shift * i), 0)
        turtle.dot(15)
        turtle.penup()
        turtle.goto(umbrella_top)


def main():
    window = turtle.Screen()
    turtle.showturtle()
    umbrella()
    turtle.hideturtle()
    window.mainloop()


main()