import turtle as t

CRESCENT_SIZE = 300
CRESCENT_WIDTH = 80
CRESCENT_COLOR = 'yellow'
BACKGROUND_COLOR = 'blue'

def draw_circle(size, color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(size)
    t.end_fill()


def move_phase(size, circle_1_start_pos, circle_2_start_pos, color):
    t.goto(circle_1_start_pos)
    circle_2_x_pos = circle_2_start_pos[0]
    circle_1_x_pos = circle_1_start_pos[0]
    while circle_2_x_pos > circle_1_x_pos:
        circle_2_x_pos -= 3
        t.goto(circle_2_x_pos, circle_2_start_pos[1])
        draw_circle(size, color)



def draw_crescent(size, color):
    t.Screen().bgcolor(BACKGROUND_COLOR)
    t.setheading(90)

    start_position = CRESCENT_SIZE // 2, 0
    t.goto(start_position)

    draw_circle(size, color)
    circle_1_start_pos = t.pos()[0], 0
    circle_2_start_pos = t.pos()[0] + CRESCENT_SIZE * 2, 0
    t.goto(circle_2_start_pos)

    move_phase(CRESCENT_SIZE, circle_1_start_pos, circle_2_start_pos, BACKGROUND_COLOR)
 
    t.setheading(180)
    t.forward(1)
    t.setheading(0)




def main():
    window = t.Screen()
    t.showturtle()
    t.penup()
    t.speed(0)

    draw_crescent(CRESCENT_SIZE, CRESCENT_COLOR)

    # t.hideturtle()
    t.pensize(1)
    window.mainloop()


main()
