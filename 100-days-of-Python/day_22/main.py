from turtle import Turtle, Screen
from paddle import Paddle
from pong import Pong
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle((-280,0))
right_paddle = Paddle((280,0))
pong = Pong()
scores = Scoreboard()

screen.listen()
screen.onkey(left_paddle.up,"w")
screen.onkey(left_paddle.down,"s")
screen.onkey(right_paddle.up,"Up")
screen.onkey(right_paddle.down,"Down")

game_is_on = True
while game_is_on:
    time.sleep(pong.move_speed)
    screen.update()
    pong.move()
    
    # #detect collision with wall
    if pong.ycor() > 280 or pong.ycor() < -280:
        #bounce the ball
        pong.bounce_y()
    
    # Detect collision with paddles
    if pong.distance(right_paddle) < 50 and pong.xcor() > 260 or pong.distance(left_paddle) < 50 and pong.xcor() < -260:
        # bounce 
        pong.bounce_x()

    # Detect if the pong goes out of bounds (right)
    if pong.xcor() > 300:
        pong.reset()
        scores.add_l_score()
    
    # Detect if the pong goes out of bounds (left)
    if  pong.xcor() < -300:
        pong.reset()
        scores.add_r_score()

screen.exitonclick()