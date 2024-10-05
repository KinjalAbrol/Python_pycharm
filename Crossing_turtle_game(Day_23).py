import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoooreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create player
player = Player()

# Control player
screen.listen()
screen.onkeypress(player.move, "Up")# go_up

# Instantiate CarManager
car_manager = CarManager()

# Create Scoreboard
scoooreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()

    # Create and move car
    car_manager.make_car()
    car_manager.move()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoooreboard.game_over()
            game_is_on = False
            scoooreboard.game_over()

    # Detect successful crossing and speed up cars
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoooreboard.increase_level()


screen.exitonclick()