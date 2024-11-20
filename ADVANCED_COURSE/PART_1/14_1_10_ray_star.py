import turtle

SIDE = 200
RAY_AMOUNT = 12


def ray(side):
    for _ in range(2):
        turtle.forward(side)
        turtle.left(180)


#
# intenting to use a square func as an argument of below func, not working yet
def turn_figure(shift, figure_amount):
    angle = 0
    for _ in range(figure_amount):
        ray(SIDE)
        angle += shift
        turtle.setheading(angle)


def main():
    window = turtle.Screen()
    turtle.showturtle()
    shift_angle = 360 / RAY_AMOUNT
    turn_figure(shift_angle, RAY_AMOUNT)
    turtle.hideturtle()
    window.mainloop()


main()
