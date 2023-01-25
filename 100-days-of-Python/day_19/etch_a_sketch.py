from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_back():
    tim.backward(10)

def move_counter_closkwise():
    tim.left(10)
    
def move_clockwise():
    tim.right(10)

def clearscreen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    
screen.listen()
screen.onkey(key="w",fun=move_forwards)
screen.onkey(key="s",fun=move_back)
screen.onkey(key="a",fun=move_counter_closkwise)
screen.onkey(key="d",fun=move_clockwise)
screen.onkey(key="c",fun=clearscreen)
screen.exitonclick()