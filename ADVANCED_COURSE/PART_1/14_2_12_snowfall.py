import turtle as t

RADIUS = 100



def snowflake(x_pos, y_pos):
    angle = 360 / 8
    for _ in range(8):
        t.forward(RADIUS)
        t.penup()
        t.goto(x_pos, y_pos)
        t.left(angle)
        t.pendown()
    t.forward(RADIUS / 4)
    # t.speed(1)
    t.left(angle)
    t.forward(RADIUS / 4)
    for _ in range(6):
        t.left(135)
        t.forward(RADIUS / 4)
        t.right(90)
        t.forward(RADIUS / 4)
    # t.left(135)
    # t.forward(RADIUS / 4)
    # t.right(90)
    # t.forward(RADIUS / 4)
    # t.left(135)
    # t.forward(RADIUS / 4)
    # t.right(90)
    t.forward(RADIUS / 4)
    t.left(135)
    t.forward(RADIUS / 4)




def main():
    window = t.Screen()
    t.showturtle()
    t.speed(0)
    t.pensize(5)
    snowflake(0, 0)
    # t.hideturtle()
    window.mainloop()


main()