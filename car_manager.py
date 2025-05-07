from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        # self.goto(600, 0)

    def spawn_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.goto(280, random.randint(-280, 280))
        new_car.setheading(180)
        self.cars.append(new_car)  # keep track of it so move & clean it up later

    def move_cars(self):
        for car in self.cars:
            car.forward(self.move_distance)
