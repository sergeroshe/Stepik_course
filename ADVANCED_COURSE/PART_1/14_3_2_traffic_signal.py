import turtle as t

BODY_SIZE = 350
LAMP_SIZE = BODY_SIZE // 10


def draw_rectangle(size, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(size // 3)
        t.left(90)
        t.forward(size)
        t.left(90)
    t.end_fill()


def draw_signal_lamps(size, color_list):

    for i in range(3):
        t.setheading(0)

        t.fillcolor(color_list[i])
        t.begin_fill()
        t.circle(size)
        t.end_fill()
        t.left(90)
        t.forward(size * 2.5)


def draw_traffic_signal():
    t.goto(0, -BODY_SIZE // 2)
    frame_size = BODY_SIZE // 6
    start_pos = t.pos()
    center = (start_pos[0] + frame_size, start_pos[1])
    color_list = ['green', 'yellow', 'red']
    t.pendown()

    print(start_pos)

    draw_rectangle(BODY_SIZE, 'black')

    t.goto(center)
    t.goto(center[0], center[1] + frame_size)

    draw_signal_lamps(LAMP_SIZE, color_list)


def main():
    window = t.Screen()
    # t.hideturtle()
    t.penup()
    t.speed(0)

    draw_traffic_signal()

    t.pensize(1)
    window.mainloop()


main()
