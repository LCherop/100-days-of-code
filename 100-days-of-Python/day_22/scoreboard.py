from turtle import Turtle
import random 

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.updateScoreboard()

    def updateScoreboard(self):
        self.clear()
        # Position the left sided score
        self.goto(-100,200)
        self.write(self.l_score, align="center",font=("Terminal",50,"normal"))

        # Position the right sided score
        self.goto(100,200)
        self.write(self.r_score, align="center",font=("Terminal",50,"normal"))
        
    def add_l_score(self):
        self.l_score += 1
        self.updateScoreboard()
    
    def add_r_score(self):
        self.r_score += 1
        self.updateScoreboard()