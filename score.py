from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
    def levelup(self):
        self.clear()
        self.level += 1
        self.hideturtle()
        self.penup()
        self.goto(-280,278)
        self.write(f"level : {self.level}",align="left",font="Arial")
    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(-50,0)
        self.write(f"Game Over", align="left", font="Arial",)
