import turtle as t

CIRCLE_MIN_SIZE = 40
CIRCLE_MAX_SIZE = 300

COLOR_LIST = ["#FF0000", "#FFA600", "#FFFF00", "#62FF00", "#89F590", "#69C5FF", 
  "#1E56FC","#4800FF","#CC00FF","#FF5099"]
SHIFT_SIZE = CIRCLE_MAX_SIZE // 8

def draw_circle(size, color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(size)
    t.end_fill()


# give a proper name
def draw_picture():
    t.goto(0, -CIRCLE_MAX_SIZE)
    size = CIRCLE_MAX_SIZE
    i = 0
    pos = t.pos()
    while i < len(COLOR_LIST) - 1:
        draw_circle(size, COLOR_LIST[i])
        pos = pos[0], pos[1] + SHIFT_SIZE
        t.goto(pos)
        size -= SHIFT_SIZE
        i += 1
        



def main():
    window = t.Screen()
    t.hideturtle()
    t.penup()
    t.speed(0)

    draw_picture()

    t.pensize(1)
    window.mainloop()


main()
