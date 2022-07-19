from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.goto(0,-270)

    def move(self):
        self.forward(10)
