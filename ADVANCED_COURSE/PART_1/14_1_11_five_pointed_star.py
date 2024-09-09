import turtle

SIDE = 200
SIDE_AMOUNT = 5


def star(side, side_amount, angle):
    for _ in range(side_amount):
        turtle.forward(side)
        turtle.right(angle)


def main():
    window = turtle.Screen()
    turtle.showturtle()
    angle = 720 / SIDE_AMOUNT
    star(SIDE, SIDE_AMOUNT, angle)
    turtle.hideturtle()
    window.mainloop()


main()
