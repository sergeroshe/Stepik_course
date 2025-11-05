import turtle as t
from math import sin, cos, radians

OCTAGON_SIZE = 347
OCTAGON_OUTER_SIDE = 161
OCTAGON_INNER_SIDE = 150
BORDER = 10

t.Screen().colormode(255)
t.Screen().setup(1000, 250)


def draw_octagon(side):
    angle = 360 / 8
    t.pendown()

    for _ in range(8):
        t.forward(side)
        t.left(angle)
    t.penup()


def draw_stop_sign():
    t.goto(-OCTAGON_OUTER_SIDE // 2, -OCTAGON_SIZE // 2)
    cur_pos = t.position()

    draw_octagon(OCTAGON_OUTER_SIDE)

    t.setheading(45)
    t.forward(BORDER)
    t.setheading(0)

    draw_octagon(OCTAGON_INNER_SIDE)




def main():
    window = t.Screen()
    t.colormode(255)
    t.showturtle()
    t.speed(0)
    t.pensize(2)
    t.pencolor('black')
    t.penup()

    draw_stop_sign()

    window.mainloop()


main()
