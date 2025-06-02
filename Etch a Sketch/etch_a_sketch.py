from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.speed("fastest")

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    tim.setheading(tim.heading() + 10)

def turn_right():
    tim.setheading(tim.heading() - 10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def change_color_red():
    tim.pencolor("red")

def change_color_blue():
    tim.pencolor("blue")

def change_color_green():
    tim.pencolor("green")

def increase_pen_size():
    tim.pensize(tim.pensize() + 1)

def decrease_pen_size():
    if tim.pensize() > 1:
        tim.pensize(tim.pensize() - 1)

pen_is_down = True
def toggle_pen():
    global pen_is_down
    if pen_is_down:
        tim.penup()
    else:
        tim.pendown()
    pen_is_down = not pen_is_down

screen.listen()
screen.onkey(move_forwards, "Up")
screen.onkey(move_backwards, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "c")
screen.onkey(change_color_red, "r")
screen.onkey(change_color_blue, "b")
screen.onkey(change_color_green, "g")
screen.onkey(increase_pen_size, "=")
screen.onkey(decrease_pen_size, "-")
screen.onkey(toggle_pen, "space")
screen.onkey(tim.undo, "u")

screen.exitonclick()
# This code creates an Etch-a-Sketch style drawing application using the Turtle graphics library.