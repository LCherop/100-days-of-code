from turtle import Turtle
POSITION = (0,260)

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(POSITION)
        self.update_score()
        
    def update_score(self):
        self.write(f"Score : {self.score}",align="center",font=("Arial",16,"normal"))
      
    def increase_score(self):
        self.score +=1
        self.clear()
        self.update_score()
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=("Arial",16,"normal"))
      