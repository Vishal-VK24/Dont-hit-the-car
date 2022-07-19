from turtle import Screen
from player import Player
from cars import Cars
from score import Score
import time
s= Screen()

s.setup(height=600,width=600)
s.tracer(0)
p = Player()
s.update()
s.listen()
s.onkey(p.move,"Up")
c = Cars()
score =Score()
check = True
score.levelup()
while check:
    time.sleep(0.1)
    s.update()
    c.create_car()
    c.move_car()
    if p.ycor() > 280:
        p.goto(0,-270)
        c.speedup()
        score.levelup()
        s.tracer(0)
        for i in c.cars:
            i.hideturtle()
        c.cars.clear()
    for i in c.cars:
        if p.distance(i) < 20:
            score.game_over()
            check = False

s.exitonclick()