import turtle as t
import math as m
import random as r

COLOR_LIST = ['green', 'red', 'yellow', 'black', 'blue', 'brown']


def figure(n, square, color):
  size = (square * 4 * m.tan(m.radians(180 / n)) / n) ** 0.5
  t.fillcolor(color)
  t.begin_fill()
  
  t.forward(size / 2)
  t.left(360 / n)
  for i in range(n - 1):
    t.forward(size)
    t.left(360 / n)
  t.forward(size / 2)

  t.end_fill()
  
    
def main():
  t.speed(0)
  t.hideturtle()

  for y in range(130, -200, -75):
    for x in range(-150, 170, 75):
      t.penup()
      t.goto(x, y)
      t.pendown()
      color = r.choice(COLOR_LIST)
      figure(r.randint(3, 6), 1800, color)
      
    
main()