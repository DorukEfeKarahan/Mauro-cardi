import turtle
import random

screen = turtle.Screen()
screen.bgcolor(black)
t =  turtle.Turtle()
t.speed(0)
t.width(3)

colors = ["red", "yellow"]

for _ in range(200):
    t.color(random.choice(colors))
    t.forward(30)
    t.setheaging(random.choice([0, 90, 180, 270]))

t.hideturtle
turtle.done()