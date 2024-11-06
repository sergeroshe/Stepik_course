import turtle as t

RADIUS = 100


def snowflake(x_pos, y_pos):
    center = x_pos, y_pos
    t.goto(center)
    angle = 45
    for _ in range(8):
        t.forward(RADIUS)
        t.penup()
        t.goto(x_pos, y_pos)
        t.left(angle)
        t.pendown()
    t.forward(RADIUS // 4)
    t.right(225)
    for _ in range(8):
        t.right(90)
        t.forward(RADIUS // 4)
        t.left(135)
        t.forward(RADIUS // 4)
    t.speed(1)
    t.penup()
    t.setheading(0)
    x_pos = t.pos()[0]
    y_pos = t.pos()[1]
    shift = RADIUS // 4
    angle = 0
    # t.goto(x_pos + shift, y_pos)
    for i in range(1, 8):
        t.goto(center)
        t.left(angle)

        for _ in range(3):
            # make it go to the proper position!
            t.goto(x_pos + shift, y_pos)
            x_pos = t.pos()[0]
            y_pos = t.pos()[1]
            t.penup()
            t.left(45)
            t.pendown()
            t.forward(RADIUS // 4)
            t.penup()
            t.goto(x_pos, y_pos)
            t.setheading(angle)
            t.right(45)
            t.pendown()
            t.forward(RADIUS // 4)
            t.goto(x_pos, y_pos)
            t.setheading(angle)
        angle += 45



        # x_pos = t.pos()[0]
        # y_pos = t.pos()[1]
        # shift += RADIUS // 4

    # for _ in range(3):
    #     t.left(45)
    #     t.pendown()
    #     t.forward(RADIUS / 4)
    #     t.penup()
    #     t.goto(x, y)
    #     t.setheading(0)
    #     t.right(45)
    #     t.pendown()
    #     t.forward(RADIUS / 4)
    #     t.goto(x, y)



def main():
    window = t.Screen()
    t.showturtle()
    t.speed(0)
    t.pensize(5)
    snowflake(0, 0)
    # t.hideturtle()
    window.mainloop()


main()
