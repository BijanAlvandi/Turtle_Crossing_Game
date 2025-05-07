from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def spawn_car(self):
        # Try up to 10 times to find a Y that doesn't collide with the last four cars
        attempts = 0
        while attempts < 10:
            candidate_y = random.randint(-280, 280)
            recent_cars = self.cars[-4:]
            # Check that this candidate is at least 40px away from each recent car
            if all(abs(candidate_y - car.ycor()) > 40 for car in recent_cars):
                new_car = Turtle()
                new_car.shape("square")
                new_car.shapesize(stretch_wid=1, stretch_len=2)
                new_car.color(random.choice(COLORS))
                new_car.penup()
                new_car.goto(280, candidate_y)
                new_car.setheading(180)
                self.cars.append(new_car)
                return  # spawn one car and exit
            attempts += 1
        # If no valid spot found after 10 tries, skip spawning this tick

    def move_cars(self):
        for car in self.cars:
            car.forward(self.move_distance)

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT
