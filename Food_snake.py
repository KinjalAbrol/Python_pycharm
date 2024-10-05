from turtle import Turtle
import random
# the food class have all capabilites of Turtle class but it also have some specific things.

class Food(Turtle):# superclass Turtle # inherit food class from turtle.it contains all things of turtle class but also some we add.
    def __init__(self):
        super().__init__()# give super class # syntax of class inhertance.
        self.shape("circle")# method of turtle class that we are modyfying in food class.
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)# shapesize:- stretch turtle along its length and width.
        # now it become 10 by 10 circle.All the three above methods come from turtle superclass.
        self.color("blue")
        self.speed("fastest")
        self.refresh()
        # create new method.it is going to refresh the food and go to new random_x and y location.
    def refresh(self):
        random_x = random.randint(-280, 280)# it is of 300 l and w so to generate food in between take some less i.e-280t0280
        #same in y-axis generate food between random anywhere from -280 b/w 280 .
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)# goto:-for moving  x,y loction we give but in this we move it to random x,position as we did above.

