from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def restart_position(self):
        self.goto(STARTING_POSITION)

    def cross_over(self):
        if self.goto(0, FINISH_LINE_Y):
            self.restart_position()









