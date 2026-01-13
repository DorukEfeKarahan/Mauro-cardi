import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle
pen.shape("triangle")
pen.penup()

def draw_star(x, y):
    pen.goto(x, y)
    colors = ["red", "yellow", "blue", "green", "purple", "white"]
    pen.color(random.choice(colors))
    pen.begin_fill()
    for _ in range(5):
        pen.forward(50)
        pen.right(144)
    pen.end_fill()

    for _ in range(10):
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        draw_star(x, y)

        turtle.done()