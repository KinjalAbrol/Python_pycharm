# colorgram.py for color tuple numners go save image and the save in file and extraxt color numbers from image
#extract rgb from hirst image# put drag the image in this main file
# install colorgram by go to settings package in pycharm
import colorgram
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
print(rgb_colors)

# final project hirst drawing the dots day 18
from turtle import Turtle, Screen
import turtle
import random

turtle.colormode(255)
timmy_the_turtle = turtle.Turtle()
timmy_the_turtle.speed("fastest")
timmy_the_turtle.penup()
timmy_the_turtle.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
timmy_the_turtle.setheading(225)
timmy_the_turtle.forward(300)
timmy_the_turtle.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    timmy_the_turtle.dot(20, random.choice(color_list))
    timmy_the_turtle.forward(50)

    if dot_count % 10 == 0:
        timmy_the_turtle.setheading(90)
        timmy_the_turtle.forward(50)
        timmy_the_turtle.setheading(180)
        timmy_the_turtle.forward(500)
        timmy_the_turtle.setheading(0)

screen = Screen()
screen.exitonclick()