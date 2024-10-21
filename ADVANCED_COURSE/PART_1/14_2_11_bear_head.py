import turtle as t

HEAD_RADIUS = 170
FACE_RADIUS = 100
NOSE_RADIUS = 10
JAW_HEIGHT = 70
MOUTH_HEIGHT = 10
EAR_RADIUS = 50


def bear_head():
    t.circle(NOSE_RADIUS)
    t.goto(0, -JAW_HEIGHT)
    t.penup()
    t.goto(t.pos()[0], t.pos()[1] - JAW_HEIGHT)
    t.pendown()
    t.circle(FACE_RADIUS)
    t.circle(HEAD_RADIUS)
    t.penup()
    t.goto(120, 165)
    t.pendown()
    t.circle(EAR_RADIUS)
    t.penup()
    t.goto(t.pos()[0] - 240, t.pos()[1])
    t.pendown()
    t.circle(EAR_RADIUS)
    t.penup()
    t.goto(t.pos()[0] + 50, t.pos()[1] - FACE_RADIUS)
    t.pendown()
    t.dot(30)
    t.penup()
    t.goto(t.pos()[0] + 140, t.pos()[1])
    t.dot(30)


def main():
    window = t.Screen()
    t.showturtle()
    t.speed(0)
    t.pensize(5)
    bear_head()
    # t.hideturtle()
    window.mainloop()


main()
