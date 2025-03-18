import turtle as t
import math as m
import random as r

COLOR_LIST = ['green', 'red', 'yellow', 'black', 'blue', 'brown']
FIELD_SIZE = 200
FIGURE_SIDE = 50
FIGURE_SIDE_AMOUNT = 5
STEP = 75


def draw_polygon(side_amount, side_length, color):
  t.fillcolor(color)
  t.begin_fill()
  
  for i in range(side_amount):
    t.forward(side_length)
    t.left(360 / side_amount)

  t.end_fill()
  
    
def draw_polygons():
  window = t.Screen()
  t.showturtle()
  t.speed(3)
  t.pensize(1)
  side = FIGURE_SIDE
  side_amount = r.randint(3, 10)
  area = (side_amount * side ** 2) / (4 * m.tan(180 / side_amount))
  step = side * 4

  for y in range(FIELD_SIZE, -FIELD_SIZE, -step):
    for x in range(-FIELD_SIZE, FIELD_SIZE, step):
      t.penup()
      t.goto(x, y)
      t.pendown()
      color = r.choice(COLOR_LIST)
      draw_polygon(side_amount, side, color)
      print(area)

  t.hideturtle()
  window.mainloop()
      

def main():

  draw_polygons()

main()
