from turtle import Turtle, Screen

import random
is_race_on = False
screen = Screen()
screen.setup(width = 500,height=400)

user_bet = screen.textinput(title="Place your bet",prompt="Which turtle do you think will win? Enter a color in the rainbow:")
colors = ["red","orange","yellow","green","blue","indigo","violet"]
racers =[]
first = -60
for i in range(0,7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-240,y=first)
    first += 30
    racers.append(new_turtle)

if user_bet:
    is_race_on= True
    
while is_race_on:
    for turtle in racers:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
               print(f"You've won the bet! {winner} won the race ") 
            else:
                print(f"You've lost the bet! {winner} won the race ") 
            
        dist = random.randint(0,10)
        turtle.forward(dist)
        
    
screen.exitonclick()