# using turtle graphics to create turtle,screen,get shape,color,forward
# from turtle import Turtle, Screen
# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
#
# screen = Screen()
# screen.exitonclick()
# # challenge1 on turtle(turtle draw a sqaure)
# from turtle import Turtle, Screen
#
# timmy_the_turtle = Turtle()
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(98)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(98)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(98)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.left(98)
#
# screen = Screen()
# screen.exitonclick()
# #challenge1 as for loop for simple code
# from turtle import Turtle, Screen
# timmy_the_turtle= Turtle()
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(98)
#
# screen = Screen()
# screen.exitonclick()
# # challenge2 on turtle(draw a dashed line)
# from turtle import Turtle, Screen
# timmy_the_turtle = Turtle()
# timmy_the_turtle.forward(10)
# timmy_the_turtle.penup()
# timmy_the_turtle.forward(10)
# timmy_the_turtle.pendown()
# timmy_the_turtle.forward(10)
# timmy_the_turtle.penup()
# timmy_the_turtle.forward(10)
# timmy_the_turtle.pendown()
# timmy_the_turtle.forward(10)
# timmy_the_turtle.penup()
# timmy_the_turtle.forward(10)
# timmy_the_turtle.pendown()
# timmy_the_turtle.forward(10)
# timmy_the_turtle.penup()
# timmy_the_turtle.forward(10)
# timmy_the_turtle.pendown()
# #same as 15 time
#
# screen = Screen()
# screen.exitonclick()
#challenge2 second using for loop
# from turtle import Turtle, Screen
# timmy_the_turtle = Turtle()
# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()
#
#
# screen = Screen()
# screen.exitonclick()
# Challenge3(drawing different shapes one only.eg square, triangle,nonagonetc.)
# from turtle import Turtle, Screen
# timmy_the_turtle = Turtle()
# num_sides = 5
# for _ in range(num_sides):
#     angle = 360/num_sides
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(angle)
#
# screen = Screen()
# screen.exitonclick()
# challenge3 (drawing different shapes all together from triangle to decagon 1-10.eg square, triangle,nonagonetc.)
# use of def function
# from turtle import Turtle, Screen
# import random
# timmy_the_turtle = Turtle()
# colours = ["dim gray", "medium blue", "light blue", "light sea green", "dark red", "snow"]
# num_sides = 5
# def draw_shapes(num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)
# for shape_side_n in range(3,11):
#     timmy_the_turtle.color(random.choice(colours))
#     draw_shapes(shape_side_n)
#
#
#
# screen = Screen()
# screen.exitonclick()
# Challenge4(Generate a random walk)
# from turtle import Turtle, Screen
# import random
# timmy_the_turtle = Turtle()
# colours = ["dim gray", "medium blue", "light blue", "light sea green", "dark red", "snow"]
# directions = [0, 90, 180, 270]#east north west south
# timmy_the_turtle.pensize(15)
# timmy_the_turtle.speed("fastest")
#
# for _ in range(200):
#     timmy_the_turtle.color(random.choice(colours))
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.setheading(random.choice(directions))
#
# screen = Screen()
# screen.exitonclick()
# Python tuple
# my_tuple = (1, 3, 8)
# print(my_tuple[2])
# print(my_tuple)
# there are no changes possible in tuple like change or remove something
# so to change put it simply into list.
# my_tuple = (1, 3, 8)
# print(list(my_tuple))
# Use of tuple and colormode in (challenge 4)
# from turtle import Turtle, Screen
# import turtle
# import random
# timmy_the_turtle = Turtle()
# #created colormode
# turtle.colormode(255)
# #now get rid of color list and create random colour
# # instead of list create a new functiom
# def random_colour():
#     r = random.randint(0, 255)# randint bcoz integers
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     # now generate tuple
#     random_colour = (r, g, b)
#     return random_colour
#
# directions = [0, 90, 180, 270]#east north west south
# timmy_the_turtle.pensize(15)
# timmy_the_turtle.speed("fastest")
#
# for _ in range(200):
#     timmy_the_turtle.color(random_colour())
#     timmy_the_turtle.forward(30)
#     timmy_the_turtle.setheading(random.choice(directions))
#
# screen = Screen()
# screen.exitonclick()
# challenge5(Draw a spirograph)
from turtle import Turtle, Screen
import turtle
import random

timmy_the_turtle = Turtle()
turtle.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):# it gives float value like 3.4  and range donot work with float values thats why we use integer int
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
        # getting heading = current and setting or chaning heading = setheading.
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)

draw_spirograph(5)
screen = Screen()
screen.exitonclick()