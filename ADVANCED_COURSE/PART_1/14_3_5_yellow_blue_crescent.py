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



def draw_crescent(size, color, crescent_width):
    t.Screen().bgcolor(BACKGROUND_COLOR)
    t.setheading(90)


    draw_circle(size, color)
 
    t.setheading(180)
    t.forward(crescent_width)
    t.setheading(90)

    draw_circle(size, BACKGROUND_COLOR)




def main():
    window = t.Screen()
    t.showturtle()
    t.penup()
    t.speed(0)
    start_position = CRESCENT_SIZE // 2, 0
    t.goto(start_position)


    draw_crescent(CRESCENT_SIZE, CRESCENT_COLOR, CRESCENT_WIDTH)

    t.hideturtle()
    t.pensize(1)
    window.mainloop()


main()
