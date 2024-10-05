from turtle import Turtle, Screen
screen = Screen()
screen.setup(width = 600, height = 600)# for setup the screen height and width.use keyboard for more clear.
screen.bgcolor("black")# changing the colour of background of screen.
screen.title("My snake game")#  giving title on screen.
screen.tracer(0)
starting_positions =[(0,0),(-20,0),(-40,0)]
segments = []# create empty then append it later below
for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()# while moving it doesnot draw a line.
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    for seg in segments:
        seg.forward(20)
        screen.update()
        time.sleep(1)


screen.exitonclick()