import turtle as t
import math as m
import random as r

FIELD_SIZE = 300
FIGURE_MIN_SIDE_AMOUNT = 3
FIGURE_MAX_SIDE_AMOUNT = 12
POLYGON_AREA = 2500
STEP = POLYGON_AREA // 30


def draw_polygon(side_amount, side_length, color):
  t.fillcolor(color)
  # align the figure to the center
  t.forward(side_length // 2 + 1)

  t.begin_fill()

  t.left(360 / side_amount)
  for i in range(side_amount - 1):
    t.forward(side_length)
    t.left(360 / side_amount)
  t.forward(side_length // 2)
  
  t.end_fill()


def get_polygon_params(area):
  radian_degrees = m.radians(180)
  side_amount = r.randint(FIGURE_MIN_SIDE_AMOUNT, FIGURE_MAX_SIDE_AMOUNT)
  # calculate side length through area and side amount     
  side = m.sqrt((4 * area * m.tan(radian_degrees / side_amount))/ side_amount)
  color = tuple((r.randint(0, 255) for _ in range(3)))

  return side, side_amount, color

  
    
def draw_polygons():
  for y in range(FIELD_SIZE, -FIELD_SIZE, -STEP):
    for x in range(-FIELD_SIZE, FIELD_SIZE, STEP):
      t.penup()
      t.goto(x, y)
      t.pendown()

      side, side_amount, color = get_polygon_params(POLYGON_AREA)

      draw_polygon(side_amount, side, color)


def main():
  window = t.Screen()
  t.colormode(255)
  t.showturtle()
  t.speed(3)
  t.pensize(1)

  draw_polygons()

  t.hideturtle()
  window.mainloop()

main()
