from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from score_board import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scores = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

snake_is_alive = True 
  
while snake_is_alive:
    screen.update()
    time.sleep(0.2)
    
    snake.move()
    
    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scores.increase_score()
        snake.extend()
    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake_is_alive = False
    #detect collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(food) < 10:
            snake_is_alive = False
    
scores.game_over()     
screen.exitonclick()