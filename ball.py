from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        # create another attribute for bounce
        self.x_move = 10#these gonna start out at 10
        self.y_move = 10
        self.move_speed = 0.1


    def move(self):
        new_x = self.xcor() + self.x_move#everytime it moves increase by 10 time
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):#y_cor
        self.y_move *= -1# it reverse the direction of y_cor by multiply -1 now above 10 become -10 now it adds -10 to y_cor.
    def bounce_x(self):
        self.x_move *= -1# same as y reason.
        self.move_speed *= 0.9# work as per game seen by teacher.
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()



