from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def go_up(self):
        y_new = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), y_new)

    def is_at_finish(self):
        return self.ycor() > FINISH_LINE_Y

    def reset_position(self):
        self.goto(STARTING_POSITION)
