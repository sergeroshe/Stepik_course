import turtle as t

RADIUS = 100


def snowflake(x_pos, y_pos):
    t.speed(0)
    angle = 45
    center = x_pos, y_pos

    for i in range(8):
        t.goto(center)
        # t.setheading(0)
        t.left(angle * i)
        # t.forward(RADIUS)
        # # t.penup()

        for j in range(1, 4):
            t.goto(center)
            t.setheading(angle * i)
            t.pendown()
            t.forward((RADIUS // 4) * j)
            rod_pos = t.pos()[0], t.pos()[1]
            t.left(angle)
            t.pendown()
            t.forward(RADIUS // 4)
            # t.penup()
            t.goto(rod_pos)
            t.setheading(angle * i)
            t.right(angle)
            t.pendown()
            t.forward(RADIUS // 4)
            t.penup()
            t.goto(rod_pos)
            t.setheading(angle * i)
            t.pendown()
            t.forward(RADIUS // 4)


        # if j == 1:
        #     t.left(135)
        #     t.pendown()
        #     t.forward(RADIUS // 4)
        #     t.penup()
        # t.goto(rod_pos)
        # t.setheading(angle * i)
        # t.right(angle)
        # t.pendown()
        # t.forward(RADIUS // 4)
        # t.penup()


def main():
    window = t.Screen()
    t.showturtle()
    t.speed(0)
    t.pensize(5)
    snowflake(0, 0)
    # t.hideturtle()
    window.mainloop()


main()
