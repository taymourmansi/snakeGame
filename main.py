from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time
# Screen Setup
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
# Create Body
snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(snake.down,"Down")
gameIsOn = True

while gameIsOn:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # SCORE/EAT FOOD
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increaseScore()
        snake.increaseSize()

    # WALL COLLISION DETECTION
    if snake.head.xcor()> 280 or snake.head.ycor()> 280 or snake.head.xcor()< -280 or snake.head.ycor() < -280:
        time.sleep(2)
        scoreboard.reset()
        snake.reset()
    # TAIL COLLISION DETECTION

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            time.sleep(2)
            scoreboard.reset()
            snake.reset()

screen.exitonclick()