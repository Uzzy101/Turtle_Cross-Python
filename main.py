import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor('white')
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

player = Player()
screen.onkeypress(fun=player.up, key='Up')

car_manager = CarManager()


scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    #Collision
    for car in car_manager.all_cars:
        if player.distance(car) < 22:
            game_is_on = False

    #Finish a lap
    if player.ycor() > 290:
        player.reset()
        car_manager.speed_up()
        scoreboard.update_score()


screen.exitonclick()
