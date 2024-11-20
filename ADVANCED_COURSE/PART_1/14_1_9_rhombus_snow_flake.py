import turtle

SIDE = 200
SNOW_FLAKE_CRYSTAL_AMOUNT = 10


def rhombus(size):
    angle = 0
    shift_list = [60, 120]
    for i in range(4):
        turtle.forward(size)
        angle = shift_list[i % len(shift_list)]
        turtle.left(angle)


#
# intenting to use a square func as an argument of below func, not working yet
def turn_figure(shift, figure_amount):
    angle = 0
    for _ in range(figure_amount):
        rhombus(SIDE)
        angle += shift
        turtle.setheading(angle)


def main():
    window = turtle.Screen()
    turtle.showturtle()
    shift_angle = 360 / SNOW_FLAKE_CRYSTAL_AMOUNT
    turn_figure(shift_angle, SNOW_FLAKE_CRYSTAL_AMOUNT)
    turtle.hideturtle()
    window.mainloop()


main()
