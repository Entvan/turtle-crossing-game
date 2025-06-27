from turtle import Turtle
FONT = ("Courier", 22, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-220, 260)
        self.score = 0
        self.write(f"Level: {self.score}", True, "center", FONT)

    def update_scoreboard(self):
        self.write(f"Level: {self.score}", True, "center", FONT)
        self.clear()
        self.score += 1
        self.penup()
        self.color("black")
        self.goto(-220, 260)
        self.write(f"Level: {self.score}", True, "center", FONT)



