# challenge etch a sketch using all we learn previous in turtle and use of turtle documentation.
from turtle import Turtle, Screen
timmy_the_turtle = Turtle()
screen = Screen()
screen.listen()
def move_foward():
    timmy_the_turtle.forward(10)


screen.onkey(key= "W", fun= move_foward)

def move_backward():
    timmy_the_turtle.backward(10)


screen.onkey(key= "S", fun= move_backward)

def turn_left():
    new_heading = timmy_the_turtle.heading() + 10
    timmy_the_turtle.setheading(new_heading)
    # in two lines only use timmy_the_turtle.left(10)


screen.onkey(key= "A", fun= turn_left)
def turn_right():
    new_heading = timmy_the_turtle.heading() - 10
    timmy_the_turtle.setheading(new_heading)
    #in two lines only use timmy_the_turtle.right(10)

def clear_screen():
    timmy_the_turtle.clear()
    timmy_the_turtle.penup()  # penup when going to middle as it donot draw anything
    timmy_the_turtle.home()# as it return to middle after clear
    timmy_the_turtle.pendown()# after reaching middle pendown
screen.onkey(key= "C", fun= clear_screen)



screen.exitonclick()