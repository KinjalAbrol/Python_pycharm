import turtle
import random
from turtle import Turtle, Screen
is_race_on = False
timmy_the_turtle = Turtle()# no use line write below
screen = Screen()
screen.setup(width=500,height=400)# setup for height and width of screen.also use keyword argument it more clear here than positional.#height width
# use of textinput for taking input of your question. then call it by variable to print ouput in console.
user_bet = screen.textinput(title="Make a bet.", prompt="Which turtle will win the race?Enter a color:")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "purple", "blue"]
y_positions = [-70, -40, -10, 20, 50, 80]# x remains same and ychanges bcoz all turle same start from x coordinate but at y they have to roughly distrbuted at middle.
all_turtles = []
for turtle_index in range(0, 6):
    timmy_the_turtle = Turtle()  # now turtle work start write here or above its choice here more clear tha turtle work begin.
    timmy_the_turtle.shape("turtle")  # also give upper Turtle(shape = "turtle).
    timmy_the_turtle.color(colors[turtle_index])
    timmy_the_turtle.penup()  # we dont want the line to draw so keep pen up
    timmy_the_turtle.goto(x=-230, y= y_positions[turtle_index])  # to move turtle to only left side of screen using x,y coordinates.
    # by above line coordinates it moves pretty much start of the window.
    all_turtles.append(timmy_the_turtle)
if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner.")
            else:
                print(f"You lost! The {winning_color} turtle is the winner.")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)





screen.exitonclick()