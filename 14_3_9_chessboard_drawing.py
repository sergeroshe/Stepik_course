import turtle as t
import math as m
import random as r

FIELD_SIZE = 100
SQUARE_SIZE = 25
CHESSBOARD_SIZE = FIELD_SIZE // SQUARE_SIZE

COLOR_LIST = ['black', 'white']


def draw_square(side_length):
    for _ in range(4):
        t.forward(side_length)
        t.left(90)


def get_square_params():
  pass

    
def draw_squares(chessboard_size, square_side, color_list):
  t.penup()
  t.goto(-chessboard_size // 2, chessboard_size // 2)
  t.pendown()
  setheading_list = [0, 180]
  step_list = [square_side * 2, 0]
  color_list_idx = 0

  for i in range(chessboard_size):
    if i:
      t.forward(step_list[i % 2])    
    t.setheading(setheading_list[i % 2])
    for j in range(chessboard_size):
      t.fillcolor(color_list[color_list_idx % 2])

      t.begin_fill()
      draw_square(square_side)
      t.end_fill()

      t.forward(square_side)
      color_list_idx += 1
      print(f'idx = {color_list_idx}')          

    t.left(90)

    
  pass


def main():
  window = t.Screen()
  t.showturtle()
  t.speed(3)
  t.pensize(1)

  draw_squares(CHESSBOARD_SIZE, SQUARE_SIZE, COLOR_LIST)

  t.hideturtle()
  window.mainloop()

main()
