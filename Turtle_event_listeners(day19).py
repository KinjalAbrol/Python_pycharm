# event listener example controlllling the turtle using keystroke.
from turtle import Turtle, Screen
timmy_the_turtle = Turtle()
screen = Screen()# create screen object which control the window when run our code
def move_foward():
    timmy_the_turtle.forward(10)

screen.listen()# to get hold on events tell the object screen to listen
# this is when we press space key then it allows only to move forward.
screen.onkey(key= "space", fun= move_foward)# so for this we have to crete some function above
screen.exitonclick()# when we click the screen exit
# now in ouput hit the space bar check turtle is moving.
# Higher order function example.
# it means a function working with another func. Calculator as a higher order func as it takes func as an input and work with it.
def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2
def calculator(n1,n2,func):
    return func(n1,n2)
result = calculator(2,3,add)
print(result)


