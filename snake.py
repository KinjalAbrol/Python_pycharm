from turtle import Turtle

STARTING_POSITIONS =[(0,0),(-20,0),(-40,0)]# taking as constants so capitilized.
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
# these two below func are going to create our snake(create and add)
    def create_snake(self):
        for position in STARTING_POSITIONS:#change of starting_position as constant as above used.
    # take from for loop and add it to add_segment# then call this function and then pass into position that were looping through.
            # new_segment = Turtle("square")
            # new_segment.color("white")
            # new_segment.penup()  # while moving it doesnot draw a line.
            # new_segment.goto(position)
            # self.segments.append(new_segment)#use of self due to above attribute segment.
            self.add_segemnt(position)
# this function is require to add segemnt in which position.
    def add_segemnt(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()  # while moving it doesnot draw a line.
        new_segment.goto(position)
        self.segments.append(new_segment)  # use of self due to above attribute segment.

# add segment to snake when eat food as it grows in length.
    def extend(self):
        self.add_segemnt(self.segments[-1].position())# write - for counting from end of list.

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0,-1):

            new_x = self.segments[seg_num - 1].xcor()#use of self with segment due to self attribute .
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVING_DISTANCE)  # at position zero [0]
        # segments[0].left(90)#if turns left

    def up(self):
        if self.head.heading() != DOWN:
           self.head.setheading(UP)

    def down(self):
        if self.head.heading() != DOWN:
           self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
           self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
           self.head.setheading(RIGHT)

