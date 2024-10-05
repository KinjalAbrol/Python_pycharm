from turtle import Turtle, Screen
from snake import Snake#import snake class from snake file.
from Food_snake import Food# import food class from food_snake file.
from Scoreboard import Scoreboard# import scoreboard from Scoreboard file.
import time
# screen setup
screen = Screen()
screen.setup(width = 600, height = 600)# for setup the screen height and width.use keyboard for more clear.
screen.bgcolor("black")# changing the colour of background of screen.
screen.title("My snake game")#  giving title on screen.
screen.tracer(0)# animation off that we donot see that each sqauare move one by one.it make screen blank so make use of update that it refresh the screen.

snake = Snake()#creating snake object from snake class.when this line get triggered it show the snake body on screen.
food = Food()
scoreboard = Scoreboard()
# Control the snake with keypress.(up,down,left,right arrow keys)
screen.listen()
screen.onkey(snake.up,"Up")#snake goes  up when Up key is pointed.
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")
# # snake body in explained code
# segment_1 = Turtle()# making a turtle.
# segment_1.shape("square")# giving a shape to turtle
# segment_1.color("white")# giving turtle color.
# # now create other two white square(turtle)
# segment_2 = Turtle()# making a turtle.
# segment_2.shape("square")# giving a shape to turtle
# segment_2.color("white")# giving turtle color.
# # now create position so that it doesnot overlap each other and looks like what we wanted as a snake.
# segment_2.goto(x= -20,y= 0)# backward 20 in x-coordinate that it is at left of ist square.
# # third one
# segment_3 = Turtle()# making a turtle.
# segment_3.shape("square")# giving a shape to turtle
# segment_3.color("white")# giving turtle color.
# segment_3.goto(x= -40,y= 0)# backward 40 in x-coordinate that it is left from ist and second square.
# snake body using tuple and for loop
# Moving the snake on screen.
#line 27 to 34 we put in snake file for organising the code by making snake class.
# starting_positions =[(0,0),(-20,0),(-40,0)]
# segments = []# create empty then append it later below
# for position in starting_positions:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()# while moving it doesnot draw a line.
#     new_segment.goto(position)
#     segments.append(new_segment)

game_is_on = True#create a while loop for continuosly something happens and create a variable.
while game_is_on:
    # use of update after each segment move bcoz we use tracer(0) and wanted screen upadte.
    screen.update()# it shows square not piece by peice together on screen.to refresh the screen and see what is happening.
    time.sleep(0.1)

    snake.move()#every time screen refresh the snake going to move by using the snake file def move function by one step.
#line 43 to 50 put in snake file for organising the code by making snake class.
    #Now make a loop for each segment to move in all direction go from last segement to first one.(basically in reverse order)
    # for seg_num in range(len(segments) - 1, 0,-1):# bcoz 3one is 2 ist one is 0 as computer as we know position in python
    #     #above line explain#start=2(len(seg)-1,stop = 0, step = -1)0ist,1sec,2third
    #     new_x = segments [seg_num - 1] .xcor()
    #     new_y = segments [seg_num - 1].ycor()
    #     segments[seg_num].goto(new_x,new_y)
    # segments[0].forward(20)#at position zero [0]
    # # segments[0].left(90)#if turns left
    # detect collison with food:-
    # turtle.distance()# distance of turtle to distance we put in() x,y.
    if snake.head.distance(food) < 15:# distance of dnake head from the food also 15 is a good no for collision.
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detetct collision with wall
    # create a boundary of 280 in all 4 300 len and width.
    # any four of the situation happen snake hits the wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
       game_is_on = False
       scoreboard.game_over()
    # detect collision with tail
    # if head collision with any segment of tail game over!
    for segment in snake.segments:
        if segment == snake.head:#bypassing the snake head.
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()




















screen.exitonclick()# it disappear when click on screen.