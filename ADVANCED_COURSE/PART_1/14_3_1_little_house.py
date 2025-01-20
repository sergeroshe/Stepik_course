import turtle as t


HOUSE_BODY_PARAMS = (300, 'blue')
HOUSE_ROOF_PARAMS = (380, 'brown')


def draw_square(size, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()


def draw_triangle(size, color):
    t.goto(-size // 2, 0)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(3):
        t.forward(size)
        t.left(120)
    t.end_fill()


def draw_house():
    square_size = HOUSE_BODY_PARAMS[0]
    square_color = HOUSE_BODY_PARAMS[1]
    body_start_pos = (-square_size // 2, -square_size)
    t.penup()
    t.goto(body_start_pos)
    t.pendown()
    draw_square(square_size, square_color)
    roof_start_pos = (0, 0)
    t.penup()
    t.goto(roof_start_pos)
    triangle_size = HOUSE_ROOF_PARAMS[0]
    triangle_color = HOUSE_ROOF_PARAMS[1]
    t.pendown()
    draw_triangle(triangle_size, triangle_color)


def main():
    window = t.Screen()
    t.hideturtle()
    draw_house()
    t.speed(3)
    t.pensize(1)
    window.mainloop()


main()


