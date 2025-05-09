from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('My Snake Game')

screen.tracer(0) # to turn off tracer

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.09)
    snake.move()

    # Detect the collision of food and snake head
    if snake.head.distance (food) <15: 
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    
    #Detect collision with wall 
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detect Collision with tail
    for segment in snake.segments[1:]:
        #if segment collides with any segment of tail:
        if  snake.head.distance(segment) < 10:
            #gameover!
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()