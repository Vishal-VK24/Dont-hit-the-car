from turtle import Turtle
import random
colors= ["red","blue","yellow","green","purple","brown"]
class Cars():
    def __init__(self):
        self.cars = []
        self.speed=8
    def create_car(self):
        k = random.randint(1,7)
        if k==2:
            t = Turtle()
            t.shape("square")
            t.shapesize(stretch_len=2)
            t.color(random.choice(colors))
            t.setheading(180)
            t.penup()
            y = random.randint(-250,280)
            t.goto(x=300,y=y)
            self.cars.append(t)
    def move_car(self):
        for i in self.cars:
            i.forward(self.speed)
    def speedup(self):
        self.speed+=3
