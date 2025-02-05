import turtle as t

CIRCLE_MIN_SIZE = 30
CIRCLE_MAX_SIZE = 300

COLOR_LIST = ['pink', 'violet', 'blue', 'white', 'yellow', 'orange', 'red', 'green', 'brown']
SHIFT_SIZE = CIRCLE_MAX_SIZE // 8

def draw_circle(size, color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(size)
    t.end_fill()


# give a proper name
def draw_picture():
    t.goto(0, -CIRCLE_MAX_SIZE)
    size = CIRCLE_MAX_SIZE
    i = len(COLOR_LIST) - 1
    pos = t.pos()
    while i:
        draw_circle(size, COLOR_LIST[i])
        pos = pos[0], pos[1] + SHIFT_SIZE
        t.goto(pos)
        size -= SHIFT_SIZE
        i -= 1
        



def main():
    window = t.Screen()
    t.hideturtle()
    t.penup()
    t.speed(0)

    draw_picture()

    t.pensize(1)
    window.mainloop()


main()
