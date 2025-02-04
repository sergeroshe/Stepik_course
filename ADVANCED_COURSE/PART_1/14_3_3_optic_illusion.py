import turtle as t

TRIANGLE_SIZE = 400
DOT_SIZE = 125
START_POSITION = -TRIANGLE_SIZE // 2, -TRIANGLE_SIZE // 4



def draw_triangle(size, color):
    for _ in range(3):
        t.forward(size)
        t.left(120)


def draw_dots(init_position, circle_size, side, color):
    t.goto(init_position)
    for _ in range(3):
        t.dot(circle_size, color)
        t.forward(side)
        t.left(120)


def draw_illusion(triangle_size, dot_size, color):
    start_position = START_POSITION
    t.goto(start_position)
    t.pendown()
    draw_triangle(triangle_size, color)
    second_triangle_postition = (start_position[0] + triangle_size,
                                 start_position[1] + triangle_size * 0.60)
    t.penup()
    t.goto(second_triangle_postition)
    t.right(180)
    t.pendown()
    draw_dots(second_triangle_postition, dot_size, triangle_size, 'black', )
    t.fillcolor('white')
    t.begin_fill()
    t.penup()
    draw_triangle(triangle_size, color)
    t.end_fill()

def main():
    window = t.Screen()
    t.hideturtle()
    t.penup()
    t.speed(0)

    draw_illusion(TRIANGLE_SIZE, DOT_SIZE, 'black')

    t.pensize(1)
    window.mainloop()


main()
