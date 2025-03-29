import turtle as t

RING_RADIUS = 100
RING_WIDTH = 20


def olimpic_rings(rad):
    t.penup()
    # move turtle to fit figure the screen with any size
    t.goto(0, -rad)
    pos = t.pos()
    x = pos[0]
    y = pos[1]
    t.pencolor('green')
    t.pendown()
    t.circle(rad)
    t.penup()
    t.goto(x + rad + RING_WIDTH, y + rad * 1.3 + RING_WIDTH)
    t.pendown()
    color_list = ['red', 'black', 'blue']
    for i in range(3):
        t.pencolor(color_list[i])
        shift = rad * 2 + RING_WIDTH
        pos = t.pos()
        x = pos[0]
        y = pos[1]
        x -= shift
        t.circle(rad)
        t.penup()
        t.goto(x, y)
        t.pendown()
    t.penup()
    t.goto(x + rad * 3 + RING_WIDTH, y - (rad * 1.3 + RING_WIDTH))
    t.pencolor('yellow')
    t.pendown()
    t.circle(rad)


def main():
    window = t.Screen()
    t.showturtle()
    t.pensize(RING_WIDTH)
    t.speed(0)
    olimpic_rings(RING_RADIUS)
    # t.hideturtle()
    window.mainloop()


main()