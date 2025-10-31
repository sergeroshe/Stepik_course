import turtle as t
from math import sin, cos, radians

PLANETS_PARAM_DICT = {1: (115, (255, 252, 138), 'Солнце'), 2: (24, (229, 189, 87), 'Меркурий'),
                      3: (33, (229, 189, 87), 'Венера'),
                      4: (26, 'white', 'Земля', 'Earth-1.gif'), 5: (18, (252, 129, 101), 'Марс'),
                      6: (67, (229, 189, 87), 'Юпитер'), 7: (67, (229, 189, 87), 'Сатурн'),
                      8: (58, (111, 198, 221), 'Уран'), 9: (30, 'white', 'Нептун', 'Neptune-1.gif'),
                      10: (12, (229, 189, 87), 'Плутон')}


def draw_oval(width, height, cur_planet_radius):
    cur_x = t.xcor()
    cur_y = -cur_planet_radius // 2
    t.goto(cur_x, cur_y)

    for degree in range(361):
        radian = radians(degree)
        x = width * sin(radian) + cur_x
        y = -height * cos(radian) + height + cur_y
        t.pendown()

        t.goto(x, y)

        t.penup()


def draw_planet(size, color):
    t.pendown()
    t.colormode(255)
    t.color(color)
    t.begin_fill()
    t.pencolor('black')

    t.circle(size)

    t.end_fill()
    t.penup()


def draw_picture_based_planet(cur_pos, pic):
    t.Screen().addshape(pic)
    t.shape(pic)
    t.goto(cur_pos[0], -1)

    t.stamp()
    t.penup()


def get_next_planet_position(cur_pos, cur_planet_radius, next_planet_radius):
    indent = cur_planet_radius + next_planet_radius
    next_planet_position = (cur_pos[0] + indent + 40, -next_planet_radius)
    return next_planet_position


def get_total_polar_system_space():
    total_space = 0
    for planet in PLANETS_PARAM_DICT:
        total_space += PLANETS_PARAM_DICT[planet][0] * 2 + 10
    return total_space


def write_planet_name(name, cur_pos, planet_radius):
    t.goto(cur_pos[0], cur_pos[1] - 20)
    t.write(name, align='center', font=('Arial', 10, 'normal'))


def draw_solar_system():
    total_space = get_total_polar_system_space()
    t.penup()
    t.goto(-total_space // 2, - PLANETS_PARAM_DICT[1][0])

    for planet in PLANETS_PARAM_DICT:
        cur_pos = t.pos()
        cur_planet_radius = PLANETS_PARAM_DICT[planet][0]
        color = PLANETS_PARAM_DICT[planet][1]
        draw_planet(cur_planet_radius, color)
        name = PLANETS_PARAM_DICT[planet][2]
        write_planet_name(name, cur_pos, cur_planet_radius)

        if planet != 10:
            next_planet_radius = PLANETS_PARAM_DICT[planet + 1][0]
            next_planet_position = get_next_planet_position(cur_pos, cur_planet_radius, next_planet_radius)
            if planet == 7:
                draw_oval(85, 33, cur_planet_radius)

            elif planet == 4 or planet == 9:
                pic = PLANETS_PARAM_DICT[planet][3]
                draw_picture_based_planet(cur_pos, pic)
                t.shape('classic')
            t.setpos(next_planet_position)

        else:
            t.hideturtle()


def main():
    window = t.Screen()

    t.colormode(255)

    t.showturtle()
    t.speed(0)
    t.pensize(2)
    t.pencolor('black')

    draw_solar_system()

    window.mainloop()


main()
