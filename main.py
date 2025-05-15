import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.go_up, "Up")

frame_counter = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    frame_counter += 1
    if frame_counter % 6 == 0:
        car_manager.spawn_car()
    car_manager.move_cars()
    if car_manager.check_collision(player):
        game_is_on = False
        scoreboard.game_over()
        screen.update()
    if player.is_at_finish():
        scoreboard.increase_score()
        scoreboard.update_score()
        player.reset_position()
        car_manager.increase_speed()

