import turtle as t

SIZE = 300


def draw_triangle(size, color):
    for _ in range(3):
        t.forward(size)
        t.left(120)


def draw_illusion(size, color):
    start_position = (-size // 2, -size // 2)
    t.goto(start_position)
    t.pendown()
    draw_triangle(size, color)
    pass


def main():
    window = t.Screen()
    # t.hideturtle()
    t.penup()
    t.speed(0)

    draw_illusion(SIZE, 'black')

    t.pensize(1)
    window.mainloop()


main()
