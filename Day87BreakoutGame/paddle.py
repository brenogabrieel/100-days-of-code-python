from turtle import Turtle
from time import sleep

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.penup()
        self.goto(position)

    def move_right(self):
        new_x = self.xcor() + 30
        self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - 30
        self.goto(new_x, self.ycor())