import turtle as t

MOON_SIZE = 400
MOON_COLOR = 'gold3'
BACKGROUND_COLOR = 'darkblue'
SHADOW_SIZE = 40
SHADOW_COLOR = 'darkblue'
    

def draw_moon():
    t.bgcolor('darkblue')
    t.penup()
    t.speed(0)
    t.dot(200, 'gold3')
    t.forward(200)
    t.shape('circle')
    t.shapesize(10)
    t.color('darkblue')

    
def move_shadow():
    while True: 
        for _ in range(400):
            t.backward(1)
        t.forward(400)

def main():
    window = t.Screen()
    t.showturtle()
    t.penup()

    draw_moon()
    move_shadow()

    # t.hideturtle()
    t.pensize(1)
    window.mainloop()


main()
