import turtle as t
import math as m
import random as r

COLOR_LIST = ['green', 'red', 'yellow', 'black', 'blue', 'brown']
FIELD_SIZE = 200
FIGURE_MIN_SIDE_AMOUNT = 3
FIGURE_MAX_SIDE_AMOUNT = 9

POLYGON_AREA = 5000


def draw_polygon(side_amount, side_length, color):
  t.fillcolor(color)
  t.begin_fill()
  
  t.forward(side_length // 2)
  t.left(360 / side_amount)
  for i in range(side_amount - 1):
    t.forward(side_length)
    t.left(360 / side_amount)
  t.forward(side_length // 2)
  

  t.end_fill()


def get_polygon_params(area, side_amount):
  # area = (side_amount * side ** 2) / (4 * m.tan(m.radians(180) / side_amount)) 
  radian_degrees = m.radians(180)
  side = m.sqrt((4 * area * m.tan(radian_degrees / side_amount))/ side_amount)
  radius = int(side / (2 * (m.sin(180 / side_amount))))

  return side, radius

  
    
def draw_polygons():
  window = t.Screen()
  t.showturtle()
  t.speed(3)
  t.pensize(1)
  side, radius = get_polygon_params(POLYGON_AREA, FIGURE_MAX_SIDE_AMOUNT)
  
  step = POLYGON_AREA // 40

  for y in range(FIELD_SIZE, -FIELD_SIZE, -step):
    for x in range(-FIELD_SIZE, FIELD_SIZE, step):
      t.penup()
      t.goto(x, y)
      t.pendown()
      side_amount = r.randint(3, 9)      
      side, radius = get_polygon_params(POLYGON_AREA, side_amount)
      color = r.choice(COLOR_LIST)

      draw_polygon(side_amount, side, color)

      print(side, radius, step)

  t.hideturtle()
  window.mainloop()
      

def main():

  draw_polygons()

main()
