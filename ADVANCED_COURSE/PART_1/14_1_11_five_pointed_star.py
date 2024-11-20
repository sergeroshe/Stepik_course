import turtle

SIDE = 200

def star(side, angle):
    for _ in range(5):
        turtle.forward(side)
        turtle.right(angle)


def main():
    window = turtle.Screen()
    turtle.showturtle()
    star(SIDE, 144)
    turtle.hideturtle()
    window.mainloop()


main()
