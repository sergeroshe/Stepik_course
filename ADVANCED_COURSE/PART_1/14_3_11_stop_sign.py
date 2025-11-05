import turtle as t
from math import sin, cos, radians

OCTAGON_SIZE = 347
OCTAGON_OUTER_SIDE = 161
OCTAGON_INNER_SIDE = 150
BORDER = 5
BOLD = 57

t.Screen().colormode(255)
t.Screen().setup(1000, 250)


def draw_octagon(side):
    angle = 360 / 8
    t.pendown()

    for _ in range(8):
        t.forward(side)
        t.left(angle)
    t.penup()


def write_instruction(cur_pos):
    t.goto(cur_pos[0] - 15, cur_pos[1] + OCTAGON_INNER_SIDE - 5)
    t.fillcolor('white')
    t.begin_fill()
    t.write('STOP', font=('Arial', 57, 'bold'))
    t.end_fill()

def draw_stop_sign():
    t.goto(-OCTAGON_OUTER_SIDE // 2, -OCTAGON_SIZE // 2)
    cur_pos = t.position()

    draw_octagon(OCTAGON_OUTER_SIDE)

    # t.setheading(45)
    t.goto(cur_pos[0] + 5, cur_pos[1] + 14)
    t.setheading(0)
    t.fillcolor('red')
    t.begin_fill()
    # t.write('STOP', font=('Arial', 57, 'bold'))

    draw_octagon(OCTAGON_INNER_SIDE)

    t.end_fill()

    write_instruction(cur_pos)





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
