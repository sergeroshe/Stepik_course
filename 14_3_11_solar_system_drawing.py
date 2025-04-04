import turtle as t

PLANETS_PARAMS_DICT = {'Меркурий': ('size', 'color'), 'Венера': ('size', 'color'),
                        'Земля': ('size', 'color'), 'Марс': ('size', 'color'), 
                        'Юпитер': ('size', 'color'), 'Сатурн': ('size', 'color'),
                          'Уран': ('size', 'color'), 'Нептун': ('size', 'color'), 
                          'Плутон': ('size', 'color'), }


def draw_solar_system():
  pass


def main():
  window = t.Screen()
  t.showturtle()
  t.speed(3)
  t.pensize(1)

  draw_solar_system()

  t.hideturtle()
  window.mainloop()

main()