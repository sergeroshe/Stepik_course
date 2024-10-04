import turtle

INIT_STEP = 5
LIMIT_STEP = 200
STEP_INCREASE = 5
SIZE_INCREASE = 1
FINAL_POSITION_ANGLE = 180
SPIRAL_ANGLE = 45
STEP = 3
PENCOLOR_LIST = ['red', 'blue', 'yellow', 'green', 'violet', 'orange']


def spiral(init_step, step_increase, limit_step, size_increase, color_list, final_position_angle):
    angle = 0
    heading = turtle.heading()

    step = init_step
    size_reached = step > limit_step
    turned_correct_side = heading == final_position_angle + SPIRAL_ANGLE
    color_list_len = len(color_list)
    spiral_complete = size_reached and turned_correct_side
    size = 1
    i = 0
    while not spiral_complete:
        turtle.pensize(size)
        turtle.pencolor(color_list[i])
        step += step_increase
        size += size_increase
        turtle.forward(step)
        turtle.left(SPIRAL_ANGLE)
        heading = turtle.heading()
        print(i)
        print(step)
        turned_correct_side = heading == final_position_angle + SPIRAL_ANGLE
        size_reached = step > limit_step
        spiral_complete = size_reached and turned_correct_side
        i += 1
        if i > color_list_len - 1:
            i = 0


def main():
    window = turtle.Screen()
    turtle.showturtle()
    spiral(INIT_STEP, STEP_INCREASE, LIMIT_STEP, SIZE_INCREASE, PENCOLOR_LIST, FINAL_POSITION_ANGLE)
    window.mainloop()


main()