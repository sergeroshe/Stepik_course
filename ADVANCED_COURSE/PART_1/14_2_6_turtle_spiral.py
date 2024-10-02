import turtle

INIT_STEP = 5
LIMIT_STEP = 20
ANGLE_REDUCTION = 30
FINAL_POSITION_ANGLE = 0
STEP = 3


def spiral(init_step, step_increase, limit_step, angle_reduction, final_position_angle):
    angle = 0
    heading = turtle.heading()

    step = init_step
    size_reached = step > limit_step
    turned_correct_side = final_position_angle - step <= heading <= final_position_angle

    spiral_complete = size_reached and turned_correct_side
    while not spiral_complete:
        turtle.stamp()
        turtle.penup()
        turtle.forward(step)
        turtle.setheading(angle)

        angle -= angle_reduction
        step += step_increase

        heading = turtle.heading()
        print(heading)
        turned_correct_side = final_position_angle - step <= heading <= final_position_angle
        size_reached = step > limit_step
        spiral_complete = size_reached and turned_correct_side


def main():
    window = turtle.Screen()
    turtle.Screen().bgcolor('green')
    turtle.showturtle()
    turtle.shape('turtle')
    spiral(INIT_STEP, STEP, LIMIT_STEP, ANGLE_REDUCTION, FINAL_POSITION_ANGLE)
    window.mainloop()


main()
