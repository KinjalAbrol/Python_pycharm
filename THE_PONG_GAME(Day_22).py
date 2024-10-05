from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scooreboard import Scoreboard
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width= 800, height= 600)
screen.title("Pong")

screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scooreboard = Scoreboard()

# put these line to paddle file
# paddle = Turtle()
# paddle.shape("square")
# paddle.color("white")
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.penup()
# paddle.goto(350, 0)
# def go_up(self):
#     new_y = paddle.ycor() + 20
#     paddle.goto(paddle.xcor(), new_y)
#
#
# def go_down(self):
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(r_paddle.go_up, key= "Up")
screen.onkey(r_paddle.go_down,  key="Down")
screen.onkey(l_paddle.go_up, key= "w")
screen.onkey(l_paddle.go_down, key= "s")
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # detect collision with ball
    if ball.ycor() > 280 or ball.ycor() < -280:
    # its needs to bounce
       ball.bounce_y()
    # detect collsion with r_paddle
    if ball.distance(r_paddle) < 50 and ball.x_cor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # detect when r_paddle missed
    if ball.xcor() > 380:
        ball.reset_position()
        scooreboard.l_point()
    #detect l_paddle missed
    if ball.xcor() < -380:
        ball.reset_position()
        scooreboard.r_point()





screen.exitonclick()