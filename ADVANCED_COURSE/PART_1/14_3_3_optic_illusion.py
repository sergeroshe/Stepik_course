import turtle as t

SIZE = 300


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


def draw_illusion(size, color):
    start_position = (-size // 2, -size // 2)
    t.goto(start_position)
    t.pendown()
    draw_triangle(size, color)
    second_triangle_postition = (start_position[0] + size,
                                 start_position[1] + size * 0.60)
    t.penup()
    t.goto(second_triangle_postition)
    t.right(180)
    t.pendown()
    circle_size = 70
    draw_dots(second_triangle_postition, circle_size, size, 'black', )
    t.fillcolor('white')
    t.begin_fill()
    t.penup()
    draw_triangle(size, color)
    t.end_fill()

def main():
    window = t.Screen()
    # t.hideturtle()
    t.penup()
    t.speed(0)

    draw_illusion(SIZE, 'black')

    t.pensize(1)
    window.mainloop()


main()
