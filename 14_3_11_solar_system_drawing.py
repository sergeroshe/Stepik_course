import turtle as t
from math import sin, cos, radians

objects = {'Sun': ('Солнце', 150, (255, 252, 138), -95), 'Mercury': ('Меркурий', 20, (229, 189, 87), -45),
           'Venus': ('Венера', 40, (229, 189, 87), -45), 'Earth': ('Земля', 50, 'Earth-1.gif', -45),
           'Mars': ('Марс', 30, (252, 129, 101), -45), 'Jupiter': ('Юпитер', 90, (229, 189, 87), -65),
           'Saturn': ('Сатурн', 80, (229, 189, 87), -65), 'Uranus': ('Уран', 70, (111, 198, 221), -55),
           'Neptune': ('Нептун', 60, 'Neptune-1.gif', -55), 'Pluto': ('Плутон', 15, (229, 189, 87), -55)}

PLANETS_PARAM_DICT = {'Солнце': (0, 230, 'color'), 'Меркурий': (268, 48, 'color'), 'Венера': (87, 67, 'color'),
                        'Земля': (76, 52, 'color'), 'Марс': (78, 36, 'color'), 
                        'Юпитер': (58, 134, 'color'), 'Сатурн': (170, 134, 'orange'),
                          'Уран': (172, 117, 'color'), 'Нептун': (149, 79, 'color'), 
                          'Плутон': (112, 24, 'color')}


def draw_oval(width, height):
  cur_x = t.xcor()
  cur_y = t.ycor()
  for degree in range(361):
      radian = radians(degree)
      x = width * sin(radian) + cur_x
      y = -height * cos(radian) + height + cur_y
      t.goto(x, y)


def draw_planet(size, color):
   t.color(color)
   t.begin_fill()

   t.circle(size)

   t.end_fill()


def draw_solar_system():
   total_space = 0
   for planet in PLANETS_PARAM_DICT:
      total_space += (PLANETS_PARAM_DICT[planet][0] + PLANETS_PARAM_DICT[planet][1])
   t.penup()
   t.goto(-total_space // 2, 0)

   
   for planet in PLANETS_PARAM_DICT:
     indent = PLANETS_PARAM_DICT[planet][0] + PLANETS_PARAM_DICT[planet][1]
     size = PLANETS_PARAM_DICT[planet][1]
     t.forward(indent)
     draw_planet(size, 'red')
  # draw_oval(width, height)


def main():
  window = t.Screen()
  t.showturtle()
  t.speed(3)
  t.pensize(1)

  draw_solar_system()

  # t.hideturtle()
  window.mainloop()

main()