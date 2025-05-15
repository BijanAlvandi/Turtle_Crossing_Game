from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=-200, y=250)
        self.color("black")
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1

    def game_over(self, player):
        self.goto(x=0, y=-280)
        self.clear()
        self.write("GAME OVER", align="center", font=FONT)


