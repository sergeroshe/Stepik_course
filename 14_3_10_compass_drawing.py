import turtle as t

CIRCLE_SIZE, CROSS_SIZE = 100, 200
NAME_LIST = [('Восток', False, 'left', ('Arial', 15, 'bold')), 
         ('Север', False, 'center', ('Arial', 15, 'bold')),
         ('Запад', False, 'right', ('Arial', 15, 'bold')),
         ('Юг', False, 'center', ('Arial', 15, 'bold'))]


def draw_circle(size):
    t.penup()
    t.goto(0, -size)
    t.pendown()
    t.circle(size)
    t.penup()

def draw_cross(center, size, name_list):
    for name in name_list:
        t.goto(center)
        t.pendown()
        t.forward(size)
        t.penup()
        t.forward(50)
        t.write(*name)
        t.left(90)


def draw_compass(circle_size, cross_size, name_list):
    center = (0, 0)
    print(center)

    draw_circle(circle_size)
    draw_cross(center, cross_size, name_list)


def main():
  window = t.Screen()
  t.showturtle()
  t.speed(3)
  t.pensize(1)

  draw_compass(CIRCLE_SIZE, CROSS_SIZE, NAME_LIST)

  t.hideturtle()
  window.mainloop()

main()