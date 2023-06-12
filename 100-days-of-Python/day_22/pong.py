from turtle import Turtle
import random 

class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        # self.shapesize(1,1)
        self.color("white")
        self.penup()
        # self.goto(0,0)
        self.x_move = 1
        self.y_move = 1
        self.move_speed = 0.025
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
        
    def bounce_y(self): #bounce off the wall
        self.y_move *= -1
    
    def bounce_x(self): #bounce off the paddle
        self.x_move *= -1
        self.move_speed *=0.5

    def reset(self):
        self.goto(0,0)
        self.move_speed = 0.025
        self.bounce_x()