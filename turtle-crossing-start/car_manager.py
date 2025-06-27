from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.car_speed = STARTING_MOVE_DISTANCE
        self.cars = []

    def add_car(self):
        new_car = Turtle("square")
        new_car.shapesize(1, 2)
        car_color = random.choice(COLORS)
        new_car.color(car_color)
        new_car.penup()
        random_y = random.randint(-200, 200)
        new_car.goto(300, random_y)
        self.cars.append(new_car)

    def car_move(self):
        for car in self.cars:
            car.backward(self.car_speed)












