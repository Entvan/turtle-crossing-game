import time
import turtle
from turtle import Screen, Turtle
from player import Player, FINISH_LINE_Y
from car_manager import CarManager, MOVE_INCREMENT
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
hidden_turtle = Turtle()
hidden_turtle.hideturtle()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.move, "Up")

game_is_on = True
counter = 0

while game_is_on:
    counter += 1
    if counter % 6 == 0:
        car_manager.add_car()
    time.sleep(0.1)
    screen.update()
    car_manager.car_move()

    if player.ycor() == FINISH_LINE_Y:
        player.restart_position()
        scoreboard.update_scoreboard()
        car_manager.car_speed += MOVE_INCREMENT

    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            turtle.write("GAME OVER", False, "center", ("Courier", 18, "bold"))


screen.exitonclick()
