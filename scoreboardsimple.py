from turtle import Turtle
class Scoreboard(Turtle):# add turtle as superclass and scoreboard as class and do everything as turtle can do.
    def __init__(self):
        super().__init__()

        self.score = 0
        self.color("white")
        self.penup()# not show line on screen befor it moves to goto location.
        self.goto(0,270)# move x,y position.
        # write score on screen.print score give align = l,r or c give font.#line 16
        self.hideturtle()# hide turtle show on screen after running.
        self.update_scoreboard()

# delete previous score that new doesnot overlap it
    def update_scoreboard(self):
        self.write(f"Score:{self.score}", align="center", font=("Arial", 24, "normal"))

# when snake touches the wall

    def game_over(self):
        self.goto(0, 0)  # write it in centre nit at top as score.
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

 #now keep tract of score and increase when eat food.
    def increase_score(self):
        self.score += 1
        # then call self.write
        self.clear()
        self.write(f"Score:{self.score}", align="center", font=("Arial", 24, "normal"))
