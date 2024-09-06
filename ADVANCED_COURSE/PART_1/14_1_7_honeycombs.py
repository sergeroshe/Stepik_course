import turtle

SIDE = 50


def hexagon(side):
    for _ in range(6):
        turtle.forward(side)
        turtle.left(60)


def honeycombs(side, num):
    right_angle = 0
    angle = 60
    i = 0
    while i < num:
        hexagon(side)
        turtle.forward(side)
        turtle.right(angle)
        right_angle += angle
        if right_angle == 360:
            turtle.left(120)
            turtle.forward(side)
            turtle.right(angle)
        i += 1


def main():
    window = turtle.Screen()
    turtle.showturtle()
    honeycombs(SIDE, 10)
    turtle.hideturtle()
    window.mainloop()


main()
