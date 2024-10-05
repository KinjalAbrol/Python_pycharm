from turtle import Turtle, Screen
from snakesimple import Snake#import snake class from snakes file.
from food_snake_simple import Food
from scoreboardsimple import Scoreboard
import time
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collison with food:-
    # turtle.distance()# distance of turtle to distance we put in() x,y.
    if snake.head.distance(food) < 15:  # distance of dnake head from the food also 15 is a good no for collision.
        scoreboard.increase_score()
        food.refresh()
        snake.extend()
    # detetct collision with wall
    # create a boundary of 280 in all 4 300 len and width.
    # any four of the situation happen snake hits the wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
       game_is_on = False
       scoreboard.game_over()
       # detect collision with tail
       # if head collision with any segment of tail game over!
       for segment in snake.segments[1:]:# slicing tuple for easy simple code.
           # if segment == snake.head:  # bypassing the snake head.
           #     pass
           if snake.head.distance(segment) < 10:
               game_is_on = False
               scoreboard.game_over()



screen.exitonclick()